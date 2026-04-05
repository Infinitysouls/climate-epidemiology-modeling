# Climate Disease Surveillance Toolkit

A Python toolkit for analyzing climate data in public health disease surveillance. Fetches meteorological data from NASA's POWER API and combines it with outbreak data for epidemiological analysis.

## Overview

This toolkit enables public health professionals to:

- Fetch climate data (temperature, precipitation, humidity, wind speed) for any geographic location
- Correlate climate factors with disease outbreak patterns
- Support evidence-based surveillance and response planning

## Features

- **NASA POWER API Integration**: Access 30+ years of climate data globally
- **Automated Data Fetching**: Batch process multiple outbreak locations
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
| `[Date of Outbreak]` | Date in YYYY-MM-DD format |
| `[Latitude]` | Decimal degrees (e.g., 23.45) |
| `[Longitude]` | Decimal degrees (e.g., 77.56) |
| `[State]` | State name |
| `[District_Clean]` | District name |

Set the input file path:
```bash
export IDSP_INPUT_CSV=your_outbreak_data.csv
export IDSP_OUTPUT_CSV=climate_results.csv
python scripts/fetch_climate.py
```

**Windows:**
```cmd
set IDSP_INPUT_CSV=your_outbreak_data.csv
set IDSP_OUTPUT_CSV=climate_results.csv
python scripts/fetch_climate.py
```

## Output

The script generates a CSV file with climate data:

| Column | Description |
|--------|-------------|
| `Date of Outbreak` | Original outbreak date |
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

- **Epidemiological Research**: Study climate-disease relationships
- **Disease Surveillance**: Support early warning systems
- **Public Health Planning**: Inform prevention strategies
- **Academic Research**: Source data for publications

## Data Sources

- **Climate Data**: [NASA POWER API](https://power.larc.nasa.gov/) (Public Domain)
- **Outbreak Data**: Integrated Disease Surveillance Programme (IDSP), India

## Ethical Statement

This toolkit is designed for legitimate public health research and surveillance purposes. Users must:

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
@software{climate_disease_surveillance,
  title = {Climate Disease Surveillance Toolkit},
  author = {Public Health Research Community},
  year = {2024},
  url = {https://github.com/Infinitysouls/climate-disease-surveillance}
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

*This toolkit is intended for public health professionals and researchers.*
