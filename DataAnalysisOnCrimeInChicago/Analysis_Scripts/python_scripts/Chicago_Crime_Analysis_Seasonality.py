from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.pyplot import show
from datetime import datetime,date
from Chicago_Crime_DataCollection import crime_data,dir_path,day,month,year,hour,minute,second,OUTPUT_FILES_RESULT_PATH
import os

crime_data['Month'] = crime_data['Date'].apply(lambda x: datetime.strptime(x,'%m/%d/%Y %I:%M:%S %p').date().strftime('%B'))
new_df = crime_data.groupby(['Primary Type','Year','Month']).size().reset_index(name="Crimes Count")
new_df1 = new_df.loc[new_df['Primary Type'].isin(['HOMICIDE','PROSTITUTION','ASSAULT','NARCOTICS','MOTOR VEHICLE THEFT'])]
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
mapping = {month: i for i, month in enumerate(months)}
key = new_df1['Month'].map(mapping)
new_df2 = new_df1.iloc[key.argsort()]

def ensure_dir(f):
    if not os.path.exists(f):
        os.makedirs(f)

date_path = dir_path+OUTPUT_FILES_RESULT_PATH+ "/%i_%i_%i" % (month, day, year)
ensure_dir(date_path)
time_path = date_path + "/%i_%i_%i" % (hour, minute, second)
ensure_dir(time_path)
analysis_folder_path = time_path + "/Chicago_Crime_Analysis_Seasonality"
ensure_dir(analysis_folder_path)
csv_file_path = analysis_folder_path + "/CSV"
ensure_dir(csv_file_path)
png_graph_path = analysis_folder_path + "/OutputGraphs"
ensure_dir(png_graph_path)

os.chdir(csv_file_path)
new_df1.to_csv(path_or_buf= 'SeasonalitySelectedCrimes:Jan2001-Present.csv',index =False)

os.chdir(png_graph_path)
def create_graph(primary_type_list):
    for primary_type in primary_type_list:
        sns.set_style('white')
        #sns.set(font_scale=1.2)
        g = sns.factorplot(x="Month", y="Crimes Count", hue="Year", data= new_df2[new_df2['Primary Type'] == primary_type], size=8, aspect=2)
        g.set_xticklabels(rotation=90)
        g.fig.suptitle('Seasonality selected crimes: Jan 2001 - present, Primary Type = %s' %(primary_type),fontsize=15)
        g.set_xlabels(fontsize=15)
        g.set_ylabels(fontsize=15)

        plt.savefig('SeasonalitySelectedCrimes:Jan2001-Present,PrimaryType=%s.png' %(primary_type),dpi=100, facecolor='w', edgecolor='w', orientation='portrait', bbox_inches='tight')

create_graph(['HOMICIDE','PROSTITUTION','ASSAULT','NARCOTICS','MOTOR VEHICLE THEFT'])
os.chdir(dir_path)

