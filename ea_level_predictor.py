
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    # Line of best fit using all data
    slope, intercept, r_value, p_value, std_err = linregress(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    years = pd.Series(range(1880, 2051))
    ax.plot(
        years,
        slope * years + intercept,
        "r",
        label="Best fit line (1880–2050)"
    )

    # Line of best fit using data from 2000 onwards
    recent_df = df[df["Year"] >= 2000]

    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(
        recent_df["Year"],
        recent_df["CSIRO Adjusted Sea Level"]
    )

    recent_years = pd.Series(range(2000, 2051))
    ax.plot(
        recent_years,
        slope_recent * recent_years + intercept_recent,
        "g",
        label="Best fit line (2000–2050)"
    )

    # Labels and title
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")

    ax.legend()

    # Save and return plot
    fig.savefig("sea_level_plot.png")
    return fig
