## Crime in Chicago:
![picture alt](https://github.com/AmeyKelekar/DataAnalysisUsingPython/blob/master/DataAnalysisOnCrimeInChicago/ChicagoCrimeSampleImage.jpeg "Crime in Chicago")

##Problem Statement / Question:
-  Use the Chicago Crime Dataset from Jan 2001 to Present and perform 5 analysis on the data collected.
- The dataset can be downladed from the following path: [**chicagocrime**] [/chicagocrime]
- The dataset reflects reported incidents of crime (with the exception of murders where data exists for each victim) that occurred in the City of Chicago from 2001 to present, minus the most recent seven days.
- Sample Dataset looks like:

	ID        |  Case Number |  Date          |  Block               |  IUCR   |  Primary Type        |  Description     |  Location Description   |  Arrest |  Domestic  |  Beat  |  District  |  Ward	 |  Community Area  |  FBI Code  |  X Coordinate  |  Y Coordinate  |  Year  |  Updated On     |	 Latitude     |  Longitude     |  Location
	----------|--------------|----------------|----------------------|---------|----------------------|------------------|-------------------------|---------|------------|--------|------------|--------|------------------|------------|----------------|----------------|--------|-----------------|---------------|----------------|--------------------------------
	10776695  |  HZ543234    |  12/1/16 0:00  |  012XX W GRACE ST	 | 	1310   |  CRIMINAL DAMAGE     |  TO PROPERTY     |  APARTMENT              |  FALSE  |  FALSE     |  1923  |  19	    |  44	 |  6	            |  14        |                |                |  2016  |  12/8/16 15:55  |               |                |
	10774757  |  HZ540108    |  12/1/16 0:00  |  011XX N HOWE ST     |  820    |  THEFT               |  $500 AND UNDER  |  APARTMENT              |  FALSE  |  FALSE     |  1822  |  18	    |  27	 |  8	            |  6         |  1171780	      |  1908001	   |  2016  |  12/8/16 15:55  |	 41.90301358  |  -87.64445672  |  (41.903013579, -87.644456722)
	10771987  |  HZ537398    |  12/1/16 0:00  |  036XX W FLOURNOY ST | 	910    |  MOTOR VEHICLE THEFT |  AUTOMOBILE      |  STREET                 |  FALSE  |  TRUE      |  1133  |  11	    |  24	 |  27	            |  7         |  1152232	      |  1896783	   |  2016  |  12/8/16 15:55  |	 41.87263854  |  -87.71655668  |  (41.872638542, -87.716556677)
	10771468  |  HZ536986    |  12/1/16 0:00  |  084XX S KENNETH AVE |	810    |  THEFT               |  OVER $500       |  STREET	               |  FALSE  |  FALSE     |  834   |  8	        |  18	 |  70	            |  6         |  1148223	      |  1848277	   |  2016  |  12/8/16 15:55  |  41.73960892  |	 -87.73252059  |  (41.739608919, -87.732520588)
	10770887  |  HZ536388    |  12/1/16 0:00  |  030XX N SAYRE AVE   |  820    |  THEFT               |  $500 AND UNDER  |  VEHICLE NON-COMMERCIAL |  FALSE  |  FALSE     |  2511  |  25	    |  36	 |  18	            |  6         |  1129052	      |  1919628	   |  2016  |  12/8/16 15:55  |	 41.93575385  |	 -87.80114211  |  (41.935753851, -87.80114211)

## Analysis and visualization done on dataset:
**1) Homicides by location description:**
- Here we compute crime count for each location description.
- The result is saved in a CSV file and looks like below :

	Location Description |  Crime Count  
	---------------------|---------------------------
	STREET	             |  3895      
	AUTO	             |  985    
	APARTMENT	         |  698 
	ALLEY	             |  517 
	HOUSE	             |  463
	PORCH	             |  247
	YARD	             |  164
    PARKING LOT	         |  139
    PARK PROPERTY        |  95
    VACANT LOT	         |  93
 
- **Some Observation:**
	- Why is it called “street crime”? 
	- By the location description, most murders appear to take place in the “street”. 
	- A surprising amount also took place in cars. 
	- Some of the lower-number-locations are also interesting, such as that 16 murders that happened in a vestibule.
