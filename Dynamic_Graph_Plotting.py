#  HOW THE USER CAN INTERACT WITH THE APP IN REALTIME
# WE ARE USING QUANDL FOR EXTRACTING DATA ABOUT WHATEVA YOU TYPE IN THERE INSIDE THE SEARCH BOX.
import datetime
import pandas_datareader.data as web
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input , Output

# start = datetime.datetime(2015, 4, 4)
# end = datetime.datetime.now()
# stock = 'TSLA'
# df = web.DataReader(stock , 'google' , start , end)
# # Data Frames (Excel for pyrthon)
# df = web.DataReader("TSLA", 'morningstar', start, end)
# df.reset_index(inplace=True)
# df.set_index("Date", inplace=True)
# df = df.drop("Symbol", axis=1)

# print(df.head())


app = dash.Dash()

app.layout = html.Div(children=[
    html.Div(children='''
        Your Symbol To Plot.
    '''),

    dcc.Input(id = 'input' , value = '' , type = 'text'),
    html.Div(id = 'output-graph')
    # dcc.Graph(
    #     id='example-graph',
    #     figure={
    #         'data': [
    #             {'x': df.index, 'y': df.Close, 'type': 'line', 'name': stock},
    #         ],
    #         'layout': {
    #             'title': stock
    #         }
    #     }
    # )
])

@app.callback(
	Output(component_id = 'output-graph' , component_property = 'children'),
	[Input (component_id = 'input' , component_property = 'value')]
	)


def update_graph(input_data):
	start = datetime.datetime(2015, 4, 4)
	end = datetime.datetime.now()
	df = web.DataReader(input_data , 'google' , start , end)	
	return dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df.index, 'y': df.Close, 'type': 'line', 'name': input_data},
            ],
            'layout': {
                'title': input_data
            }
        }
    )


if __name__ == '__main__':
    app.run_server(debug=True)