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
from datetime import datetime

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

# =================================================================


if __name__ == '__main__':
	app.run( debug = True, host = "0.0.0.0" )