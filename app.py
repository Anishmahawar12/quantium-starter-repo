import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

# Load the processed data
data = pd.read_csv('processed_sales_data.csv')

# Verify columns and add 'sales' if not present
if 'sales' not in data.columns:
    data['sales'] = data['price'] * data['quantity']

# Convert the 'date' column to datetime format
data['date'] = pd.to_datetime(data['date'])

# Remove rows with missing values
data = data.dropna(subset=['product', 'region', 'date', 'sales'])

# Extract unique products
unique_products = data['product'].unique()

# Create the Dash app
app = dash.Dash(__name__)

# Layout of the app
app.layout = html.Div([
    html.H1("Sales Analysis: Impact of Pink Morsel Price Increase", style={'textAlign': 'center'}),
    
    # Dropdown for product selection
    html.Div([
        html.H2("Select Product"),
        dcc.Dropdown(
            id='product-dropdown',
            options=[{'label': product, 'value': product} for product in unique_products],
            value=unique_products[0],  # Default value
            style={'width': '50%'}
        )
    ], style={'textAlign': 'center', 'marginBottom': '20px'}),

    # Graph for displaying sales data
    dcc.Graph(id='sales-graph'),

    # Div for displaying sales summary insights
    html.Div(id='sales-summary', style={'textAlign': 'center', 'marginTop': '20px', 'fontSize': '18px'})
])

# Callback to update the graph and display insights
@app.callback(
    [Output('sales-graph', 'figure'),
     Output('sales-summary', 'children')],
    Input('product-dropdown', 'value')
)
def update_graph(selected_product):
    # Filter data based on selected product
    filtered_data = data[data['product'] == selected_product]

    # Split data into before and after January 15, 2021
    before_data = filtered_data[filtered_data['date'] < '2021-01-15']
    after_data = filtered_data[filtered_data['date'] >= '2021-01-15']

    # Calculate total sales for each period
    before_sales = before_data['sales'].sum()
    after_sales = after_data['sales'].sum()

    # Determine which period had higher sales
    if before_sales > after_sales:
        result = "Sales were higher before the price increase."
    else:
        result = "Sales were higher after the price increase."

    # Create the line chart
    fig = px.line(
        filtered_data,
        x='date',
        y='sales',
        title=f'Sales Over Time for {selected_product}',
        labels={'sales': 'Sales ($)', 'date': 'Date'}
    )

    # Generate sales summary
    summary = f"Total sales before January 15, 2021: ${before_sales:.2f}. " \
              f"Total sales after January 15, 2021: ${after_sales:.2f}. {result}"

    return fig, summary

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
