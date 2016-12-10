from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.pyplot import show
from Chicago_Crime_DataCollection import crime_data,dir_path,day,month,year,hour,minute,second,OUTPUT_FILES_RESULT_PATH
import os

homicides_by_location_description_df= crime_data[crime_data['Primary Type'] == 'HOMICIDE']['Location Description'].value_counts().reset_index()

def ensure_dir(f):
    if not os.path.exists(f):
        os.makedirs(f)

date_path = dir_path+OUTPUT_FILES_RESULT_PATH+ "/%i_%i_%i" % (month, day, year)
ensure_dir(date_path)
time_path = date_path + "/%i_%i_%i" % (hour, minute, second)
ensure_dir(time_path)
analysis_folder_path = time_path + "/Chicago_Crime_Analysis_HomicidesByLocationDescription"
ensure_dir(analysis_folder_path)
csv_file_path = analysis_folder_path + "/CSV"
ensure_dir(csv_file_path)
png_graph_path = analysis_folder_path + "/OutputGraphs"
ensure_dir(png_graph_path)

os.chdir(csv_file_path)
homicides_by_location_description_df.to_csv(path_or_buf= 'HomicidesByLocationDescription.csv',index =False)

#homicides_by_location_description_df.to_csv(path_or_buf= dir_path+'/HomicidesByLocationDescription.csv',index =False)

os.chdir(png_graph_path)
#Change your figure size to be (25,100)
plt.subplots(figsize=(25,100))
#Make backround while
sns.set_style('white')
#every bar should have same color - windows blue
ax = sns.barplot(x='Location Description',y='index',data= homicides_by_location_description_df,n_boot = 200, color='#3778bf')
#change font size of ticks and labels to make them look big(Don't use deafult font size)
ax.xaxis.get_label().set_fontsize(20)
ax.yaxis.get_label().set_fontsize(20)
ax.set_xbound(0,5000)
ax.tick_params(axis='x',which='major',labelsize=20)
ax.tick_params(axis='y',which='major',labelsize=20)
#change the tilte
ax.set_title('Homicides by location description: Jan 2001 - present')
ax.title.set_fontsize(25)
for p in ax.patches:
    output = str(p.get_width()) + ' | ' +  '%1.2f'%((100 * p.get_width())/len(crime_data[crime_data['Primary Type'] == 'HOMICIDE'])) + '%'
    ax.annotate(output,(p.get_width() * 1.005, p.get_y() + 0.5),fontsize=30)
plt.savefig('Homicides_By_LocationDescription:Jan2001-Present.png', dpi=100, facecolor='w', edgecolor='w', orientation='portrait', bbox_inches='tight')
os.chdir(dir_path)
