#1
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('MX_Torres.csv')

melted_df = data.melt(id_vars='Year', var_name='Location', value_name='Percentage')

plt.figure(figsize=(10, 6))

sns.lineplot(data=melted_df, x='Year', y='Percentage', hue='Location', marker='o')

plt.title('Pecentage of Live Births in the 2 Years preceding the Survey by place of delivery. From 2017 to 2022.')
plt.xlabel('Year')
plt.ylabel('Percentage')
plt.grid(True)

for _, row in melted_df.iterrows():
    plt.text(row['Year'], row['Percentage'], f"{row['Percentage']}%", ha='right', va='bottom', fontsize=8)

plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.xticks([2017, 2022])
plt.tight_layout()
plt.show()

#2
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

#3
import pandas as pd
import plotly.graph_objs as go


data = pd.read_csv('MX_Torres2.csv')


traces = []
colors = {'Urban': 'blue', 'Rural': 'orange', 'Total': 'green'}
for category in ['Urban', 'Rural', 'Total']:
    trace = go.Scatter(
        x=data.index,
        y=data[category],
        mode='markers',
        name=category,
        marker=dict(color=colors[category])
    )
    traces.append(trace)


layout = go.Layout(
    title='Percentage of women aged 15-49 years whose last live birth in the 2 years preceding the survey was not delivered in a health facility, by specific reasons and by residence.',
    yaxis=dict(title='Percentage', range=[-5, 105], tickvals=[], ticktext=[]),  # Adjust y-axis range and remove ticks
    showlegend=True,
    legend=dict(title='Reason', x=1, xanchor='right', y=1.05, orientation='v')
)


fig = go.Figure(data=traces, layout=layout)


for i, (urban, rural, total, reason) in enumerate(zip(data['Urban'], data['Rural'], data['Total'], data['Reason'])):
    if urban + rural + total > 0:
        fig.add_annotation(
            x=i,
            y=-5,  # Adjust y-position
            text=reason,
            showarrow=False,
            xanchor='center',
            yanchor='top',
            font=dict(color='black', size=8),
            textangle=-90
        )

fig.show()

