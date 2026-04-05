import argparse
import requests
import csv
import time
import os
from datetime import datetime, timedelta

CLIMATE_API_URL = "https://power.larc.nasa.gov/api/temporal/daily/point"
PARAMETERS = ["T2M", "PRECTOTCORR", "RH2M", "WS2M"]

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_INPUT = os.path.join(SCRIPT_DIR, "..", "data.csv")
DEFAULT_OUTPUT = os.path.join(SCRIPT_DIR, "..", "climate_output.csv")


def fetch_and_parse(lat, lon, start_date_str, end_date_str):
    """Fetch and parse climate API response"""
    start_fmt = start_date_str.replace("-", "")
    end_fmt = end_date_str.replace("-", "")

    params = {
        "community": "RE",
        "parameters": ",".join(PARAMETERS),
        "latitude": lat,
        "longitude": lon,
        "start": start_fmt,
        "end": end_fmt,
        "format": "JSON",
    }

    response = requests.get(CLIMATE_API_URL, params=params, timeout=30)

    if response.status_code != 200:
        return None, f"HTTP {response.status_code}"

    try:
        data = response.json()
    except:
        return None, "JSON parse error"

    if "properties" not in data or "parameter" not in data["properties"]:
        return None, "Invalid structure"

    param_data = data["properties"]["parameter"]

    temps = []
    precips = []
    humidities = []
    winds = []

    if "T2M" in param_data:
        for date_key, value in param_data["T2M"].items():
            if isinstance(value, (int, float)):
                temps.append(value)

    if "PRECTOTCORR" in param_data:
        for date_key, value in param_data["PRECTOTCORR"].items():
            if isinstance(value, (int, float)):
                precips.append(value)

    if "RH2M" in param_data:
        for date_key, value in param_data["RH2M"].items():
            if isinstance(value, (int, float)):
                humidities.append(value)

    if "WS2M" in param_data:
        for date_key, value in param_data["WS2M"].items():
            if isinstance(value, (int, float)):
                winds.append(value)

    if not temps:
        return None, "No valid data"

    return {
        "Temp_Mean": round(sum(temps) / len(temps), 2),
        "Temp_Min": round(min(temps), 2),
        "Temp_Max": round(max(temps), 2),
        "Precip_Total": round(sum(precips), 2) if precips else 0,
        "Precip_Days": len([p for p in precips if p > 0]),
        "Humidity_Mean": round(sum(humidities) / len(humidities), 2)
        if humidities
        else None,
        "Wind_Mean": round(sum(winds) / len(winds), 2) if winds else None,
        "Days_Data": len(temps),
    }, None


def main():
    parser = argparse.ArgumentParser(
        description="Fetch climate data for health event locations"
    )
    parser.add_argument(
        "-i",
        "--input",
        default=os.environ.get("CLIMATE_INPUT", DEFAULT_INPUT),
        help="Input CSV file with location data",
    )
    parser.add_argument(
        "-o",
        "--output",
        default=os.environ.get("CLIMATE_OUTPUT", DEFAULT_OUTPUT),
        help="Output CSV file for results",
    )
    args = parser.parse_args()

    input_csv = args.input
    output_csv = args.output

    print(f"Loading data from: {input_csv}")

    records = []
    with open(input_csv, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append(row)

    print(f"Loaded {len(records)} records")
    print()

    results = []
    success_count = 0

    for idx, row in enumerate(records):
        date_str = row["[Date of Event]"]
        lat = row["[Latitude]"]
        lon = row["[Longitude]"]
        region1 = row["[Region1]"]
        region2 = row["[Region2]"]

        event_date = datetime.strptime(date_str[:10], "%Y-%m-%d")
        start_date = (event_date - timedelta(days=30)).strftime("%Y-%m-%d")
        end_date = event_date.strftime("%Y-%m-%d")

        print(
            f"Processing {idx + 1}/{len(records)}: {region2}, {region1} ({date_str[:10]})"
        )

        climate_data, error = fetch_and_parse(lat, lon, start_date, end_date)

        if climate_data:
            result = {
                "Date of Event": date_str[:10],
                "Latitude": lat,
                "Longitude": lon,
                "Region1": region1,
                "Region2": region2,
                "Climate_Start": start_date,
                "Climate_End": end_date,
            }
            result.update(climate_data)
            results.append(result)
            success_count += 1
            print(
                f"  OK: {climate_data['Days_Data']} days, Temp: {climate_data['Temp_Mean']}C, Precip: {climate_data['Precip_Total']}mm"
            )
        else:
            print(f"  ERROR: {error}")
            results.append(
                {
                    "Date of Event": date_str[:10],
                    "Latitude": lat,
                    "Longitude": lon,
                    "Region1": region1,
                    "Region2": region2,
                    "Climate_Start": start_date,
                    "Climate_End": end_date,
                    "Error": error,
                }
            )

        time.sleep(0.3)

    with open(output_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)

    print()
    print("=== COMPLETE ===")
    print(f"Output saved to: {output_csv}")
    print(f"Records with data: {success_count}/{len(records)}")


if __name__ == "__main__":
    main()
