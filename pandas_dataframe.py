import pandas as pd

data = pd.DataFrame({
    "name":["Amy", "Bob", "Charles"],
    "salary":[30000, 50000, 40000]
}, index = ['a', 'b', 'c'])

print(data)
print('=' * 30)
print('DataSize:', data.size)
print('DataShape：', data.shape)
print('DataIndex:', data.index)

print('=' * 30)
print(data.iloc[1])
print('=' * 30)
print(data.loc['c'])

print(data['name'])

names = data['name']
print(names.str.upper())

salaries = data['salary']
print(salaries.mean())

data["revenue"] = [500000, 400000, 300000]
print(data)
data["rank"] = pd.Series([3, 6, 1], index = ['a', 'b', 'c'])
data["cp"] = data["revenue"]/data["salary"]
print(data)

import practice_counts