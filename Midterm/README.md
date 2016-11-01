##Question:
Use the StackExchange REST API to collect the data for stackoverflow. You are supposed to use at least 3 per-site method. 
Perform 5 analysis on the data that you collect.

##Files: 
I have designed 2 scripts, namely:

**1) Midterm_StackOver_DataCollection.py:**
..* This script collects the data for stackoverflow from the StackExchange REST API and saves the details fetched in a csv file. 
..* Following are the per-site methods used: 
* [**/questions**] [/questions]: Get all questions on the site.
* [**/users/{ids}**] [/users/{ids}]: Get the users identified by a set of ids.
* [**/users/{ids}/tags**] [/users/{ids}/tags]: Get the tags that the users (identified by a set of ids) have been active in.
* [**/users/{ids}/badges**] [/users/{ids}/badges]: Get the badges earned by the users identified by a set of ids.

[/questions]: https://api.stackexchange.com/docs/questions
[/users/{ids}]: https://api.stackexchange.com/docs/users-by-ids
[/users/{ids}/tags]: https://api.stackexchange.com/docs/tags-on-users
[/users/{ids}/badges]: https://api.stackexchange.com/docs/badges-on-users

