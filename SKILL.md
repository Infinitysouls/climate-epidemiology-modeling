# Climate Epidemiology Modeling Skill

## Description

A Python toolkit for climate data analysis in infectious disease epidemiology research. Fetches satellite-based meteorological data and computes 122 variables including epidemiological indices for disease transmission modeling globally.

## Scientific Background

### Key Concepts

| Concept | Definition | Global Applicability |
|---------|------------|---------------------|
| **Extrinsic Incubation Period (EIP)** | Time for pathogen development within vector; temperature-dependent | Universal across all tropical/temperate regions |
| **Vector Capacity** | Potential for vector-borne transmission; composite of density, survival, behavior | Applicable to all vector-borne diseases |
| **Climate Suitability Index** | Integrated measure of environmental conditions for transmission | Works globally across climate zones |
| **Transmission Risk Proxy** | Empirical estimate of climate-driven transmission potential | Universal metric |

### Climate-Disease Relationships

| Climate Factor | Effect on Disease | Global Pattern |
|----------------|-------------------|----------------|
| Temperature ↑ | Faster EIP, higher vector survival (up to threshold) | Faster transmission in tropical vs temperate |
| Precipitation ↑ | More breeding sites, higher vector abundance | Monsoon patterns vs arid regions |
| Humidity ↑ | Longer vector survival, increased biting | Tropical humidity supports year-round transmission |
| Wind | Affects vector dispersal and long-range spread | Important for epidemic spread |

## Capabilities

- `fetch_climate_data` - Retrieve satellite-based climate data for any location globally
- `compute_epidemiological_indices` - Calculate EIP, vector capacity, transmission risk
- `analyze_climate_disease` - Correlate climate with disease patterns
- `generate_derived_variables` - Create interaction terms, composites, lags

## Prerequisites

### System Requirements
- Python 3.8+
- Internet connection (for API access)
- CSV data with location and date columns

### Python Dependencies
```
requests>=2.28.0
```

### Installation
```bash
pip install -r requirements.txt
```

## Input Format

### Required CSV Structure

| Column | Type | Example | Description |
|--------|------|---------|-------------|
| `[Date of Event]` | Date | 2017-05-15 | Event date (YYYY-MM-DD) |
| `[Latitude]` | Float | 23.456 | Latitude (-90 to 90) |
| `[Longitude]` | Float | 77.890 | Longitude (-180 to 180) |
| `[Region1]` | String | StateName | Primary administrative region |
| `[Region2]` | String | DistrictName | Secondary administrative region |

### Example CSV
```csv
[Date of Event],[Latitude],[Longitude],[Region1],[Region2]
2017-05-15,23.456,77.890,StateName,DistrictName
2017-06-20,25.317,82.456,StateName,DistrictName
2017-07-10,19.876,75.456,StateName,DistrictName
```

## Output

### 122 Computed Variables

| Category | Count | Key Variables |
|----------|-------|---------------|
| Metadata | 7 | Date, Latitude, Longitude, Region1, Region2, Climate_Start, Climate_End |
| Temperature | 22 | Temp_Mean, Temp_Max, Temp_P75, Hot_Days_Count, Growing_Degree_Days |
| Precipitation | 22 | Precip_Total, Precip_Days, Heavy_Rain_Days, Wet_Days_Streak |
| Humidity | 13 | Humidity_Mean, High_Humidity_Days, Humidity_Change |
| Wind | 10 | Wind_Mean, Wind_Max, Calm_Days |
| Interactions | 12 | Heat_Index_Celsius, Transmission_Risk_Proxy |
| Disease Indices | 13 | EIP_Days, Vector_Capacity, Larval_Survival, IR_Score |
| Composites | 10 | Climate_Suitability_Index, Wet_Season_Indicator |
| Temporal | 4 | Month, Week_Number, Season, Day_Of_Year |
| Lagged | 6 | Temp_Lag_7d, Precip_Anomaly, Temp_Trend |
| Summary | 3 | Days_Data, Valid_Data_Flag, Processing_Status |

### Key Epidemiological Variables

