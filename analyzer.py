import csv

def main():
    laps = []
    try:
        with open('race_data.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    lap_time = float(row['LapTime'])
                    laps.append({'Driver': row['Driver'], 'LapTime': lap_time})
                    print(f"Driver: {row['Driver']}, Lap Time: {lap_time}")
                except (ValueError, KeyError):
                    print(f"Skipping invalid row: {row}")
    except FileNotFoundError:
        print("Error: race_data.csv not found!")
    return laps

if __name__ == "__main__":
    main()
