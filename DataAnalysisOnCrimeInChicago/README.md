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
- Top 5 hours and the percentage are displayed for each year


[/chicagocrime]: https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2

##Run the script:
```sh
python Midterm_StackOver_DataCollection.py
```

##Dependencies:
* [**python**] [python]: 3.5 or higher (prefered: Python 3.5.2 **Latest version**)

[python]: https://www.python.org/downloads/release 

##Standard Libraries used:
* datetime
* os
* csv
* glob
* json
* collections

Please refer the following documenation [**The Python Standard Library**][The Python Standard Library] to learn more about python inbuilt/standard librarries

[The Python Standard Library]: https://docs.python.org/3/library/

##External Libraries used:
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

##Some important points:
* Keep both the files: **Midterm_StackOver_DataCollection.py** and **Midterm_Analysis.py** in the same directory.
* Run the script in the path where you store the files
* The path containing the scripts will be selected as your current working directory.
* A new folder with name "Stackoverflow_Search" will be created in the current working directory, if not present. If folder already exists, then it will use it without creating a new one.
* A new folder with today's date will be created inside the folder "Stackoverflow_Search" (../Stackoverflow_Search/today's date), if not present. If exists, then it will use it without creating a new one. For example: ../Stackoverflow_Search/11_1_2016
* Everytime a new folder will be created with the current time inside today's date (../Stackoverflow_Search/today's date/currenttime). For example: ../Stackoverflow_Search/11_1_2016/1_10_55
* All the data and output csv files will be written into the time folder






