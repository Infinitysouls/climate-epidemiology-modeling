# Output Variables Documentation

Complete dictionary of all 122 variables computed by the Climate Epidemiology Modeling Toolkit.

---

## Scientific Background

### Climate-Disease Transmission Framework

The toolkit computes variables based on the conceptual framework linking environmental conditions to infectious disease transmission globally:

```
Environmental Conditions → Vector Biology → Transmission Potential → Outbreak Risk
     (T, P, RH, Wind)    (EIP, Survival)     (Vector Capacity)      (Risk Score)
```

### Global Applicability

This toolkit is designed for **universal application** across all climate zones:

| Climate Zone | Temperature | Humidity | Transmission Pattern |
|--------------|-------------|----------|---------------------|
| Tropical | 20-35°C year-round | High | Year-round potential |
| Subtropical | 15-35°C seasonal | Moderate-high | Seasonal peaks |
| Temperate | -10 to 35°C | Moderate | Seasonal, temperature-limited |
| Arid | 10-45°C | Low | Limited by moisture |
| Semi-arid | 5-40°C | Low-moderate | Seasonal, precipitation-limited |

### Key Epidemiological Relationships

| Variable Category | Scientific Relevance | Global Applicability |
|------------------|---------------------|---------------------|
| Temperature | Affects pathogen development rate, vector metabolism, survival | Universal |
| Precipitation | Creates breeding sites, influences vector abundance | Universal |
| Humidity | Affects vector desiccation resistance, biting behavior | Universal |
| Wind | Influences vector dispersal, pathogen spread | Universal |
| Disease Indices | Integrate multiple factors for transmission estimates | Universal |

---

## Metadata (7 variables)

| Variable | Type | Description | Unit | Global Applicability |
|----------|------|-------------|------|---------------------|
| `Date of Event` | Date | Original event/outbreak date | YYYY-MM-DD | Universal |
| `Latitude` | Float | Location latitude (-90 to 90) | degrees | Universal |
| `Longitude` | Float | Location longitude (-180 to 180) | degrees | Universal |
| `Region1` | String | Primary administrative region | - | Universal |
| `Region2` | String | Secondary administrative region | - | Universal |
| `Climate_Start` | Date | Start of 30-day climate data window | YYYY-MM-DD | Universal |
| `Climate_End` | Date | End of 30-day climate data window | YYYY-MM-DD | Universal |

---

## Temperature Statistics (22 variables)

### Basic Statistics

| Variable | Description | Scientific Relevance | Unit | Global Context |
|----------|-------------|---------------------|------|-----------------|
| `Temp_Mean` | Mean temperature over 30-day window | Primary driver of EIP and vector metabolism | °C | Universal |
| `Temp_Min` | Minimum temperature | Affects overnight vector survival | °C | Universal |
| `Temp_Max` | Maximum temperature | Influences stress thresholds | °C | Universal |
| `Temp_Std` | Standard deviation | Indicates temperature variability | °C | Universal |
| `Temp_Range` | Temperature range (max - min) | Daily thermal amplitude | °C | Universal |

### Percentiles

| Variable | Description | Scientific Relevance | Unit | Global Context |
|----------|-------------|---------------------|------|-----------------|
| `Temp_P25` | 25th percentile | Lower temperature exposure | °C | Universal |
| `Temp_P50` | Median temperature | Central tendency | °C | Universal |
| `Temp_P75` | 75th percentile | Upper temperature exposure | °C | Universal |
| `Temp_P90` | 90th percentile | Extreme high temperature | °C | Universal |

### Weekly Averages

| Variable | Description | Scientific Relevance | Unit | Global Context |
|----------|-------------|---------------------|------|-----------------|
| `Temp_W1_Avg` | Week 1 mean (first 25% of days) | Early period temperature | °C | Universal |
| `Temp_W2_Avg` | Week 2 mean | Mid-period temperature | °C | Universal |
| `Temp_W3_Avg` | Week 3 mean | Late period temperature | °C | Universal |
| `Temp_W4_Avg` | Week 4 mean (last 25% of days) | Final period temperature | °C | Universal |

### Threshold Counts

| Variable | Threshold | Scientific Relevance | Unit | Global Context |
|----------|-----------|---------------------|------|-----------------|
| `Hot_Days_Count` | > 30°C | Heat stress days for vectors | days | Applicable to warm climates |
| `Cold_Days_Count` | < 15°C | Cold stress limiting development | days | Important for temperate/altitude |
| `Very_Hot_Days` | > 35°C | Extreme heat potentially lethal | days | Desert/tropical summer |
| `Ideal_Days` | 20-30°C | Optimal temperature range | days | Universal optimal range |

