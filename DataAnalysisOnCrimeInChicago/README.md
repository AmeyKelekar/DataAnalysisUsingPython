##Question:
Use the Chicago Crime Dataset from Jan 2001 to Present and perform 5 analysis on the data that you collect.

##Files: 
I have designed 6 scripts, namely:

**1) Chicago_Crime_DataCollection.py:**
This script reads the data from the Crimes_-_2001_to_present CSV file and then performs 5 different analysis on the data. 
The csv file can be downladed from the following path: 
* [**chicagocrime**] [/chicagocrime]: This dataset reflects reported incidents of crime (with the exception of murders where data exists for each victim) that occurred in the City of Chicago from 2001 to present, minus the most recent seven days

**2) Chicago_Crime_Analysis_HomicidesByLocationDescription.py:**
- This script first collects all the data from the file where crime type is **HOMICIDE** and then further gives count of total crime grouped by location description. It also gives you percentage value of crime for each location.

**3) Chicago_Crime_Analysis_Seasonality.py:**
- Since month column is not given in the CSV file, this script first derives the month value for each crime date. 
- Then the count of crimes are calculated grouped by **Crime Type**, **Year** and **Month**
- Here, we are only analyzing crime for 5 specific crimes: **HOMICIDE** , **PROSTITUTION**, **ASSAULT**, **NARCOTICS** and **MOTOR VEHICLE THEFT**. So, we only select these 5 crime types.

**4)Chicago_Crime_Analysis_CrimeOverTime.py:**
- Since hour column is not given in the CSV file, this script first derives the hour value for each crime date.
- Then the count of crimes are calculated grouped by **Year** and **Hour**
- Further percentage for each crime count is calculated grouped by **Year** and **Hour**
- Top 5 hours and percentage are displayed grouped by each year

**5)Chicago_Crime_Analysis_OverallArrestRates.py:**
- The Chicago data include a dimension on arrest = true/false
- This script first calculates arrest percentage grouped by crime type
- Further calculates arrest percentage grouped by **Year** and **Crime Type**
- Arrest rate is divided into 3 categories: high-arrest-rate, mid-arrest-rate and low-arrest-rate
- High-arrest-rate = Arrest percentage > 50, mid-arrest-rate=  Arrest percentage in (50,15) and low-arrest-rate = Arrest percentage <=15

**6)Chicago_Crime_Analysis_ChicagoCrimeRatesByCommunityArea.py:**
- Since community name(neighbourhood) is not given in the CSV file, this script first derives the community name for each record. 
- If end date is provided by the user, it goes 30 days back and fetches all the records. 
- Else considers end date as current date and then goes 30 days back and fetches all the records.
- Calculates crime count grouped by community name and crime type.
- Only 11 crime types: **ASSAULT**, **ROBBERY**, **BATTERY**, **CRIM SEXUAL ASSAULT**, **HOMICIDE**, **ARSON**, **THEFT**, **BURGLARY**, **MOTOR VEHICLE THEFT**, **CRIMINALDAMAGE**, **PROSTITUTION** and **NARCOTICS** are selected
- Even these 11 crimes are futher sub-categorized as:
	- **VIOLENT**: ASSAULT, ROBBERY, BATTERY, CRIM SEXUAL ASSAULT and HOMICIDE 
	- **PROPERTY**:  ARSON', THEFT, BURGLARY and MOTOR VEHICLE THEFT
	- **QUALITY OF LIFE**: CRIMINALDAMAGE, PROSTITUTION and NARCOTICS
- We find crime rate all the the 3 cartegories individually and even combined.


[/chicagocrime]: https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2

##Run the script:
```sh
python Chicago_Crime_DataCollection.py
```

##Dependencies:
* [**python**] [python]: 3.5 or higher (prefered: Python 3.5.2 **Latest version**)

[python]: https://www.python.org/downloads/release 

##Standard Libraries used:
* datetime
* os
* argparse
* csv
* json

Please refer the following documenation [**The Python Standard Library**][The Python Standard Library] to learn more about python inbuilt/standard librarries

[The Python Standard Library]: https://docs.python.org/3/library/

##External Libraries used:
* [**matplotlib**][matplotlib]
* [**seaborn**][seaborn]
* [**pandas**][pandas]

[matplotlib]: http://matplotlib.org/
[seaborn]: http://seaborn.pydata.org/
[pandas]: http://pandas.pydata.org/

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

##Some important points:
* Keep both the files: **Midterm_StackOver_DataCollection.py** and **Midterm_Analysis.py** in the same directory.
* Run the script in the path where you store the files
* The path containing the scripts will be selected as your current working directory.
* A new folder with name "Stackoverflow_Search" will be created in the current working directory, if not present. If folder already exists, then it will use it without creating a new one.
* A new folder with today's date will be created inside the folder "Stackoverflow_Search" (../Stackoverflow_Search/today's date), if not present. If exists, then it will use it without creating a new one. For example: ../Stackoverflow_Search/11_1_2016
* Everytime a new folder will be created with the current time inside today's date (../Stackoverflow_Search/today's date/currenttime). For example: ../Stackoverflow_Search/11_1_2016/1_10_55
* All the data and output csv files will be written into the time folder






