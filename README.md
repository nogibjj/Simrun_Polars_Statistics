# POLARS Data Analysis: Log GDP per Capita and Infant Mortality Rate
[![CI](https://github.com/nogibjj/Simrun_Polars_Statistics/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/Simrun_Polars_Statistics/actions/workflows/main.yml)
## Data Source

The dataset used in this analysis is sourced from the World Development Indicators dataset for the year 2015. You can access the data from the following URL: [World Development Indicators 2015 Dataset](https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv).

## Why Polars and Not Pandas?
Both Polars and Pandas aim to be memory-efficient, but they achieve this goal through different strategies.

Pandas, by default, loads an entire DataFrame into memory. While it provides options like memory-mapped files and chunking to manage memory for large datasets, it still can consume a significant amount of memory when working with very large datasets.

Polars, on the other hand, focuses on optimizing operations performed on columns. This means that Polars is designed to execute operations in a way that minimizes memory usage. For example, when you perform operations on columns in Polars, it can process and release data in smaller chunks, reducing the overall memory footprint during the execution of these operations.

So, in essence, Polars' efficiency in processing operations on columns can help reduce memory usage compared to Pandas, especially when working with large datasets and complex operations. However, it's essential to note that both libraries offer ways to manage memory efficiently, and the choice between them depends on the specific use case and requirements.

## Code Overview

### 1. Loading the Dataset

The script loads the World Development Indicators dataset into a Polars DataFrame. This Dataset takes a look at all the countries apart of World Bank. The World Bank is made up of 189 member countries. These member countries are represented by a Board of Governors, who are the ultimate policymakers at the World Bank. In this dataset I wanted to understand how a country's GDP Per Capita serves as a strong indicator of resource allocation, wealth, and well-being of a country's health/population. I specfically chose Mortality rate, under-5 (per 1,000 live births) to understand if a country's wealth is a indicator of the country's youth mortailty rate.

### 3. Data Visualization
The data visualization is where we see the real magic of this analysis come together. With an alpha transparency of 0.7 we can clearly see a trend, our GDP Per Capita is on the rise while our Infant Mortality Rate falls. However we can also see some outliers that serve as influential points in the graph and indicate a important note. We can note that sometimes country's who have a high GDP Per Capita might struggle with resource allocation, understanding population needs, or hospital resources. These downfalls show that some countries had a high Infant Mortality Rate despite having a high GDP Per Capita. 

A legend was also created to in a clear white background to indicate how my descriptive statistics fall in my plot. This is to showcase how these statistics play in the data plot visualization. 

### 4. Descriptive Statistics

This Descriptive Statistics analysis highlights the statistics that I felt were important to understand the relationship between GDP Per Capita and Infant Mortality Rate. I used a computation function which looked into the mean, median, and standard deviation error summary statistics of GDP Per Capita and my outcome variable. 

## Results

After executing the code, the following descriptive statistics were obtained for the GDP per capita variable:

- **Mean**: The mean GDP per capita is approximately 15,335.72. This statistic represents the average wealth per person in the countries included in the analysis.

- **Median**: The median GDP per capita is approximately 6,134.94. This statistic provides the middle value in the dataset and is less sensitive to extreme outliers than the mean.

- **Standard Deviation**: The standard deviation of approximately 22,881.31 indicates the spread or variability in GDP per capita values across the countries. A higher standard deviation suggests greater variability.

These statistics offer valuable insights into the central tendency and spread of the GDP per capita data. They help us better understand the distribution of wealth among the countries in the World Bank dataset.

![Visualization Example](https://user-images.githubusercontent.com/141798228/266807301-e455df10-7308-42a5-bb9d-d055e5e45f8f.jpg)


## Conclusion

This script enables us to explore the relationship between GDP per capita and the infant mortality rate using the World Development Indicators data. By calculating and visualizing descriptive statistics, we gain valuable insights into how economic prosperity may influence a country's child mortality rate. These findings contribute to a broader understanding of the socioeconomic factors affecting child health and well-being globally.