### Derived Indices

| Variable | Formula | Scientific Relevance | Unit | Global Context |
|----------|---------|---------------------|------|-----------------|
| `Growing_Degree_Days` | Σ(T - 10) for T > 10°C | Accumulated heat for development | °C-days | Universal |
| `Diurnal_Range_Avg` | Mean(max - min) | Daily thermal amplitude | °C | Universal |
| `Temp_Trend` | Direction of change | Warming/cooling pattern | -1/0/1 | Universal |
| `Temp_Change_Rate` | (T_final - T_initial) / days | Rate of temperature change | °C/day | Universal |
| `Temp_Skewness` | Distribution asymmetry | Temperature distribution shape | - | Universal |
| `Temp_Kurtosis` | Distribution peakedness | Temperature extreme frequency | - | Universal |

---

## Precipitation Statistics (22 variables)

### Basic Statistics

| Variable | Description | Scientific Relevance | Unit | Global Context |
|----------|-------------|---------------------|------|-----------------|
| `Precip_Total` | Total precipitation | Water availability for breeding | mm | Universal |
| `Precip_Days` | Number of rainy days | Breeding site frequency | days | Universal |
| `Precip_Mean_Daily` | Mean daily precipitation | Average water input | mm/day | Universal |
| `Precip_Max_Daily` | Maximum daily precipitation | Potential flooding | mm | Universal |
| `Precip_Std` | Precipitation variability | Rainfall stability | mm | Universal |

### Percentiles

| Variable | Description | Scientific Relevance | Unit | Global Context |
|----------|-------------|---------------------|------|-----------------|
| `Precip_P25` | 25th percentile | Light rainfall | mm | Universal |
| `Precip_P75` | 75th percentile | Heavy rainfall | mm | Universal |

### Days Count

| Variable | Threshold | Scientific Relevance | Unit | Global Context |
|----------|-----------|---------------------|------|-----------------|
| `No_Rain_Days` | = 0mm | Dry conditions, breeding site loss | days | Universal |
| `Heavy_Rain_Days` | > 10mm | May flush breeding sites | days | Monsoon regions |
| `Very_Heavy_Rain_Days` | > 25mm | Significant flooding | days | Tropical regions |
| `Moderate_Rain_Days` | 5-10mm | Ideal breeding conditions | days | Universal |

### Derived Indices

| Variable | Description | Scientific Relevance | Unit | Global Context |
|----------|-------------|---------------------|------|-----------------|
| `Rain_Probability` | % of rainy days | Breeding site persistence | % | Universal |
| `Rain_Volume_CV` | Coefficient of variation | Precipitation variability | % | Universal |
| `Precip_Intensity_Ratio` | Heavy rain / total | Rainfall intensity pattern | - | Universal |
| `Precip_Intensity` | Mean on rainy days | Rainfall intensity | mm/day | Universal |

### Weekly Totals

| Variable | Description | Scientific Relevance | Unit | Global Context |
|----------|-------------|---------------------|------|-----------------|
| `Precip_W1_Total` | Week 1 precipitation | Early period rainfall | mm | Universal |
| `Precip_W2_Total` | Week 2 precipitation | Mid-period rainfall | mm | Universal |
| `Precip_W3_Total` | Week 3 precipitation | Late period rainfall | mm | Universal |
| `Precip_W4_Total` | Week 4 precipitation | Final period rainfall | mm | Universal |

### Cumulative

| Variable | Description | Scientific Relevance | Unit | Global Context |
|----------|-------------|---------------------|------|-----------------|
| `Cumulative_7d` | 7-day total | Recent rainfall accumulation | mm | Universal |
| `Cumulative_14d` | 14-day total | Extended rainfall pattern | mm | Universal |

### Streaks

| Variable | Description | Scientific Relevance | Unit | Global Context |
|----------|-------------|---------------------|------|-----------------|
| `Wet_Days_Streak` | Max consecutive rainy days | Sustained breeding conditions | days | Tropical/monsoon |
| `Dry_Days_Streak` | Max consecutive dry days | Drought stress, breeding site loss | days | Arid/semi-arid |

---

## Humidity Statistics (13 variables)

### Basic Statistics

