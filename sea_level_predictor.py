import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Step 1: Read the data
    df = pd.read_csv('epa-sea-level.csv')

    # Step 2: Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Observed Data', color='blue')

    # Step 3: Perform linear regression on all data
    res_full = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_full = pd.Series(range(1880, 2051))
    sea_level_full = res_full.slope * years_full + res_full.intercept
    plt.plot(years_full, sea_level_full, label='Best Fit Line (1880–2050)', color='red')

    # Step 4: Perform linear regression on data from year 2000
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2051))
    sea_level_recent = res_recent.slope * years_recent + res_recent.intercept
    plt.plot(years_recent, sea_level_recent, label='Best Fit Line (2000–2050)', color='green')

    # Step 5: Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()