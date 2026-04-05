# Climate Epidemiology Modeling Toolkit

A Python toolkit for climate data analysis in infectious disease epidemiology research. Fetches satellite-based meteorological data and computes comprehensive climate and epidemiological variables for disease transmission modeling.

---

## Overview

This toolkit enables researchers to:

- **Fetch Climate Data**: Retrieve 30+ years of satellite-based climate data for any global location
- **Compute Epidemiological Indices**: Calculate vector biology metrics including EIP, vector capacity, and transmission risk
- **Analyze Climate-Disease Relationships**: Correlate environmental factors with infectious disease patterns
- **Support Surveillance Systems**: Develop climate-informed early warning systems

---

## Scientific Background

### Climate and Infectious Disease Dynamics

Environmental factors play a critical role in infectious disease transmission, particularly for vector-borne diseases. Key relationships include:

| Climate Factor | Disease Mechanism |
|---------------|-------------------|
| **Temperature** | Affects vector development rate, survival, and pathogen replication (Extrinsic Incubation Period) |
| **Precipitation** | Creates breeding sites, influences vector abundance |
| **Humidity** | Affects vector survival and biting behavior |
| **Wind** | Influences vector dispersal and pathogen spread |

### Key Epidemiological Concepts

**Extrinsic Incubation Period (EIP)**: The time required for a pathogen to develop within a vector before transmission is possible. Warmer temperatures accelerate EIP, increasing transmission potential.

**Vector Capacity**: A composite metric representing the potential for vector-borne disease transmission, incorporating vector density, survival rates, and biting behavior.

**Climate Suitability Index**: An integrated measure of environmental conditions favorable for disease transmission.

---

## Features

| Feature | Description |
|---------|-------------|
| **122 Computed Variables** | Comprehensive set of climate and epidemiological metrics |
| **Satellite Data** | Global coverage from NASA POWER API (1981-present) |
| **Vector Biology Indices** | EIP, vector capacity, survival rates |
| **Composite Indices** | Climate suitability, transmission risk |
| **Temporal Analysis** | Weekly lags, seasonal patterns, trends |
| **Quality Indicators** | Data validation and completeness flags |

---

## Quick Start

### Installation

```bash
git clone https://github.com/Infinitysouls/climate-epidemiology-modeling.git
cd climate-epidemiology-modeling
pip install -r requirements.txt
```

### Basic Usage

```bash
# Windows
fetch_climate.bat

# Linux/macOS
python scripts/fetch_climate.py -i your_data.csv -o climate_results.csv
```

### Input Format

Prepare a CSV with:

| Column | Description | Example |
|--------|-------------|---------|
| `[Date of Event]` | Event date (YYYY-MM-DD) | 2017-05-15 |
| `[Latitude]` | Decimal degrees | 23.456 |
| `[Longitude]` | Decimal degrees | 77.890 |
| `[Region1]` | Primary region | Rajasthan |
| `[Region2]` | Secondary region | Jaipur |

---

## Scientific Use Cases

### 1. Vector-Borne Disease Transmission Modeling

**Objective**: Assess climate suitability for vector-borne disease transmission

**Variables Used**:
- `EIP_Days` - Extrinsic incubation period
- `Vector_Capacity` - Transmission potential
- `Larval_Survival` - Immature vector viability
- `Adult_Survival` - Adult vector longevity

**Analysis**: Identify regions where climate conditions favor sustained transmission

**Example**:
```python
import pandas as pd
df = pd.read_csv('climate_results.csv')

# High transmission potential areas
high_risk = df[(df['Vector_Capacity'] > 60) & (df['EIP_Category'] == 'High')]
```

### 2. Climate-Based Early Warning Systems

**Objective**: Develop predictive models for disease outbreaks

**Variables Used**:
- `Temp_Trend` - Temperature trajectory
- `Precip_Cumulative_14d` - Recent rainfall patterns
- `Outbreak_Risk_30d` - 30-day risk projection
- `Critical_Threshold` - Risk threshold exceeded

**Analysis**: Correlate climate anomalies with outbreak occurrence

**Example**:
```python
# Identify预警阈值触发的区域
alerts = df[df['Critical_Threshold'] == 1]
print(f"Alert regions: {len(alerts)}")
```

### 3. Seasonal Transmission Patterns

**Objective**: Characterize seasonal dynamics of disease transmission

**Variables Used**:
- `Season` - Climate season classification
- `Mosquito_Dev_Days` - Vector development days
- `Persistence_Days` - Consecutive risk days
- `Wet_Season_Indicator` - Seasonal rainfall

**Analysis**: Compare transmission metrics across seasons

**Example**:
```python
seasonal = df.groupby('Season').agg({
    'Vector_Capacity': 'mean',
    'EIP_Days': 'mean',
    'Transmission_Risk_Proxy': 'mean'
}).round(2)
```

### 4. Entomological Risk Assessment

**Objective**: Evaluate vector population dynamics

**Variables Used**:
- `Larval_Survival` - Breeding site productivity
- `Vector_Fecundity` - Vector reproductive capacity
- `Gonotrophic_Cycle` - Reproductive cycle duration
- `Blood_Feeding_Rate` - Feeding frequency

**Analysis**: Estimate vector abundance potential

**Example**:
```python
# High entomological risk areas
entomological_risk = df[
    (df['Larval_Survival'] > 70) & 
    (df['Vector_Fecundity'] > 5)
]
```

### 5. Climate Change Impact Assessment