| Variable | Description | Scientific Relevance | Unit | Global Context |
|----------|-------------|---------------------|------|-----------------|
| `Humidity_Mean` | Mean relative humidity | Vector desiccation resistance | % | Universal |
| `Humidity_Min` | Minimum humidity | Desiccation stress period | % | Universal |
| `Humidity_Max` | Maximum humidity | Peak moisture conditions | % | Universal |
| `Humidity_Std` | Humidity variability | Moisture stability | % | Universal |
| `Humidity_Range` | Humidity range | Daily moisture amplitude | % | Universal |

### Percentiles

| Variable | Description | Scientific Relevance | Unit | Global Context |
|----------|-------------|---------------------|------|-----------------|
| `Humidity_P25` | 25th percentile | Lower moisture exposure | % | Universal |
| `Humidity_P75` | 75th percentile | Upper moisture exposure | % | Universal |

### Weekly Averages

| Variable | Description | Scientific Relevance | Unit | Global Context |
|----------|-------------|---------------------|------|-----------------|
| `Humidity_W1_Avg` | Week 1 mean humidity | Early period moisture | % | Universal |
| `Humidity_W2_Avg` | Week 2 mean humidity | Mid-period moisture | % | Universal |
| `Humidity_W3_Avg` | Week 3 mean humidity | Late period moisture | % | Universal |
| `Humidity_W4_Avg` | Week 4 mean humidity | Final period moisture | % | Universal |

### Threshold Counts

| Variable | Threshold | Scientific Relevance | Unit | Global Context |
|----------|-----------|---------------------|------|-----------------|
| `High_Humidity_Days` | > 80% | Optimal for vector survival | days | Tropical regions |
| `Low_Humidity_Days` | < 40% | Desiccation risk | days | Arid regions |

### Derived

| Variable | Description | Scientific Relevance | Unit | Global Context |
|----------|-------------|---------------------|------|-----------------|
| `Humidity_Change` | Change over period | Moisture trend | % | Universal |

---

## Wind Statistics (10 variables)

### Basic Statistics

| Variable | Description | Scientific Relevance | Unit | Global Context |
|----------|-------------|---------------------|------|-----------------|
| `Wind_Mean` | Mean wind speed | Vector dispersal potential | m/s | Universal |
| `Wind_Max` | Maximum wind speed | Extreme dispersal events | m/s | Universal |
| `Wind_Std` | Wind variability | Wind pattern stability | m/s | Universal |

### Percentiles

| Variable | Description | Scientific Relevance | Unit | Global Context |
|----------|-------------|---------------------|------|-----------------|
| `Wind_P25` | 25th percentile | Calm conditions | m/s | Universal |
| `Wind_P75` | 75th percentile | Windy conditions | m/s | Universal |

### Threshold Counts

| Variable | Threshold | Scientific Relevance | Unit | Global Context |
|----------|-----------|---------------------|------|-----------------|
| `Calm_Days` | < 2 m/s | Stagnant air, pathogen accumulation | days | Universal |
| `Windy_Days` | > 5 m/s | Vector dispersal, dilution | days | Coastal/highland |
| `Moderate_Wind_Days` | 2-5 m/s | Moderate dispersal | days | Universal |
| `Very_Windy_Days` | > 8 m/s | Strong dispersal | days | Highland/coastal |

### Derived

| Variable | Formula | Scientific Relevance | Unit | Global Context |
|----------|---------|---------------------|------|-----------------|
| `Calm_Percentage` | Calm_Days / Total × 100 | Stagnation frequency | % | Universal |
| `Wind_Gust_Proxy` | Wind_Max × 1.5 | Estimated gusts | m/s | Universal |

---

## Two-Variable Interactions (12 variables)

| Variable | Formula | Scientific Relevance | Unit | Global Context |
|----------|---------|---------------------|------|-----------------|
| `Heat_Index_Celsius` | T + 0.5×(RH-40) | Apparent temperature, thermal stress | °C | Universal |
| `Discomfort_Index` | (T + RH) / 2 | Combined thermal-moisture discomfort | °C/% | Universal |
| `Tropical_Nights` | Nights Tmin > 20°C | Warm overnight conditions | days | Tropical |
| `Warm_Nights` | Nights Tmin > 25°C | Hot overnight conditions | days | Tropical summer |
| `Summer_Season` | Days T>25 & RH>70% | Optimal transmission conditions | days | Tropical/monsoon |
| `Muggy_Days` | Days T>20 & RH>80% | High moisture stress | days | Tropical |
| `Dry_Heat_Days` | Days T>30 & RH<40% | Heat + desiccation stress | days | Arid/semi-arid |
| `Humid_Cold_Days` | Days T<15 & RH>70% | Cold + moisture stress | days | Temperate winter |
| `Transmission_Risk_Proxy` | T × RH / 100 | Empirical transmission estimate | - | Universal |
| `Rain_Spread_Risk` | P × Wind | Pathogen dispersal by rain | - | Universal |
| `Precip_Wind_Ratio` | P / Wind | Rain dilution effect | - | Universal |
| `Evaporation_Proxy` | T × (100-RH) × Wind | Drying rate estimate | - | Universal |
| `Drying_Rate` | T × (100-RH) × 0.05 | Soil drying indicator | - | Universal |

