import requests
import datetime
import os
import csv
import glob
import simplejson
import json
from collections import OrderedDict

url = 'https://api.stackexchange.com/2.2/questions'
payload = {'key': 'g04eu)PhKDJkZAO2M191DA((', 'order': 'desc', 'sort': 'votes', 'tagged': 'python;pandas','site': 'stackoverflow', 'filter': '!9YdnSHzjM'}
r = requests.get(url, params=payload)

#We will use the variables day, month, year, hour, minute and second for our output file name#
now = datetime.datetime.now()
day = int(now.day)
month = int(now.month)
year = int(now.year)
hour = int(now.hour)
minute = int(now.minute)
second = int(now.second)

dir_path = os.getcwd()
new_path = dir_path + "/Stackoverflow_Search"

def ensure_dir(f):
    if not os.path.exists(f):
        os.makedirs(f)

ensure_dir(new_path)
date_path = new_path + "/%i_%i_%i" % (now.month, now.day, now.year)
ensure_dir(date_path)
time_path = date_path + "/%i_%i_%i" % (now.hour, now.minute, now.second)
ensure_dir(time_path)

os.chdir(time_path)
questions = r.json()

if __name__ == '__main__':
    #name our output file - %i will be replaced by current month, day, year, hour, minute and second
    outfn = "questions_%i_%i_%i_%i_%i_%i.csv" % (now.month, now.day, now.year, now.hour, now.minute, now.second)
    f=open(outfn,"w")
    csv_file=csv.writer(f)
    csv_file.writerow(["user_id","user_type","display_name","link","reputation","tags","is_answered","view_count","answer_count","score","question_id","question_link","title","creation_date","down_vote_count"])
    
    for entry in questions['items']:    
        csv_file.writerow([entry['owner']['user_id'],entry['owner']['user_type'],entry['owner']['display_name'],entry['owner']['link'],entry['owner']['reputation']
                           ,entry['tags'],entry['is_answered'],entry['view_count'],entry['answer_count'],entry['score'],entry['question_id']
                           ,entry['link'],entry['title'],entry['creation_date'],entry['down_vote_count']])
    f.close()

    userfn = "users_%i_%i_%i_%i_%i_%i.csv" % (now.month, now.day, now.year, now.hour, now.minute, now.second)
    userFile = open(userfn,"w")
    user_file = csv.writer(userFile)
    user_file.writerow(["user_id","user_type","display_name","link","reputation","account_id","bronze_badge","silver_badge","gold_badge"])
    
    for file in glob.glob(time_path+"/"+outfn, recursive=True):
        with open(file, newline='') as f:
            reader = csv.reader(f)
            next(reader, None)  # skip the headers
            
            for row in reader:
                payload1 = {'key': 'g04eu)PhKDJkZAO2M191DA((', 'order': 'desc', 'sort': 'reputation','site': 'stackoverflow'}
                url_user_by_id = 'https://api.stackexchange.com/2.2/users/'+row[0]
                user= requests.get(url_user_by_id, params=payload1)
                users = user.json()
                for records in users['items']:
                    user_file.writerow([records['user_id'],records['user_type'],records['display_name'],records['link'],records['reputation']
                                        ,records['account_id'],records['badge_counts']['bronze'],records['badge_counts']['silver'],records['badge_counts']['gold']])
                    
    userFile.close()

    tagfn = "tags_%i_%i_%i_%i_%i_%i.csv" % (now.month, now.day, now.year, now.hour, now.minute, now.second)
    tagsFile = open(tagfn,"w")
    tag_file = csv.writer(tagsFile)
    tag_file.writerow(["user_id","count","name"])
    
    for file in glob.glob(time_path+"/"+outfn, recursive=True):
        with open(file, newline='') as f:
            reader = csv.reader(f)
            next(reader, None)  # skip the headers
            
            for row in reader:
                payload2 = {'key': 'g04eu)PhKDJkZAO2M191DA((', 'order': 'desc', 'sort': 'popular','site': 'stackoverflow'}
                url_user_tags = 'https://api.stackexchange.com/2.2/users/'+row[0]+'/tags'
                user_tags = requests.get(url_user_tags, params=payload2)
                usersTags = user_tags.json()
                for records1 in usersTags['items']:
                    tag_file.writerow([records1['user_id'],records1['count'],records1['name']])
    
    tagsFile.close()

    badgefn = "badge_%i_%i_%i_%i_%i_%i.csv" % (now.month, now.day, now.year, now.hour, now.minute, now.second)
    badgeFile = open(badgefn,"w")
    badge_file = csv.writer(badgeFile)
    badge_file.writerow(["user_id","user_type","display_name","reputation","user_link","badge_id","link","name","rank"])
    
    for file in glob.glob(time_path+"/"+outfn, recursive=True):
        with open(file, newline='') as f:
            reader = csv.reader(f)
            next(reader, None)  # skip the headers
            
            for row in reader:
                payload3 = {'key': 'g04eu)PhKDJkZAO2M191DA((', 'order': 'desc', 'sort': 'name','site': 'stackoverflow'}
                url_user_badge = 'https://api.stackexchange.com/2.2/users/'+row[0]+'/badges'
                user_badge = requests.get(url_user_badge, params=payload3)
                usersBadge = user_badge.json()
                for records2 in usersBadge['items']:
                    badge_file.writerow([records2['user']['user_id'],records2['user']['user_type'],records2['user']['display_name']
                                         ,records2['user']['reputation'],records2['user']['link'],records2['badge_id'],records['link']
                                         ,records2['name'],records2['rank']])
    badgeFile.close()
    
    with open(outfn, "rt", encoding="UTF-8") as f:
        r = csv.reader(f)
        dict2 = {row[0]: row[1:] for row in r}
        
    with open(userfn, "rt", encoding="UTF-8") as f:
        r = csv.reader(f)
        dict1 = OrderedDict((row[0], row[5:]) for row in r)
        
    result = OrderedDict()
    for d in (dict1, dict2):
        for key, value in d.items():
            result.setdefault(key, []).extend(value)

    combinedfn = "ab_combined_%i_%i_%i_%i_%i_%i.csv" % (now.month, now.day, now.year, now.hour, now.minute, now.second)
            
    with open(combinedfn, 'w') as f:
        w = csv.writer(f)
        for key, value in result.items():
            w.writerow([key] + value)

    exec(open(dir_path+'/StackExchange_Analysis.py').read())