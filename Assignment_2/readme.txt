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
	python Assignment2_SearchAndSave.py "#Cricket" 2
	where #Cricket: search term
	and 2: Analysis you want to perform. In this case, top 5 languages 
	Note: If you want to use #hashtag, include it in quotes like above
	In case you don't want to pass hashtag, you can write command as below:
	python Assignment2_SearchAndSave.py Cricket 2


