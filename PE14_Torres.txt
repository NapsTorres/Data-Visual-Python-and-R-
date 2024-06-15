import pandas as pd
import plotly.graph_objects as go

data = pd.read_csv('Employee.csv')


data.sort_values(by='Employee_Salary', inplace=True)

fig = go.Figure()

fig.add_trace(go.Scatter(x=data['Employee_Name'], y=data['Employee_Salary'],
                         mode='markers+lines',
                         marker=dict(color='steelblue', size=10),
                         line=dict(color='black', width=2),
                         name='Salary'))

fig.update_layout(title='Increasing Salary of Employees',
                  xaxis_title='Employee Name',
                  yaxis_title='Salary',
                  showlegend=False)

fig.show()
