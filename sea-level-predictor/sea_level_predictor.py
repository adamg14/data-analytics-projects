import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# scatter plot
sea_level_df = pd.read_csv("./epa-sea-level.csv")
print(sea_level_df.head())
plt.scatter(x=sea_level_df["Year"], y=sea_level_df["CSIRO Adjusted Sea Level"])

# linregress function generating a line of best fit using linear regression method of machine learning based on the datapoints provided by the dataset
# get the slope/gradient and the y-intercept
linear_regression_result = linregress(x=sea_level_df["Year"], y=sea_level_df["CSIRO Adjusted Sea Level"])
slope = linear_regression_result.slope
intercept = linear_regression_result.intercept

x = np.linspace(1880, 2050)
# formating the line of best fit in the formula of a straight line
y = slope * x + intercept
plt.plot(x, y)

# a new line of best fit for the years 2000 onwards
sea_level_2000_df = sea_level_df[sea_level_df["Year"] >= 2000]
linear_regression_result_2000 = linregress(x=sea_level_2000_df["Year"], y=sea_level_2000_df["CSIRO Adjusted Sea Level"])
slope2 = linear_regression_result_2000.slope
intercept2 = linear_regression_result_2000.intercept

x2 = np.linspace(2000, 2050)
y2 = slope2 * x2 + intercept2

plt.plot(x2, y2)
plt.xlabel("Year")
plt.ylabel("Sea Level (Inches)")
plt.title("Rise in Sea Level")
plt.show()
plt.close()