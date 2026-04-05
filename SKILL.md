# Climate Epidemiology Modeling Skill

## Description

A Python toolkit for analyzing climate data in infectious disease epidemiology research. Fetches meteorological data from satellite-based climate APIs and computes 122 variables including epidemiological indices for disease transmission modeling.

## Capabilities

- `fetch_climate_data` - Retrieve satellite-based climate data for any geographic location
- `compute_epidemiological_indices` - Calculate EIP, vector capacity, transmission risk metrics
- `analyze_climate_disease` - Correlate climate factors with disease transmission patterns
- `generate_derived_variables` - Create interaction terms, composites, and lagged effects

## Prerequisites

### System Requirements
- Python 3.8 or higher
- pip package manager
- Internet connection (for API access)

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

The input CSV must contain these columns:

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
```

## Output

### 122 Computed Variables

The script generates a CSV with 122 variables organized into categories:

| Category | Count | Examples |
|----------|-------|----------|
| Metadata | 7 | Date, Latitude, Longitude, Region1, Region2, Climate_Start, Climate_End |
| Temperature | 22 | Temp_Mean, Temp_Min, Temp_Max, Temp_P75, Hot_Days_Count |
| Precipitation | 22 | Precip_Total, Precip_Days, Heavy_Rain_Days, Wet_Days_Streak |
| Humidity | 13 | Humidity_Mean, Humidity_Max, High_Humidity_Days |
| Wind | 10 | Wind_Mean, Wind_Max, Calm_Days, Windy_Days |
| Interactions | 12 | Heat_Index_Celsius, Discomfort_Index, Transmission_Risk_Proxy |
| Disease Indices | 13 | EIP_Days, Vector_Capacity, Larval_Survival, IR_Score |
| Composites | 10 | Climate_Suitability_Index, Vector_Capacity, Wet_Season_Indicator |
| Temporal | 4 | Month, Week_Number, Season |
| Lagged | 6 | Temp_Lag_7d, Precip_Anomaly |
| Summary | 3 | Days_Data, Valid_Data_Flag, Processing_Status |

### Key Epidemiological Variables

| Variable | Description | Unit |
|----------|-------------|------|
| `EIP_Days` | Extrinsic Incubation Period - parasite development time | days |
| `EIP_Category` | EIP risk classification | Low/Medium/High |
| `Vector_Capacity` | Vector transmission capacity | 0-100 |
| `Transmission_Risk_Proxy` | Climate transmission risk estimate | 0-100 |
| `Larval_Survival` | Immature vector survival rate | % |
| `Adult_Survival` | Adult vector survival rate | % |
| `Mosquito_Dev_Days` | Suitable vector development days | days |
| `Climate_Suitability_Index` | Overall climate suitability for transmission | 0-100 |
| `Outbreak_Risk_30d` | 30-day outbreak risk scale | 0-3 |

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
from fetch_climate import fetch_daily_data, compute_all_metrics
from datetime import datetime

# Fetch data for single location
daily_data = fetch_daily_data(23.456, 77.890, "2017-05-01", "2017-05-31")

# Compute all metrics
metrics = compute_all_metrics(daily_data, datetime(2017, 5, 15))

print(f"EIP Days: {metrics['EIP_Days']}")
print(f"Vector Capacity: {metrics['Vector_Capacity']}")
```

## AI Prompt Templates

Use these ready-to-use prompts with coding assistants:

### Template 1: Basic Data Fetch
```
Fetch climate data for all locations in my outbreak CSV file and save results to climate_output.csv
```

### Template 2: Filter High Risk Areas
```
Analyze the climate_output.csv and identify locations with EIP_Category = "High" and Vector_Capacity > 50
```

### Template 3: Statistical Analysis
```
Perform correlation analysis between Temperature_Mean and Transmission_Risk_Proxy in the output CSV
```

### Template 4: Time Series Analysis
```
Create a time series plot showing Temp_Mean trends across all events in the data
```

### Template 5: Risk Mapping
```
Generate a risk map showing Outbreak_Risk_30d values by Region1
```

### Template 6: Seasonal Analysis
```
Compare Vector_Capacity across different seasons (summer, monsoon, winter)
```

