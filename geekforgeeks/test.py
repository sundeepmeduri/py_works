import pandas as pd
# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Score': [85, 90, 78, 92, 88]}
df = pd.DataFrame(data)

print(df)
# Ranking the DataFrame based on the 'Score' column
df['Rank'] = df['Score'].rank()
df['Rank'] = df['Rank'].astype('int')
print(df.sort_values(by='Rank'))
