import pandas

df = pandas.read_csv("./adult.csv")
advanced_education = ["Bachelors", "Masters", "Doctorate"]
advanced_education_high_salary = df.loc[
    df["education"].isin(advanced_education) &
    (df["salary"] == ">50K")
]

print(advanced_education_high_salary)


# what percent of people without advanced education make more than 50k
print()
(df.loc[~df["education"].isin(advanced_education) &
(df["salary"] == ">50K")].shape[0] /
df.loc[~df["education"].isin(advanced_education)].shape[0]) * 100

# What is the minimum number of hours a person works per week
print(df.loc[df["hours-per-week"]]["hours-per-week"].min())

# What percentage of the people who work the minimum number of hours per week have a salary of more than 50K
print(df.loc[(df["hours-per-week"] == 2) & ((df["salary"] == ">50K"))].shape[0])

# What country has the highest percentage of people that earn >50K and what is that percentage
high_earners = df[df['salary'] == ">50K"]
country_population = df.groupby('native-country').size()
print(country_population.head())
country_high_earners = high_earners.groupby('native-country').size()
percent = (country_high_earners / country_population) * 100
country = percent.idxmax()
percent = percent.max()

# Identify the most popular occupation for those who earn >50K in India.
indian_high_earners = df[(df['salary'] == ">50K") & 
(df['native-country'] == "India")]
job_count = indian_high_earners["occupation"].value_counts()
print(indian_high_earners.head())
print(job_count.idxmax())