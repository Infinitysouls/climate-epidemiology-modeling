# Output Variables Documentation

Complete dictionary of all 122 variables computed by the Climate Epidemiology Modeling Toolkit.

---

## Scientific Background

### Climate-Disease Transmission Framework

The toolkit computes variables based on the conceptual framework linking environmental conditions to infectious disease transmission:

```
Environmental Conditions → Vector Biology → Transmission Potential → Outbreak Risk
     (T, P, RH, Wind)    (EIP, Survival)     (Vector Capacity)      (Risk Score)
```

### Key Epidemiological Relationships

| Variable Category | Scientific Relevance |
|------------------|---------------------|
| Temperature | Affects pathogen development rate, vector metabolism, survival |
| Precipitation | Creates breeding sites, influences vector abundance |
| Humidity | Affects vector desiccation resistance, biting behavior |
| Wind | Influences vector dispersal, pathogen spread |
| Disease Indices | Integrate multiple factors for transmission estimates |

---

## Metadata (7 variables)

| Variable | Type | Description | Unit |
|----------|------|-------------|------|
| `Date of Event` | Date | Original event/outbreak date | YYYY-MM-DD |
| `Latitude` | Float | Location latitude | degrees |
| `Longitude` | Float | Location longitude | degrees |
| `Region1` | String | Primary administrative region (e.g., State/Province) | - |
| `Region2` | String | Secondary administrative region (e.g., District/County) | - |
| `Climate_Start` | Date | Start of 30-day climate data window | YYYY-MM-DD |
| `Climate_End` | Date | End of 30-day climate data window | YYYY-MM-DD |

---

## Temperature Statistics (22 variables)

### Basic Statistics

| Variable | Description | Scientific Relevance | Unit |
|----------|-------------|---------------------|------|
| `Temp_Mean` | Mean temperature over 30-day window | Primary driver of EIP and vector metabolism | °C |
| `Temp_Min` | Minimum temperature | Affects overnight vector survival | °C |
| `Temp_Max` | Maximum temperature | Influences stress thresholds | °C |
| `Temp_Std` | Standard deviation | Indicates temperature variability | °C |
| `Temp_Range` | Temperature range (max - min) | Daily thermal amplitude | °C |

### Percentiles

| Variable | Description | Scientific Relevance | Unit |
|----------|-------------|---------------------|------|
| `Temp_P25` | 25th percentile | Lower temperature exposure | °C |
| `Temp_P50` | Median temperature | Central tendency | °C |
| `Temp_P75` | 75th percentile | Upper temperature exposure | °C |
| `Temp_P90` | 90th percentile | Extreme high temperature | °C |

### Weekly Averages

| Variable | Description | Scientific Relevance | Unit |
|----------|-------------|---------------------|------|
| `Temp_W1_Avg` | Week 1 mean (first 25% of days) | Early period temperature | °C |
| `Temp_W2_Avg` | Week 2 mean | Mid-period temperature | °C |
| `Temp_W3_Avg` | Week 3 mean | Late period temperature | °C |
| `Temp_W4_Avg` | Week 4 mean (last 25% of days) | Final period temperature | °C |

### Threshold Counts

| Variable | Threshold | Scientific Relevance | Unit |
|----------|-----------|---------------------|------|
| `Hot_Days_Count` | > 30°C | Heat stress days for vectors | days |
| `Cold_Days_Count` | < 15°C | Cold stress limiting development | days |
| `Very_Hot_Days` | > 35°C | Extreme heat potentially lethal | days |
| `Ideal_Days` | 20-30°C | Optimal temperature range | days |

### Derived Indices

| Variable | Formula | Scientific Relevance | Unit |
|----------|---------|---------------------|------|
| `Growing_Degree_Days` | Σ(T - 10) for T > 10°C | Accumulated heat for development | °C-days |
| `Diurnal_Range_Avg` | Mean(max - min) | Daily thermal amplitude | °C |
| `Temp_Trend` | Direction of change | Warming/cooling pattern | -1/0/1 |
| `Temp_Change_Rate` | (T_final - T_initial) / days | Rate of temperature change | °C/day |
| `Temp_Skewness` | Distribution asymmetry | Temperature distribution shape | - |
| `Temp_Kurtosis` | Distribution peakedness | Temperature extreme frequency | - |

---

## Precipitation Statistics (22 variables)

### Basic Statistics

| Variable | Description | Scientific Relevance | Unit |
|----------|-------------|---------------------|------|
| `Precip_Total` | Total precipitation | Water availability for breeding | mm |
| `Precip_Days` | Number of rainy days | Breeding site frequency | days |
| `Precip_Mean_Daily` | Mean daily precipitation | Average water input | mm/day |
| `Precip_Max_Daily` | Maximum daily precipitation | Potential flooding | mm |
| `Precip_Std` | Precipitation variability | Rainfall stability | mm |

