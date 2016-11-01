import csv
import glob
import os
from collections import OrderedDict
import operator

path = os.getcwd()
os.chdir(path)

def Analysis_Top_Questions_Weightage():
    dict1 = {}
    for file in glob.glob(path+'/ab*.csv', recursive=True):
        with open(file, newline='') as f:
            reader = csv.reader(f)
            with open('output_top_questions.csv', 'w') as csvoutput:
                writer = csv.writer(csvoutput, lineterminator='\n')
                
                all = []
                row = next(reader)
                row.append('Weightage')
                all.append(row)
                writer.writerow(all[0])
                
                for row in reader:
                    row.append((int(row[2])*2) + (int(row[3])*5) + (int(row[4])*10))
                    all.append(row)
                    
                sortedData = all[1:]
                sortedlist = sorted(sortedData, key=lambda row: row[-1], reverse=True)
                writer.writerows(sortedlist)
                
                for row in sortedData:
                    dictList = {'title':row[-4],'weightage':(int(row[2])*2) + (int(row[3])*5) + (int(row[4])*10)}
                    dict1[row[-6]] = dictList

            csvoutput.close()
    newDict = OrderedDict(sorted(dict1.items(), key=lambda kv: kv[1]['weightage'], reverse=True)[:1])
    print("Top Question is ")
    for key, value in newDict.items():
        print('{} \t----->\t\t {}'.format(key,value))

def Analysis_Top_User_Per_Topic():
    Tags = []
    for file in glob.glob(path+'/tags_*.csv', recursive=True):
        with open(file, newline='') as f:
            reader = csv.reader(f)
            next(reader, None)  # skip the headers
            for row in reader:
                if row[2] not in Tags:
                    Tags.append(row[2])

    for data in Tags:
        userIds =[]
        for file in glob.glob(path+'/tags_*.csv', recursive=True):
            with open(file, newline='') as f:
                reader = csv.reader(f)
                next(reader, None)  # skip the headers
                for row in reader:
                    if row[2] == data:
                        userIds.append(row[0])
    
        dict2 = {}
        for file in glob.glob(path+'/questions_*.csv', recursive=True): 
            with open(file, newline='') as f:
                reader = csv.reader(f)
                all = []
                test = ["user_id","user_type","display_name","link","reputation"]
                all.append(test)
                next(reader, None)  # skip the headers
                for row in reader:
                    if row[0] in userIds:
                        all.append(row[:5])
                def ensure_dir(f):
                    if not os.path.exists(f):
                        os.makedirs(f)
                ensure_dir('output_top_users')
            
                with open('output_top_users/'+data+'.csv', 'w') as csvoutput:
                    writer = csv.writer(csvoutput, lineterminator='\n')
                    writer.writerow(all[0])
                    sortedData = all[1:]
                    sortedlist = sorted(sortedData, key=lambda row: row[-1], reverse=True)
                    writer.writerows(sortedlist)
                
                    for row in sortedData:
                        dictList = {'name':row[2],'link':row[3], 'reputation': row[4]}
                        dict2[row[0]] = dictList
    
        newDict = OrderedDict(sorted(dict2.items(), key=lambda kv: kv[1]['reputation'], reverse=True)[:1])
        print("Top User for %s is: " % data)
        for key, value in newDict.items():
            print('{} \t----->\t\t {}'.format(key,value))
                
        csvoutput.close() 

def Analysis_Popular_Badge_User():
    Badges = []
    for file in glob.glob(path+'/badge_*.csv', recursive=True):
        with open(file, newline='') as f:
            reader = csv.reader(f)
            next(reader, None)  # skip the headers
            for row in reader:
                if row[-2] not in Badges:
                    Badges.append(row[-2])

    def ensure_dir(f):
        if not os.path.exists(f):
            os.makedirs(f)
    ensure_dir('output_Badges')

    badgefn = "output_Badges/badge_users_count.csv"
    badgeFile = open(badgefn,"w")
    badge_file = csv.writer(badgeFile)
    badge_file.writerow(["Badge_Name","User_Ids","Count"])

    badgesData = []
    for data in Badges:
        userIdCount = 0
        userIds = []
        for file in glob.glob(path+'/badge*.csv', recursive=True):
            with open(file, newline='') as f:
                reader = csv.reader(f)
                next(reader, None)  # skip the headers
                for row in reader:
                    if row[-2] == data:
                        userIds.append(row[0])
                        userIdCount += 1
                badgesData.append([data,userIds,userIdCount])

    sortedlist = sorted(badgesData, key=lambda row: row[-1], reverse=True)
    badge_file.writerows(sortedlist)
    badgeFile.close()

    newList = sortedlist[:1]
    print(newList)
    print("Most Popular Badge among user is '%s' and count is '%s'" % (newList[0][0],newList[0][2]))