- The result is visualized as below:
![alt tag](https://github.com/AmeyKelekar/DataAnalysisUsingPython/blob/master/DataAnalysisOnCrimeInChicago/OutputFiles/12_9_2016/22_22_45/Chicago_Crime_Analysis_HomicidesByLocationDescription/OutputGraphs/Homicides_By_LocationDescription:Jan2001-Present.png)

**2) Overall arrest rates and different arrest rate trends:**
- **a) Overall arrest rates:**
	- The Chicago data include a dimension on arrest = true/false.
	- Here we compute arrest percentage grouped by crime type.
	- The result is saved in a CSV file and looks like below :

	Primary Type						|  Arrest Percentage
	------------------------------------|----------------------
	DOMESTIC VIOLENCE					|  100
	PROSTITUTION						|  99.60118301
	NARCOTICS							|  99.35619284
	PUBLIC INDECENCY					|  99.28571429
	GAMBLING							|  99.25899537
	LIQUOR LAW VIOLATION				|  99.07434617
	INTERFERENCE WITH PUBLIC OFFICER	|  91.13707165
	CONCEALED CARRY LICENSE VIOLATION	|  85.18518519
	OBSCENITY							|  83.61858191
	WEAPONS VIOLATION					|  80.238146
	CRIMINAL TRESPASS					|  74.42169163
	OTHER NARCOTIC VIOLATION			|  72.97297297
	PUBLIC PEACE VIOLATION				|  64.1938279
	HOMICIDE							|  48.54202401


	- **Some Observation:** 
	  	- It’s tempting to look at this as a prioritization issue. 
	  	- Why would Chicago arrest 99% of the time for public indecency but only 49% of the time for homicide? 
 		- But there’s a lot of selection bias in these numbers. If an officer reports public indecency, he or she has probably seen it and can make the arrest. 
 		- I’m sure there’s a lot of public indecency that happens unreported and unknown to our data set.
		- As the most serious crime there is, a homicide will (almost?) always be reported. 
		- There’s probably also a longer time period to solve a murder than a public indecency case. 
		- Still, that 51% of murders resulted in no arrests is a little disconcerting.

	- Below is an overall picture of arrest rates by primary type of crime for the whole 16-year period:
![alt tag](https://github.com/AmeyKelekar/DataAnalysisUsingPython/blob/master/DataAnalysisOnCrimeInChicago/OutputFiles/12_9_2016/22_22_45/Chicago_Crime_Analysis_OverallArrestRates/OutputGraphs/OverallArrestRateByPrimaryTypeOfCrime:Jan2001-Present.png)

- **b) Arrest rate trends (high-arrest-rate crimes):**
	- To answer more questions on arrest rates, we need to look at trends
	- Arrest percentage is calcualted grouped by **Year** and **Crime Type**
	- Dividing the crimes between high-arrest-rate crimes, mid-arrest-rate and low-arrest-rate crimes, we can get cleaner visualizations, and we can easily compare arrest rates across crimes.
	- The result is saved in a CSV file and looks like below :

	Primary Type	                    |  Year	 |  Arrest Count  |  Total Count  |  Arrest Rate
	------------------------------------|--------|----------------|---------------|-----------------
	CONCEALED CARRY LICENSE VIOLATION	|  2014	 |  6	          |  15	          |  40
	CONCEALED CARRY LICENSE VIOLATION	|  2015	 |  32	          |  34	          |  94.11764706
	CONCEALED CARRY LICENSE VIOLATION	|  2016	 |  31	          |  32	          |  96.875
	CRIMINAL TRESPASS	                |  2001	 |  10262	      |  13240	      |  77.50755287
	CRIMINAL TRESPASS	                |  2002	 |  10632	      |  13880	      |  76.59942363

	- **Some Observation:** 
		- There’s a weird aberration in 2008 where arrest rates for a lot of these crimes drop. 
		- And arrest rates for public peace violation / interference with a public officer have climbed significantly over the period.
	- The result is visualized as below:
