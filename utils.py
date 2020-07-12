"""
	======================================
	
		FILE: UTILS file for MAIN_HANDLER
	
		AUTHOR: Aman Kumar
	
		WORK: Utility functions used by MAIN_HANDLER are defined here

	======================================
"""

import json
from datetime import datetime


"""
	Index function to receive movies data.
	Return list of profitable movies.
"""
def select_profit_movies( ip_data ):	
	return ip_data