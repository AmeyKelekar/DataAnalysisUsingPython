1) There are 2 scripts designed for this assignment:
	a) Assignment2_SearchAndSave.py : 
		This script saves the tweet details fetched in a csv file. I am using the Twitter Search API.
		Resource URL: https://api.twitter.com/1.1/search/tweets.json
		Type of search performed:
		When we are following an event that’s currently happening, we would be interested in search for recent tweets using the event hashtag:
		For example:
		You want: recent tweets that contain the hashtag #superbowl
		Your search URL is: https://api.twitter.com/1.1/search/tweets.json?q=%23superbowl&result_type=recent

		The script takes 2 arguements as input: 
		i) Search term and 
		ii) Analysis you want to perform: Numeric value from 1 to 5

 	b) Assignment2_Analysis.py: 
 		This script performs 5 analysis:
 		i) Across all search term , what is the average number of friends a user has each day?
 		ii) Across all search term, which are the top 5 languages each day?
 		iii) Across all search term, show the top 10 retweeted tweets for every day.
 		iv) For each search term, show top influential tweet each day
 		v) For each search term, who is the most engaged user on twitter that day

2) Run the python code as:
	Some cases:
	a)python Assignment2_SearchAndSave.py -s "#Cricket"
	where #Cricket: search term
	If you don't provide any value for analysis to be performed, by default, it will perform 'analysis 5' i.e.find out for each search term, who is the most engaged user on twitter that day
	
	Note: If you want to use #hashtag, include it in quotes like above. Otherwise it gets treated as two seperate strings and will give you an error "Assignment2_SearchAndSave.py: error: argument -s/--search: expected one argument"

	b) python Assignment2_SearchAndSave.py -s Cricket -a 3
	where Cricket: search term
	3: Analysis you want to perform. In this case, across all search term, show the top 10 retweeted tweets for every day

	c) python Assignment2_SearchAndSave.py -s Cricket -a 6 
	where Cricket: search term
	6: Analysis you want to perform. 

	Note: We don't have any analysis to be performed for 6. So it will display a message on the screen:" Nothing to analyze, please give numbers between 1 to 5!!!"


3) Some of the error cases:
	a) python Assignment2_SearchAndSave.py -s Cricket -a c
		Output:
		usage: Assignment2_SearchAndSave.py [-h] -s SEARCH [-a ANALYSIS]
		Assignment2_SearchAndSave.py: error: argument -a/--analysis: invalid int value: 'c'

	b) python Assignment2_SearchAndSave.py -s #Cricket 
		Output:
		usage: Assignment2_SearchAndSave.py [-h] -s SEARCH [-a ANALYSIS]
		Assignment2_SearchAndSave.py: error: argument -s/--search: expected one argument

	c) python Assignment2_SearchAndSave.py   
		Output:             
		usage: Assignment2_SearchAndSave.py [-h] -s SEARCH [-a ANALYSIS]
		Assignment2_SearchAndSave.py: error: the following arguments are required: -s/--search




