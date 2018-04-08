#  HOW THE USER CAN INTERACT WITH THE APP IN REALTIME

import dash
import dash_core_components as dcc
import dash_html_components as html
# ADD
from dash.dependencies import Input , Output

# Start an application.
app=dash.Dash()
app.layout = html.Div(children=[
	dcc.Input(id = 'input' , value = 'Enter Something' , type = 'text'),
	html.Div(id = 'output')
	])

@app.callback(
	Output(component_id='output',component_property='children'),
	[Input(component_id='input',component_property='value')]
	)

def update_value(input_data):
	# return "Input: {}".format(input_data)
	try:
		return str(float(input_data)**2)
	except:
		return "Some Error"	


if __name__ == '__main__':
	app.run_server(debug=True)  