### Percentiles

| Variable | Description | Scientific Relevance | Unit |
|----------|-------------|---------------------|------|
| `Precip_P25` | 25th percentile | Light rainfall | mm |
| `Precip_P75` | 75th percentile | Heavy rainfall | mm |

### Days Count

| Variable | Threshold | Scientific Relevance | Unit |
|----------|-----------|---------------------|------|
| `No_Rain_Days` | = 0mm | Dry conditions, breeding site loss | days |
| `Heavy_Rain_Days` | > 10mm | May flush breeding sites | days |
| `Very_Heavy_Rain_Days` | > 25mm | Significant flooding | days |
| `Moderate_Rain_Days` | 5-10mm | Ideal breeding conditions | days |

### Derived Indices

| Variable | Description | Scientific Relevance | Unit |
|----------|-------------|---------------------|------|
| `Rain_Probability` | % of rainy days | Breeding site persistence | % |
| `Rain_Volume_CV` | Coefficient of variation | Precipitation variability | % |
| `Precip_Intensity_Ratio` | Heavy rain / total | Rainfall intensity pattern | - |
| `Precip_Intensity` | Mean on rainy days | Rainfall intensity | mm/day |

### Weekly Totals

| Variable | Description | Scientific Relevance | Unit |
|----------|-------------|---------------------|------|
| `Precip_W1_Total` | Week 1 precipitation | Early period rainfall | mm |
| `Precip_W2_Total` | Week 2 precipitation | Mid-period rainfall | mm |
| `Precip_W3_Total` | Week 3 precipitation | Late period rainfall | mm |
| `Precip_W4_Total` | Week 4 precipitation | Final period rainfall | mm |

### Cumulative

| Variable | Description | Scientific Relevance | Unit |
|----------|-------------|---------------------|------|
| `Cumulative_7d` | 7-day total | Recent rainfall accumulation | mm |
| `Cumulative_14d` | 14-day total | Extended rainfall pattern | mm |

### Streaks

| Variable | Description | Scientific Relevance | Unit |
|----------|-------------|---------------------|------|
| `Wet_Days_Streak` | Max consecutive rainy days | Sustained breeding conditions | days |
| `Dry_Days_Streak` | Max consecutive dry days | Drought stress, breeding site loss | days |

---

## Humidity Statistics (13 variables)

### Basic Statistics

| Variable | Description | Scientific Relevance | Unit |
|----------|-------------|---------------------|------|
| `Humidity_Mean` | Mean relative humidity | Vector desiccation resistance | % |
| `Humidity_Min` | Minimum humidity | Desiccation stress period | % |
| `Humidity_Max` | Maximum humidity | Peak moisture conditions | % |
| `Humidity_Std` | Humidity variability | Moisture stability | % |
| `Humidity_Range` | Humidity range | Daily moisture amplitude | % |

### Percentiles

| Variable | Description | Scientific Relevance | Unit |
|----------|-------------|---------------------|------|
| `Humidity_P25` | 25th percentile | Lower moisture exposure | % |
| `Humidity_P75` | 75th percentile | Upper moisture exposure | % |

### Weekly Averages

| Variable | Description | Scientific Relevance | Unit |
|----------|-------------|---------------------|------|
| `Humidity_W1_Avg` | Week 1 mean humidity | Early period moisture | % |
| `Humidity_W2_Avg` | Week 2 mean humidity | Mid-period moisture | % |
| `Humidity_W3_Avg` | Week 3 mean humidity | Late period moisture | % |
| `Humidity_W4_Avg` | Week 4 mean humidity | Final period moisture | % |

### Threshold Counts

| Variable | Threshold | Scientific Relevance | Unit |
|----------|-----------|---------------------|------|
| `High_Humidity_Days` | > 80% | Optimal for vector survival | days |
| `Low_Humidity_Days` | < 40% | Desiccation risk | days |

### Derived

| Variable | Description | Scientific Relevance | Unit |
|----------|-------------|---------------------|------|
| `Humidity_Change` | Change over period | Moisture trend | % |

---

## Wind Statistics (10 variables)

### Basic Statistics

| Variable | Description | Scientific Relevance | Unit |
|----------|-------------|---------------------|------|
| `Wind_Mean` | Mean wind speed | Vector dispersal potential | m/s |
| `Wind_Max` | Maximum wind speed | Extreme dispersal events | m/s |
| `Wind_Std` | Wind variability | Wind pattern stability | m/s |

### Percentiles

| Variable | Description | Scientific Relevance | Unit |
|----------|-------------|---------------------|------|
| `Wind_P25` | 25th percentile | Calm conditions | m/s |
| `Wind_P75` | 75th percentile | Windy conditions | m/s |

