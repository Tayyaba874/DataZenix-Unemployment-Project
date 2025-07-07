import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
data = pd.read_csv('Pakistan_Poverty_Dataset_2000_2023.csv')

# Display the first few rows
print(data.head())

# Check column names
print(data.columns)

# Basic Plot
plt.figure(figsize=(10, 5))
sns.lineplot(x='Year', y='Unemployment Rate (%)', data=data)
plt.title('Unemployment Rate Over Years in Pakistan')
plt.xlabel('Year')
plt.ylabel('Unemployment Rate')
plt.grid(True)
plt.tight_layout()
plt.show()
