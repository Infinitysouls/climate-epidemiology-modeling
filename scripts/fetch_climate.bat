@echo off
REM Climate Epidemiology Modeling Toolkit
REM Fetches climate data and computes epidemiological indices

echo ============================================================
echo Climate Epidemiology Modeling Toolkit
echo ============================================================
echo.
echo This script fetches 30-day climate data for each location
echo and computes 120+ metrics for epidemiological research.
echo.

REM Set default paths (customize as needed)
set CLIMATE_INPUT=data.csv
set CLIMATE_OUTPUT=climate_output.csv

echo Input file: %CLIMATE_INPUT%
echo Output file: %CLIMATE_OUTPUT%
echo.
echo Starting climate data fetch and analysis...
echo This may take 30-60 minutes for large datasets.
echo.

python scripts\fetch_climate.py -i %CLIMATE_INPUT% -o %CLIMATE_OUTPUT%

echo.
echo Done! Press any key to exit.
pause > nul
