import pandas as pd

# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles']}
df = pd.DataFrame(data)
print(df)

# Reading data from a CSV file
df = pd.read_csv('data.csv')

# Displaying the first few rows
print(df.head())

# Information about the DataFrame
print(df.info())

# Summary statistics
print(df.describe())

# Selecting a column
ages = df['Age']

# Selecting multiple columns
subset = df[['Name', 'City']]

# Selecting rows based on conditions
filtered_df = df[df['Age'] > 25]

# Accessing specific rows and columns using iloc or loc
specific_data = df.iloc[1:3, 0:2]  # Rows 1 and 2, Columns 0 and 1

# Adding a new column
df['Gender'] = ['Female', 'Male', 'Male']

# Removing a column
df.drop('City', axis=1, inplace=True)

# Handling missing values
df.dropna()  # Drop rows with missing values
df.fillna(0)  # Fill missing values with a specific value

# Grouping data and performing aggregations
grouped_data = df.groupby('Gender').agg({'Age': 'mean', 'Name': 'count'})

# Plotting data
df['Age'].plot(kind='hist')

