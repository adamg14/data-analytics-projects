import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
def is_overweight(weight, height):
    BMI = weight / ((height / 100)**2)
    if BMI > 25:
        return 1
    else:
        return 0

def normalisation(cholesterol, gluc):
    if (cholesterol == 1 or gluc == 1):
        return 0
    else:
        return 1
        
# # add an overweight column
df = pd.read_csv("./medical_examination.csv")
df['overweight'] = df.apply(lambda row: is_overweight(row['weight'], row['height']), axis=1)
df['normalisation'] = df.apply(lambda row: normalisation(row['cholesterol'], row['gluc']), axis=1)

# plotting categorical data
# pd.melt reshapes the data so that the columns are transformed into rows under a new column (variable) with the corresponding value under another column
# this is also known as converting the data into long format
df_categorical = pd.melt(df,
                        #  cardio is the identifying variable which splits the data
                         id_vars=['cardio'],
                         value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight', ],
                         var_name='variable',
                         value_name='value')

# count the occurances of each of the combination of cardio variable and value eg cardio = 1 and gluc = 1 
# resetting the index to avoid heirarchical indexing, so that the data is flattened and easier to visualise/plot
cardio_group = df_categorical.groupby(['cardio', 'variable', 'value']).size().reset_index(name='count')

# Create the catplot
sns.catplot(
    data=cardio_group,
    x='variable',
    y='count',
    hue='value',         # Different bars for each value
    col='cardio',        # Separate plots for each cardio group
    kind='bar',
    height=5,
    aspect=1
)

# Show the plot
plt.show()
plt.close()

# creating a pivot table of value for each variable and cardio
heatmap_data = df_categorical.pivot_table(
    # categorical variable for the rows
    index='variable',
    # categorical values for columns
    columns='value',
    # agregate by counts
    values='cardio',
    aggfunc='count',
    fill_value=0
)

# drawing the heatmap
sns.heatmap(
    heatmap_data,
    annot=True,
    cmap='YlGnBu',
    fmt='d'
)

plt.title("Heatmap of categorical data")
plt.xlabel("Value")
plt.ylabel("Variable")
plt.show()
plt.close()

# data cleaning by filtering otut the following patients
# diastolic pressure is higher than systolic
# height is less than the 2.5th percentile
# height is more than the 97.5th percentile
# weight is less than the 2.5th percentile
# weight is more than the 97.5th percentile
df = df[(df["ap_lo"] <= df['ap_hi']) &
        (df["height"] >= df["height"].quantile(0.025)) &
        (df["height"] < df["height"].quantile(0.975)) &
        (df["weight"] >= df["weight"].quantile(0.025)) &
        (df["weight"] < df["weight"].quantile(0.975))]


# calculate the correlation matrix
corr_matrix = df.corr()
print(corr_matrix)

# generate a mask for the upper triangle and store in the mask variable
# the mask is applied to the correlation matrix to hide the upper triangle when plotting the correlation matrix to avoid repition in the graph
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

# set up the matplotlib figure
# plot the correlation matrix
# 
sns.heatmap(corr_matrix, mask=mask, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix with Upper Triangle Masked")
plt.show()
plt.close()
