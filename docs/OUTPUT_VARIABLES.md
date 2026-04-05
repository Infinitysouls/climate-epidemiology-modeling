# Output Variables Documentation

Complete dictionary of all variables computed by the Climate Epidemiology Modeling Toolkit.

---

## Metadata (7 variables)

| Variable | Description | Unit |
|----------|-------------|------|
| `Date of Event` | Original event date | YYYY-MM-DD |
| `Latitude` | Location latitude | degrees |
| `Longitude` | Location longitude | degrees |
| `Region1` | Primary administrative region | - |
| `Region2` | Secondary administrative region | - |
| `Climate_Start` | Start of 30-day data window | YYYY-MM-DD |
| `Climate_End` | End of 30-day data window | YYYY-MM-DD |

---

## Temperature Statistics (20 variables)

| Variable | Description | Unit |
|----------|-------------|------|
| `Temp_Mean` | Mean temperature | °C |
| `Temp_Min` | Minimum temperature | °C |
| `Temp_Max` | Maximum temperature | °C |
| `Temp_Std` | Standard deviation | °C |
| `Temp_Range` | Temperature range (max - min) | °C |
| `Temp_P25` | 25th percentile | °C |
| `Temp_P50` | Median temperature | °C |
| `Temp_P75` | 75th percentile | °C |
| `Temp_P90` | 90th percentile | °C |
| `Temp_W1_Avg` | Week 1 mean (first 25% of days) | °C |
| `Temp_W2_Avg` | Week 2 mean | °C |
| `Temp_W3_Avg` | Week 3 mean | °C |
| `Temp_W4_Avg` | Week 4 mean (last 25% of days) | °C |
| `Hot_Days_Count` | Days with temp > 30°C | days |
| `Cold_Days_Count` | Days with temp < 15°C | days |
| `Very_Hot_Days` | Days with temp > 35°C | days |
| `Ideal_Days` | Days with temp 20-30°C | days |
| `Growing_Degree_Days` | Accumulated heat units (base 10°C) | °C-days |
| `Diurnal_Range_Avg` | Average daily temperature range | °C |
| `Temp_Trend` | Temperature trend direction (1=up, -1=down) | - |
| `Temp_Change_Rate` | Rate of temperature change | °C/day |
| `Temp_Skewness` | Temperature distribution skewness | - |
| `Temp_Kurtosis` | Temperature distribution kurtosis | - |

---

## Precipitation Statistics (18 variables)

| Variable | Description | Unit |
|----------|-------------|------|
| `Precip_Total` | Total precipitation | mm |
| `Precip_Days` | Number of rainy days | days |
| `Precip_Mean_Daily` | Mean daily precipitation | mm/day |
| `Precip_Max_Daily` | Maximum daily precipitation | mm |
| `Precip_Std` | Precipitation variability | mm |
| `Precip_P25` | 25th percentile | mm |
| `Precip_P75` | 75th percentile | mm |
| `No_Rain_Days` | Days with zero precipitation | days |
| `Rain_Probability` | Probability of rain | % |
| `Rain_Volume_CV` | Coefficient of variation | % |
| `Precip_W1_Total` | Week 1 precipitation total | mm |
| `Precip_W2_Total` | Week 2 precipitation total | mm |
| `Precip_W3_Total` | Week 3 precipitation total | mm |
| `Precip_W4_Total` | Week 4 precipitation total | mm |
| `Heavy_Rain_Days` | Days with precip > 10mm | days |
| `Very_Heavy_Rain_Days` | Days with precip > 25mm | days |
| `Moderate_Rain_Days` | Days with precip 5-10mm | days |
| `Cumulative_7d` | 7-day cumulative precipitation | mm |
| `Cumulative_14d` | 14-day cumulative precipitation | mm |
| `Wet_Days_Streak` | Longest consecutive wet period | days |
| `Dry_Days_Streak` | Longest consecutive dry period | days |
| `Precip_Intensity_Ratio` | Heavy rain to total ratio | - |
| `Precip_Intensity` | Mean precipitation on rainy days | mm/day |

---

## Humidity Statistics (12 variables)