---

## Disease/Epidemiological Indices (13 variables)

### Extrinsic Incubation Period (EIP)

| Variable | Formula | Scientific Relevance | Unit | Global Context |
|----------|---------|---------------------|------|-----------------|
| `EIP_Days` | f(T_mean) | Parasite development time | days | Universal |
| `EIP_Category` | Based on EIP_Days | Risk classification | Low/Medium/High | Universal |

**EIP Interpretation**: Lower EIP = faster pathogen development = higher transmission potential

### Vector Survival Indices

| Variable | Formula | Scientific Relevance | Unit | Global Context |
|----------|---------|---------------------|------|-----------------|
| `Larval_Survival` | f(T) | Immature vector viability | % | Universal |
| `Adult_Survival` | f(T, RH) | Adult vector longevity | % | Universal |

### Vector Biology

| Variable | Formula | Scientific Relevance | Unit | Global Context |
|----------|---------|---------------------|------|-----------------|
| `Vector_Fecundity` | f(T, RH) | Vector reproductive capacity | - | Universal |
| `Gonotrophic_Cycle` | f(T) | Time between blood meals | days | Universal |
| `Blood_Feeding_Rate` | f(T) | Feeding frequency estimate | % | Universal |
| `Vector_Density_Index` | Composite | Estimated vector abundance | 0-100 | Universal |

### Transmission Risk

| Variable | Description | Scientific Relevance | Unit | Global Context |
|----------|-------------|---------------------|------|-----------------|
| `IR_Score` | Infection risk score | Composite transmission risk | - | Universal |
| `Outbreak_Risk_30d` | 30-day risk (0-3) | Short-term outbreak risk | 0-3 | Universal |
| `Critical_Threshold` | Binary indicator | High-risk threshold exceeded | 0/1 | Universal |

### Vector Development

| Variable | Description | Scientific Relevance | Unit | Global Context |
|----------|-------------|---------------------|------|-----------------|
| `Mosquito_Dev_Days` | Days with T>20, RH>60, P>0 | Vector development conditions | days | Climate-dependent |
| `Persistence_Days` | Consecutive risk days | Sustained transmission window | days | Universal |

---

## Multi-Variable Composites (10 variables)

| Variable | Formula | Scientific Relevance | Unit | Global Context |
|----------|---------|---------------------|------|-----------------|
| `Combined_Stress` | T + RH/2 + Wind×2 | Multi-factor environmental stress | - | Universal |
| `Meteorological_WBGT` | 0.567T + 0.214RH - 0.6Wind + 1.2 | Wet bulb globe temperature | °C | Universal |
| `Pet_Proxy` | Approximation | Potential evapotranspiration | mm | Universal |
| `Aridity_Index` | P / (T + 10) | Aridity measure | - | Universal |
| `Moisture_Index` | (RH × P) / (T + 20) | Moisture availability | - | Universal |
| `Climate_Health_Risk` | Composite | Overall climate health risk | 0-100 | Universal |
| `Vector_Capacity` | f(T, RH, P) | Vector transmission potential | 0-100 | Universal |
| `Wet_Season_Indicator` | P > 100mm | Monsoon/wet season | 0/1 | Climate-dependent |
| `Stagnant_Air_Days` | WS < 2 m/s days | Calm humid conditions | days | Universal |
| `Heat_Stress_Days` | HI > 35 days | Heat stress days | days | Universal |
| `Climate_Suitability_Index` | Weighted composite | Overall transmission suitability | 0-100 | Universal |

---

## Temporal Features (4 variables)

| Variable | Description | Scientific Relevance | Unit | Global Context |
|----------|-------------|---------------------|------|-----------------|
| `Month` | Event month | Seasonality | 1-12 | Universal |
| `Week_Number` | ISO week | Temporal granularity | 1-53 | Universal |
| `Day_Of_Year` | Day number | Annual position | 1-366 | Universal |
| `Season` | Season classification | Climate season | winter/summer/monsoon/post_monsoon | Universal |

