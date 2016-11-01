##Question:
Use the StackExchange REST API to collect the data for stackoverflow. You are supposed to use at least 3 per-site method. 
Perform 5 analysis on the data that you collect.

##Files: 
I have designed 2 scripts, namely:

**1) Midterm_StackOver_DataCollection.py:**
This script collects the data for stackoverflow from the StackExchange REST API and saves the details fetched in a csv file. 
Following are the per-site methods used: 
* [**/questions**] [/questions]: Get all questions on the site.
* [**/users/{ids}**] [/users/{ids}]: Get the users identified by a set of ids.
* [**/users/{ids}/tags**] [/users/{ids}/tags]: Get the tags that the users (identified by a set of ids) have been active in.
* [**/users/{ids}/badges**] [/users/{ids}/badges]: Get the badges earned by the users identified by a set of ids.

**2) Midterm_Analysis.py:**
This script performs 5 analysis:
- **Analysis 1:** Parse the body for the responses to collect a list of questions and user_id for the questions. Use the user_id obtained to send a request again to get user profile. Obtain the badges count to determine weightage. Show top questions according to the weightage.
- **Analysis 2:** For each of the User ID that you have collected, ping the API to get all the tags that user has identified with. Create a file for each topic, containing user_id,user_name and link to their profile sorted by reputation. For a given topic, what are the top users who have reputation in that topic.
- **Analysis 3:**For each of the badge type, find how many users (based on the data you have collected) have badge. We want to see what badges are popular among the users.
- **Analysis 4:** Find out the user whose questions have been downvoted the most.
- **Analysis 5:** For each of the question that is asked, find out the tags attached to it.Find how many numbers of answers have been given for each question. For each tag, calculate the number of question asked and how many times it has been answered.


[/questions]: https://api.stackexchange.com/docs/questions
[/users/{ids}]: https://api.stackexchange.com/docs/users-by-ids
[/users/{ids}/tags]: https://api.stackexchange.com/docs/tags-on-users
[/users/{ids}/badges]: https://api.stackexchange.com/docs/badges-on-users

##Run the script:
* python Midterm_StackOver_DataCollection.py

##Dependencies:
* [**python**] [python]: 3.5 or higher (prefered: Latest version)

[python]: https://www.python.org/downloads/release 

##Inbuilt Libraries used:
* datetime
* os
* csv
* glob
* json
* collections

Please refer the following link for [**The Python Standard Library**][The Python Standard Library]

[The Python Standard Library]: https://docs.python.org/3/library/

##External Libraries used:
* [**requests**][requests]
* [**simplejson**][simplejson]

[requests]: http://docs.python-requests.org/en/master/
[simplejson]: https://simplejson.readthedocs.io/en/latest/

##Some important points:
* Keep both the files: **Midterm_StackOver_DataCollection.py** and **Midterm_Analysis.py** in the same directory.
* Run the script in the path where you store the files
* The path containing the scripts will be selected as your current working directory.
* A folder with name "Stackoverflow_Search" will be created in the current working directory, if not present. If exists, then it will use it without creating a new one.
* A new folder with today's date will be created inside the folder "Stackoverflow_Search" (../Stackoverflow_Search/<today's date>), if not present. If exists, then it will use it without creating a new one. For example: ../Stackoverflow_Search/11_1_2016
* Everytime a new folder will be created with the current time inside today's date (../Stackoverflow_Search/today's date>/time). For example: ../Stackoverflow_Search/11_1_2016/1_10_55






