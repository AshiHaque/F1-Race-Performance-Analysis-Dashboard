import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
constructors_df = pd.read_csv("D:/Python Projects/F1 Race Performance Analysis Dashboard/Dataset/constructors.csv")
constructor_results_df = pd.read_csv("D:/Python Projects/F1 Race Performance Analysis Dashboard/Dataset/constructor_results.csv")
constructor_standings_df = pd.read_csv("D:/Python Projects/F1 Race Performance Analysis Dashboard/Dataset/constructor_standings.csv")
races_df = pd.read_csv("D:/Python Projects/F1 Race Performance Analysis Dashboard/Dataset/races.csv")
results_df = pd.read_csv("D:/Python Projects/F1 Race Performance Analysis Dashboard/Dataset/results.csv")

# Merge datasets
constructor_results_merged = pd.merge(constructor_results_df, races_df, on='raceId')
results_merged = pd.merge(results_df, races_df, on='raceId')

def get_constructor_stats(constructor_name):
    constructor_id = constructors_df.loc[constructors_df['name'] == constructor_name, 'constructorId'].iloc[0]

    # Total Driver Championships
    total_driver_championships = len(results_merged[(results_merged['constructorId'] == constructor_id) & (results_merged['positionOrder'] == 1)]['driverId'].unique())

    # Total Constructor Championships
    total_constructor_championships = len(constructor_standings_df[(constructor_standings_df['constructorId'] == constructor_id) & (constructor_standings_df['position'] == 1)])

    # Total Pole Positions
    total_pole_positions = len(constructor_standings_df[(constructor_standings_df['constructorId'] == constructor_id) & (constructor_standings_df['positionText'] == '1')])

    # Total Podiums
    total_podiums = len(results_merged[(results_merged['constructorId'] == constructor_id) & (results_merged['positionOrder'].isin([1, 2, 3]))])

    # Total Wins
    total_wins = len(results_merged[(results_merged['constructorId'] == constructor_id) & (results_merged['positionOrder'] == 1)])

    # Total Fastest Laps
    total_fastest_laps = len(results_merged[(results_merged['constructorId'] == constructor_id) & (results_merged['rank'] == 1)])

    # Total Retirements
    total_retirements = len(results_merged[(results_merged['constructorId'] == constructor_id) & (results_merged['statusId'] == 31)])

    # Most Pole positions in a season
    most_pole_positions_in_season = constructor_standings_df[(constructor_standings_df['constructorId'] == constructor_id) & (constructor_standings_df['positionText'] == '1')].groupby('raceId').size().max()

    # Most Podiums in a season
    most_podiums_in_season = results_merged[(results_merged['constructorId'] == constructor_id) & (results_merged['positionOrder'].isin([1, 2, 3]))].groupby('year')['positionOrder'].count().max()

    # Most Wins in a season
    most_wins_in_season = results_merged[(results_merged['constructorId'] == constructor_id) & (results_merged['positionOrder'] == 1)].groupby('year')['positionOrder'].count().max()

    # Most Fastest Laps in a season
    most_fastest_laps_in_season = results_merged[(results_merged['constructorId'] == constructor_id) & (results_merged['rank'] == 1)].groupby('year')['rank'].count().max()

    # Most retirements in a season
    most_retirements_in_season = results_merged[(results_merged['constructorId'] == constructor_id) & (results_merged['statusId'] == 31)].groupby('year')['statusId'].count().max()

    # Total Points
    total_points = constructor_standings_df[constructor_standings_df['constructorId'] == constructor_id]['points'].sum()

     # Plot Total Points over the years
    constructor_points_over_years = constructor_standings_df[constructor_standings_df['constructorId'] == constructor_id].groupby('raceId')['points'].sum().reset_index()
    races_df_subset = races_df[['raceId', 'year']]
    constructor_points_over_years = pd.merge(constructor_points_over_years, races_df_subset, on='raceId')
    constructor_points_over_years = constructor_points_over_years.groupby('year')['points'].sum().reset_index()

    plt.figure(figsize=(10, 6))
    plt.bar(constructor_points_over_years['year'], constructor_points_over_years['points'], color='skyblue')
    plt.title('Total Points Over the Years for ' + constructor_name)
    plt.xlabel('Year')
    plt.ylabel('Total Points')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


    # Display stats
    print("Constructor: ", constructor_name)
    print("Total Driver Championships:", total_driver_championships)
    print("Total Constructor Championships:", total_constructor_championships)
    print("Total Pole Positions:", total_pole_positions)
    print("Total Podiums:", total_podiums)
    print("Total Wins:", total_wins)
    print("Total Fastest Laps:", total_fastest_laps)
    print("Total Retirements:", total_retirements)
    print("Most Pole positions in a season:", most_pole_positions_in_season)
    print("Most Podiums in a season:", most_podiums_in_season)
    print("Most Wins in a season:", most_wins_in_season)
    print("Most Fastest Laps in a season:", most_fastest_laps_in_season)
    print("Most retirements in a season:", most_retirements_in_season)
    print("Total Points:", total_points)

# Test the function with a specific constructor
get_constructor_stats("Ferrari")