### Threshold Counts

| Variable | Threshold | Scientific Relevance | Unit |
|----------|-----------|---------------------|------|
| `Calm_Days` | < 2 m/s | Stagnant air, pathogen accumulation | days |
| `Windy_Days` | > 5 m/s | Vector dispersal, dilution | days |
| `Moderate_Wind_Days` | 2-5 m/s | Moderate dispersal | days |
| `Very_Windy_Days` | > 8 m/s | Strong dispersal | days |

### Derived

| Variable | Formula | Scientific Relevance | Unit |
|----------|---------|---------------------|------|
| `Calm_Percentage` | Calm_Days / Total × 100 | Stagnation frequency | % |
| `Wind_Gust_Proxy` | Wind_Max × 1.5 | Estimated gusts | m/s |

---

## Two-Variable Interactions (12 variables)

| Variable | Formula | Scientific Relevance | Unit |
|----------|---------|---------------------|------|
| `Heat_Index_Celsius` | T + 0.5×(RH-40) | Apparent temperature, thermal stress | °C |
| `Discomfort_Index` | (T + RH) / 2 | Combined thermal-moisture discomfort | °C/% |
| `Tropical_Nights` | Nights Tmin > 20°C | Warm overnight conditions | days |
| `Warm_Nights` | Nights Tmin > 25°C | Hot overnight conditions | days |
| `Summer_Season` | Days T>25 & RH>70% | Optimal transmission conditions | days |
| `Muggy_Days` | Days T>20 & RH>80% | High moisture stress | days |
| `Dry_Heat_Days` | Days T>30 & RH<40% | Heat + desiccation stress | days |
| `Humid_Cold_Days` | Days T<15 & RH>70% | Cold + moisture stress | days |
| `Transmission_Risk_Proxy` | T × RH / 100 | Empirical transmission estimate | - |
| `Rain_Spread_Risk` | P × Wind | Pathogen dispersal by rain | - |
| `Precip_Wind_Ratio` | P / Wind | Rain dilution effect | - |
| `Evaporation_Proxy` | T × (100-RH) × Wind | Drying rate estimate | - |
| `Drying_Rate` | T × (100-RH) × 0.05 | Soil drying indicator | - |

---

## Disease/Epidemiological Indices (13 variables)

### Extrinsic Incubation Period (EIP)

| Variable | Formula | Scientific Relevance | Unit |
|----------|---------|---------------------|------|
| `EIP_Days` | f(T_mean) | Parasite development time | days |
| `EIP_Category` | Based on EIP_Days | Risk classification | Low/Medium/High |

**EIP Interpretation**: Lower EIP = faster pathogen development = higher transmission potential

### Vector Survival Indices

| Variable | Formula | Scientific Relevance | Unit |
|----------|---------|---------------------|------|
| `Larval_Survival` | f(T) | Immature vector viability | % |
| `Adult_Survival` | f(T, RH) | Adult vector longevity | % |

### Vector Biology

| Variable | Formula | Scientific Relevance | Unit |
|----------|---------|---------------------|------|
| `Vector_Fecundity` | f(T, RH) | Vector reproductive capacity | - |
| `Gonotrophic_Cycle` | f(T) | Time between blood meals | days |
| `Blood_Feeding_Rate` | f(T) | Feeding frequency estimate | % |
| `Vector_Density_Index` | Composite | Estimated vector abundance | 0-100 |

### Transmission Risk

| Variable | Description | Scientific Relevance | Unit |
|----------|-------------|---------------------|------|
| `IR_Score` | Infection risk score | Composite transmission risk | - |
| `Outbreak_Risk_30d` | 30-day risk (0-3) | Short-term outbreak risk | 0-3 |
| `Critical_Threshold` | Binary indicator | High-risk threshold exceeded | 0/1 |

### Vector Development

| Variable | Description | Scientific Relevance | Unit |
|----------|-------------|---------------------|------|
| `Mosquito_Dev_Days` | Days with T>20, RH>60, P>0 | Vector development conditions | days |
| `Persistence_Days` | Consecutive risk days | Sustained transmission window | days |

---

## Multi-Variable Composites (10 variables)

| Variable | Formula | Scientific Relevance | Unit |
|----------|---------|---------------------|------|
| `Combined_Stress` | T + RH/2 + Wind×2 | Multi-factor environmental stress | - |
| `Meteorological_WBGT` | 0.567T + 0.214RH - 0.6Wind + 1.2 | Wet bulb globe temperature | °C |
| `Pet_Proxy` | Approximation | Potential evapotranspiration | mm |
| `Aridity_Index` | P / (T + 10) | Aridity measure | - |
| `Moisture_Index` | (RH × P) / (T + 20) | Moisture availability | - |
| `Climate_Health_Risk` | Composite | Overall climate health risk | 0-100 |
| `Vector_Capacity` | f(T, RH, P) | Vector transmission potential | 0-100 |
| `Wet_Season_Indicator` | P > 100mm | Monsoon/wet season | 0/1 |
| `Stagnant_Air_Days` | WS < 2 m/s days | Calm humid conditions | days |
| `Heat_Stress_Days` | HI > 35 days | Heat stress days | days |
| `Climate_Suitability_Index` | Weighted composite | Overall transmission suitability | 0-100 |

