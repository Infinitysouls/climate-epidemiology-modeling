import argparse
import requests
import csv
import time
import os
import math
from datetime import datetime, timedelta
from collections import defaultdict

CLIMATE_API_URL = "https://power.larc.nasa.gov/api/temporal/daily/point"
PARAMETERS = ["T2M", "PRECTOTCORR", "RH2M", "WS2M"]

DEFAULT_INPUT = os.path.join(os.path.dirname(__file__), "..", "data.csv")
DEFAULT_OUTPUT = os.path.join(os.path.dirname(__file__), "..", "climate_output.csv")


def safe_div(a, b, default=0):
    return round(a / b, 2) if b != 0 else default


def safe_mean(lst, default=None):
    return round(sum(lst) / len(lst), 2) if lst else default


def safe_std(lst):
    if len(lst) < 2:
        return 0
    mean = sum(lst) / len(lst)
    variance = sum((x - mean) ** 2 for x in lst) / (len(lst) - 1)
    return round(math.sqrt(variance), 2)


def safe_percentile(lst, p):
    if not lst:
        return None
    sorted_lst = sorted(lst)
    idx = (len(sorted_lst) - 1) * p / 100
    floor = int(idx)
    ceil = floor + 1
    if ceil >= len(sorted_lst):
        return sorted_lst[-1]
    return round(sorted_lst[floor] * (ceil - idx) + sorted_lst[ceil] * (idx - floor), 2)


def count_consecutive(lst, threshold, direction="gt"):
    max_streak = current = 0
    for val in lst:
        if (direction == "gt" and val > threshold) or (
            direction == "lt" and val < threshold
        ):
            current += 1
            max_streak = max(max_streak, current)
        else:
            current = 0
    return max_streak


def get_season(month):
    if month in [12, 1, 2]:
        return "winter"
    elif month in [3, 4, 5]:
        return "summer"
    elif month in [6, 7, 8, 9]:
        return "monsoon"
    else:
        return "post_monsoon"


def fetch_daily_data(lat, lon, start_date_str, end_date_str):
    """Fetch raw daily data from API"""
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
        return None

    try:
        data = response.json()
    except:
        return None

    if "properties" not in data or "parameter" not in data["properties"]:
        return None

    param_data = data["properties"]["parameter"]

    daily_data = defaultdict(dict)
    for date_key, value in param_data.get("T2M", {}).items():
        if isinstance(value, (int, float)):
            daily_data[date_key]["T2M"] = value
    for date_key, value in param_data.get("PRECTOTCORR", {}).items():
        if isinstance(value, (int, float)):
            daily_data[date_key]["PRECTOTCORR"] = value
    for date_key, value in param_data.get("RH2M", {}).items():
        if isinstance(value, (int, float)):
            daily_data[date_key]["RH2M"] = value
    for date_key, value in param_data.get("WS2M", {}).items():
        if isinstance(value, (int, float)):
            daily_data[date_key]["WS2M"] = value

    return dict(daily_data)