| Variable | Description | Interpretation | Global Applicability |
|----------|-------------|----------------|---------------------|
| `EIP_Days` | Parasite development time | Lower = faster transmission | Universal |
| `EIP_Category` | Risk level | High/Medium/Low | Works globally |
| `Vector_Capacity` | Transmission potential (0-100) | Higher = more potential | Universal |
| `Larval_Survival` | Immature viability (%) | Higher = more breeding | Universal |
| `Adult_Survival` | Adult longevity (%) | Higher = longer infectious period | Universal |
| `Mosquito_Dev_Days` | Vector development days | More days = higher abundance | Climate-dependent |
| `Climate_Suitability_Index` | Overall suitability (0-100) | Higher = better conditions | Universal |
| `Outbreak_Risk_30d` | 30-day risk (0-3) | 3 = highest risk | Universal |

## Global Climate Zone Applicability

### Supported Climate Zones

| Zone | Temperature Range | Humidity | Precipitation | Regions |
|------|-------------------|----------|---------------|---------|
| Tropical | 20-35°C year-round | High (60-90%) | High year-round | SE Asia, Central Africa, Amazon |
| Subtropical | 15-35°C | Moderate-high | Seasonal | Mediterranean, Southern US |
| Temperate | -10 to 35°C | Moderate | Seasonal | Europe, Northern US |
| Arid | 10-45°C | Low (<40%) | Very low | Middle East, Central Asia |
| Semi-arid | 5-40°C | Low-moderate | Low-moderate | Sahel, Southwestern US |

### Season Classifications

| Classification | Northern Hemisphere | Southern Hemisphere | Transmission |
|---------------|--------------------|--------------------|--------------|
| Winter | Dec-Feb | Jun-Aug | Low |
| Spring | Mar-May | Sep-Nov | Rising |
| Summer | Jun-Aug | Dec-Feb | Peak (tropical) |
| Autumn | Sep-Nov | Mar-May | Declining |
| Monsoon | Jun-Sep | Dec-Mar | Peak (tropical regions) |
| Dry Season | Nov-May | May-Nov | Low transmission |

## Usage

### Command Line Interface

```bash
# Basic usage
python scripts/fetch_climate.py -i input.csv -o output.csv

# Using environment variables
export CLIMATE_INPUT=input.csv
export CLIMATE_OUTPUT=output.csv
python scripts/fetch_climate.py
```

### Windows Batch File
```cmd
fetch_climate.bat
```

### Python API
```python
from datetime import datetime
from fetch_climate import fetch_daily_data, compute_all_metrics

# Fetch and compute for any global location
daily_data = fetch_daily_data(23.456, 77.890, "2017-05-01", "2017-05-31")
metrics = compute_all_metrics(daily_data, datetime(2017, 5, 15))

# Key epidemiological metrics
print(f"EIP: {metrics['EIP_Days']} days")
print(f"Vector Capacity: {metrics['Vector_Capacity']}")
print(f"Risk Level: {metrics['Outbreak_Risk_30d']}")
```

## AI Prompt Templates for Global Scientific Analysis

### Template 1: Global Risk Assessment
```
Analyze climate_output.csv for global vector-borne disease risk:
1. Identify locations with EIP_Category = "High" AND Vector_Capacity > 60
2. Compare risk levels across different climate zones (use Season as proxy)
3. Calculate proportion of high-risk areas globally and by region
4. Create risk stratification (low/medium/high) based on Outbreak_Risk_30d
```

### Template 2: Tropical vs Temperate Comparison
```
Compare transmission dynamics between climate zones:
1. Classify locations as tropical (Temp_Mean > 25) or temperate
2. Compare Vector_Capacity, EIP_Days, and Transmission_Risk_Proxy between zones
3. Perform statistical test (t-test) for significance
4. Identify which climate variables drive zone differences
```

### Template 3: Seasonal Pattern Analysis (Global)
```
Analyze seasonal transmission patterns across the dataset:
1. Group data by Season column
2. Calculate mean Vector_Capacity, EIP_Days, and Transmission_Risk_Proxy per season
3. Identify peak transmission season globally
4. Create summary statistics table by season
```