| Variable | Description | Unit |
|----------|-------------|------|
| `Humidity_Mean` | Mean relative humidity | % |
| `Humidity_Min` | Minimum humidity | % |
| `Humidity_Max` | Maximum humidity | % |
| `Humidity_Std` | Humidity variability | % |
| `Humidity_Range` | Humidity range (max - min) | % |
| `Humidity_P25` | 25th percentile | % |
| `Humidity_P75` | 75th percentile | % |
| `Humidity_W1_Avg` | Week 1 mean humidity | % |
| `Humidity_W2_Avg` | Week 2 mean humidity | % |
| `Humidity_W3_Avg` | Week 3 mean humidity | % |
| `Humidity_W4_Avg` | Week 4 mean humidity | % |
| `High_Humidity_Days` | Days with humidity > 80% | days |
| `Low_Humidity_Days` | Days with humidity < 40% | days |
| `Humidity_Change` | Change in humidity over period | % |

---

## Wind Statistics (10 variables)

| Variable | Description | Unit |
|----------|-------------|------|
| `Wind_Mean` | Mean wind speed | m/s |
| `Wind_Max` | Maximum wind speed | m/s |
| `Wind_Std` | Wind variability | m/s |
| `Wind_P25` | 25th percentile | m/s |
| `Wind_P75` | 75th percentile | m/s |
| `Calm_Days` | Days with wind < 2 m/s | days |
| `Windy_Days` | Days with wind > 5 m/s | days |
| `Moderate_Wind_Days` | Days with wind 2-5 m/s | days |
| `Very_Windy_Days` | Days with wind > 8 m/s | days |
| `Calm_Percentage` | Percentage of calm days | % |
| `Wind_Gust_Proxy` | Estimated wind gusts | m/s |

---

## Two-Variable Interactions (12 variables)

| Variable | Description | Formula/Notes |
|----------|-------------|--------------|
| `Heat_Index_Celsius` | Apparent temperature | f(T, RH) |
| `Discomfort_Index` | Thermal discomfort | (T + RH) / 2 |
| `Tropical_Nights` | Nights with Tmin > 20°C | days |
| `Warm_Nights` | Nights with Tmin > 25°C | days |
| `Summer_Season` | Days with T > 25 & RH > 70% | days |
| `Muggy_Days` | Days with T > 20 & RH > 80% | days |
| `Dry_Heat_Days` | Days with T > 30 & RH < 40% | days |
| `Humid_Cold_Days` | Days with T < 15 & RH > 70% | days |
| `Transmission_Risk_Proxy` | Climate transmission risk | T × RH / 100 |
| `Rain_Spread_Risk` | Rain dispersal by wind | P × Wind |
| `Precip_Wind_Ratio` | Precipitation to wind ratio | P / Wind |
| `Evaporation_Proxy` | Estimated evaporation | f(T, RH, Wind) |
| `Drying_Rate` | Soil drying indicator | f(T, RH) |

---

## Disease/Epidemiological Indices (12 variables)

| Variable | Description | Formula/Notes |
|----------|-------------|--------------|
| `EIP_Days` | Extrinsic Incubation Period | f(T) - parasite development time |
| `EIP_Category` | EIP risk level | Low / Medium / High |
| `Larval_Survival` | Immature vector survival | f(T) - larval viability |
| `Adult_Survival` | Adult vector survival | f(T, RH) - adult viability |
| `Vector_Fecundity` | Vector breeding capacity | f(T, RH) |
| `Gonotrophic_Cycle` | Egg laying cycle duration | f(T) - days |
| `Blood_Feeding_Rate` | Vector feeding frequency | f(T) - % |
| `Vector_Density_Index` | Estimated vector density | composite score |
| `IR_Score` | Infection risk score | composite |
| `Outbreak_Risk_30d` | 30-day outbreak risk | 0-3 scale |
| `Critical_Threshold` | Risk threshold exceeded | 0 / 1 |
| `Mosquito_Dev_Days` | Suitable vector development days | days with T>20, RH>60, P>0 |
| `Persistence_Days` | Consecutive risk days | days |

