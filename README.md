# Epidemiological Climate Toolkit

A Python toolkit for analyzing climate data in epidemiological research. Fetches meteorological data from satellite-based climate APIs and combines it with health event data for research analysis.

## Overview

This toolkit enables researchers and public health professionals to:

- Fetch climate data (temperature, precipitation, humidity, wind speed) for any geographic location
- Correlate climate factors with health event patterns
- Support evidence-based epidemiological research

## Features

- **Satellite Climate Data Integration**: Access 30+ years of climate data globally
- **Automated Data Fetching**: Batch process multiple locations
- **Climate Metrics**: Temperature, precipitation, humidity, and wind speed analysis
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

### Input Format

Prepare a CSV file with the following columns:

| Column | Description |
|--------|-------------|
| `[Date of Event]` | Date in YYYY-MM-DD format |
| `[Latitude]` | Decimal degrees (e.g., 23.45) |
| `[Longitude]` | Decimal degrees (e.g., 77.56) |
| `[State]` | State name |
| `[District_Clean]` | District name |

Set the input file path:
```bash
export CET_INPUT_CSV=your_data.csv
export CET_OUTPUT_CSV=climate_results.csv
python scripts/fetch_climate.py
```

**Windows:**
```cmd
set CET_INPUT_CSV=your_data.csv
set CET_OUTPUT_CSV=climate_results.csv
python scripts/fetch_climate.py
```

## Output

The script generates a CSV file with climate data:

| Column | Description |
|--------|-------------|
| `Date of Event` | Original event date |
| `Latitude`, `Longitude` | Location |
| `State`, `District` | Administrative divisions |
| `Climate_Start`, `Climate_End` | Data retrieval window |
| `Temp_Mean`, `Temp_Min`, `Temp_Max` | Temperature statistics (°C) |
| `Precip_Total` | Total precipitation (mm) |
| `Humidity_Mean` | Mean relative humidity (%) |
| `Wind_Mean` | Mean wind speed (m/s) |
| `Days_Data` | Number of days of data retrieved |

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

- **Epidemiological Research**: Study climate-health relationships
- **Health Surveillance**: Support early warning systems
- **Public Health Planning**: Inform prevention strategies
- **Academic Research**: Source data for publications

## Data Sources

- **Climate Data**: Satellite-based climate API (Public Domain)
- **Health Data**: User-provided surveillance data

## Ethical Statement

This toolkit is designed for legitimate public health research purposes. Users must:

- Comply with applicable data protection regulations
- Attribute data sources appropriately
- Not attempt to identify individuals from aggregated data
- Use findings responsibly for public health benefit

See [docs/ETHICS_GUIDELINES.md](docs/ETHICS_GUIDELINES.md) for full guidelines.

## Documentation

- [Installation Guide](docs/INSTALLATION.md)
- [Usage Instructions](docs/USAGE.md)
- [API Reference](docs/API_REFERENCE.md)
- [Ethics Guidelines](docs/ETHICS_GUIDELINES.md)

## Citation

If you use this toolkit in your research, please cite:

```bibtex
@software{epidemiological_climate_toolkit,
  title = {Epidemiological Climate Toolkit},
  author = {Research Community},
  year = {2024},
  url = {https://github.com/Infinitysouls/epidemiological-climate-toolkit}
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

*This toolkit is intended for researchers and public health professionals.*
