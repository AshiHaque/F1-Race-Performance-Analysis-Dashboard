import pandas as pd

# Load datasets
circuits_df = pd.read_csv("D:/Python Projects/F1 Race Performance Analysis Dashboard/Dataset/circuits.csv")
races_df = pd.read_csv("D:/Python Projects/F1 Race Performance Analysis Dashboard/Dataset/races.csv")
results_df = pd.read_csv("D:/Python Projects/F1 Race Performance Analysis Dashboard/Dataset/results.csv")
drivers_df = pd.read_csv("D:/Python Projects/F1 Race Performance Analysis Dashboard/Dataset/drivers.csv")
constructors_df = pd.read_csv("D:/Python Projects/F1 Race Performance Analysis Dashboard/Dataset/constructors.csv")

# Merge datasets
results_merged = pd.merge(results_df, races_df, on='raceId')

def get_circuit_info(circuit_name):
    circuit_info = circuits_df[circuits_df['name'] == circuit_name]
    if circuit_info.empty:
        print("Circuit not found!")
        return

    circuit_id = circuit_info['circuitId'].iloc[0]

    # Total Races Held
    total_races_held = len(races_df[races_df['circuitId'] == circuit_id])

    # Total Winners
    winners_df = results_merged[(results_merged['circuitId'] == circuit_id) & (results_merged['positionOrder'] == 1)]
    total_winners = len(winners_df['driverId'].unique())

    # Most Successful Drivers
    most_successful_drivers = winners_df['driverId'].map(drivers_df.set_index('driverId')['forename'] + ' ' + drivers_df.set_index('driverId')['surname']).value_counts().head(3)

    # Most Successful Constructors
    most_successful_constructors = winners_df['constructorId'].map(constructors_df.set_index('constructorId')['name']).value_counts().head(3)

    # Display Circuit Info
    print("Circuit Name:", circuit_name)
    print("Location:", circuit_info['location'].iloc[0])
    print("Country:", circuit_info['country'].iloc[0])
    print("Latitude:", circuit_info['lat'].iloc[0])
    print("Longitude:", circuit_info['lng'].iloc[0])
    print("Altitude:", circuit_info['alt'].iloc[0], "meters")
    print("Total Races Held:", total_races_held)
    print("Total Winners:", total_winners)
    print("Most Successful Drivers:")
    for driver, wins in most_successful_drivers.items():
        print("-", driver, "(", wins, "wins )")
    print("Most Successful Constructors:")
    for constructor, wins in most_successful_constructors.items():
        print("-", constructor, "(", wins, "wins )")

# Test the function with a specific circuit
get_circuit_info("Autodromo Enzo e Dino Ferrari")
