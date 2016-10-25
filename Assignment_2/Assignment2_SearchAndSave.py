import requests
from requests_oauthlib import OAuth1
import argparse
import sys
import string
import simplejson
import json
import os
import datetime
import csv

url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1('wsa9XC1P3lfM0IihoICjgJUjw', 'fa7RwF9HoeGChYTIcpgignp2WqgsKPWGpegC2IkvxaW0BFERSi',
                  '788872315253755904-J0Pe363NDpZaBYku6iex8KUdabudXiq', '1vkKNfixNHT4CI8g5UZg5UYbOAGL2zANEsCnf0bQjIewG')
requests.get(url, auth=auth)

parser = argparse.ArgumentParser(description='Take the search string and value from 1 to 5 for Analysis you want to perform as input')
parser.add_argument('search',metavar='N', nargs=2, help='Search term and analysis value')

args = parser.parse_args()
print(args.search)
payload = {'q': args.search[0], 'result_type': 'recent'}
r = requests.get('https://api.twitter.com/1.1/search/tweets.json',auth=auth, params=payload)
print(r.url)

#We will use the variables day, month, year, hour, minute and second for our output file name#
now = datetime.datetime.now()
day = int(now.day)
month = int(now.month)
year = int(now.year)
hour = int(now.hour)
minute = int(now.minute)
second = int(now.second)

dir_path = os.getcwd()
print(dir_path)
new_path = dir_path + "/Twitter_Search"
print(new_path)
def ensure_dir(f):
    if not os.path.exists(f):
        os.makedirs(f)
ensure_dir(new_path)
date_path = new_path + "/%i_%i_%i" % (now.month, now.day, now.year)
ensure_dir(date_path)
search_dir = date_path + "/" + args.search[0]
ensure_dir(search_dir)
os.chdir(search_dir)

tweets = r.json()

#name our output file - %i will be replaced by current month, day, year, hour, minute and second
outfn = args.search[0] + "_%i_%i_%i_%i_%i_%i.csv" % (now.month, now.day, now.year, now.hour, now.minute, now.second)

f=open(outfn,"w")
csv_file=csv.writer(f)

csv_file.writerow(["id","screen_name","name","created_at","url","followers_count","friends_count","statuses_count","favourites_count","listed_count","contributors_enabled","description","protected","location","lang","retweet_count"])

for entry in tweets['statuses']:    
    csv_file.writerow([entry['id'],entry['user']['screen_name'],entry['user']['name'],entry['user']['created_at'],entry['user']['url']
    ,entry['user']['followers_count'],entry['user']['friends_count'],entry['user']['statuses_count'],entry['user']['favourites_count']
    ,entry['user']['listed_count'],entry['user']['contributors_enabled'],entry['user']['description'],entry['user']['protected']
    ,entry['user']['location'], entry['user']['lang'],entry['retweet_count']])

f.close()

os.chdir(dir_path)
#os.system('python Assignment2_Analysis.py 1')
exec(open('Assignment2_Analysis.py').read())