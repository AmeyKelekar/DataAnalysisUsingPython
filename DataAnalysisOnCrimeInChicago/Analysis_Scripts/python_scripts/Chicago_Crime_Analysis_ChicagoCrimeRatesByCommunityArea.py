from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.pyplot import show
from datetime import datetime,date
from Chicago_Crime_DataCollection import crime_data,dir_path,day,month,year,hour,minute,second,OUTPUT_FILES_RESULT_PATH,args,startdate
import os

community_area = pd.read_csv(dir_path+'/Chicago_Community_Area/chicago_communinity_area_data.csv')
crime_data_community_name = crime_data.merge(community_area,how='outer')
crime_data_community_name['Date'] = pd.to_datetime(crime_data_community_name['Date'])
mask = (crime_data_community_name['Date'] > startdate) & (crime_data_community_name['Date'] <= args.enddate)
df = crime_data_community_name.loc[mask].reset_index()
new_df = df.groupby(['Community Name','Primary Type']).size().reset_index(name="Crimes Count")
new_df1 = new_df.loc[new_df['Primary Type'].isin (['ASSAULT','ROBBERY','BATTERY','CRIM SEXUAL ASSAULT','HOMICIDE','ARSON','THEFT','BURGLARY','MOTOR VEHICLE THEFT','CRIMINAL DAMAGE','PROSTITUTION','NARCOTICS'])]
new_df1['Crime Category'] = new_df1['Primary Type'].apply(lambda x : "VIOLENT" if x in ['ASSAULT','ROBBERY','BATTERY','CRIM SEXUAL ASSAULT','HOMICIDE'] else "PROPERTY" if x in ['ARSON','THEFT','BURGLARY','MOTOR VEHICLE THEFT'] else "QUALITY OF LIFE")
combined_df = new_df1.groupby(['Community Name','Crime Category']).agg({'Crimes Count': 'sum'}).reset_index()
combined_df['Percentage Crime Rate'] = 100*combined_df['Crimes Count']/len(df)
property_df = new_df1[new_df1['Crime Category'] == 'PROPERTY']
property_df['Percentage Crime Rate'] = 100*property_df['Crimes Count']/len(df)
property_df1 = property_df.pivot(index='Community Name', columns='Primary Type', values='Percentage Crime Rate').fillna(value=0).reset_index()
quality_of_life_df = new_df1[new_df1['Crime Category'] == 'QUALITY OF LIFE']
quality_of_life_df['Percentage Crime Rate'] = 100*quality_of_life_df['Crimes Count']/len(df)
quality_of_life_df1 = quality_of_life_df.pivot(index='Community Name', columns='Primary Type', values='Percentage Crime Rate').fillna(value=0).reset_index()
violent_df = new_df1[new_df1['Crime Category'] == 'VIOLENT']
violent_df['Percentage Crime Rate'] = 100*violent_df['Crimes Count']/len(df)
violent_df1 = violent_df.pivot(index='Community Name', columns='Primary Type', values='Percentage Crime Rate').fillna(value=0).reset_index()
new_combined_df = combined_df.pivot(index='Community Name', columns='Crime Category', values='Percentage Crime Rate').reset_index()

def ensure_dir(f):
    if not os.path.exists(f):
        os.makedirs(f)

date_path = dir_path+OUTPUT_FILES_RESULT_PATH+ "/%i_%i_%i" % (month, day, year)
ensure_dir(date_path)
time_path = date_path + "/%i_%i_%i" % (hour, minute, second)
ensure_dir(time_path)
analysis_folder_path = time_path + "/Chicago_Crime_Analysis_ChicagoCrimeRatesByCommunityArea:%s_%s" % (str(args.enddate),str(startdate))
ensure_dir(analysis_folder_path)
csv_file_path = analysis_folder_path + "/CSV"
ensure_dir(csv_file_path)
png_graph_path = analysis_folder_path + "/OutputGraphs"
ensure_dir(png_graph_path)

os.chdir(csv_file_path)
new_combined_df.to_csv(path_or_buf= 'CrimeByTypePerCommunityArea.csv',index =False) 
violent_df1.to_csv(path_or_buf= 'ViolentCrimePerCommunityArea.csv',index =False)
quality_of_life_df1.to_csv(path_or_buf= 'QualityOfLifeCrimePerCommunityArea.csv',index =False)
property_df1.to_csv(path_or_buf= 'PropertyCrimePerCommunityArea.csv',index =False)

os.chdir(png_graph_path)

def create_graph(dFrame,title_list,color,xlim,filename):
    sns.set(style="whitegrid")
    # Make the PairGrid
    g = sns.PairGrid(dFrame, x_vars=dFrame.columns[1:], y_vars=["Community Name"], size=12, aspect=.25)

    # Draw a dot plot using the stripplot function
    g.map(sns.stripplot, size=10, orient="h", palette= color, edgecolor="gray")

    # Use the same x axis limits on all columns and add better labels
    g.set(xlim=(0, xlim), xlabel="Percentage Crime Rate", ylabel="")

    # Use semantically meaningful titles for the columns
    titles = title_list

    for ax, title in zip(g.axes.flat, titles):
        # Set a different title for each axes
        ax.set(title=title)
         # Make the grid horizontal instead of vertical
        ax.xaxis.grid(False)
        ax.yaxis.grid(True)

    sns.despine(left=True, bottom=True)
    plt.savefig(filename, dpi=100, facecolor='w', edgecolor='w', orientation='portrait', bbox_inches='tight')

create_graph(property_df1,["ARSON", "BURGLARY", "MOTOR VEHICLE THEFT", "THEFT"],"BuGn_r",0.5,"PropertyCrimePerCommunityArea.png")
create_graph(quality_of_life_df1,['CRIMINAL DAMAGE', 'NARCOTICS', 'PROSTITUTION'],sns.cubehelix_palette(8),0.5,"QualityOfLifeCrimePerCommunityArea.png")
create_graph(violent_df1,['ASSAULT', 'BATTERY', 'CRIM SEXUAL ASSAULT', 'HOMICIDE', 'ROBBERY'],sns.color_palette("GnBu_d"),0.5,"ViolentCrimePerCommunityArea.png")
create_graph(new_combined_df,["Property Crime", "Quality of Life crime", "Violent Crime"],"Reds_r",3,"CrimeByTypePerCommunityArea.png")

os.chdir(dir_path)