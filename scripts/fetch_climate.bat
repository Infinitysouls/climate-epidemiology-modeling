@echo off
REM Climate Disease Surveillance Toolkit
REM Fetches climate data for outbreak locations using NASA POWER API

echo ============================================================
echo Climate Disease Surveillance Toolkit
echo ============================================================
echo.
echo This script fetches 30-day climate data for each outbreak
echo location from NASA POWER API.
echo.

REM Set default paths (customize as needed)
set IDSP_INPUT_CSV=malaria_master_export.csv
set IDSP_OUTPUT_CSV=climate_data.csv

echo Input file: %IDSP_INPUT_CSV%
echo Output file: %IDSP_OUTPUT_CSV%
echo.
echo Starting climate data fetch...
echo This may take 30-60 minutes for large datasets.
echo.

python scripts\fetch_climate.py

echo.
echo Done! Press any key to exit.
pause > nul
