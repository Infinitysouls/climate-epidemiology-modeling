# Installation Guide

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Step 1: Clone or Download the Repository

```bash
git clone https://github.com/Infinitysouls/epidemiological-climate-toolkit.git
cd epidemiological-climate-toolkit
```

Or download and extract the ZIP file from GitHub.

## Step 2: Create a Virtual Environment (Recommended)

**Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs the following packages:
- `requests` - For making HTTP requests to climate API

## Step 4: Verify Installation

```bash
python scripts/fetch_climate.py --help
```

You should see the script run and prompt for input data.

## Optional: Additional Dependencies

For advanced analysis features:

```bash
pip install pandas numpy matplotlib scipy
```

## Data File Setup

Create or obtain a CSV file with health event data containing:

| Column | Required | Description |
|--------|----------|-------------|
| `[Date of Event]` | Yes | Date in YYYY-MM-DD format |
| `[Latitude]` | Yes | Decimal degrees |
| `[Longitude]` | Yes | Decimal degrees |
| `[State]` | Yes | State name |
| `[District_Clean]` | Yes | District name |

## Configuration (Optional)

Set environment variables to customize file paths:

```bash
# Linux/macOS
export CET_INPUT_CSV=your_data.csv
export CET_OUTPUT_CSV=climate_results.csv
```

```cmd
# Windows
set CET_INPUT_CSV=your_data.csv
set CET_OUTPUT_CSV=climate_results.csv
```

## Troubleshooting

### "ModuleNotFoundError: No module named 'requests'"

Ensure you've activated the virtual environment and installed requirements:

```bash
pip install -r requirements.txt
```

### API Errors

- Check your internet connection
- Climate API may be temporarily unavailable - wait and retry
- Verify your input CSV has valid coordinates

### Slow Performance

The script adds a 0.3-second delay between API calls to respect rate limits. For large datasets, expect 30-60 minutes processing time.

## Next Steps

See [USAGE.md](USAGE.md) for detailed usage instructions.
