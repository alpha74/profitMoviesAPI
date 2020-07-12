"""
	======================================
	
		FILE: UTILS file for MAIN_HANDLER
	
		AUTHOR: Aman Kumar
	
		WORK: Utility functions used by MAIN_HANDLER are defined here

	======================================
"""

import json
from datetime import datetime

# Start date of year to be considered.
BASE_YEAR = 2020
BASE_DATE = datetime( BASE_YEAR, 1, 1 )


"""
	Converts date string to datetime object
		Input: date in format "%d %b", Eg: "8 Jan"
		Output: datetime object
"""
def get_datetime_object( datestr ):
	dateobj = datetime.strptime( datestr + " " + str(BASE_YEAR), "%d %b %Y" )
	return dateobj


"""
	Returns difference in days between passed datetime and BASE_DATE + 1
"""
def get_offset_days( datestr ):
	date_compare = get_datetime_object( datestr )
	diff = date_compare - BASE_DATE
	return diff.days + 1


"""
	Returns indices of profitable movies.
		- Uses pre-built "movie_selector/choose_movies.exe"
		- Writes data to file "movie_selector/movie_schedules.txt"
		- Reads selected movies from "movie_selector/chosen_schedule.txt"
		- Returns as Python object
"""
def get_profitable_movies( movies_days ):
	# Example selections
	list = [ 1, 3, 4 ]
	
	return list

"""
	Modifies dates in input data to number of days as offset.
	Returns new data as a list
"""
def modify_dates( ip_data ):
	movies = ip_data[ "schedule" ]
	
	movies_days = []
	
	#
	# Extracts each movie schedule.
	# Converts dates to days offset.
	# Stores in list: movies_days
	#
	
	for movie in movies:
		movie_record = {
							"movie_name" : movie["movie_name"],
							"start" : get_offset_days( movie["start_date"] ),
							"end" : get_offset_days( movie["end_date"] )
						}
		
		movies_days.append( movie_record )
		
	# Returns data in new format	
	return movies_days	


"""
	Index function to receive movies data.
	Return list of profitable movies.
"""
def select_profit_movies( ip_data ):	
	# Change dates to days offsets
	movies_days = modify_dates( ip_data )
	
	# Get profitable movies indices. Example output. Will use func call
	selected_movies = get_profitable_movies( movies_days )

	# Return movies which are profitable. 
	profit_movies = []
	
	for index in selected_movies:
		profit_movies.append( ip_data["schedule"][index] )
		
	return profit_movies	
	
	