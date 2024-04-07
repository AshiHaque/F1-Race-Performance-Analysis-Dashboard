import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
drivers_df = pd.read_csv("D:/Python Projects/F1 Race Performance Analysis Dashboard/Dataset/drivers.csv")
results_df = pd.read_csv("D:/Python Projects/F1 Race Performance Analysis Dashboard/Dataset/results.csv")
races_df = pd.read_csv("D:/Python Projects/F1 Race Performance Analysis Dashboard/Dataset/races.csv")

# Merge datasets
results_merged = pd.merge(results_df, races_df, on='raceId')

def get_driver_stats(driver_name):
    driver_id = drivers_df.loc[(drivers_df['forename'] + ' ' + drivers_df['surname']) == driver_name, 'driverId'].iloc[0]

    # Total Pole Positions
    total_pole_positions = len(results_merged[(results_merged['driverId'] == driver_id) & (results_merged['grid'] == 1)])

    # Total Podiums
    total_podiums = len(results_merged[(results_merged['driverId'] == driver_id) & (results_merged['positionOrder'].isin([1, 2, 3]))])

    # Total Wins
    total_wins = len(results_merged[(results_merged['driverId'] == driver_id) & (results_merged['positionOrder'] == 1)])

    # Total Fastest Laps
    total_fastest_laps = len(results_merged[(results_merged['driverId'] == driver_id) & (results_merged['rank'] == 1)])

    # Total Retirements
    total_retirements = len(results_merged[(results_merged['driverId'] == driver_id) & (results_merged['statusId'] != 1)])

    # Most Wins in a season
    most_wins_in_season = results_merged[(results_merged['driverId'] == driver_id) & (results_merged['positionOrder'] == 1)].groupby('year')['positionOrder'].count().max()

    # Most Podiums in a season
    most_podiums_in_season = results_merged[(results_merged['driverId'] == driver_id) & (results_merged['positionOrder'].isin([1, 2, 3]))].groupby('year')['positionOrder'].count().max()

    # Most retirements in a season
    most_retirements_in_season = results_merged[(results_merged['driverId'] == driver_id) & (results_merged['statusId'] != 1)].groupby('year')['statusId'].count().max()

    # Most Pole positions in a season
    most_pole_positions_in_season = results_merged[(results_merged['driverId'] == driver_id)].groupby('year')['grid'].apply(lambda x: (x == 1).sum()).max()

    # Most Fastest Laps in a season
    most_fastest_laps_in_season = results_merged[(results_merged['driverId'] == driver_id) & (results_merged['rank'] == 1)].groupby('year')['rank'].count().max()

    # Total Championships
    total_championships = len(results_merged[(results_merged['driverId'] == driver_id) & (results_merged['positionOrder'] == 1)]['year'].unique())

    # Display stats
    print("Driver: ", driver_name)
    print("Total Pole Positions:", total_pole_positions)
    print("Total Podiums:", total_podiums)
    print("Total Wins:", total_wins)
    print("Total Fastest Laps:", total_fastest_laps)
    print("Total Retirements:", total_retirements)
    print("Most Wins in a season:", most_wins_in_season)
    print("Most Podiums in a season:", most_podiums_in_season)
    print("Most retirements in a season:", most_retirements_in_season)
    print("Most Pole positions in a season:", most_pole_positions_in_season)
    print("Most Fastest Laps in a season:", most_fastest_laps_in_season)
    print("Total Championships:", total_championships)

# Test the function with a specific driver
get_driver_stats("Lewis Hamilton")
