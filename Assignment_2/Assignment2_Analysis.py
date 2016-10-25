import argparse
import csv
import glob
import Assignment2_SearchAndSave
import os
import operator
from collections import Counter

def Analysis_Average_Number_Of_Friends():
    path = Assignment2_SearchAndSave.date_path
    print(path)
    os.chdir(path)
    dict1 = {}
    for file in glob.glob(path+'/**/*.csv', recursive=True):
        with open(file, newline='') as f:
            reader = csv.reader(f)
            next(reader, None)  # skip the headers
            for row in reader:
                dictList = {'friends_count':int(row[6]),'count':1}
                if not row[1] in dict1:
                    dict1[row[1]] = dictList
                else:
                    dict1[row[1]]['count'] += 1
                    dict1[row[1]]['friends_count'] += int(row[6])
    print("Screen_Name Average_Friends")
    for key, value in dict1.items():
        print(key,int(value['friends_count']/value['count']))

def Analysis_Top_5_Languages():
    path = Assignment2_SearchAndSave.date_path
    print(path)
    os.chdir(path)
    dict2 = {}
    for file in glob.glob(path+'/**/*.csv', recursive=True):
        with open(file, newline='') as f:
            reader = csv.reader(f)
            next(reader, None)  # skip the headers
            for row in reader:
                if not row[-2] in dict2:
                    dict2[row[-2]] = 1
                else:
                    dict2[row[-2]] += 1
    print(dict2)
    newDict = dict(sorted(dict2.items(), key=operator.itemgetter(1), reverse=True)[:5])
    print("Top Five Languages are: ",newDict)

def Analysis_Top_10_Retweeted_Tweets():
    path = Assignment2_SearchAndSave.search_dir
    print(path)
    os.chdir(path)
    dict3 = {}
    for file in glob.glob(path+'/**/*.csv', recursive=True):
        with open(file, newline='') as f:
            reader = csv.reader(f)
            next(reader, None)  # skip the headers
            for row in reader:
                dict3[row[-5]] = int(row[-1])

    filtered_dic = {k:v for k,v in dict3.items() if v != 0}
    newDict2 = dict(sorted(filtered_dic.items(), key=operator.itemgetter(1), reverse=True)[:10])
    print("Top 10 retweeeted tweets are: ")
    for key in newDict2.items():
        print(key)

def Analysis_Influential_Tweet_Per_Topic():
    path = Assignment2_SearchAndSave.date_path
    print(path)
    os.chdir(path)
    subdirs = filter(None,[x[1] for x in os.walk(path)])
    for subdir in subdirs: 
        print(subdir)
        for dirValue in subdir:
            dict4 = {}
            print(dirValue)
            print(path+"/"+dirValue)
            for file in glob.glob(path+"/"+dirValue+'/**/*.csv', recursive=True):
                with open(file, newline='') as f:
                    reader = csv.reader(f)
                    next(reader, None)  # skip the headers
                    for row in reader:
                        dictList = {'followers_count':int(row[5])*int(row[-1]),'count':1}
                        if not row[-5] in dict4:
                            dict4[row[-5]] = dictList
                        else:
                            dict4[row[-5]]['count'] += 1
                            dict4[row[-5]]['followers_count'] += int(row[5])*int(row[-1])
        
            combined_dict={}
            for key, value in dict4.items():
                combined_dict[key] = int(value['followers_count']/value['count'])
            newDict3 = dict(sorted(combined_dict.items(), key=operator.itemgetter(1), reverse=True)[:1])
            print("Top influential tweet for topic %s is: " % dirValue)
            for key in newDict3.items():
                print(key)

def Analysis_Most_Engaged_User_On_Topic():
    path = Assignment2_SearchAndSave.date_path
    print(path)
    os.chdir(path)
    subdirs = filter(None,[x[1] for x in os.walk(path)])
    for subdir in subdirs: 
        print(subdir)
        for dirValue in subdir:
            dict4 = {}
            print(dirValue)
            print(path+"/"+dirValue)
            for file in glob.glob(path+"/"+dirValue+'/**/*.csv', recursive=True):
                with open(file, newline='') as f:
                    reader = csv.reader(f)
                    next(reader, None)  # skip the headers
                    for row in reader:
                        dictList = {'statuses_count':int(row[7]),'count':1}
                        if not row[1] in dict4:
                            dict4[row[1]] = dictList
                        else:
                            dict4[row[1]]['count'] += 1
                            dict4[row[1]]['statuses_count'] += int(row[7])
        
            combined_dict={}
            for key, value in dict4.items():
                combined_dict[key] = int(value['statuses_count']/value['count'])
            newDict3 = dict(sorted(combined_dict.items(), key=operator.itemgetter(1), reverse=True)[:1])
            print("Most engaged user for topic %s is: " % dirValue)
            for key in newDict3.items():
                print(key)

number = int(Assignment2_SearchAndSave.args.search[1])
print(number)

def numbers_to_strings(arguement):
    if arguement == 1:
        Analysis_Average_Number_Of_Friends()
    elif arguement == 2:
        Analysis_Top_5_Languages()
    elif arguement == 3:
        Analysis_Top_10_Retweeted_Tweets()
    elif arguement == 4:
    	Analysis_Influential_Tweet_Per_Topic() 
    elif arguement == 5:
    	Analysis_Most_Engaged_User_On_Topic()   
    else:
        print("Nothing to analyze, please give numbers between 1 to 5!!!")

numbers_to_strings(number)