### Template 4: Correlation Analysis (Universal)
```
For the climate_output.csv data:
1. Calculate Pearson correlation between Temp_Mean and Transmission_Risk_Proxy
2. Calculate correlation between Precip_Total and Vector_Capacity
3. Test significance (p < 0.05)
4. Create scatter plots with regression lines
```

### Template 5: Geographic Risk Mapping
```
From climate_output.csv:
1. Create a risk score combining Vector_Capacity and Outbreak_Risk_30d
2. Rank regions by mean risk score (Region1 level)
3. Identify top 10 highest-risk administrative regions globally
4. Generate summary table with 95% confidence intervals
```

### Template 6: Climate Zone Analysis
```
Analyze transmission patterns across climate zones:
1. Use Season and Temp_Mean to classify climate zones
2. Calculate mean vector biology indices by zone
3. Identify which zones have year-round transmission potential
4. Compare wet vs dry season impacts by zone
```

### Template 7: Extreme Climate Event Analysis
```
Analyze global relationship between extreme climate and risk:
1. Filter locations with Hot_Days_Count > 20 OR Heavy_Rain_Days > 5
2. Compare Vector_Capacity between extreme and non-extreme locations
3. Perform t-test for statistical significance
4. Calculate odds ratio for high-risk classification
```

### Template 8: Entomological Assessment (Global)
```
From climate_output.csv, assess global vector entomological conditions:
1. Identify locations with Larval_Survival > 70% AND Vector_Fecundity > 5
2. Calculate mean Blood_Feeding_Rate by Region1
3. Estimate vector density proxy (Vector_Density_Index) distribution
4. Create entomological risk categories globally
```

### Template 9: Temporal Trend Analysis
```
Analyze temporal patterns globally:
1. Calculate Temp_Trend and Precip_Anomaly statistics
2. Identify locations with positive transmission trend
3. Calculate persistence of risk conditions (Persistence_Days)
4. Create time-series visualization of risk metrics
```

### Template 10: Climate Suitability Modeling (Global)
```
Build global climate suitability model:
1. Use Climate_Suitability_Index as dependent variable
2. Identify key predictors (Temp_Mean, Precip_Total, Humidity_Mean)
3. Fit multiple linear regression
4. Calculate R-squared and identify significant predictors
5. Create suitability prediction equation
```

### Template 11: Intervention Prioritization (Global)
```
For global resource allocation planning:
1. Rank locations by composite risk score (Vector_Capacity + IR_Score + Outbreak_Risk_30d)
2. Identify intervention priority zones (top 20% by risk)
3. Calculate population-level risk by Region1
4. Generate prioritized intervention list
```

### Template 12: Data Quality Assessment (Global)
```
Global data quality report:
1. Identify records where Valid_Data_Flag = 0
2. Check Days_Data distribution (should be ≥25 for reliability)
3. Calculate completeness percentage for each variable
4. Flag regions requiring data validation
```

## Integration Patterns

### With Pandas
```python
import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv('climate_output.csv')

# Risk filtering
high_risk = df[(df['EIP_Category'] == 'High') & (df['Vector_Capacity'] > 60)]

# Seasonal analysis
seasonal = df.groupby('Season').agg({
    'Vector_Capacity': ['mean', 'std'],
    'EIP_Days': 'mean',
    'Outbreak_Risk_30d': 'mean'
}).round(2)

# Regional summary
regional = df.groupby('Region1').agg({
    'Vector_Capacity': ['mean', 'std'],
    'EIP_Days': 'mean',
    'Outbreak_Risk_30d': 'mean'
}).round(2)
```

### With R
```r
library(tidyverse)
library(rstatix)

df <- read_csv('climate_output.csv')

# Global risk analysis
global_risk <- df %>%
  filter(EIP_Category == 'High', Vector_Capacity > 60)

# Seasonal comparison
seasonal_summary <- df %>%
  group_by(Season) %>%
  summarise(
    mean_capacity = mean(Vector_Capacity, na.rm = TRUE),
    mean_eip = mean(EIP_Days, na.rm = TRUE)
  )

# Regional comparison
regional_summary <- df %>%
  group_by(Region1) %>%
  summarise(
    mean_capacity = mean(Vector_Capacity, na.rm = TRUE),
    mean_risk = mean(Outbreak_Risk_30d, na.rm = TRUE)
  )
```

