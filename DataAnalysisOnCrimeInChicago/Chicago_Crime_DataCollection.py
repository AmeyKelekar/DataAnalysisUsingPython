import pandas as pd
import os
import datetime
import argparse

#Constant Variables
DATASET_FILE_PATH = '/Chicago_crime/Crimes_-_2001_to_present.csv'
ANALYSIS_PYTHON_SCRIPT_PATH = '/Analysis_Scripts/python_scripts'
OUTPUT_FILES_RESULT_PATH = '/OutputFiles'

def valid_date(s):
    try:
        return datetime.strptime(s, "%Y-%m-%d")
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)

parser = argparse.ArgumentParser(description='Take the date as input for 5 for Analysis: Chicago crime rates by community area - PAST 30 DAYS ')
parser.add_argument('-e', "--enddate", help="The Start Date - format YYYY-MM-DD", type=valid_date)
args = parser.parse_args()

if args.enddate is None:
	args.enddate = datetime.datetime.now()
	startdate = datetime.datetime.now() + datetime.timedelta(-30)
else :
	startdate =  args.enddate + datetime.timedelta(-30)
	
print(startdate)
print(args.enddate)

#We will use the variables day, month, year, hour, minute and second for creating our folder structure#
now = datetime.datetime.now()
day = int(now.day)
month = int(now.month)
year = int(now.year)
hour = int(now.hour)
minute = int(now.minute)
second = int(now.second)

dir_path = os.getcwd()
print(dir_path+DATASET_FILE_PATH)
crime_data = pd.read_csv(dir_path+DATASET_FILE_PATH)

if __name__ == '__main__': 
	exec(open(dir_path+ANALYSIS_PYTHON_SCRIPT_PATH+'/Chicago_Crime_Analysis_Seasonality.py').read())  
	exec(open(dir_path+ANALYSIS_PYTHON_SCRIPT_PATH+'/Chicago_Crime_Analysis_CrimeOverTime.py').read())
	exec(open(dir_path+ANALYSIS_PYTHON_SCRIPT_PATH+'/Chicago_Crime_Analysis_HomicidesByLocationDescription.py').read())
	exec(open(dir_path+ANALYSIS_PYTHON_SCRIPT_PATH+'/Chicago_Crime_Analysis_OverallArrestRates.py').read())
	exec(open(dir_path+ANALYSIS_PYTHON_SCRIPT_PATH+'/Chicago_Crime_Analysis_ChicagoCrimeRatesByCommunityArea.py').read())

	