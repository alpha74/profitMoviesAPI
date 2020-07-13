"""
	===========================================================================
	
	FILE: MAIN_HDNLER
	
	AUTHOR: Aman Kumar
	
	WORK: Main handler program for API requests.
			
	===========================================================================	
"""

import json
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
	
	status_code = "Success"
	
	try:
		# Passes json to function. Function data as Python list
		list_movies = utils.select_profit_movies( ip_data )
	
	except Exception as e:
		print( "Exception occured: " + str(e) )
		
		# If any error ocurrs, change status_code to Failed
		status_code = "Failed"
	
	
	# Create new dict which will be returned back to caller
	response = { 
				"status" : status_code
			 }
	
	# Attach result status to response
	if( status_code == "Success" ):
		response[ "result" ] = list_movies
	
	# Return result to caller. End of API.
	return Response( json.dumps( response ), mimetype = 'text/json' )
	
	

# =================================================================


if __name__ == '__main__':
	app.run( debug = True, host = "0.0.0.0" )
	