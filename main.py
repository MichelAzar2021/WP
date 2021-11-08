# !pip install vega_datasets
# !pip install plotly
# !pip install dash
# !pip install jupyter-dash
# from jupyter_dash import JupyterDash


from vega_datasets import data
import plotly.graph_objects as go
import plotly.express as px
import dash
from dash import dcc
from dash import html


def data_preparation():
    # Import data and sort values
    source = data.barley().sort_values(by=['variety', 'site'])
    # Calculate Median and add it as a feature
    df_median = source.groupby(["site", "year"], as_index=False)['yield'].median().rename(
        columns={"yield": "median_yield"})
    transformed_data = source.merge(df_median, how='left', on=['site', 'year'])
    return transformed_data


def display_stacked_histogram(barley_data):
    fig = go.Figure(px.histogram(barley_data, x="variety", y='yield', color="site", histfunc="sum")
                    .update_xaxes(categoryorder='category ascending',
                                  constraintoward='middle', tickangle=-90, ticks="outside")
                    .update_yaxes(showgrid=True, ticks="outside", range=[0, 500], nticks=11))

    fig.update_layout(
        height=700,
        width=800,
        title="<b>Stacked Histogram</b>",
        xaxis_title="<b>Variety</b>",
        yaxis_title="<b>Sum of yield</b>",
        legend_title="<b>Site</b>",
        font=dict(
            family="Arial",
            size=12,
            color="black"
        )
    )

    return fig


def display_line_graph(barley_data):
    fig = go.Figure(px.line(barley_data, x="year", y="median_yield",
                            color='site', markers=True)
                    .update_xaxes(categoryorder='category ascending', constraintoward='middle', tickangle=-90,
                                  showgrid=True, nticks=4, ticks="outside", type='category', rangemode="tozero")
                    .update_yaxes(showgrid=True, ticks="outside", tickvals=list(range(0, 56, 5)), rangemode="tozero"))

    fig.update_layout(
        height=700,
        width=300,
        title="<b>Line Graph</b>",
        xaxis_title="<b>year</b>",
        yaxis_title="<b>Median of yield</b>",
        legend_title="<b>Site</b>",
        font=dict(
            family="Arial",
            size=12,
            color="black"
        )
    )

    return fig


if __name__ == '__main__':
    # transform data and display the corresponding visualizations separately
    t_data = data_preparation()
    # display_stacked_histogram(t_data).show()
    # display_line_graph(t_data).show()


    # Run the visualization functions for dashboard display
    fig1 = display_stacked_histogram(t_data)
    fig2 = display_line_graph(t_data)

    # Use CSS to be able to visualize the two graphs next to each other
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
    app.layout = html.Div(children=[
        html.Div([
            html.Div([dcc.Graph(id='graph1', figure=fig1)], className='six columns'),
            html.Div([dcc.Graph(id='graph2', figure=fig2)], className='six columns')
        ], className='row')
    ])

    app.run_server(host='localhost', port=5000, debug=True, use_reloader=False)  # Turn off re-loader if inside Jupyter