### Template 7: Extreme Events
```
Identify locations with Hot_Days_Count > 20 and Heavy_Rain_Days > 5
```

### Template 8: Export Subsets
```
Export only locations in the monsoon season with Climate_Suitability_Index > 60
```

### Template 9: Summary Statistics
```
Calculate mean, median, and standard deviation for all disease indices by Region1
```

### Template 10: Data Quality Check
```
Identify records where Valid_Data_Flag = 0 or Days_Data < 25
```

### Template 11: Custom Analysis
```
For locations with EIP_Category = "High", calculate the correlation between humidity metrics and transmission risk
```

### Template 12: Visualization
```
Create a scatter plot of Temp_Mean vs Precip_Total colored by Season
```

## Integration Patterns

### With Pandas
```python
import pandas as pd

df = pd.read_csv('climate_output.csv')

# High risk areas
high_risk = df[(df['EIP_Category'] == 'High') & (df['Vector_Capacity'] > 60)]

# Seasonal summary
seasonal = df.groupby('Season')[['EIP_Days', 'Vector_Capacity']].mean()
```

### With R
```r
library(tidyverse)

df <- read_csv('climate_output.csv')

# Risk analysis
high_risk <- df %>%
  filter(EIP_Category == 'High', Vector_Capacity > 60)

# Correlation
cor(df$Temp_Mean, df$Transmission_Risk_Proxy)
```

### With QGIS
```
Import climate_output.csv as delimited text layer
Style by Vector_Capacity using graduated symbols
Label by Region2
```

### With Statistical Software
```python
# SPSS/R/SAS import
df.to_csv('climate_for_analysis.csv', index=False)
# Then import into your preferred statistical software
```

## Tips for AI Agents

### Data Handling
1. Always validate CSV column names match the required format
2. Check for missing values in latitude/longitude
3. Verify date format is YYYY-MM-DD

### Variable Selection
1. For transmission modeling: Focus on `EIP_Days`, `Vector_Capacity`, `Transmission_Risk_Proxy`
2. For climate analysis: Focus on `Temp_Mean`, `Precip_Total`, `Humidity_Mean`
3. For risk stratification: Use `Outbreak_Risk_30d`, `Climate_Suitability_Index`

### Performance
1. Process large datasets in batches of 100 records
2. The script includes 0.3s delay between API calls (respects rate limits)
3. For 300+ locations, expect 30-60 minutes processing time

### Error Handling
1. Records with insufficient data get `Valid_Data_Flag = 0`
2. Check `Processing_Status` column for errors
3. API errors are logged with error messages in output

## Default Thresholds

| Variable | Threshold | Used For |
|----------|-----------|----------|
| Hot day | > 30°C | Hot_Days_Count |
| Very hot day | > 35°C | Very_Hot_Days |
| Cold day | < 15°C | Cold_Days_Count |
| Heavy rain | > 10mm | Heavy_Rain_Days |
| High humidity | > 80% | High_Humidity_Days |
| Calm wind | < 2 m/s | Calm_Days |

## Data Sources

- **Climate Data**: Satellite-based climate API (Public Domain)
- **API Endpoint**: https://power.larc.nasa.gov/api/temporal/daily/point
- **Coverage**: Global, 1981-present

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
  doi = {10.5281/zenodo.XXX},
  license = {MIT}
}
```

### APA 7th Edition
```
Dr. Avinash M.. (2026). Climate Epidemiology Modeling Toolkit (Version 2.0) 
[Computer software]. GitHub. https://github.com/Infinitysouls/climate-epidemiology-modeling
```

### IEEE
```
"Climate Epidemiology Modeling Toolkit," Dr. Avinash M., Version 2.0, Jan. 2026. 
[Online]. Available: https://github.com/Infinitysouls/climate-epidemiology-modeling
```

### Harvard
```
@online{climate2026,
  author = {Dr. Avinash M.},
  title = {Climate Epidemiology Modeling Toolkit},
  year = {2026},
  url = {https://github.com/Infinitysouls/climate-epidemiology-modeling},
  accessdate = {April 2026}
}
```

## License

MIT License - See LICENSE file

## Support

For issues or questions, open an issue on GitHub.
