import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('MX_Torres1.csv')

data_sorted = data.sort_values(by='Percentage delivered in a health facility', ascending=True)


plt.figure(figsize=(5, 5))
sns.set_palette("Accent")
bar_plot = sns.barplot(x='Percentage delivered in a health facility', y='Region', data=data_sorted)
plt.title('Percentage of Live Births in the 2 Years preceding the survey that were delivered in a health facility byregion.')
plt.xlabel('Percentage Delivered')
plt.ylabel('Region')


for index, value in enumerate(data_sorted['Percentage delivered in a health facility']):
    bar_plot.text(value, index, f'{value}%', va='center')


plt.show()
