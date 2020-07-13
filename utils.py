"""
	======================================
	
		FILE: UTILS file for MAIN_HANDLER
	
		AUTHOR: Aman Kumar
	
		WORK: Utility functions used by MAIN_HANDLER are defined here

	======================================
"""

import subprocess
import json
from datetime import datetime

# Start date of year to be considered.
BASE_YEAR = 2020
BASE_DATE = datetime( BASE_YEAR, 1, 1 )

MOVIE_SELECTOR = "movie_selector\\choose_movies.exe"
WRITE_FILE = "movie_selector/movie_schedules.txt"
READ_FILE = "movie_selector/chosen_schedule.txt"


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
		- Uses pre-built MOVIE_SELECTOR
		- Writes data to file WRITE_FILE
		- Reads selected movies from READ_FILE
		- Returns as Python object
"""
def get_profitable_movies( movies_days ):
	
	# Write input data to WRITE_FILE
	fwrite = open( WRITE_FILE, "w" )
	
	for movie in movies_days:
		fwrite.write( str(movie['start']) + " " + str(movie['end']) )
		fwrite.write( "\n" )
	
	fwrite.close()
	
	# Run MOVIE_SELECTOR as cmd
	subprocess.call( "movie_selector\choose_movies.exe" )
	
	
	# Read chosen indices from file	
	chosenlist = []
	with open( READ_FILE, 'r' ) as file:
		chosenlist = file.read()
		
	# Separate the indices using split. Convert str to int
	chosenlist = chosenlist.split(" ")
	chosenindex = []		# New variable for storing int values 
	
	for index in chosenlist:
		chosenindex.append(int(index))
		
	# Return the indices as int	
	return chosenindex

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
	
	