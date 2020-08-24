# Profit Movies API
#### alpha74

Project created for implementing the task which is [here](https://github.com/alpha74/profitMoviesAPI/blob/master/task_Movies.pdf)

### Tech Used:
- Python
- Flask framework for API handling
- C++ in `movie_selector/choose_movies.cpp` used in computation.

-----

### Run

#### Step1

- Build the file `movie_selector/choose_movies.cpp`.
- Place the executable file in dir `movie_selector`.
- Update path to this file in `utils.py` as var `MOVIE_SELECTOR`.

#### Step2

- Create a virtual environment from `requirements.txt`.
- Run `python mainhandler.py`.
- By default, the server runs on `localhost:5000`, if no errors are encountered.

-----

### APIs
- `/`
	- Method : `GET`
	- Used to check if server is running.

- `/api/get_profit_movies`
	- Method : `POST`
	- Returns data of chosen profitable movies.


### Sample Payload in JSON 
- Payload for `/api/get_profit_movies`

```
{
	"schedule" : [
		{
			"movie_name" : "Bala",
			"start_date" : "8 Jan",
			"end_date" : "28 Jan"
		},
		{
			"movie_name" : "Rock",
			"start_date" : "20 Jan",
			"end_date" : "30 Jan"
		},
		{
		    "movie_name": "Brave",
		    "start_date": "2 Feb",
		    "end_date": "14 Feb"
		},
		{
		    "movie_name": "Race",
		    "start_date": "15 Feb",
		    "end_date": "28 Feb"
		}
	]
}
```

### Sample output in JSON
- Output for `/api/get_profit_movies`. 
- Returns `Success` when computation is completed with no internal errors.
- Returns `Failure` when some internal error occurs.

#### Success output
```
{
    "status": "Success",
    "result": [
        {
            "movie_name": "Rock",
            "start_date": "20 Jan",
            "end_date": "30 Jan"
        },
        {
            "movie_name": "Brave",
            "start_date": "2 Feb",
            "end_date": "14 Feb"
        },
        {
            "movie_name": "Race",
            "start_date": "15 Feb",
            "end_date": "28 Feb"
        }
    ]
}
```


#### Failure output
```
{
    "status": "Failed"
}
```

-----

### Dependencies:
- APIs are tested using `Postman v7.25.0`.
- Python scripts call `movie_selector/choose_movies.exe` (executable file generated after build in Step1) internally to generate results.
- Communication between python scripts and cpp executable is done using file I/O.
- Input and Output file names in python scripts and cpp programs should be same.
- Executable paths if changed, should be updated in python scripts.


### PRs
- PRs accepted on `master`