def compute_temperature_stats(daily_data):
    temps = [v["T2M"] for v in daily_data.values() if "T2M" in v]
    if not temps:
        return {}

    stats = {}
    sorted_temps = sorted(temps)
    n = len(temps)

    stats["Temp_Mean"] = safe_mean(temps)
    stats["Temp_Min"] = round(min(temps), 2)
    stats["Temp_Max"] = round(max(temps), 2)
    stats["Temp_Std"] = safe_std(temps)
    stats["Temp_Range"] = round(max(temps) - min(temps), 2)
    stats["Temp_P50"] = sorted_temps[n // 2]
    stats["Temp_P25"] = safe_percentile(temps, 25)
    stats["Temp_P75"] = safe_percentile(temps, 75)
    stats["Temp_P90"] = safe_percentile(temps, 90)

    if len(temps) >= 4:
        quarter = n // 4
        stats["Temp_W1_Avg"] = safe_mean(temps[:quarter])
        stats["Temp_W2_Avg"] = safe_mean(temps[quarter : quarter * 2])
        stats["Temp_W3_Avg"] = safe_mean(temps[quarter * 2 : quarter * 3])
        stats["Temp_W4_Avg"] = safe_mean(temps[quarter * 3 :])
    else:
        stats["Temp_W1_Avg"] = safe_mean(temps[: max(1, n // 2)])
        stats["Temp_W2_Avg"] = safe_mean(temps[max(1, n // 2) :])
        stats["Temp_W3_Avg"] = None
        stats["Temp_W4_Avg"] = None

    stats["Hot_Days_Count"] = len([t for t in temps if t > 30])
    stats["Cold_Days_Count"] = len([t for t in temps if t < 15])
    stats["Very_Hot_Days"] = len([t for t in temps if t > 35])
    stats["Ideal_Days"] = len([t for t in temps if 20 <= t <= 30])
    stats["Growing_Degree_Days"] = round(sum(max(0, t - 10) for t in temps), 2)

    daily_ranges = []
    for v in daily_data.values():
        if "T2M" in v:
            daily_ranges.append(0)
    if len(sorted_temps) >= 2:
        stats["Diurnal_Range_Avg"] = round((stats["Temp_Range"]) / 2, 2)
    else:
        stats["Diurnal_Range_Avg"] = 0

    first_half = temps[: n // 2]
    second_half = temps[n // 2 :]
    if first_half and second_half:
        stats["Temp_Trend"] = (
            1 if safe_mean(second_half) > safe_mean(first_half) else -1
        )
    else:
        stats["Temp_Trend"] = 0

    stats["Temp_Change_Rate"] = (
        round((temps[-1] - temps[0]) / max(1, n - 1), 4) if n > 1 else 0
    )

    if temps:
        mean_t = sum(temps) / len(temps)
        n = len(temps)
        if n > 2:
            m = (
                n * sum(i * t for i, t in enumerate(temps)) - sum(range(n)) * sum(temps)
            ) / (n * sum(i**2 for i in range(n)) - (sum(range(n))) ** 2)
            stats["Temp_Skewness"] = round(m, 4) if m else 0
        else:
            stats["Temp_Skewness"] = 0
    else:
        stats["Temp_Skewness"] = 0

    stats["Temp_Kurtosis"] = 0

    return stats


def compute_precipitation_stats(daily_data):
    precips = [v["PRECTOTCORR"] for v in daily_data.values() if "PRECTOTCORR" in v]
    if not precips:
        return {}

    stats = {}
    sorted_precips = sorted(precips)
    n = len(precips)

    stats["Precip_Total"] = round(sum(precips), 2)
    stats["Precip_Days"] = len([p for p in precips if p > 0])
    stats["Precip_Mean_Daily"] = safe_mean(precips)
    stats["Precip_Max_Daily"] = round(max(precips), 2) if precips else 0
    stats["Precip_Std"] = safe_std(precips)
    stats["Precip_P25"] = safe_percentile(precips, 25)
    stats["Precip_P75"] = safe_percentile(precips, 75)
    stats["No_Rain_Days"] = len([p for p in precips if p == 0])
    stats["Rain_Probability"] = round((stats["Precip_Days"] / max(1, n)) * 100, 2)
    stats["Rain_Volume_CV"] = (
        round((safe_std(precips) / safe_mean(precips) * 100), 2)
        if safe_mean(precips)
        else 0
    )

    if len(precips) >= 4:
        quarter = n // 4
        stats["Precip_W1_Total"] = round(sum(precips[:quarter]), 2)
        stats["Precip_W2_Total"] = round(sum(precips[quarter : quarter * 2]), 2)
        stats["Precip_W3_Total"] = round(sum(precips[quarter * 2 : quarter * 3]), 2)
        stats["Precip_W4_Total"] = round(sum(precips[quarter * 3 :]), 2)
    else:
        half = n // 2
        stats["Precip_W1_Total"] = round(sum(precips[:half]), 2)
        stats["Precip_W2_Total"] = round(sum(precips[half:]), 2)
        stats["Precip_W3_Total"] = 0
        stats["Precip_W4_Total"] = 0

    stats["Heavy_Rain_Days"] = len([p for p in precips if p > 10])
    stats["Very_Heavy_Rain_Days"] = len([p for p in precips if p > 25])
    stats["Moderate_Rain_Days"] = len([p for p in precips if 5 <= p <= 10])

    stats["Cumulative_7d"] = (
        round(sum(precips[-7:]), 2) if len(precips) >= 7 else round(sum(precips), 2)
    )
    stats["Cumulative_14d"] = (
        round(sum(precips[-14:]), 2) if len(precips) >= 14 else round(sum(precips), 2)
    )

    stats["Wet_Days_Streak"] = count_consecutive(precips, 0, "gt")
    stats["Dry_Days_Streak"] = count_consecutive(precips, 0, "eq")

    rainy_precips = [p for p in precips if p > 0]
    stats["Precip_Intensity_Ratio"] = (
        round(stats["Precip_Max_Daily"] / max(1, stats["Precip_Total"]), 4)
        if stats["Precip_Total"] > 0
        else 0
    )

    precip_rainy = [p for p in precips if p > 0]
    stats["Precip_Intensity"] = safe_mean(precip_rainy) if precip_rainy else 0

    return stats


def compute_humidity_stats(daily_data):
    humidities = [v["RH2M"] for v in daily_data.values() if "RH2M" in v]
    if not humidities:
        return {}

    stats = {}
    n = len(humidities)
    sorted_humidities = sorted(humidities)

    stats["Humidity_Mean"] = safe_mean(humidities)
    stats["Humidity_Min"] = round(min(humidities), 2)
    stats["Humidity_Max"] = round(max(humidities), 2)
    stats["Humidity_Std"] = safe_std(humidities)
    stats["Humidity_Range"] = round(max(humidities) - min(humidities), 2)
    stats["Humidity_P25"] = safe_percentile(humidities, 25)
    stats["Humidity_P75"] = safe_percentile(humidities, 75)

    if len(humidities) >= 4:
        quarter = n // 4
        stats["Humidity_W1_Avg"] = safe_mean(humidities[:quarter])
        stats["Humidity_W2_Avg"] = safe_mean(humidities[quarter : quarter * 2])
        stats["Humidity_W3_Avg"] = safe_mean(humidities[quarter * 2 : quarter * 3])
        stats["Humidity_W4_Avg"] = safe_mean(humidities[quarter * 3 :])
    else:
        half = n // 2
        stats["Humidity_W1_Avg"] = safe_mean(humidities[:half])
        stats["Humidity_W2_Avg"] = safe_mean(humidities[half:])
        stats["Humidity_W3_Avg"] = None
        stats["Humidity_W4_Avg"] = None

    stats["High_Humidity_Days"] = len([h for h in humidities if h > 80])
    stats["Low_Humidity_Days"] = len([h for h in humidities if h < 40])

    first_half = humidities[: n // 2]
    second_half = humidities[n // 2 :]
    if first_half and second_half:
        stats["Humidity_Change"] = round(
            safe_mean(second_half) - safe_mean(first_half), 2
        )
    else:
        stats["Humidity_Change"] = 0

    return stats


def compute_wind_stats(daily_data):
    winds = [v["WS2M"] for v in daily_data.values() if "WS2M" in v]
    if not winds:
        return {}

    stats = {}
    n = len(winds)

    stats["Wind_Mean"] = safe_mean(winds)
    stats["Wind_Max"] = round(max(winds), 2)
    stats["Wind_Std"] = safe_std(winds)
    stats["Wind_P25"] = safe_percentile(winds, 25)
    stats["Wind_P75"] = safe_percentile(winds, 75)

    stats["Calm_Days"] = len([w for w in winds if w < 2])
    stats["Windy_Days"] = len([w for w in winds if w > 5])
    stats["Moderate_Wind_Days"] = len([w for w in winds if 2 <= w <= 5])
    stats["Very_Windy_Days"] = len([w for w in winds if w > 8])

    stats["Calm_Percentage"] = round((stats["Calm_Days"] / max(1, n)) * 100, 2)
    stats["Wind_Gust_Proxy"] = round(stats["Wind_Max"] * 1.5, 2)

    return stats


def compute_interaction_indices(
    temp_stats, precip_stats, humid_stats, wind_stats, daily_data
):
    indices = {}

    t_mean = temp_stats.get("Temp_Mean", 25)
    rh_mean = humid_stats.get("Humidity_Mean", 50)

    indices["Heat_Index_Celsius"] = round(t_mean + 0.5 * (rh_mean - 40), 2)
    indices["Discomfort_Index"] = round((t_mean + rh_mean) / 2, 2)

    indices["Tropical_Nights"] = len(
        [v.get("T2M") for v in daily_data.values() if v.get("T2M", 0) > 20]
    )
    indices["Warm_Nights"] = len(
        [v.get("T2M") for v in daily_data.values() if v.get("T2M", 0) > 25]
    )

    hot_humid_days = 0
    for v in daily_data.values():
        if v.get("T2M", 0) > 25 and v.get("RH2M", 0) > 70:
            hot_humid_days += 1
    indices["Summer_Season"] = hot_humid_days

    muggy_days = len(
        [
            v
            for v in daily_data.values()
            if v.get("T2M", 0) > 20 and v.get("RH2M", 0) > 80
        ]
    )
    indices["Muggy_Days"] = muggy_days

    dry_heat_days = len(
        [
            v
            for v in daily_data.values()
            if v.get("T2M", 0) > 30 and v.get("RH2M", 0) < 40
        ]
    )
    indices["Dry_Heat_Days"] = dry_heat_days

    humid_cold_days = len(
        [
            v
            for v in daily_data.values()
            if v.get("T2M", 0) < 15 and v.get("RH2M", 0) > 70
        ]
    )
    indices["Humid_Cold_Days"] = humid_cold_days

    indices["Transmission_Risk_Proxy"] = round((t_mean * rh_mean) / 100, 2)

    precips = [v["PRECTOTCORR"] for v in daily_data.values() if "PRECTOTCORR" in v]
    winds = [v["WS2M"] for v in daily_data.values() if "WS2M" in v]
    rain_spread = 0
    if precips and winds:
        rain_spread = round(sum(precips) * safe_mean(winds), 2)
    indices["Rain_Spread_Risk"] = rain_spread

    if precips and temp_stats:
        precip_wind_corr = safe_div(sum(precips), len(winds), 0) if winds else 0
    else:
        precip_wind_corr = 0
    indices["Precip_Wind_Ratio"] = round(precip_wind_corr, 2)

    indices["Evaporation_Proxy"] = (
        round(t_mean * (100 - rh_mean) * 0.01 * safe_mean(winds), 2) if winds else 0
    )
    indices["Drying_Rate"] = round(t_mean * (100 - rh_mean) * 0.05, 2)

    return indices


def compute_disease_indices(temp_stats, precip_stats, humid_stats, daily_data):
    indices = {}

    t_mean = temp_stats.get("Temp_Mean", 25)

    eip_days = round(10 / ((t_mean - 20) / 7 + 0.1), 1) if t_mean > 20 else 30
    indices["EIP_Days"] = max(5, min(30, eip_days))

    if t_mean >= 30:
        indices["EIP_Category"] = "High"
    elif t_mean >= 25:
        indices["EIP_Category"] = "Medium"
    else:
        indices["EIP_Category"] = "Low"

    larv_surv = max(0, min(100, (t_mean - 15) * 5))
    indices["Larval_Survival"] = round(larv_surv, 2)

    adult_surv = max(
        0, min(100, (40 - t_mean) * 3 + humid_stats.get("Humidity_Mean", 50))
    )
    indices["Adult_Survival"] = round(adult_surv, 2)

    indices["Vector_Fecundity"] = round(
        max(0, (t_mean - 20) * humid_stats.get("Humidity_Mean", 50) / 100), 2
    )

    gonotrophic = round(2 + (25 - t_mean) / 3, 1) if t_mean < 30 else 5
    indices["Gonotrophic_Cycle"] = max(2, min(10, gonotrophic))

    feeding_rate = max(0, min(100, 100 - (t_mean - 25) * 5))
    indices["Blood_Feeding_Rate"] = round(feeding_rate, 2)

    vector_density = (
        indices["Larval_Survival"]
        * indices["Adult_Survival"]
        * indices["Vector_Fecundity"]
        / 10000
    )
    indices["Vector_Density_Index"] = round(max(0, min(100, vector_density)), 2)

    ir_score = (
        temp_stats.get("Temp_Mean", 25)
        * humid_stats.get("Humidity_Mean", 50)
        * precip_stats.get("Precip_Days", 0)
    ) / 1000
    indices["IR_Score"] = round(ir_score, 2)

    outbreak_risk = 0
    if (
        t_mean >= 25
        and humid_stats.get("Humidity_Mean", 0) >= 60
        and precip_stats.get("Precip_Total", 0) > 10
    ):
        outbreak_risk = 3
    elif t_mean >= 20 and humid_stats.get("Humidity_Mean", 0) >= 50:
        outbreak_risk = 2
    elif t_mean >= 15:
        outbreak_risk = 1
    indices["Outbreak_Risk_30d"] = outbreak_risk

    indices["Critical_Threshold"] = 1 if outbreak_risk >= 3 else 0

    mosq_days = len(
        [
            v
            for v in daily_data.values()
            if v.get("T2M", 0) > 20
            and v.get("RH2M", 0) > 60
            and v.get("PRECTOTCORR", 0) > 0
        ]
    )
    indices["Mosquito_Dev_Days"] = mosq_days

    persistence = count_consecutive(
        [
            1 if v.get("T2M", 0) > 20 and v.get("RH2M", 0) > 60 else 0
            for v in daily_data.values()
        ],
        0,
        "gt",
    )
    indices["Persistence_Days"] = persistence

    return indices


def compute_composite_indices(
    temp_stats, precip_stats, humid_stats, wind_stats, daily_data
):
    indices = {}

    combined_stress = (
        temp_stats.get("Temp_Mean", 25)
        + humid_stats.get("Humidity_Mean", 50) / 2
        + wind_stats.get("Wind_Mean", 2) * 2
    )
    indices["Combined_Stress"] = round(combined_stress, 2)

    t_mean = temp_stats.get("Temp_Mean", 25)
    p_total = precip_stats.get("Precip_Total", 0)
    rh_mean = humid_stats.get("Humidity_Mean", 50)
    ws_mean = wind_stats.get("Wind_Mean", 2)

    indices["Meteorological_WBGT"] = round(
        0.567 * t_mean + 0.214 * rh_mean - 0.6 * ws_mean + 1.2, 2
    )

    pet_proxy = round(t_mean * (1 + (100 - rh_mean) / 100) * (1 + ws_mean / 100) / 3, 2)
    indices["Pet_Proxy"] = pet_proxy

    aridity = safe_div(p_total, (t_mean + 10), 0)
    indices["Aridity_Index"] = round(aridity, 4)

    moisture = safe_div(rh_mean * p_total, (t_mean + 20), 0)
    indices["Moisture_Index"] = round(moisture, 2)

    climate_risk = (
        (
            temp_stats.get("Temp_Mean", 25) / 40
            + humid_stats.get("Humidity_Mean", 50) / 100
            + safe_div(p_total, 100, 0)
        )
        / 3
        * 100
    )
    indices["Climate_Health_Risk"] = round(climate_risk, 2)

    vector_cap = (
        temp_stats.get("Temp_Mean", 25)
        / 40
        * humid_stats.get("Humidity_Mean", 50)
        / 100
        * min(1, precip_stats.get("Precip_Total", 0) / 100)
    )
    indices["Vector_Capacity"] = round(vector_cap * 100, 2)

    indices["Wet_Season_Indicator"] = 1 if p_total > 100 else 0

    stagnant_days = sum(1 for v in daily_data.values() if v.get("WS2M", 10) < 2)
    indices["Stagnant_Air_Days"] = stagnant_days

    heat_index_vals = [
        v.get("T2M", 20) + 0.5 * (v.get("RH2M", 40) - 40) for v in daily_data.values()
    ]
    heat_stress = len([hi for hi in heat_index_vals if hi > 35])
    indices["Heat_Stress_Days"] = heat_stress

    suitability = (
        temp_stats.get("Temp_Mean", 25) / 40 * 0.3
        + humid_stats.get("Humidity_Mean", 50) / 100 * 0.3
        + min(precip_stats.get("Precip_Total", 0) / 200, 1) * 0.2
        + max(0, 1 - wind_stats.get("Wind_Mean", 2) / 10) * 0.2
    )
    indices["Climate_Suitability_Index"] = round(suitability * 100, 2)

    return indices


def compute_temporal_features(event_date):
    features = {}
    features["Month"] = event_date.month
    features["Week_Number"] = event_date.isocalendar()[1]
    features["Day_Of_Year"] = event_date.timetuple().tm_yday
    features["Season"] = get_season(event_date.month)
    return features


def compute_lagged_effects(daily_data):
    features = {}

    sorted_dates = sorted(daily_data.keys())

    if len(sorted_dates) >= 8:
        first_half_temps = [
            daily_data[d].get("T2M")
            for d in sorted_dates[: len(sorted_dates) // 2]
            if daily_data[d].get("T2M")
        ]
        second_half_temps = [
            daily_data[d].get("T2M")
            for d in sorted_dates[len(sorted_dates) // 2 :]
            if daily_data[d].get("T2M")
        ]
        features["Temp_Lag_7d"] = (
            safe_mean(second_half_temps) if second_half_temps else None
        )
    else:
        features["Temp_Lag_7d"] = None

    features["Temp_Lag_14d"] = None

    if len(sorted_dates) >= 8:
        first_half_precips = [
            daily_data[d].get("PRECTOTCORR")
            for d in sorted_dates[: len(sorted_dates) // 2]
            if daily_data[d].get("PRECTOTCORR")
        ]
        features["Precip_Lag_7d"] = (
            round(sum(first_half_precips), 2) if first_half_precips else 0
        )
    else:
        features["Precip_Lag_7d"] = None

    features["Precip_Lag_14d"] = None

    all_temps = [v.get("T2M") for v in daily_data.values() if v.get("T2M") is not None]
    if all_temps:
        mean_temp = sum(all_temps) / len(all_temps)
        features["Temp_Anomaly"] = (
            round(all_temps[-1] - mean_temp, 2) if all_temps else 0
        )
    else:
        features["Temp_Anomaly"] = 0

    all_precips = [
        v.get("PRECTOTCORR")
        for v in daily_data.values()
        if v.get("PRECTOTCORR") is not None
    ]
    if all_precips:
        mean_precip = sum(all_precips) / len(all_precips) if all_precips else 0
        features["Precip_Anomaly"] = (
            round(all_precips[-1] - mean_precip, 2) if all_precips else 0
        )
    else:
        features["Precip_Anomaly"] = 0

    return features


def compute_all_metrics(daily_data, event_date):
    temp_stats = compute_temperature_stats(daily_data)
    precip_stats = compute_precipitation_stats(daily_data)
    humid_stats = compute_humidity_stats(daily_data)
    wind_stats = compute_wind_stats(daily_data)

    interaction = compute_interaction_indices(
        temp_stats, precip_stats, humid_stats, wind_stats, daily_data
    )
    disease = compute_disease_indices(temp_stats, precip_stats, humid_stats, daily_data)
    composite = compute_composite_indices(
        temp_stats, precip_stats, humid_stats, wind_stats, daily_data
    )
    temporal = compute_temporal_features(event_date)
    lagged = compute_lagged_effects(daily_data)

    all_metrics = {}
    all_metrics.update(temp_stats)
    all_metrics.update(precip_stats)
    all_metrics.update(humid_stats)
    all_metrics.update(wind_stats)
    all_metrics.update(interaction)
    all_metrics.update(disease)
    all_metrics.update(composite)
    all_metrics.update(temporal)
    all_metrics.update(lagged)

    all_metrics["Days_Data"] = len(daily_data)
    all_metrics["Valid_Data_Flag"] = 1 if len(daily_data) >= 25 else 0
    all_metrics["Processing_Status"] = "Success"

    return all_metrics


def main():
    parser = argparse.ArgumentParser(
        description="Fetch and compute climate metrics for epidemiological research"
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

    if not os.path.exists(input_csv):
        print(f"Error: Input file not found: {input_csv}")
        return

    print(f"Loading data from: {input_csv}")

    records = []
    with open(input_csv, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append(row)

    if not records:
        print("Error: No records found in input file")
        return

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

        try:
            event_date = datetime.strptime(date_str[:10], "%Y-%m-%d")
        except:
            print(f"Skipping row {idx + 1}: Invalid date format")
            continue

        start_date = (event_date - timedelta(days=30)).strftime("%Y-%m-%d")
        end_date = event_date.strftime("%Y-%m-%d")

        print(
            f"Processing {idx + 1}/{len(records)}: {region2}, {region1} ({date_str[:10]})"
        )

        daily_data = fetch_daily_data(lat, lon, start_date, end_date)

        if daily_data and len(daily_data) >= 10:
            result = {
                "Date of Event": date_str[:10],
                "Latitude": lat,
                "Longitude": lon,
                "Region1": region1,
                "Region2": region2,
                "Climate_Start": start_date,
                "Climate_End": end_date,
            }

            metrics = compute_all_metrics(daily_data, event_date)
            result.update(metrics)
            results.append(result)
            success_count += 1

            print(
                f"  OK: {len(daily_data)} days, Temp: {metrics.get('Temp_Mean', 'N/A')}C, "
                f"Precip: {metrics.get('Precip_Total', 'N/A')}mm, Variables: {len(result)}"
            )
        else:
            print(
                f"  ERROR: Insufficient data ({len(daily_data) if daily_data else 0} days)"
            )
            result = {
                "Date of Event": date_str[:10],
                "Latitude": lat,
                "Longitude": lon,
                "Region1": region1,
                "Region2": region2,
                "Climate_Start": start_date,
                "Climate_End": end_date,
                "Days_Data": len(daily_data) if daily_data else 0,
                "Valid_Data_Flag": 0,
                "Processing_Status": "Insufficient data",
            }
            results.append(result)

        time.sleep(0.3)

    if results:
        with open(output_csv, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=results[0].keys())
            writer.writeheader()
            writer.writerows(results)

        print()
        print("=" * 60)
        print("COMPLETE")
        print("=" * 60)
        print(f"Output saved to: {output_csv}")
        print(f"Successful: {success_count}/{len(records)}")
        print(f"Total variables computed: {len(results[0]) - 7 if results else 0}")
    else:
        print("Error: No results to write")


if __name__ == "__main__":
    main()
