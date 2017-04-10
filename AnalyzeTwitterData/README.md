## Question:
Use the Twitter Api to fetch the Tweets for a topic. Create a script that asks for a search term and can perform 5 analysis on it.

## Files: 
I have designed 2 scripts, namely:

**1) TwitterSearchAPI_SearchAndSave.py :**
- This script saves the tweet details fetched in a csv file. I am using the Twitter Search API.
- Resource URL: https://api.twitter.com/1.1/search/tweets.json
- Type of search performed:
	When we are following an event that’s currently happening, we would be interested in search for recent tweets using the event hashtag:
- For example:
	You want: recent tweets that contain the hashtag #superbowl
	Your search URL is: https://api.twitter.com/1.1/search/tweets.json?q=%23superbowl&result_type=recent
- The script takes 2 arguements as input: 
	i) Search term and 
	ii) Analysis you want to perform: Numeric value from 1 to 5

**2) TwitterSearchAPI_Analysis.py :**
This script performs 5 analysis:
- Across all search term , what is the average number of friends a user has each day?
- Across all search term, which are the top 5 languages each day?
- Across all search term, show the top 10 retweeted tweets for every day.
- For each search term, show top influential tweet each day
- For each search term, who is the most engaged user on twitter that day

## Dependencies:
* [**python**] [python]: 3.5 or higher (prefered: Python 3.5.2 **Latest version**)

[python]: https://www.python.org/downloads/release 

## Standard Libraries used:
* datetime
* os
* csv
* glob
* json
* collections
* operator
* argparse
* sys

Please refer the following documenation [**The Python Standard Library**][The Python Standard Library] to learn more about python inbuilt/standard librarries

[The Python Standard Library]: https://docs.python.org/3/library/

## External Libraries used:
* [**requests**][requests]
* [**simplejson**][simplejson]

[requests]: http://docs.python-requests.org/en/master/
[simplejson]: https://simplejson.readthedocs.io/en/latest/

## How to install External Libraries:
**requests**
- Binary installers for the latest released version are available at the [Python
package index](http://pypi.python.org/pypi/requests/) and on conda.

```sh
# conda
conda install requests
```

```sh
# or PyPI
pip install requests
```

**simplejson**
- Binary installers for the latest released version are available at the [Python
package index](http://pypi.python.org/pypi/simplejson/) and on conda.

```sh
# conda
conda install simplejson
```

```sh
# or PyPI
pip install simplejson
```

## Run the code:
```sh
python TwitterSearchAPI_SearchAndSave.py -s "#Cricket"
```
	- #Cricket: search term
	- If you don't provide any value for analysis to be performed, by default, it will perform 'analysis 5' i.e.find out for each search term, who is the most engaged user on twitter that day
	- Note: If you want to use #hashtag, include it in quotes like above. Otherwise it gets treated as two seperate strings and will give you an error "TwitterSearchAPI_SearchAndSave.py: error: argument -s/--search: expected one argument"

```sh
python TwitterSearchAPI_SearchAndSave.py -s Cricket -a 3
```
	- Cricket: search term
	- 3: Analysis you want to perform. In this case, across all search term, show the top 10 retweeted tweets for every day

```sh
python TwitterSearchAPI_SearchAndSave.py -s Cricket -a 6 
```
	- Cricket: search term
	- 6: Analysis you want to perform. 
	- Note: We don't have any analysis to be performed for 6. So it will display a message on the screen:" Nothing to analyze, please give numbers between 1 to 5!!!"

## Error Scenario:

```sh
python TwitterSearchAPI_SearchAndSave.py -s Cricket -a c
```
	- Output :
	usage: TwitterSearchAPI_SearchAndSave.py [-h] -s SEARCH [-a ANALYSIS]
	TwitterSearchAPI_SearchAndSave.py: error: argument -a/--analysis: invalid int value: 'c'

```sh
python TwitterSearchAPI_SearchAndSave.py -s #Cricket 
```
	- Output :
	usage: TwitterSearchAPI_SearchAndSave.py [-h] -s SEARCH [-a ANALYSIS]
	TwitterSearchAPI_SearchAndSave.py: error: argument -s/--search: expected one argument

```sh
python TwitterSearchAPI_SearchAndSave.py 
```
	- Output :
	usage: TwitterSearchAPI_SearchAndSave.py [-h] -s SEARCH [-a ANALYSIS]
	TwitterSearchAPI_SearchAndSave.py: error: the following arguments are required: -s/--search