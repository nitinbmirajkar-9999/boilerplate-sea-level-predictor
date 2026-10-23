
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    years = range(1880, 2051)
    plt.plot(
        years,
        slope * pd.Series(years) + intercept,
        color="red"
    )

    # Create second line of best fit
    recent_df = df[df["Year"] >= 2000]

    slope_recent, intercept_recent, r_value, p_value, std_err = linregress(
        recent_df["Year"],
        recent_df["CSIRO Adjusted Sea Level"]
    )

    recent_years = range(2000, 2051)
    plt.plot(
        recent_years,
        slope_recent * pd.Series(recent_years) + intercept_recent,
        color="green"
    )

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("sea_level_plot.png")
    return plt.gca()
