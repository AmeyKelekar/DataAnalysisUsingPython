from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.pyplot import show
from datetime import datetime,date
from matplotlib.font_manager import FontProperties
from Chicago_Crime_DataCollection import crime_data,dir_path,day,month,year,hour,minute,second,OUTPUT_FILES_RESULT_PATH
import os

crime_data['Hour'] = crime_data['Date'].apply(lambda x: str(datetime.strptime(x,'%m/%d/%Y %I:%M:%S %p').hour)+':00')
df1 = crime_data.groupby(['Year','Hour']).size().reset_index(name="Crime Count")
crime_count_percentage = df1.groupby(['Year', 'Hour']).agg({'Crime Count': 'sum'})
crime_pcts = crime_count_percentage.groupby(level=0).apply(lambda x: 100*x/float(x.sum())).reset_index()
df_agg = crime_pcts.groupby(['Year','Hour']).agg({'Crime Count':sum})
g = df_agg['Crime Count'].groupby(level=0, group_keys=False)
res = g.apply(lambda x: x.sort_values(ascending=False).head(5)).reset_index()

def ensure_dir(f):
    if not os.path.exists(f):
        os.makedirs(f)

date_path = dir_path+OUTPUT_FILES_RESULT_PATH+ "/%i_%i_%i" % (month, day, year)
ensure_dir(date_path)
time_path = date_path + "/%i_%i_%i" % (hour, minute, second)
ensure_dir(time_path)
analysis_folder_path = time_path + "/Chicago_Crime_Analysis_CrimeOverTime"
ensure_dir(analysis_folder_path)
csv_file_path = analysis_folder_path + "/CSV"
ensure_dir(csv_file_path)
png_graph_path = analysis_folder_path + "/OutputGraphs"
ensure_dir(png_graph_path)

os.chdir(csv_file_path)
res.to_csv(path_or_buf= 'CrimeOverTime-Top5HoursPerYear.csv',index =False)
#res.to_csv(path_or_buf= dir_path+'/CrimeOverTime-Top5HoursPerYear.csv',index =False)

os.chdir(png_graph_path)
sns.set_style('white')
fontP = FontProperties()
for i, group in res.groupby('Year'):
    fig = plt.figure()
    ax = group.plot(x='Hour', y='Crime Count', kind = 'bar', title= str(i), figsize=(20,8), fontsize = 20, legend= True)
    ax.set_ybound(0,7)
    ax.title.set_fontsize(25)
    ax.xaxis.get_label().set_fontsize(22)
    legend = ax.legend(loc=0, ncol=1, bbox_to_anchor=(0, 0, 1, 1), prop = fontP,fancybox=True,shadow=False)
    plt.setp(legend.get_title(),fontsize=20)

    for p in ax.patches: 
        ax.annotate(str('%1.2f'%(p.get_height())+'%'),(p.get_x() * 1.005, p.get_height() * 1.005),fontsize=15)

    plt.savefig('CrimeOverTime-Top5HoursPerYear-Year=%s.png' %(i),dpi=100, facecolor='w', edgecolor='w', orientation='portrait', bbox_inches='tight')

os.chdir(dir_path)
