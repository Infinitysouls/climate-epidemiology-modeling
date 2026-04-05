# Usage Guide

## Basic Usage

### Windows

```cmd
fetch_climate.bat
```

### Linux/macOS

```bash
python scripts/fetch_climate.py
```

The script will:
1. Load your outbreak data from the configured input file
2. Fetch 30-day climate data for each outbreak location
3. Calculate summary statistics
4. Save results to the output CSV file

## Input File Requirements

Your outbreak data CSV must contain these columns:

| Column Name | Example | Description |
|-------------|---------|-------------|
| `[Date of Outbreak]` | 2017-05-15 | Date in YYYY-MM-DD format |
| `[Latitude]` | 23.456 | Latitude in decimal degrees |
| `[Longitude]` | 77.890 | Longitude in decimal degrees |
| `[State]` | Rajasthan | State name |
| `[District_Clean]` | Jaipur | District name |

### Example CSV Structure

```csv
[Date of Outbreak],[Latitude],[Longitude],[State],[District_Clean]
2017-05-15,23.456,77.890,Rajasthan,Jaipur
2017-06-20,25.317,82.456,Uttar Pradesh,Varanasi
2017-07-10,19.876,75.456,Maharashtra,Pune
```

## Configuration

### Using Environment Variables

**Windows:**
```cmd
set IDSP_INPUT_CSV=malaria_outbreaks.csv
set IDSP_OUTPUT_CSV=climate_data.csv
python scripts/fetch_climate.py
```

**Linux/macOS:**
```bash
export IDSP_INPUT_CSV=malaria_outbreaks.csv
export IDSP_OUTPUT_CSV=climate_data.csv
python scripts/fetch_climate.py
```

### Default Values

If environment variables are not set, defaults are used:
- Input: `malaria_master_export.csv` (in project root)
- Output: `climate_data.csv` (in project root)

## Understanding Output

The script generates a CSV with the following columns:

| Column | Description | Unit |
|--------|-------------|------|
| `Date of Outbreak` | Original outbreak date | - |
| `Latitude` | Location latitude | degrees |
| `Longitude` | Location longitude | degrees |
| `State` | State name | - |
| `District` | District name | - |
| `Climate_Start` | Start of 30-day window | YYYY-MM-DD |
| `Climate_End` | End of 30-day window | YYYY-MM-DD |
| `Temp_Mean` | Mean temperature | °C |
| `Temp_Min` | Minimum temperature | °C |
| `Temp_Max` | Maximum temperature | °C |
| `Precip_Total` | Total precipitation | mm |
| `Precip_Days` | Number of rainy days | days |
| `Humidity_Mean` | Mean relative humidity | % |
| `Wind_Mean` | Mean wind speed | m/s |
| `Days_Data` | Days of data retrieved | days |

## Climate Window

By default, the script fetches climate data for the 30 days prior to each outbreak date. This window can be adjusted by modifying the `fetch_and_parse()` function call in the script.

## Progress and Logging

The script displays progress for each location:
- Current location and date
- Success/failure status
- Key statistics (temperature, precipitation)

## Error Handling

If data cannot be retrieved for a location:
- An error message is displayed
- The record is saved with an "Error" column
- Processing continues with remaining locations

## Performance Notes

- Processing time: ~30-60 minutes for 300+ locations
- Rate limiting: 0.3 second delay between API calls
- Network: Requires stable internet connection

## Integration with Analysis Tools

The output CSV can be used with:
- Pandas for statistical analysis
- R for epidemiological modeling
- QGIS for geospatial visualization
- Excel/LibreOffice for basic analysis

## Common Issues

### "File not found" error
- Verify the input CSV path is correct
- Check file permissions

### Empty or missing data
- Check coordinates are valid (lat: -90 to 90, lon: -180 to 180)
- Verify date format is correct
- Check NASA POWER API status

### Rate limiting
- Reduce the sleep delay (not recommended)
- Process data in batches
- Use multiple API keys (enterprise users)
