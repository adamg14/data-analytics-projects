import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

time_df = pd.read_csv("./fcc-forum-pageviews.csv", index_col="date")
# data cleaning -
# filering out the top 2.5% and bottom 2.5% of page views
line_time_df = time_df[(time_df["value"] < time_df["value"].quantile(0.975)) &
                       (time_df["value"] > time_df["value"].quantile(0.025))]


plt.plot(line_time_df.index, line_time_df["value"])
plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
plt.xlabel("Date")

plt.xticks(ticks=np.arange(0, len(line_time_df.index), step=60), labels=line_time_df.index[::60], rotation=45)
plt.ylabel("Page Views")
plt.show()
plt.close()


# bar plot
# group by month - convert date to datetime64 format

bar_plot = time_df
bar_plot.index = pd.to_datetime(bar_plot.index)

monthly_views = bar_plot.resample('M').mean()

# extract year and month
monthly_views["year"] = monthly_views.index.year
monthly_views["month"] = monthly_views.index.strftime("%B")

# sorting the months in order

pivot_data = monthly_views.pivot(
    index='year',
    columns='month',
    values='value'
)

pivot_data.plot(kind='bar', figsize=(12, 6))

print(pivot_data.head())

plt.title("Monthly Average Values by Year")
plt.xlabel("Year")
plt.ylabel("Average Value")
plt.legend(title="Months")

plt.show()
plt.close()

box_plot = time_df
box_plot.index = pd.to_datetime(bar_plot.index)
box_plot["year"] = box_plot.index.year
box_plot["month"] = box_plot.index.strftime("%B")


month_order = ['January', 'Feburary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

fig, axis = plt.subplots(1, 2,figsize=(15, 6))

sns.boxplot(data=box_plot,
            x='year',
            y='value',
            ax=axis[0])

axis[0].set_title("Year-wise Box Plot (Trend)")
axis[0].set_xlabel("Year")
axis[0].set_ylabel("Page Views")

sns.boxplot(data=box_plot,
            x="month",
            y="value",
            order=month_order,
            ax=axis[1])

axis[1].set_title("Month-wise Box Plot (Seasonality)")
axis[1].set_xlabel("Month")
axis[1].set_ylabel("Page Views")
axis[1].set_xticklabels(axis[1].get_xticklabels(), rotation=45)

plt.show()
plt.close()