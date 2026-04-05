import requests
import csv
import time
import os
from datetime import datetime, timedelta

NASA_POWER_API_URL = "https://power.larc.nasa.gov/api/temporal/daily/point"
PARAMETERS = ["T2M", "PRECTOTCORR", "RH2M", "WS2M"]

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_CSV = os.environ.get(
    "IDSP_INPUT_CSV", os.path.join(SCRIPT_DIR, "..", "malaria_master_export.csv")
)
OUTPUT_CSV = os.environ.get(
    "IDSP_OUTPUT_CSV", os.path.join(SCRIPT_DIR, "..", "climate_data.csv")
)


def fetch_and_parse(lat, lon, start_date_str, end_date_str):
    """Fetch and parse NASA Power API response"""
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

    response = requests.get(NASA_POWER_API_URL, params=params, timeout=30)

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
    print(f"Loading outbreak data from: {INPUT_CSV}")
    outbreaks = []
    with open(INPUT_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            outbreaks.append(row)

    print(f"Loaded {len(outbreaks)} outbreak records")
    print()

    results = []
    success_count = 0

    for idx, row in enumerate(outbreaks):
        date_str = row["[Date of Outbreak]"]
        lat = row["[Latitude]"]
        lon = row["[Longitude]"]
        state = row["[State]"]
        district = row["[District_Clean]"].replace("/", "_")

        outbreak_date = datetime.strptime(date_str[:10], "%Y-%m-%d")
        start_date = (outbreak_date - timedelta(days=30)).strftime("%Y-%m-%d")
        end_date = outbreak_date.strftime("%Y-%m-%d")

        print(
            f"Processing {idx + 1}/{len(outbreaks)}: {district}, {state} ({date_str[:10]})"
        )

        climate_data, error = fetch_and_parse(lat, lon, start_date, end_date)

        if climate_data:
            result = {
                "Date of Outbreak": date_str[:10],
                "Latitude": lat,
                "Longitude": lon,
                "State": state,
                "District": district,
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
                    "Date of Outbreak": date_str[:10],
                    "Latitude": lat,
                    "Longitude": lon,
                    "State": state,
                    "District": district,
                    "Climate_Start": start_date,
                    "Climate_End": end_date,
                    "Error": error,
                }
            )

        time.sleep(0.3)

    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)

    print()
    print("=== COMPLETE ===")
    print(f"Output saved to: {OUTPUT_CSV}")
    print(f"Records with data: {success_count}/{len(outbreaks)}")


if __name__ == "__main__":
    main()