---

## Temporal Features (4 variables)

| Variable | Description | Scientific Relevance | Unit |
|----------|-------------|---------------------|------|
| `Month` | Event month | Seasonality | 1-12 |
| `Week_Number` | ISO week | Temporal granularity | 1-53 |
| `Day_Of_Year` | Day number | Annual position | 1-366 |
| `Season` | Season classification | Winter/Summer/Monsoon/Post-monsoon | - |

### Season Classification

| Month Range | Season | Transmission Pattern |
|-------------|--------|---------------------|
| Dec-Feb | Winter | Low transmission |
| Mar-May | Summer | Pre-monsoon, rising risk |
| Jun-Sep | Monsoon | Peak transmission |
| Oct-Nov | Post-monsoon | Declining risk |

---

## Lagged Effects (6 variables)

| Variable | Description | Scientific Relevance | Unit |
|----------|-------------|---------------------|------|
| `Temp_Lag_7d` | 7-day lagged temperature | Delayed temperature effect | °C |
| `Temp_Lag_14d` | 14-day lagged temperature | Extended lag effect | °C |
| `Precip_Lag_7d` | 7-day lagged precipitation | Delayed precipitation effect | mm |
| `Precip_Lag_14d` | 14-day lagged precipitation | Extended precipitation lag | mm |
| `Temp_Anomaly` | Deviation from 30-day mean | Temperature anomaly | °C |
| `Precip_Anomaly` | Deviation from 30-day mean | Precipitation anomaly | mm |

**Note**: Lag effects are important for capturing delayed relationships between climate and disease.

---

## Summary Indicators (3 variables)

| Variable | Description | Scientific Relevance | Unit |
|----------|-------------|---------------------|------|
| `Days_Data` | Days with satellite data | Data completeness | days |
| `Valid_Data_Flag` | Data quality (1=good) | Reliability indicator | 0/1 |
| `Processing_Status` | Processing outcome | Error identification | text |

---

## Default Thresholds Summary

| Category | Threshold | Variable |
|----------|-----------|----------|
| Temperature | > 30°C | Hot_Days_Count |
| Temperature | > 35°C | Very_Hot_Days |
| Temperature | < 15°C | Cold_Days_Count |
| Temperature | 20-30°C | Ideal_Days |
| Precipitation | > 10mm | Heavy_Rain_Days |
| Precipitation | > 25mm | Very_Heavy_Rain_Days |
| Precipitation | 5-10mm | Moderate_Rain_Days |
| Humidity | > 80% | High_Humidity_Days |
| Humidity | < 40% | Low_Humidity_Days |
| Wind | < 2 m/s | Calm_Days |
| Wind | > 5 m/s | Windy_Days |
| Combined | Tmin > 20°C | Tropical_Nights |
| Combined | T > 25 & RH > 70% | Summer_Season |
| Combined | HI > 35°C | Heat_Stress_Days |

---

## Usage Notes

### Data Quality
1. Filter records with `Valid_Data_Flag = 0` for analysis
2. Minimum 25 days recommended for reliable statistics
3. Check `Processing_Status` for API errors

### Variable Selection by Research Question

| Research Question | Recommended Variables |
|------------------|---------------------|
| What drives transmission? | EIP_Days, Vector_Capacity, Transmission_Risk_Proxy |
| Where is risk highest? | Outbreak_Risk_30d, Climate_Suitability_Index, IR_Score |
| When does transmission peak? | Season, Mosquit_Dev_Days, Persistence_Days |
| How do extremes affect risk? | Hot_Days_Count, Heavy_Rain_Days, Dry_Days_Streak |
| Which regions need intervention? | Regional aggregates of Vector_Capacity, Outbreak_Risk_30d |

### Statistical Considerations
1. Non-parametric tests recommended for non-normal distributions
2. Account for spatial autocorrelation in regional analysis
3. Consider lagged effects in time-series modeling
4. Report effect sizes alongside significance tests

---

## References

1. Craig MH, et al. (1999). Climate change and malaria risk. *Parasitology Today*
2. Paaijmans KP, et al. (2009). Temperature variation and malaria transmission. *PNAS*
3. World Health Organization. (2018). Climate change and health.
4. NASA Langley Research Center. POWER Project Documentation.
