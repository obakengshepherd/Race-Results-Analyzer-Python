import csv

def calculate_average_lap_time(laps):
    if not laps:
        return 0
    total = sum(lap['LapTime'] for lap in laps)
    return total / len(laps)

def main():
    laps = []
    try:
        with open('race_data.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    lap_time = float(row['LapTime'])
                    laps.append({'Driver': row['Driver'], 'LapTime': lap_time})
                except (ValueError, KeyError):
                    print(f"Skipping invalid row: {row}")
    except FileNotFoundError:
        print("Error: race_data.csv not found!")
        return
    
    if not laps:
        print("No valid lap data found.")
        return
    
    print("\nRace Results:")
    print(f"{'Driver':<15} {'Lap Time':<10}")
    print("-" * 25)
    for lap in laps:
        print(f"{lap['Driver']:<15} {lap['LapTime']:<10.2f}")
    avg_time = calculate_average_lap_time(laps)
    print(f"\nAverage Lap Time: {avg_time:.2f} seconds")

if __name__ == "__main__":
    main()