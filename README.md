# Climate Epidemiology Modeling Toolkit

A Python toolkit for climate data analysis in infectious disease epidemiology modeling. Fetches meteorological data from satellite-based climate APIs and computes comprehensive metrics for epidemiological research.

## Overview

This toolkit enables researchers and public health professionals to:

- Fetch climate data (temperature, precipitation, humidity, wind speed) for any geographic location
- Compute 120+ climate metrics including epidemiological indices
- Correlate climate factors with infectious disease transmission patterns
- Support evidence-based epidemiological modeling and surveillance

## Features

- **Satellite Climate Data Integration**: Access 30+ years of climate data globally
- **Comprehensive Metrics**: 120+ computed variables including vector biology indices
- **Epidemiological Indices**: EIP, vector capacity, transmission risk estimates
- **Portable Design**: Works on Windows, Linux, and macOS

## Quick Start

### Installation

```bash
pip install -r requirements.txt
```

### Basic Usage

**Windows:**
```bash
fetch_climate.bat
```

**Linux/macOS:**
```bash
python scripts/fetch_climate.py
```

### Command Line Arguments

```bash
python scripts/fetch_climate.py -i input.csv -o output.csv
```

**Environment Variables:**
```bash
export CLIMATE_INPUT=your_data.csv
export CLIMATE_OUTPUT=climate_results.csv
python scripts/fetch_climate.py
```

### Input Format

Prepare a CSV file with the following columns:

| Column | Description |
|--------|-------------|
| `[Date of Event]` | Date in YYYY-MM-DD format |
| `[Latitude]` | Decimal degrees (e.g., 23.45) |
| `[Longitude]` | Decimal degrees (e.g., 77.56) |
| `[Region1]` | Primary region (e.g., State/Province) |
| `[Region2]` | Secondary region (e.g., District/County) |

### Example CSV Structure

```csv
[Date of Event],[Latitude],[Longitude],[Region1],[Region2]
2017-05-15,23.456,77.890,StateName,DistrictName
2017-06-20,25.317,82.456,StateName,DistrictName
2017-07-10,19.876,75.456,StateName,DistrictName
```

## Output Variables

The script generates a CSV with **120+ computed variables**:

| Category | Variables | Description |
|----------|-----------|-------------|
| **Metadata** | 7 | Date, Location, Region |
| **Temperature** | 20 | Mean, min, max, percentiles, weekly, thresholds |
| **Precipitation** | 18 | Total, days, intensity, streaks, cumulative |
| **Humidity** | 12 | Mean, min, max, percentiles, weekly |
| **Wind** | 10 | Mean, max, variability, thresholds |
| **Interactions** | 12 | Heat index, discomfort, correlations |
| **Disease Indices** | 12 | EIP, vector survival, transmission risk |
| **Composites** | 10 | Stress indices, suitability scores |
| **Temporal** | 10 | Season, month, day of year, lags |
| **Summary** | 3 | Data quality indicators |

See [docs/OUTPUT_VARIABLES.md](docs/OUTPUT_VARIABLES.md) for complete variable dictionary.

## Climate Parameters

| Parameter | Description | Unit |
|-----------|-------------|------|
| T2M | Temperature at 2 meters | °C |
| PRECTOTCORR | Precipitation (corrected) | mm |
| RH2M | Relative Humidity at 2 meters | % |
| WS2M | Wind Speed at 2 meters | m/s |

See [docs/API_REFERENCE.md](docs/API_REFERENCE.md) for detailed API documentation.

## Use Cases

This toolkit is designed for:

- **Infectious Disease Modeling**: Climate-disease transmission analysis
- **Epidemiological Research**: Vector biology and climate relationships
- **Health Surveillance**: Early warning system development
- **Public Health Planning**: Climate-informed intervention strategies
- **Academic Research**: Source data for publications

## Data Sources

- **Climate Data**: Satellite-based climate API (Public Domain)
- **Health Data**: User-provided surveillance data

## Ethical Statement

This toolkit is designed for legitimate public health research and epidemiological studies. Users must:

- Comply with applicable data protection regulations
- Attribute data sources appropriately
- Not attempt to identify individuals from aggregated data
- Use findings responsibly for public health benefit

See [docs/ETHICS_GUIDELINES.md](docs/ETHICS_GUIDELINES.md) for full guidelines.

## Documentation

- [Installation Guide](docs/INSTALLATION.md)
- [Usage Instructions](docs/USAGE.md)
- [API Reference](docs/API_REFERENCE.md)
- [Output Variables](docs/OUTPUT_VARIABLES.md)
- [Ethics Guidelines](docs/ETHICS_GUIDELINES.md)

## Citation

If you use this toolkit in your research, please cite:

### BibTeX
```bibtex
@software{climate_epidemiology_modeling_2024,
  title = {Climate Epidemiology Modeling Toolkit},
  version = {2.0},
  author = {Research Community},
  year = {2024},
  month = {January},
  url = {https://github.com/Infinitysouls/climate-epidemiology-modeling},
  license = {MIT}
}
```

### APA 7th Edition
```
Research Community. (2024). Climate Epidemiology Modeling Toolkit (Version 2.0) 
[Computer software]. GitHub. https://github.com/Infinitysouls/climate-epidemiology-modeling
```

### IEEE
```
"Climate Epidemiology Modeling Toolkit," Research Community, Version 2.0, Jan. 2024. 
[Online]. Available: https://github.com/Infinitysouls/climate-epidemiology-modeling
```

### Harvard
```
@online{climate2024,
  author = {Research Community},
  title = {Climate Epidemiology Modeling Toolkit},
  year = {2024},
  url = {https://github.com/Infinitysouls/climate-epidemiology-modeling},
  accessdate = {January 2024}
}
```

See also: `CITATION.cff` for formatted citation files.

## License

MIT License - See [LICENSE](LICENSE) file.

## Contributing

Contributions welcome! Please read the contribution guidelines and submit pull requests.

## Support

For questions or issues, please open an issue on GitHub.

---

*This toolkit is intended for researchers and public health professionals in infectious disease epidemiology.*
