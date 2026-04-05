# NASA POWER API Reference

## Overview

This toolkit uses the [NASA Langley Research Center (LaRC) POWER Project](https://power.larc.nasa.gov/) API to retrieve climate data. NASA POWER provides over 30 years of satellite-based meteorology data globally.

## API Endpoint

```
https://power.larc.nasa.gov/api/temporal/daily/point
```

## Base URL

```python
NASA_POWER_API_URL = "https://power.larc.nasa.gov/api/temporal/daily/point"
```

## Request Parameters

| Parameter | Required | Description | Example |
|-----------|----------|-------------|---------|
| `community` | Yes | Data community (RE for renewable energy) | `RE` |
| `parameters` | Yes | Comma-separated list of parameters | `T2M,PRECTOTCORR` |
| `latitude` | Yes | Decimal degrees (-90 to 90) | `23.45` |
| `longitude` | Yes | Decimal degrees (-180 to 180) | `77.56` |
| `start` | Yes | Start date (YYYYMMDD) | `20170501` |
| `end` | Yes | End date (YYYYMMDD) | `20170531` |
| `format` | No | Response format (default: JSON) | `JSON` |

## Climate Parameters

### T2M - Temperature at 2 Meters

| Property | Value |
|----------|-------|
| Full Name | Temperature at 2 Meters |
| Unit | °C (Celsius) |
| Description | Air temperature at 2 meters above ground |

### PRECTOTCORR - Precipitation

| Property | Value |
|----------|-------|
| Full Name | Precipitation (Corrected) |
| Unit | mm (millimeters) |
| Description | Total precipitation including rain, snow, and hail |

### RH2M - Relative Humidity

| Property | Value |
|----------|-------|
| Full Name | Relative Humidity at 2 Meters |
| Unit | % (percent) |
| Description | Ratio of actual to saturation vapor pressure |

### WS2M - Wind Speed

| Property | Value |
|----------|-------|
| Full Name | Wind Speed at 2 Meters |
| Unit | m/s (meters per second) |
| Description | Horizontal wind speed at 2 meters |

## Example API Call

```python
import requests

params = {
    "community": "RE",
    "parameters": "T2M,PRECTOTCORR,RH2M,WS2M",
    "latitude": 23.45,
    "longitude": 77.56,
    "start": "20170501",
    "end": "20170531",
    "format": "JSON"
}

response = requests.get(
    "https://power.larc.nasa.gov/api/temporal/daily/point",
    params=params,
    timeout=30
)

data = response.json()
```

## Response Structure

```json
{
  "properties": {
    "parameter": {
      "T2M": {
        "20170501": 28.5,
        "20170502": 29.1,
        ...
      },
      "PRECTOTCORR": {
        "20170501": 0.0,
        "20170502": 5.2,
        ...
      }
    }
  }
}
```

## Data Coverage

| Parameter | Coverage |
|-----------|----------|
| Temporal | July 1981 - present |
| Spatial | Global land surfaces |
| Resolution | Daily |

## Data Quality Notes

- Data is derived from satellite observations and reanalysis
- Some missing values may occur (marked as null)
- Corrections applied for gauge undercatch (precipitation)

## API Limitations

- **Rate Limit**: Recommended 1 request per second
- **Temporal Limit**: Single date range per request
- **Spatial Limit**: Single point per request

## Citation

When using NASA POWER data, please cite:

> Stackhouse, P.W., Maxwell, S., DiGirolamo, L., Haines, D., Booth, M., Cox, S., Tucker, C., Hoell, A., Blunschi, T., Anderson, J., Semeraro, J., Gokhan, B., and Zhang, J.: NASA LaRC POWER Project - Updated to v8.0.12, NASA Langley Atmospheric Science Data Center DAAC, accessed May 2024, https://power.larc.nasa.gov/, 2022.

## Additional Resources

- [NASA POWER Website](https://power.larc.nasa.gov/)
- [API Documentation](https://power.larc.nasa.gov/api/pages/en/)
- [Data Availability](https://power.larc.nasa.gov/api/pages/en/!#!/)

## Troubleshooting

| Issue | Solution |
|-------|----------|
| 403 Forbidden | Check API endpoint URL is correct |
| 404 Not Found | Verify latitude/longitude are valid |
| Timeout | Reduce date range or check network |
| Empty data | Date range may have no satellite coverage |
