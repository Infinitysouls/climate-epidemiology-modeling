@echo off
REM Epidemiological Climate Toolkit
REM Fetches climate data for health event locations

echo ============================================================
echo Epidemiological Climate Toolkit
echo ============================================================
echo.
echo This script fetches 30-day climate data for each location
echo from satellite-based climate API.
echo.

REM Set default paths (customize as needed)
set CLIMATE_INPUT=data.csv
set CLIMATE_OUTPUT=climate_output.csv

echo Input file: %CLIMATE_INPUT%
echo Output file: %CLIMATE_OUTPUT%
echo.
echo Starting climate data fetch...
echo This may take 30-60 minutes for large datasets.
echo.

python scripts\fetch_climate.py -i %CLIMATE_INPUT% -o %CLIMATE_OUTPUT%

echo.
echo Done! Press any key to exit.
pause > nul
