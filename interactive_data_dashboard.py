import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Sample dataset (replace with your own data)
data = {
    'Category': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'],
    'Value': [10, 15, 7, 12, 18, 9, 8, 14, 6],
    'Date': pd.date_range('2022-01-01', periods=9)
}

df = pd.DataFrame(data)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Interactive Data Dashboard"),
    
    dcc.Graph(
        id='line-plot',
        figure=px.line(df, x='Date', y='Value', color='Category', title='Line Plot')
    ),
    
    dcc.Graph(
        id='bar-plot',
        figure=px.bar(df, x='Category', y='Value', color='Category', title='Bar Plot')
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
