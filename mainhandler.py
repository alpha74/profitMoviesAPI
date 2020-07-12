"""
	===========================================================================
	
	FILE: MAIN_HDNLER
	
	AUTHOR: Aman Kumar
	
	WORK: Main handler program for API requests.
			
	===========================================================================	
"""

from flask import Flask
from flask import request
from flask import Response

import utils

app = Flask( __name__ )


"""
	All routes
"""

"""
	Index route.
	- Check if the server is running.
"""
@app.route( "/", methods = [ 'GET' ] )
def index():
	return "MH Success"
	

"""
	API to get chosen max profit movies
"""
@app.route( "/api/get_profit_movies", methods = [ 'POST' ] ) 
def get_profit_movies():

	# Fetch payload movies data
	ip_data = request.get_json()
	
	# Passes json to function. Function data as Python list
	list_movies = utils.select_profit_movies( ip_data )
	
	# Return result to caller. End of API.
	return Response( json.dumps( list_movies ), mimetype = 'text/json' )
	
	

# =================================================================


if __name__ == '__main__':
	app.run( debug = True, host = "0.0.0.0" )