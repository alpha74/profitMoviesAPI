/*
	Movie selector program 
	Author: Aman Kumar
*/

#include <iostream>
#include <fstream>
#include <vector>

using namespace std ;


/*
	The input and output file names
*/
#define INPUT_FILE "movie_schedules.txt"
#define OUTPUT_FILE "chosen_schedule.txt"


class MovieSchedule
{
	public:
			int id ;		// Unique ID
			int start ;		// Start day
			int end ;		// End day
		
		
			// Default ctor
			MovieSchedule()
			{
				id = -1 ;
				start = -1 ;
				end = -1 ;
			}
			
			// Parametrized ctor
			MovieSchedule( int pid, int pstart, int pend )
			{
				id = pid ;
				start = pstart ;
				end = pend ;
			}
			
} ;


/*
	====================== UTILITY FUNCTIONS =========================
*/

/*
	Fills input data from INPUT_FILE. Uses call by reference.
		@movie_sch : object of class MovieSchedule
*/
void fill_input_data( vector<MovieSchedule> &movie_sch ) 
{
	int rowid = 0 ;
	
	// Open the file to read input
	ifstream fin ;
	fin.open( INPUT_FILE, ios::in ) ;
	
	while( fin )
	{
		int ip_start, ip_end ;
		
		fin >> ip_start >> ip_end ;
		
		// Create new Object 
		MovieSchedule new_row( rowid++, ip_start, ip_end ) ;
		movie_sch.push_back( new_row ) ;	
		
		if( fin.eof() )
			break ;
		
	}
	
	fin.close() ;
}


vector<int> select_max_movies( vector<MovieSchedule> &movie_sch ) 
{
	vector<int> list ;
	
	list.push_back( 1 ) ;
	list.push_back( 2 ) ;
	list.push_back( 3 ) ;
	
	return list ;
}


/*
	Writes chosen movies ID to OUTPUT_FILE.
		@chosen_movies : list of ids of selected movies
		
*/
void write_output_data( vector<int> chosen_movies )
{
	ofstream fout ;
	fout.open( OUTPUT_FILE, ios::out ) ;
	
	for( int i = 0 ; i < chosen_movies.size() ; i++ )
	{
		fout << chosen_movies[ i ] ;
		fout << "\n" ;
	}
	
	fout.close() ;
}

/*
	============================ MAIN ================================
*/
int main()
{
	vector<MovieSchedule> movie_sch ;
	
	// Fills input data from file
	fill_input_data( movie_sch ) ;
	
	for( int i = 0 ; i < movie_sch.size() ; i++ )
	{
		cout << "\n\n ID: " << movie_sch[ i ].id ;
		cout << "\n start: " << movie_sch[ i ].start ;
		cout << "\n end: " << movie_sch[ i ].end ;
	}
	
	// Stores list of selected movies
	vector<int> chosen_movies ;
	
	chosen_movies = select_max_movies( movie_sch ) ;
	
	// Write selected movies to file
	write_output_data( chosen_movies ) ;
	
	return 0 ;
}