![alt tag](https://github.com/AmeyKelekar/DataAnalysisUsingPython/blob/master/DataAnalysisOnCrimeInChicago/OutputFiles/12_9_2016/22_22_45/Chicago_Crime_Analysis_OverallArrestRates/OutputGraphs/Arrest_RateTrend_For_High-arrest-rate_crimes.png)

- **c) Arrest rate trends (mid-arrest-rate crimes):**
	- The result is saved in a CSV file and looks like below :

	Primary Type  |  Year	 |  Arrest Count  |  Total Count  |  Arrest Rate
	--------------|----------|----------------|---------------|-----------------
	ASSAULT	      |  2001	 |  7150	      |  31384	      |  22.78230946
	ASSAULT	      |  2002	 |  7340	      |  31521	      |  23.28606326
	ASSAULT	      |  2003	 |  6909	      |  29477	      |  23.43861316
	ASSAULT	      |  2004	 |  7004	      |  28850	      |  24.27729636
	ASSAULT	      |  2005	 |  6631	      |  27066	      |  24.49937191

	- **Some Observation:** 
		- Homicides always sticks out: here because the rate is around 60%-63% in the past (so murders committed years ago still doesn’t get the best closure). 
		- But it also is interesting because of the downward trend. 
		- Again, part of this trend is most likely that the time to close a murder case is longer than for, say, a liquor law violation in the above graph.
	- The result is visualized as below:
![alt tag](https://github.com/AmeyKelekar/DataAnalysisUsingPython/blob/master/DataAnalysisOnCrimeInChicago/OutputFiles/12_9_2016/22_22_45/Chicago_Crime_Analysis_OverallArrestRates/OutputGraphs/Arrest_RateTrend_For_Medium-arrest-rate_crimes.png)

**3) Seasonality:**
- Crime Count is calculated grouped by **Crime Type**, **Year** and **Month**
- We are only analyzing for 5 specific crimes: **HOMICIDE** , **PROSTITUTION**, **ASSAULT**, **NARCOTICS** and **MOTOR VEHICLE THEFT**.
- The result is saved in a CSV file and looks like below :
	
	Primary Type  |  Year  |  Month     |  Crimes Count
	--------------|--------|------------|-----------------
	ASSAULT		  |	 2001  |  April	    |  2746
	ASSAULT	      |  2001  |  August	|  3021
	ASSAULT	      |  2001  |  December	|  2078
	ASSAULT		  |  2001  |  February	|  2029
	ASSAULT		  |  2001  |  January	|  2123
	ASSAULT		  |  2001  |  July	    |  3019
	ASSAULT		  |  2001  |  June	    |  2767
	ASSAULT	      |  2001  |  March	    |  2824
	ASSAULT	      |  2001  |  May	    |  2903
	ASSAULT	      |  2001  |  November	|  2394

- **Some Observation:**
	- I’ve heard that certain crimes are committed during different parts of the year.  
	- It turns out that homicides do appear to spike in the summer. 
	- Assault shows a similar, but broader, trend. Instead of spiking in the summer, it’s more accurate to say that assaults drop in the winter. 
	- Narcotics, stealing cars and prostitution seem to know no breaks. Being crimes of money rather than passion, this is expected.