### With QGIS
```
1. Import climate_output.csv as Delimited Text Layer
2. Style Vector_Capacity using graduated symbols
3. Create heat map of Outbreak_Risk_30d
4. Label high-risk zones
5. Export for regional analysis
```

## Tips for AI Agents

### Data Handling
1. Validate column names match required format exactly
2. Check for missing coordinates (latitude/longitude = NA)
3. Verify date format is YYYY-MM-DD
4. Filter records with Valid_Data_Flag = 0 for analysis

### Variable Selection by Analysis Type

| Analysis | Primary Variables | Secondary Variables |
|----------|-------------------|-------------------|
| Transmission modeling | EIP_Days, Vector_Capacity | IR_Score, Outbreak_Risk_30d |
| Entomological | Larval_Survival, Adult_Survival | Vector_Fecundity, Gonotrophic_Cycle |
| Climate drivers | Temp_Mean, Precip_Total, Humidity_Mean | Temp_Trend, Precip_Anomaly |
| Risk stratification | Outbreak_Risk_30d, Climate_Suitability_Index | Critical_Threshold |
| Seasonal patterns | Season, Mosquito_Dev_Days, Persistence_Days | Weekly temperature/precip |
| Climate zone analysis | Temp_Mean, Season, Humidity_Mean | Climate_Suitability_Index |

### Statistical Recommendations (Global Applicability)
1. Use non-parametric tests for non-normal distributions
2. Apply Bonferroni correction for multiple comparisons
3. Report effect sizes alongside p-values
4. Consider mixed-effects models for hierarchical data
5. Account for spatial autocorrelation in regional analysis

### Performance Optimization
1. Process in batches of 100 for large datasets
2. API rate limiting: 0.3s delay included in script
3. Expect 30-60 minutes for 300+ locations
4. Enable parallel processing for multiple files

## Default Thresholds (Globally Applicable)

| Variable | Threshold | Used For | Global Context |
|----------|-----------|----------|----------------|
| Hot day | > 30°C | Hot_Days_Count | Tropical highland threshold |
| Very hot day | > 35°C | Very_Hot_Days | Extreme heat |
| Cold day | < 15°C | Cold_Days_Count | Temperate/altitude threshold |
| Heavy rain | > 10mm | Heavy_Rain_Days | Breeding site creation |
| High humidity | > 80% | High_Humidity_Days | Optimal vector survival |
| Calm wind | < 2 m/s | Calm_Days | Stagnant conditions |
| Tropical night | Tmin > 20°C | Tropical_Nights | Warm overnight |
| Heat stress | HI > 35°C | Heat_Stress_Days | Heat stress index |

## Data Sources

- **Climate Data**: NASA Langley Research Center POWER Project
- **API Endpoint**: https://power.larc.nasa.gov/api/temporal/daily/point
- **Coverage**: Global land surfaces, July 1981 - present
- **Resolution**: Daily temporal, point-based spatial
- **Limitations**: Reduced data quality in polar regions

## Citation

If using results from this toolkit, please cite:

### BibTeX
```bibtex
@software{climate_epidemiology_modeling_2026,
  title = {Climate Epidemiology Modeling Toolkit},
  version = {2.0},
  author = {Dr. Avinash M.},
  year = {2026},
  month = {April},
  url = {https://github.com/Infinitysouls/climate-epidemiology-modeling},
  license = {MIT}
}
```

### APA 7th Edition
```
Dr. Avinash M. (2026). Climate Epidemiology Modeling Toolkit (Version 2.0) 
[Computer software]. GitHub. https://github.com/Infinitysouls/climate-epidemiology-modeling
```

## License

MIT License - See LICENSE file

## Support

For issues or questions, open an issue on GitHub.