def Analysis_User_Question_Downvoted_Most():
    dict3 = {}
    for file in glob.glob(path+'/questions*.csv', recursive=True): 
        with open(file, newline='') as f:
            reader = csv.reader(f)
            all = []
            test = ["user_id","display_name","question_id","title","down_vote_count"]
            all.append(test)
            next(reader, None)  # skip the headers
        
            for row in reader:
                test1 =[row[0],row[2],row[-5],row[-3],row[-1]]
                all.append(test1)
            
            def ensure_dir(f):
                if not os.path.exists(f):
                    os.makedirs(f)
            ensure_dir('output_down_vote_count')
        
            with open('output_down_vote_count/'+'downVoteCount.csv', 'w') as csvoutput:
                writer = csv.writer(csvoutput, lineterminator='\n')
                writer.writerow(all[0])
                sortedData = all[1:]
                sortedlist = sorted(sortedData, key=lambda row: row[-1], reverse=True)
                writer.writerows(sortedlist)
            
                for row in sortedData:
                    dictList = {'name':row[1],'question_id':row[2], 'title': row[3], 'down_vote_count': row[4]}
                    dict3[row[0]] = dictList
            csvoutput.close()   
        
    newDict = OrderedDict(sorted(dict3.items(), key=lambda kv: kv[1]['down_vote_count'], reverse=True)[:1])
    print("The user whose question have been downvoted the most:")
    for key, value in newDict.items():
        print('{} \t----->\t\t {}'.format(key,value))

def Analysis_Tagwise_NoOfQuestion_And_Answer():
    dict4 = {}

    for file in glob.glob(path+'/questions*.csv', recursive=True): 
        with open(file, newline='') as f:
            reader = csv.reader(f)
            all = []
            test = ["question_id","question_link","title","answer_count","tags"]
            all.append(test)
            next(reader, None)  # skip the headers
        
            for row in reader:
                test1 =[row[-5],row[-4],row[-3],row[8],row[5][1:-1]]
                all.append(test1)
            
            def ensure_dir(f):
                if not os.path.exists(f):
                    os.makedirs(f)
            ensure_dir('output_answerCounts_tags')
        
            with open('output_answerCounts_tags/'+'tagsAndanswerCount.csv', 'w') as csvoutput:
                writer = csv.writer(csvoutput, lineterminator='\n')
                writer.writerow(all[0])
                sortedData = all[1:]
                sortedlist = sorted(sortedData, key=lambda row: row[-1], reverse=True)
                writer.writerows(sortedlist)
        
            csvoutput.close()

    Tags =[]
    for file in glob.glob(path+'/output_answerCounts_tags/tagsAndAnswerCount.csv', recursive=True):
        with open(file, newline='') as f:
            reader = csv.reader(f)
            next(reader, None)  # skip the headers
            for row in reader:
                if row[-1] not in Tags:
                    Tags.append(row[-1].replace("'", ""))
    result =[]
    for tag in Tags:
        result.append((tag.replace(",", "")).split())
    result1 = set(value for tag in result for value in tag)

    countfn = "output_answerCounts_tags/question_answer_count.csv"
    countFile = open(countfn,"w")
    count_file = csv.writer(countFile)
    count_file.writerow(["Tag_Name","questions_asked_count","Total_answered_count"])

    countData=[]
    
    for data in result1:
        anwerCount = 0
        questionCount = 0
        for file in glob.glob(path+'/output_answerCounts_tags/tagsAndAnswerCount.csv', recursive=True):
            with open(file, newline='') as f:
                reader = csv.reader(f)
                next(reader, None)  # skip the headers
                for row in reader:
                    if data in row[-1]:
                        anwerCount += int(row[-2])
                        questionCount += 1
                countData.append([data,questionCount,anwerCount])

    sortedlist = sorted(countData, key=lambda row: row[-1], reverse=True)
    count_file.writerows(sortedlist)
    countFile.close()

    newList = sortedlist[:1]
    print("Most Answered Tag is '%s'" % newList[0][0])

Analysis_Top_Questions_Weightage()
Analysis_Top_User_Per_Topic()
Analysis_Popular_Badge_User()
Analysis_User_Question_Downvoted_Most()
Analysis_Tagwise_NoOfQuestion_And_Answer()

