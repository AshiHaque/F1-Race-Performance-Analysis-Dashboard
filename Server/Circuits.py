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
        return {"error": "Circuit not found!"}

    circuit_id = circuit_info['circuitId'].iloc[0]
    # Extract all necessary fields from the dataset
    location = circuit_info['location'].iloc[0]
    country = circuit_info['country'].iloc[0]
    lat = circuit_info['lat'].iloc[0]
    lng = circuit_info['lng'].iloc[0]
    alt = circuit_info['alt'].iloc[0]

    # Construct the response dictionary with all fields
    circuit_info_dict = {
        "Circuit Name": circuit_name,
        "Location": location,
        "Country": country,
        "Latitude": lat,
        "Longitude": lng,
        "Altitude": alt
    }

    return circuit_info_dict

def get_all_circuit_names():
    # Extract all circuit names from the 'name' column of the circuits dataframe
    circuit_names = circuits_df['name'].tolist()
    return circuit_names
