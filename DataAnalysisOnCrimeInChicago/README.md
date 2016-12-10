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

Please refer the following documenation [**The Python Standard Library**][The Python Standard Library] to learn more about python inbuilt/standard librarries

[The Python Standard Library]: https://docs.python.org/3/library/

##External Libraries used:
* [**matplotlib**][matplotlib]
* [**seaborn**][seaborn]
* [**pandas**][pandas]
* [**numpy**][numpy]

[matplotlib]: http://matplotlib.org/
[seaborn]: http://seaborn.pydata.org/
[pandas]: http://pandas.pydata.org/
[numpy]: http://www.numpy.org/

## How to install External Libraries:
**pandas**
- Binary installers for the latest released version are available at the [Python
package index](https://pypi.python.org/pypi/pandas/) and on conda.

```sh
# conda
conda install pandas
```

```sh
# or PyPI
pip install pandas
```

**matplotlib**
- Binary installers for the latest released version are available at the [Python
package index](https://pypi.python.org/pypi/matplotlib/) and on conda.

```sh
# conda
conda install matplotlib
```

```sh
# or PyPI
pip install matplotlib
```

**seaborn**
- Binary installers for the latest released version are available at the [Python
package index](https://pypi.python.org/pypi/seaborn/) and on conda.

```sh
# conda
conda install seaborn
```

```sh
# or PyPI
pip install seaborn
```

**numpy**
- Binary installers for the latest released version are available at the [Python
package index](https://pypi.python.org/pypi/numpy/) and on conda.

```sh
# conda
conda install numpy
```

```sh
# or PyPI
pip install numpy
```

##Folder Structure:
- **Data Collection File:** ../Chicago_Crime_DataCollection.py
- **Python Scripts for Analysis:**  ../Analysis_Scripts/python_scripts/<python-scripts>
	- example : ../Analysis_Scripts/python_scripts/Chicago_Crime_Analysis_Seasonality.py
- **Ipython notebooks for Analysis:** ../Analysis_Scripts/ipython_notebooks/<ipython-notebooks>
	- example : ../Analysis_Scripts/ipython_notebooks/Chicago_Crime_Analysis_Seasonality.ipynb
- **Data Set file:** ../Chicago_crime/Crimes_-_2001_to_present.csv
- **CSV Result:** ../OutputFiles/<current-date>/<current-time>/<analysis-name>/CSV/<result>
	- example : ../OutputFiles/12_9_2016/22_22_45/Chicago_Crime_Analysis_Seasonality/CSV/SeasonalitySelectedCrimes:Jan2001-Present.csv
- Graph Result:** ../OutputFiles/<current-date>/<current-time>/<analysis-name>/OutputGraphs/<result>
	- example : ../OutputFiles/12_9_2016/22_22_45/Chicago_Crime_Analysis_Seasonality/OutputGraphs/SeasonalitySelectedCrimes:Jan2001-Present,PrimaryType=ASSAULT.png


##Some important points:
* Run the script from the path where Data Collection File (Chicago_Crime_DataCollection.py) is stored
* The path containing the scripts will be selected as your current working directory.
* A new folder with today's date will be created inside the folder "OutputFiles", if not present. If exists, then it will use it without creating a new one. 
* Everytime a new folder will be created with the current time inside today's date.

## Analysis and Graphs:
**1) Homicides by location description:**
 - Why is it called “street crime”? By the location description, most murders appear to take place in the “street”. A surprising amount also took place in cars. Some of the lower-number-locations are also interesting, such as that 16 murders that happened in a vestibule.

 ![alt tag](https://github.com/AmeyKelekar/DataAnalysisUsingPython/blob/master/DataAnalysisOnCrimeInChicago/OutputFiles/12_9_2016/22_22_45/Chicago_Crime_Analysis_HomicidesByLocationDescription/OutputGraphs/Homicides_By_LocationDescription:Jan2001-Present.png)

**2.a) Overall arrest rates:**
- The Chicago data include a dimension on arrest = true/false. 
- Below is an overall picture of arrest rates by primary type of crime for the whole 16-year period. It’s tempting to look at this as a prioritization issue. Why would Chicago arrest 99% of the time for public indecency but only 49% of the time for homicide? 
- But there’s a lot of selection bias in these numbers. If an officer reports public indecency, he or she has probably seen it and can make the arrest. I’m sure there’s a lot of public indecency that happens unreported and unknown to our data set.
- As the most serious crime there is, a homicide will (almost?) always be reported. There’s probably also a longer time period to solve a murder than a public indecency case. Still, that 51% of murders resulted in no arrests is a little disconcerting.

![alt tag](https://github.com/AmeyKelekar/DataAnalysisUsingPython/blob/master/DataAnalysisOnCrimeInChicago/OutputFiles/12_9_2016/22_22_45/Chicago_Crime_Analysis_OverallArrestRates/OutputGraphs/OverallArrestRateByPrimaryTypeOfCrime:Jan2001-Present.png)

**2.b) Arrest rate trends (high-arrest-rate crimes):**
- To answer more questions on arrest rates, we need to look at trends
- Dividing the crimes between high-arrest-rate crimes, mid-arrest-rate and low-arrest-rate crimes, we can get cleaner visualizations, and we can easily compare arrest rates across crimes.
- There’s a weird aberration in 2008 where arrest rates for a lot of these crimes drop. And arrest rates for public peace violation / interference with a public officer have climbed significantly over the period.

![alt tag](https://github.com/AmeyKelekar/DataAnalysisUsingPython/blob/master/DataAnalysisOnCrimeInChicago/OutputFiles/12_9_2016/22_22_45/Chicago_Crime_Analysis_OverallArrestRates/OutputGraphs/Arrest_RateTrend_For_High-arrest-rate_crimes.png)

**2.c) Arrest rate trends (mid-arrest-rate crimes):**
- Homicides always sticks out: here because the rate is around 60%-63% in the past (so murders committed years ago still doesn’t get the best closure). But it also is interesting because of the downward trend. Again, part of this trend is most likely that the time to close a murder case is longer than for, say, a liquor law violation in the above graph.

![alt tag](https://github.com/AmeyKelekar/DataAnalysisUsingPython/blob/master/DataAnalysisOnCrimeInChicago/OutputFiles/12_9_2016/22_22_45/Chicago_Crime_Analysis_OverallArrestRates/OutputGraphs/Arrest_RateTrend_For_Medium-arrest-rate_crimes.png)

**3) Seasonality:**
- I’ve heard that certain crimes are committed during different parts of the year.  
- It turns out that homicides do appear to spike in the summer. 
- Assault shows a similar, but broader, trend. Instead of spiking in the summer, it’s more accurate to say that assaults drop in the winter. 
- Narcotics, stealing cars and prostitution seem to know no breaks. Being crimes of money rather than passion, this is expected.

![alt tag](https://github.com/AmeyKelekar/DataAnalysisUsingPython/blob/master/DataAnalysisOnCrimeInChicago/OutputFiles/12_9_2016/22_22_45/Chicago_Crime_Analysis_Seasonality/OutputGraphs/SeasonalitySelectedCrimes:Jan2001-Present%2CPrimaryType%3DASSAULT.png)
![alt tag](https://github.com/AmeyKelekar/DataAnalysisUsingPython/blob/master/DataAnalysisOnCrimeInChicago/OutputFiles/12_9_2016/22_22_45/Chicago_Crime_Analysis_Seasonality/OutputGraphs/SeasonalitySelectedCrimes:Jan2001-Present%2CPrimaryType%3DHOMICIDE.png)
![alt tag](https://github.com/AmeyKelekar/DataAnalysisUsingPython/blob/master/DataAnalysisOnCrimeInChicago/OutputFiles/12_9_2016/22_22_45/Chicago_Crime_Analysis_Seasonality/OutputGraphs/SeasonalitySelectedCrimes:Jan2001-Present%2CPrimaryType%3DMOTOR%20VEHICLE%20THEFT.png)
![alt tag](https://github.com/AmeyKelekar/DataAnalysisUsingPython/blob/master/DataAnalysisOnCrimeInChicago/OutputFiles/12_9_2016/22_22_45/Chicago_Crime_Analysis_Seasonality/OutputGraphs/SeasonalitySelectedCrimes:Jan2001-Present%2CPrimaryType%3DNARCOTICS.png)
![alt tag](https://github.com/AmeyKelekar/DataAnalysisUsingPython/blob/master/DataAnalysisOnCrimeInChicago/OutputFiles/12_9_2016/22_22_45/Chicago_Crime_Analysis_Seasonality/OutputGraphs/SeasonalitySelectedCrimes:Jan2001-Present%2CPrimaryType%3DPROSTITUTION.png)

## Run the code:
```sh
python Chicago_Crime_DataCollection.py -e 2016-11-30
```
	- 2016-11-30 is the enddate  and start date is calculated 30 days back as 2016-10-31
	- this input is only used for the Chicago Crime Rates By Community Area Analysis

```sh
python Chicago_Crime_DataCollection.py
```
	- current date is the enddate and start date is calculated as 30 days back
	- again the input is only used for the Chicago Crime Rates By Community Area Analysis

## Error Scenario:
```sh
python Chicago_Crime_DataCollection.py -e abc
```
	- Output :
	usage: Chicago_Crime_DataCollection.py [-h] [-e ENDDATE]
	Chicago_Crime_DataCollection.py: error: argument -e/--enddate: Not a valid date: 'abc'.