**Objective**: Project future transmission patterns under climate scenarios

**Variables Used**:
- `Temp_Mean`, `Temp_Trend` - Temperature changes
- `Precip_Total`, `Rain_Probability` - Precipitation patterns
- `Climate_Suitability_Index` - Integrated suitability
- `Aridity_Index` - Dryness indicator

**Analysis**: Compare current and projected conditions

**Example**:
```python
# Expanding transmission zones
suitable_areas = df[df['Climate_Suitability_Index'] > 50]
```

### 6. Geographic Risk Stratification

**Objective**: Classify regions by transmission risk level

**Variables Used**:
- `Outbreak_Risk_30d` - Risk classification (0-3)
- `IR_Score` - Infection risk score
- `Vector_Density_Index` - Vector abundance proxy
- `Region1`, `Region2` - Administrative divisions

**Analysis**: Prioritize resources by risk level

**Example**:
```python
risk_stratification = df.groupby('Region1').agg({
    'Outbreak_Risk_30d': 'max',
    'IR_Score': 'mean'
}).sort_values('IR_Score', ascending=False)
```

### 7. Extreme Climate Event Analysis

**Objective**: Assess impact of weather extremes on transmission

**Variables Used**:
- `Hot_Days_Count` - Heat wave days
- `Heavy_Rain_Days` - Flooding risk
- `Dry_Days_Streak` - Drought conditions
- `Wet_Days_Streak` - Prolonged rainfall

**Analysis**: Identify transmission windows following extreme events

**Example**:
```python
# Post-flood transmission risk
post_flood = df[(df['Heavy_Rain_Days'] > 5) & (df['Humidity_Mean'] > 70)]
```

### 8. Intervention Timing Optimization

**Objective**: Identify optimal timing for control measures

**Variables Used**:
- `Mosquito_Dev_Days` - Vector development conditions
- `Persistence_Days` - Sustained risk periods
- `Season` - Seasonal classification
- `Temp_W1_Avg` to `W4_Avg` - Weekly temperature progression

**Analysis**: Determine intervention windows

**Example**:
```python
# Pre-monsoon intervention window
pre_monsoon = df[(df['Season'] == 'summer') & (df['Mosquito_Dev_Days'] > 15)]
```

---

## Output Variables (122 Total)

| Category | Count | Key Variables |
|----------|-------|---------------|
| **Temperature** | 22 | Temp_Mean, Temp_Max, Temp_Std, Hot_Days_Count, Growing_Degree_Days |
| **Precipitation** | 22 | Precip_Total, Precip_Days, Heavy_Rain_Days, Wet_Days_Streak |
| **Humidity** | 13 | Humidity_Mean, High_Humidity_Days, Humidity_Change |
| **Wind** | 10 | Wind_Mean, Wind_Max, Calm_Days |
| **Interactions** | 12 | Heat_Index_Celsius, Discomfort_Index, Transmission_Risk_Proxy |
| **Disease Indices** | 13 | EIP_Days, EIP_Category, Vector_Capacity, Larval_Survival |
| **Composites** | 10 | Climate_Suitability_Index, Vector_Capacity, Wet_Season_Indicator |
| **Temporal** | 4 | Month, Week_Number, Season, Day_Of_Year |
| **Lagged** | 6 | Temp_Lag_7d, Precip_Anomaly, Temp_Trend |
| **Metadata** | 7 | Date, Location, Regions |

See [docs/OUTPUT_VARIABLES.md](docs/OUTPUT_VARIABLES.md) for complete documentation.

---

## Climate Parameters

| Parameter | Description | Source |
|-----------|-------------|--------|
| T2M | Temperature at 2 meters | NASA POWER API |
| PRECTOTCORR | Precipitation (corrected) | NASA POWER API |
| RH2M | Relative Humidity at 2 meters | NASA POWER API |
| WS2M | Wind Speed at 2 meters | NASA POWER API |

---

## Data Sources

- **Climate Data**: [NASA Langley Research Center POWER Project](https://power.larc.nasa.gov/) (Public Domain)
- **Coverage**: Global land surfaces, 1981-present
- **Resolution**: Daily temporal, point-based spatial

---

## Ethical Statement

This toolkit is designed for legitimate public health research and epidemiological studies. Users must:

- Comply with applicable data protection regulations
- Attribute data sources appropriately
- Not attempt to identify individuals from aggregated data
- Use findings responsibly for public health benefit

See [docs/ETHICS_GUIDELINES.md](docs/ETHICS_GUIDELINES.md) for full guidelines.

---

## Documentation

| Document | Description |
|----------|-------------|
| [SKILL.md](SKILL.md) | AI agent instructions and prompt templates |
| [Installation Guide](docs/INSTALLATION.md) | Setup instructions |
| [Usage Guide](docs/USAGE.md) | Detailed usage instructions |
| [API Reference](docs/API_REFERENCE.md) | Climate API documentation |
| [Output Variables](docs/OUTPUT_VARIABLES.md) | Complete variable dictionary |
| [Ethics Guidelines](docs/ETHICS_GUIDELINES.md) | Data ethics and best practices |

---

## Citation

If you use this toolkit in your research, please cite:

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

---

## License

MIT License - See [LICENSE](LICENSE) file.

---

## Contributing

Contributions welcome! Please submit pull requests or open issues for suggestions.

---

## Support

For questions or issues, please open an issue on GitHub.

---

*This toolkit is intended for researchers and public health professionals in infectious disease epidemiology.*
