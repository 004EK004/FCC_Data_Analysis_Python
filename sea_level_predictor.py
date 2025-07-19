import pandas as pd  #Pandas used for reading the files, data manipulation and analysis.
import matplotlib.pyplot as plt # Creates the visualisations.
from scipy.stats import linregress # Used for calculating linear regression statistics

def draw_plot():
    # Reads Data From The File Mentioned.
    df = pd.read_csv('epa-sea-level.csv')
    
    # Creates scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data Points')
    
    # Creates first line of best fit (all data)
    res1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred1 = pd.Series([i for i in range(1880, 2051)])
    y_pred1 = res1.slope * x_pred1 + res1.intercept
    plt.plot(x_pred1, y_pred1, 'r', label='Best Fit Line 1880-2013')
    
    # Create second line of best fit (from year 2000)
    df_recent = df[df['Year'] >= 2000]
    res2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_pred2 = pd.Series([i for i in range(2000, 2051)])
    y_pred2 = res2.slope * x_pred2 + res2.intercept
    plt.plot(x_pred2, y_pred2, 'green', label='Best Fit Line 2000-2013')
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()