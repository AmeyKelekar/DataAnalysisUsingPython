import requests
import os
import csv
import json

url = 'http://crime.chicagotribune.com/api/1.0-beta1/communityarea/'
payload = {'format' : 'json'}
r = requests.get(url, params=payload)

dir_path = os.getcwd()
new_path = dir_path + "/Chicago_Community_Area"
def ensure_dir(f):
    if not os.path.exists(f):
        os.makedirs(f)
ensure_dir(new_path)
os.chdir(new_path)

community_area = r.json()

#NAME OUR OUTPUT FILE 
outfn = "chicago_communinity_area_data.csv"

f=open(outfn,"w")
csv_file=csv.writer(f)
csv_file.writerow(["Community Area","Community Name"])

#csv_file.writerow(["Community Area","Community Name","Hardship Index","Pct_Crowded","Pct_No_Diploma","Pct_Old_and_Young","Pct_Poverty","Pct_Unemployed","Per_Capita_Income","Population_2000","Population_2010","Shape_Area","Shape_Len"])

#THE VARIABLE 'USERS' CONTAINS INFORMATION OF THE 32 TWITTER USER IDS LISTED ABOVE
#THIS BLOCK WILL LOOP OVER EACH OF THESE IDS, CREATE VARIABLES, AND OUTPUT TO FILE
for entry in community_area['objects']: 
    csv_file.writerow([entry['area_number'],entry['name']])
    #csv_file.writerow([entry['area_number'],entry['name'],entry['hardship_index'],entry['pct_crowded'],entry['pct_no_diploma'],entry['pct_old_and_young']
    #,entry['pct_poverty'],entry['pct_unemployed'],entry['per_capita_income'],entry['population_2000'], entry['population_2010'],entry['shape_area']
    #,entry['shape_len']])
f.close()