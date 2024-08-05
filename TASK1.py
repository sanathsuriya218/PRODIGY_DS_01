import pandas as pd
import matplotlib.pyplot as plt
file_path = '/Users/Sanath/Downloads/world_population.csv' 
data = pd.read_csv(file_path)
print(data.head())
print(data.columns)
"data = data[['Country/Territory', '2021']].dropna()"
plt.figure(figsize=(12, 8))
plt.bar(data['Country/Territory'], data['2022 Population'])
plt.title('Population by Country in 2021')
plt.xlabel('Country')
plt.ylabel('Population')
plt.xticks(rotation=90)
plt.show()