### Season Classification

| Month Range (Northern) | Month Range (Southern) | Season | Transmission Pattern |
|------------------------|----------------------|--------|---------------------|
| Dec-Feb | Jun-Aug | Winter | Low transmission |
| Mar-May | Sep-Nov | Spring | Rising risk |
| Jun-Sep | Dec-Mar | Monsoon | Peak (tropical) |
| Oct-Nov | Apr-May | Post-Monsoon | Declining risk |

---

## Lagged Effects (6 variables)

| Variable | Description | Scientific Relevance | Unit | Global Context |
|----------|-------------|---------------------|------|-----------------|
| `Temp_Lag_7d` | 7-day lagged temperature | Delayed temperature effect | °C | Universal |
| `Temp_Lag_14d` | 14-day lagged temperature | Extended lag effect | °C | Universal |
| `Precip_Lag_7d` | 7-day lagged precipitation | Delayed precipitation effect | mm | Universal |
| `Precip_Lag_14d` | 14-day lagged precipitation | Extended precipitation lag | mm | Universal |
| `Temp_Anomaly` | Deviation from 30-day mean | Temperature anomaly | °C | Universal |
| `Precip_Anomaly` | Deviation from 30-day mean | Precipitation anomaly | mm | Universal |

---

## Summary Indicators (3 variables)

| Variable | Description | Scientific Relevance | Unit | Global Context |
|----------|-------------|---------------------|------|-----------------|
| `Days_Data` | Days with satellite data | Data completeness | days | Universal |
| `Valid_Data_Flag` | Data quality (1=good) | Reliability indicator | 0/1 | Universal |
| `Processing_Status` | Processing outcome | Error identification | text | Universal |

---

## Default Thresholds Summary

| Category | Threshold | Variable | Global Applicability |
|----------|-----------|----------|---------------------|
| Temperature | > 30°C | Hot_Days_Count | Warm climates |
| Temperature | > 35°C | Very_Hot_Days | Desert/summer |
| Temperature | < 15°C | Cold_Days_Count | Temperate/altitude |
| Temperature | 20-30°C | Ideal_Days | Universal optimal |
| Precipitation | > 10mm | Heavy_Rain_Days | Universal |
| Precipitation | > 25mm | Very_Heavy_Rain_Days | Tropical |
| Precipitation | 5-10mm | Moderate_Rain_Days | Universal |
| Humidity | > 80% | High_Humidity_Days | Tropical |
| Humidity | < 40% | Low_Humidity_Days | Arid |
| Wind | < 2 m/s | Calm_Days | Universal |
| Wind | > 5 m/s | Windy_Days | Universal |
| Combined | Tmin > 20°C | Tropical_Nights | Tropical |
| Combined | T > 25 & RH > 70% | Summer_Season | Tropical/monsoon |
| Combined | HI > 35°C | Heat_Stress_Days | Universal |

---

## Usage Notes

### Data Quality
1. Filter records with `Valid_Data_Flag = 0` for analysis
2. Minimum 25 days recommended for reliable statistics
3. Check `Processing_Status` for API errors

### Variable Selection by Research Question

| Research Question | Recommended Variables | Global Applicability |
|------------------|----------------------|---------------------|
| What drives transmission? | EIP_Days, Vector_Capacity, Transmission_Risk_Proxy | Universal |
| Where is risk highest? | Outbreak_Risk_30d, Climate_Suitability_Index, IR_Score | Universal |
| When does transmission peak? | Season, Mosquito_Dev_Days, Persistence_Days | Universal |
| How do extremes affect risk? | Hot_Days_Count, Heavy_Rain_Days, Dry_Days_Streak | Universal |
| Which regions need intervention? | Regional aggregates of Vector_Capacity, Outbreak_Risk_30d | Universal |

### Statistical Considerations (Globally Applicable)
1. Non-parametric tests recommended for non-normal distributions
2. Account for spatial autocorrelation in regional analysis
3. Consider lagged effects in time-series modeling
4. Report effect sizes alongside significance tests
5. Use appropriate corrections for multiple comparisons

---

## References

1. Craig MH, et al. (1999). Climate change and malaria risk. *Parasitology Today*
2. Paaijmans KP, et al. (2009). Temperature variation and malaria transmission. *PNAS*
3. World Health Organization. (2018). Climate change and health.
4. NASA Langley Research Center. POWER Project Documentation.
5. World Meteorological Organization. Global Climate Observing System.
