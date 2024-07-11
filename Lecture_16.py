pip install pandas
import pandas as pd
data = {
  'Name': ['Alice', 'Bob', 'Charlie'],
  'Age': [25,30,35],
  'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print(df)
data = [
  {'Name': 'Alice', 'Age': 25, "City': 'New York'},
  {'Name': 'Bob', 'Age': 30, "City': 'Los Angeles'},
  {'Name': 'Charlie', 'Age': 35, "City': 'Chicago'}
   ]
df = pd.DataFrame(data)

df = pd.read_csv('dataset.csv')
print(df)
print(df.head()) #By default it will first 5 rows
print(df.head(10)) #now it will print top 10 rows

print(df.tail())

print(df.info())

print(df.describe())

print(df['Name']) 

#Selecting multiple columns
print(df[['Name','City']])

#Filtering Rows
#Filtering rows based on a condition
print(df[df['Age'] >30])

df['Salary'] = [50000,60000,70000,80000,90000]
print(df)

df['Age'] = df['Age'] + 1
print(df)

#Dropping Columns and Column
#Dropping a Column
df = df.drop(columns=['Salary'])
print(df)

#Dropping a Row
df = df.drop(index=1)
print(df)
grouped = df.groupby('City')
print(grouped['Age'].mean())

Aggregated = df.groupby('City').agg({'Age': ['mean', 'min', 'max']})

df1 = pd.DataFrame({'ID':[1,2,3], 'Name':['Alice','Bob','Charlie']})
df2 = pd.DataFrame({'ID':[1,2,4], 'Salary':[50000,60000,70000]})

merger_df = pd.merge(df1, df2, on='ID', how='inner') #inner means intersection and outer means union
print(merger_df)

df1 = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25,30]}, index=[0,1])
df2 = pd.DataFrame({'City': ['New York', 'Los Angeles']}, index=[0,2])

joined_df = df1.join(df2, how = 'left')
print(joined_df)
