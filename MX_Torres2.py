import pandas as pd
import plotly.graph_objs as go

# Read data from CSV
data = pd.read_csv('MX_Torres2.csv')

# Create a trace for each category
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

# Create layout
layout = go.Layout(
    title='Percentage of women aged 15-49 years whose last live birth in the 2 years preceding the survey was not delivered in a health facility, by specific reasons and by residence.',
    yaxis=dict(title='Percentage', range=[-5, 105], tickvals=[], ticktext=[]),  # Adjust y-axis range and remove ticks
    showlegend=True,
    legend=dict(title='Reason', x=1, xanchor='right', y=1.05, orientation='v')
)

# Create figure
fig = go.Figure(data=traces, layout=layout)

# Add annotations for reason text below the graph
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

# Show plot
fig.show()
