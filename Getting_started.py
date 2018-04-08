import dash
import dash_core_components as dcc
import dash_html_components as html

# Start an application.
app=dash.Dash()
app.layout = html.Div(children=[
	html.H1('Dash Tutorial'),
	dcc.Graph(id='example',
		figure={
			'data':[
			{'x':[1,3,2,9,0,7],'y':[6,2,8,7,6,9],'type':'line','name':'boats'},
			{'x':[4,1,6,9,7,7],'y':[4,3,7,8,9,6],'type':'bar','name':'cars'},
			],
			'layout':{
			'title':'Basic Dash Example',
			}
		})
	])

if __name__ == '__main__':
	app.run_server(debug=True)  
