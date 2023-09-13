import polars as pl
import matplotlib.pyplot as plt
import numpy as np


# Loading Dataset
wdi = pl.read_csv(
    "https://media.githubusercontent.com/"
    "media/nickeubank/MIDS_Data/"
    "master/World_Development_Indicators/wdi_small_tidy_2015.csv"
)


# Function created to understand the descriptive statistices for the dataset of WorldBank Indicators
def computation(dataframe):
    gdp_column = dataframe["GDP per capita (constant 2010 US$)"]
    average = gdp_column.mean()
    medium = gdp_column.median()
    std_dev = gdp_column.std()

    # Round the values to the desired number of decimal places
    average = round(average, 10)
    medium = round(medium, 10)
    std_dev = round(std_dev, 2)

    return (average, medium, std_dev)


# Calling the function
average, medium, std_dev = computation(wdi)

# Visualizing the data representation of the relationship between the two variables.
plt.figure(figsize=(10, 6))
plt.scatter(
    wdi["GDP per capita (constant 2010 US$)"],
    wdi["Mortality rate, under-5 (per 1,000 live births)"],
    alpha=0.7,
)

# text on the plot
text = f"Mean Gdp Per Capita:{average}\nMedian Gdp Per Capita: {medium}\nStd Dev Gdp Per Capita: {std_dev}"
plt.text(
    wdi["GDP per capita (constant 2010 US$)"].max() - 0.5,
    wdi["Mortality rate, under-5 (per 1,000 live births)"].max() - 20,
    text,
    bbox=dict(facecolor="white", alpha=0.7),
    horizontalalignment="right",
    verticalalignment="top",
)
# labeling and title
plt.xlabel("GDP per capita (constant 2010 US$)")
plt.ylabel("Mortality rate, under-5 (per 1,000 live births)")
plt.title = "Analysis of Log Gdp Per Capita and Infant Mortality Rate"


# Display of the chart
plt.show()