- The results are visualized as below:
![alt tag](https://github.com/AmeyKelekar/DataAnalysisUsingPython/blob/master/DataAnalysisOnCrimeInChicago/OutputFiles/12_9_2016/22_22_45/Chicago_Crime_Analysis_Seasonality/OutputGraphs/SeasonalitySelectedCrimes:Jan2001-Present%2CPrimaryType%3DASSAULT.png)
![alt tag](https://github.com/AmeyKelekar/DataAnalysisUsingPython/blob/master/DataAnalysisOnCrimeInChicago/OutputFiles/12_9_2016/22_22_45/Chicago_Crime_Analysis_Seasonality/OutputGraphs/SeasonalitySelectedCrimes:Jan2001-Present%2CPrimaryType%3DHOMICIDE.png)
![alt tag](https://github.com/AmeyKelekar/DataAnalysisUsingPython/blob/master/DataAnalysisOnCrimeInChicago/OutputFiles/12_9_2016/22_22_45/Chicago_Crime_Analysis_Seasonality/OutputGraphs/SeasonalitySelectedCrimes:Jan2001-Present%2CPrimaryType%3DMOTOR%20VEHICLE%20THEFT.png)
![alt tag](https://github.com/AmeyKelekar/DataAnalysisUsingPython/blob/master/DataAnalysisOnCrimeInChicago/OutputFiles/12_9_2016/22_22_45/Chicago_Crime_Analysis_Seasonality/OutputGraphs/SeasonalitySelectedCrimes:Jan2001-Present%2CPrimaryType%3DNARCOTICS.png)
![alt tag](https://github.com/AmeyKelekar/DataAnalysisUsingPython/blob/master/DataAnalysisOnCrimeInChicago/OutputFiles/12_9_2016/22_22_45/Chicago_Crime_Analysis_Seasonality/OutputGraphs/SeasonalitySelectedCrimes:Jan2001-Present%2CPrimaryType%3DPROSTITUTION.png)

**4) Chicago Crime Rates By Community Area:**
- Crime rate in each Chicago community area for a 30 days is calculated
- Only 11 crime types: ASSAULT, ROBBERY, BATTERY, CRIM SEXUAL ASSAULT, HOMICIDE, ARSON, THEFT, BURGLARY, MOTOR VEHICLE THEFT, CRIMINALDAMAGE, PROSTITUTION and NARCOTICS are selected
- Even these 11 crimes are futher sub-categorized as:
	- **VIOLENT**: ASSAULT, ROBBERY, BATTERY, CRIM SEXUAL ASSAULT and HOMICIDE 
	- **PROPERTY**:  ARSON', THEFT, BURGLARY and MOTOR VEHICLE THEFT
	- **QUALITY OF LIFE**: CRIMINALDAMAGE, PROSTITUTION and NARCOTICS
- The results are saved in a CSV files and looks like below :
	**CRIME BY TYPE PER COMMUNITY AREA, PAST 30 DAYS**

	Community Name  |  PROPERTY	     |  QUALITY OF LIFE  |  VIOLENT
	----------------|----------------|-------------------|-----------------
	Albany Park		|  0.432131368	 |  0.13444087	     |  0.312094877
	Archer Heights	|  0.216065684	 |  0.067220435	     |  0.067220435
	Armour Square	|  0.13924233	 |  0.024007298	     |  0.196859845
	Ashburn			|  0.499351803	 |  0.211264224	     |  0.331300715
	Auburn Gresham	|  0.715417487	 |  0.523359101	     |  1.094732799

	**PROPERTY CRIME PER COMMUNITY AREA, PAST 30 DAYS**

	Community Name  |  ARSON		|  BURGLARY		 |  MOTOR VEHICLE THEFT  |  THEFT
	----------------|---------------|----------------|-----------------------|----------------
	Albany Park		|  0			|  0.100830653	 |	0.057617516			 |  0.2736832
	Archer Heights	|  0			|  0.057617516	 |	0.067220435			 |  0.091227733
	Armour Square	|  0			|  0.024007298	 |	0.00480146			 |  0.110433572
	Ashburn			|  0.00480146	|  0.081624814	 |	0.192058386			 |  0.220867144
	Auburn Gresham	|  0			|  0.192058386	 |	0.115235031			 |  0.40812407

	**QUALITY OF LIFE CRIME PER COMMUNITY AREA, PAST 30 DAYS**

	Community Name  |  CRIMINAL DAMAGE  |  NARCOTICS     |  PROSTITUTION
	----------------|-------------------|----------------|-----------------
	Albany Park	    |  0.12963941		|  0.00480146	 |	0
	Archer Heights	|  0.057617516		|  0.009602919	 |	0
	Armour Square	|  0.014404379		|  0.009602919	 |	0
	Ashburn	        |  0.206462765		|  0.00480146	 |	0
	Auburn Gresham	|  0.451337207		|  0.067220435	 |	0.00480146

	**VIOLENT CRIME PER COMMUNITY AREA, PAST 30 DAYS**

	Community Name	|  ASSAULT	     |  BATTERY		 |  CRIM SEXUAL ASSAULT	 |  HOMICIDE	 |	ROBBERY
	----------------|----------------|---------------|-----------------------|---------------|------------------
	Albany Park	    |  0.048014596	 |	0.148845249	 |	0.009602919			 |	0			 |	0.105632112
	Archer Heights	|  0.00480146	 |	0.043213137	 |	0					 |	0.00480146	 |	0.014404379
	Armour Square	|  0.00480146	 |	0.100830653	 |	0					 |	0.00480146	 |	0.086426274
	Ashburn	        |  0.072021895	 |	0.124837951	 |	0					 |	0			 |	0.13444087
	Auburn Gresham	|  0.201661305	 |	0.66740289	 |	0.014404379			 |	0.014404379  |	0.196859845

- **Some Observation:**
	- We can clearly observe that Austin Community topped in all the crime categories. 
	- South Deering shows a consistent value for all crime categories
	- Burnside is almost zero for all  crime categories

- The results are visualized as below:
**CRIME BY TYPE PER COMMUNITY AREA, PAST 30 DAYS**
![alt tag](https://github.com/AmeyKelekar/DataAnalysisUsingPython/blob/master/DataAnalysisOnCrimeInChicago/OutputFiles/12_10_2016/3_50_39/Chicago_Crime_Analysis_ChicagoCrimeRatesByCommunityArea:2016-11-30_2016-10-31/OutputGraphs/CrimeByTypePerCommunityArea:2016-11-30_2016-10-31.png)
**PROPERTY CRIME PER COMMUNITY AREA, PAST 30 DAYS**
![alt tag](https://github.com/AmeyKelekar/DataAnalysisUsingPython/blob/master/DataAnalysisOnCrimeInChicago/OutputFiles/12_10_2016/3_50_39/Chicago_Crime_Analysis_ChicagoCrimeRatesByCommunityArea:2016-11-30_2016-10-31/OutputGraphs/PropertyCrimePerCommunityArea:2016-11-30_2016-10-31.png)
**QUALITY OF LIFE CRIME PER COMMUNITY AREA, PAST 30 DAYS**
![alt tag](https://github.com/AmeyKelekar/DataAnalysisUsingPython/blob/master/DataAnalysisOnCrimeInChicago/OutputFiles/12_10_2016/3_50_39/Chicago_Crime_Analysis_ChicagoCrimeRatesByCommunityArea:2016-11-30_2016-10-31/OutputGraphs/QualityOfLifeCrimePerCommunityArea:2016-11-30_2016-10-31.png)
**VIOLENT CRIME PER COMMUNITY AREA, PAST 30 DAYS**
![alt tag](https://github.com/AmeyKelekar/DataAnalysisUsingPython/blob/master/DataAnalysisOnCrimeInChicago/OutputFiles/12_10_2016/3_50_39/Chicago_Crime_Analysis_ChicagoCrimeRatesByCommunityArea:2016-11-30_2016-10-31/OutputGraphs/ViolentCrimePerCommunityArea:2016-11-30_2016-10-31.png)

##Files: 
I have designed 6 scripts, namely:

**1) Chicago_Crime_DataCollection.py:**
- This script reads the data from the Crimes_-_2001_to_present CSV file and then performs 5 different analysis on the data. 


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
- **Community Name Collection File:** ../Chicago_Crime_CommunityNameCollection.py
- **Python Scripts for Analysis:**  ../Analysis_Scripts/python_scripts/python-scripts
	- example : ../Analysis_Scripts/python_scripts/Chicago_Crime_Analysis_Seasonality.py
- **Ipython notebooks for Analysis:** ../Analysis_Scripts/ipython_notebooks/ipython-notebooks
	- example : ../Analysis_Scripts/ipython_notebooks/Chicago_Crime_Analysis_Seasonality.ipynb
- **Data Set file:** ../Chicago_crime/Crimes_-_2001_to_present.csv
- **CSV Result:** ../OutputFiles/current-date/current-time/analysis-name/CSV/result
	- example : ../OutputFiles/12_9_2016/22_22_45/Chicago_Crime_Analysis_Seasonality/CSV/SeasonalitySelectedCrimes:Jan2001-Present.csv
- **Graph Result:** ../OutputFiles/current-date/current-time/analysis-name/OutputGraphs/result
	- example : ../OutputFiles/12_9_2016/22_22_45/Chicago_Crime_Analysis_Seasonality/OutputGraphs/SeasonalitySelectedCrimes:Jan2001-Present,PrimaryType=ASSAULT.png


##Some important points:
* Run the script from the path where Data Collection File (Chicago_Crime_DataCollection.py) is stored
* The path containing the scripts will be selected as your current working directory.
* A new folder with today's date will be created inside the folder "OutputFiles", if not present. If exists, then it will use it without creating a new one. 
* Everytime a new folder will be created with the current time inside today's date.
* Community Name Collection file should be executed only once at the beginning when you first time execute this file. You will require to re-execute this file incase you delete the community name CSV. You don't have to execute thie file everytime.

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













