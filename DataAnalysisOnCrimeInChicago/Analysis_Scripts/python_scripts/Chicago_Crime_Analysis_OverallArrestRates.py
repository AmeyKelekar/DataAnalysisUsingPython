from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.pyplot import show
from Chicago_Crime_DataCollection import crime_data,dir_path,day,month,year,hour,minute,second,OUTPUT_FILES_RESULT_PATH
import os

new_df1 = (100*crime_data[crime_data.Arrest==True]['Primary Type'].value_counts()/crime_data['Primary Type'].value_counts()).sort_values(ascending = False).reset_index()
new_df1.columns = ['Primary Type', 'Arrest Percentage']
new_df2 = crime_data[crime_data.Arrest==True].groupby(['Primary Type','Year']).size().reset_index(name="Arrest Count")
new_df3 = crime_data.groupby(['Primary Type','Year']).size().reset_index(name="Total Count")
new_df4 = pd.merge(new_df2, new_df3,on=['Primary Type','Year'], how='inner')
new_df4['Arrest Rate'] = 100 * new_df4['Arrest Count']/new_df4['Total Count']
new_df5 = pd.merge(new_df4, new_df1[new_df1['Arrest Percentage'] > 50],on='Primary Type', how='inner').ix[:,:-1]
new_df6 = pd.merge(new_df4, new_df1[(new_df1['Arrest Percentage'] <= 50) & (new_df1['Arrest Percentage'] > 15) ],on='Primary Type', how='inner').ix[:,:-1]
new_df7 = pd.merge(new_df4, new_df1[new_df1['Arrest Percentage'] <= 15],on='Primary Type', how='inner').ix[:,:-1]

def ensure_dir(f):
    if not os.path.exists(f):
        os.makedirs(f)

date_path = dir_path+OUTPUT_FILES_RESULT_PATH+ "/%i_%i_%i" % (month, day, year)
ensure_dir(date_path)
time_path = date_path + "/%i_%i_%i" % (hour, minute, second)
ensure_dir(time_path)
analysis_folder_path = time_path + "/Chicago_Crime_Analysis_OverallArrestRates"
ensure_dir(analysis_folder_path)
csv_file_path = analysis_folder_path + "/CSV"
ensure_dir(csv_file_path)
png_graph_path = analysis_folder_path + "/OutputGraphs"
ensure_dir(png_graph_path)

os.chdir(csv_file_path)
new_df1.to_csv(path_or_buf= 'OverallArrestRateByPrimaryTypeOfCrime:Jan2001-Present.csv',index =False)
new_df4.to_csv(path_or_buf= 'ArrestRateTrendByPrimaryTypeOfCrimePerYear.csv',index =False)
new_df5.to_csv(path_or_buf= 'Arrest_RateTrend_For_High-arrest-rate_crimes:ArrestRate>50.csv',index =False)
new_df6.to_csv(path_or_buf= 'Arrest_RateTrend_For_Medium-arrest-rate_crimes:ArrestRateInRange(50,15).csv',index =False)
new_df7.to_csv(path_or_buf= 'Arrest_RateTrend_For_Low-arrest-rate_crimes:ArrestRate<15.csv',index =False)

os.chdir(png_graph_path)

#Change your figure size to be (20,50)
plt.subplots(figsize=(20,50))
#Make backround while
sns.set_style('white')
#every bar should have same color - windows blue
ax = sns.barplot(x='Arrest Percentage',y='Primary Type',data= new_df1, color='#3778bf')
#change font size of ticks and labels to make them look big(Don't use deafult font size)
ax.xaxis.get_label().set_fontsize(20)
ax.yaxis.get_label().set_fontsize(20)
ax.set_xbound(0,150)
ax.tick_params(axis='x',which='major',labelsize=20)
ax.tick_params(axis='y',which='major',labelsize=20)
#change the tilte
ax.set_title('Overall arrest rate by primary type of crime : Jan 2001 - present')
ax.title.set_fontsize(25)
for p in ax.patches:
    output = '%1.2f'%(p.get_width())+ '%'
    ax.annotate(output,(p.get_width() * 1.005, p.get_y() + 0.5),fontsize=30)
plt.savefig('OverallArrestRateByPrimaryTypeOfCrime:Jan2001-Present.png', dpi=100, facecolor='w', edgecolor='w', orientation='portrait', bbox_inches='tight')

def create_graph(df,title,filename):		
	sns.set_style('white')
	#every bar should have same color - windows blue
	ax = sns.factorplot(x="Year", y="Arrest Rate", hue="Primary Type",data= df,size=8, aspect=2)
	#change font size of ticks and labels to make them look big(Don't use deafult font size)
	ax.ax.xaxis.get_label().set_fontsize(20)
	ax.ax.yaxis.get_label().set_fontsize(20)
	ax.ax.tick_params(axis='x',which='major',labelsize=20)
	ax.ax.tick_params(axis='y',which='major',labelsize=20)
	#change the tilte
	ax.ax.set_title(title)
	ax.ax.title.set_fontsize(25)
	plt.savefig(filename, dpi=100, facecolor='w', edgecolor='w', orientation='portrait', bbox_inches='tight')

create_graph(new_df5, 'Arrest rate trend for "high-arrest-rate" crimes', 'Arrest_RateTrend_For_High-arrest-rate_crimes.png')
create_graph(new_df6, 'Arrest rate trend for "mid-arrest-rate" crimes', 'Arrest_RateTrend_For_Medium-arrest-rate_crimes.png')
create_graph(new_df7, 'Arrest rate trend for "low-arrest-rate" crimes', 'Arrest_RateTrend_For_Low-arrest-rate_crimes.png')

os.chdir(dir_path)