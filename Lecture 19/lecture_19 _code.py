pip install plotly

import pandas as pd

# Load a data_set
df = pd.read_csv('Sample.csv')
print(df.head())

import plotly.express as px

fig = px.line(df, x='Year', y='aggregation', title='Line Plot', markers=True,color_discrete_sequence=["red"], line_dash_sequence=["dash"])  # Set line style (optional)

# Update marker properties
fig.update_traces(marker=dict(size=10, color="blue",symbol="square"))  

# Update background color
fig.update_layout(plot_bgcolor="lightgrey")

fig.show()

fg = px.bar(df, x='aggregation', y='Year', title='Bar Plot', color='aggregation')
fg.show()
fig = px.histogram(df, x='Year', y='aggregation', title='Histogram', color='aggregation', nbins=300)  # Set number of bins (optional
fig.show()
fig = px.scatter(df, x='Year', y='aggregation', title='Scatter Plot', color='aggregation', hover_data=['Value']) # Changed size to 'Value'
fig.show()

fig = px.pie(df, values='Value', names='Year', title='Pie Chart')
fig.show()

fig = px.line(df, x='Year', y='aggregation', title='Line Plot', markers=True,color_discrete_sequence=["red"], line_dash_sequence=["dash"])  # Set line style (optional
fig.show()

