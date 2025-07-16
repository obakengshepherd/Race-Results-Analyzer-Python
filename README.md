# Race Results Analyzer
Python script to analyze race data from a CSV file, calculating stats like average lap time.

## v1 Features
- Reads `race_data.csv` (driver names, lap times).
- Stores data in a list of dictionaries.
- Calculates average lap time.
- Prints formatted results with aligned columns.
- Handles errors (missing file, invalid data, empty data).

## Sample Output

Race Results:
Driver          Lap Time
-------------------------
Verstappen      85.50
Hamilton        86.20
Leclerc         84.90
Sainz           85.00

Average Lap Time: 85.40 seconds


## Learned Topics
- Variables (`str`, `float`)
- Lists and dictionaries
- `for` loops
- `csv` module (`DictReader`)
- Error handling (`try-except`)
- String formatting (`f-strings`)