---

## Multi-Variable Composites (10 variables)

| Variable | Description | Formula/Notes |
|----------|-------------|--------------|
| `Combined_Stress` | Combined environmental stress | f(T, RH, Wind) |
| `Meteorological_WBGT` | Wet Bulb Globe Temperature | heat stress index |
| `Pet_Proxy` | Potential Evapotranspiration proxy | f(T, RH, Wind) |
| `Aridity_Index` | Aridity measure | P / (T + 10) |
| `Moisture_Index` | Moisture availability | (RH × P) / (T + 20) |
| `Climate_Health_Risk` | Overall climate health risk | composite 0-100 |
| `Vector_Capacity` | Vector transmission capacity | f(T, RH, P) |
| `Wet_Season_Indicator` | Wet season indicator | 0 / 1 |
| `Stagnant_Air_Days` | Calm humid days | days with WS < 2 |
| `Heat_Stress_Days` | Days with heat stress | days with HI > 35 |
| `Climate_Suitability_Index` | Overall climate suitability | composite 0-100 |

---

## Temporal Features (4 variables)

| Variable | Description | Unit |
|----------|-------------|------|
| `Month` | Event month | 1-12 |
| `Week_Number` | ISO week number | 1-53 |
| `Day_Of_Year` | Day of year | 1-366 |
| `Season` | Season classification | winter/summer/monsoon/post_monsoon |

---

## Lagged Effects (6 variables)

| Variable | Description | Unit |
|----------|-------------|------|
| `Temp_Lag_7d` | 7-day lagged temperature | °C |
| `Temp_Lag_14d` | 14-day lagged temperature | °C |
| `Precip_Lag_7d` | 7-day lagged precipitation | mm |
| `Precip_Lag_14d` | 14-day lagged precipitation | mm |
| `Temp_Anomaly` | Temperature deviation from mean | °C |
| `Precip_Anomaly` | Precipitation deviation from mean | mm |

---

## Summary Indicators (3 variables)

| Variable | Description | Unit |
|----------|-------------|------|
| `Days_Data` | Number of days with data | days |
| `Valid_Data_Flag` | Data quality flag (1=good) | 0/1 |
| `Processing_Status` | Processing status | text |

---

## Default Thresholds

| Threshold | Value | Used For |
|-----------|-------|----------|
| Hot day | > 30°C | Hot_Days_Count |
| Very hot day | > 35°C | Very_Hot_Days |
| Cold day | < 15°C | Cold_Days_Count |
| Ideal temp | 20-30°C | Ideal_Days |
| Heavy rain | > 10mm | Heavy_Rain_Days |
| Very heavy rain | > 25mm | Very_Heavy_Rain_Days |
| Moderate rain | 5-10mm | Moderate_Rain_Days |
| High humidity | > 80% | High_Humidity_Days |
| Low humidity | < 40% | Low_Humidity_Days |
| Calm wind | < 2 m/s | Calm_Days |
| Windy | > 5 m/s | Windy_Days |
| Tropical night | Tmin > 20°C | Tropical_Nights |
| Warm night | Tmin > 25°C | Warm_Nights |
| Heat stress | HI > 35 | Heat_Stress_Days |

---

## Variable Count Summary

| Category | Count |
|----------|-------|
| Metadata | 7 |
| Temperature | 22 |
| Precipitation | 22 |
| Humidity | 13 |
| Wind | 10 |
| Interactions | 12 |
| Disease Indices | 13 |
| Composites | 10 |
| Temporal | 4 |
| Lagged | 6 |
| Summary | 3 |
| **TOTAL** | **122 variables** |

---

## Usage Notes

1. **Missing Data**: Variables may be `null` if insufficient daily data
2. **Data Quality**: Check `Valid_Data_Flag` (1 = ≥25 days of data)
3. **Thresholds**: Can be modified in source code for custom definitions
4. **Derived Variables**: Some indices are estimates based on empirical relationships

---

## References

- EIP calculations based on standard entomological literature
- Heat index using NWS apparent temperature formula
- Vector biology indices derived from mosquito ecology studies
