import csv

def main():
    laps = []
    with open('race_data.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            laps.append({'Driver': row['Driver'], 'LapTime': float(row['LapTime'])})
            print(f"Driver: {row['Driver']}, Lap Time: {row['LapTime']}")

if __name__ == "__main__":
    main()