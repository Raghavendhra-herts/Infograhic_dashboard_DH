# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 19:47:04 2023

@author: Raghavendhra Rao Devineni
"""
# importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Impact of Covid-19 Pandemic on the Global Economy
def read_covid_19_data():
    '''
    

    Returns
    -------
    data1 : pandas dataframe object
        data1 contains the covid-19 transform data available from transformed_data.csv.
        this contains the columns total_cases, total_deaths, human development index, population.
        return tranformed dataframe
    data2 : pandas dataframe object
        data2 contains the covid-19 raw data available from transformed_data.csv, as both has considered to obtain the all the information without missing any data.
        this contains the columns total_cases, total_deaths, human development index, population.
        returns raw dataframe

    '''
    # calling the csv data file paths
    # path: C:/Raghavendhra Folder(Work)/SEMESTER-2 lab/data_handling_&_visualization/infographic/
    csv_path = 'transformed_data.csv'
    raw_csv_path = 'raw_data.csv'
    
    # reading the data and calling the dataframe
    data1 = pd.read_csv(csv_path)
    data2 = pd.read_csv(raw_csv_path)
    
    #rename the columns
    data1.rename(columns = {'HDI':'Human_Development_Index', 'TC':'Total_cases', 'TD':'Total_Deaths', 'POP':'Population', 'GDPCAP':'Gdp_per_capita'}, inplace=True)
    
    # returning the data variables
    return data1, data2


def read_gdp_data():
    '''
    

    Returns
    -------
    gdp_data_before_pandemic : pandas dataframe object
        the above datafram contains the gdp_per_capita of all countries whcih helps to check the gdp before  pandemic .
        dataframe contains the columns '2018','2019' to check the data before pandemic with country column
        returns the cleaned gdp data before pandemic dataframe
    gdp_data_after_pandemic : pandas dataframe object
        the above datafram contains the gdp_per_capita of all countries whcih helps to check the gdp during pandemic .
        dataframe contains the columns '2020','2021' to check the data before pandemic with country column
        returns the cleaned gdp data during pandemic dataframe

    '''
    # calling the csv data file paths
    gdp_path = 'gdp_per_capita_(current US$).csv'
    # # reading the data and calling the dataframe
    get_gdp_data = pd.read_csv(gdp_path)
    # drop the columns
    get_gdp_data.drop(['Country Code', 'Indicator Name', 'Indicator Code'], axis =1 , inplace=True)

    # converting dataframe to other format
    gdp_data_before_pandemic = pd.melt(get_gdp_data, id_vars=['Country Name'],value_vars=['2018','2019'], var_name='Year', value_name='Gdp_per_capita').sort_values('Country Name')
    gdp_data_after_pandemic = pd.melt(get_gdp_data, id_vars=['Country Name'],value_vars=['2020','2021'], var_name='Year', value_name='Gdp_per_capita').sort_values('Country Name')

    # returning the gdp data variables
    return gdp_data_before_pandemic, gdp_data_after_pandemic


def read_goods_services_data():
    '''
    

    Returns
    -------
    service_data_before_pandemic : pandas dataframe object
        the above datafram contains the imports , exports data of all countries whcih helps to check the each country contribution before  pandemic .
        dataframe contains the columns '2018','2019' to check the data before pandemic with country column
        returns the cleaned imports_exports data before pandemic dataframe
    service_data_after_pandemic : pandas dataframe object
        the above datafram contians the imports , exports data of all countries whcih helps to check the each country contribution before  pandemic .
        dataframe contains the columns '2018','2019' to check the data before pandemic with country column
        returns the cleaned imports_exports data before pandemic dataframe

    '''
    
    # # calling the csv data file paths
    goods_path = 'Imports of goods and services (% of GDP).csv'
    # # reading the data and calling the dataframe
    goods_service_path = pd.read_csv(goods_path)
    
    # converting dataframe to other format
    service_data_before_pandemic = pd.melt(goods_service_path, id_vars=['Country Name'],value_vars=['2018','2019'], var_name='Year', value_name='Goods_and_service').sort_values('Country Name')
    service_data_after_pandemic = pd.melt(goods_service_path, id_vars=['Country Name'],value_vars=['2020','2021'], var_name='Year', value_name='Goods_and_service').sort_values('Country Name')

    # # returning the imports_exports data variables
    return service_data_before_pandemic,service_data_after_pandemic


def summarize_and_show_data(data1, data2, gdp_data_before_pandemic, gdp_data_after_pandemic, service_data_before_pandemic,service_data_after_pandemic):
    '''
    

    Parameters
    ----------
    data1 : pandas dataframe object
        data1 contains the covid-19 transform data available and this contains the columns total_cases, total_deaths, human development index, population.
    data2 : pandas dataframe object
        data2 contains the covid-19 raw data  and this contains the columns total_cases, total_deaths, human development index, population.
    gdp_data_before_pandemic : pandas dataframe object
        the above parameter contains the gdp_per_capita of all countries ,dataframe contains the columns '2018','2019' to check the data before pandemic with country column
    gdp_data_after_pandemic : pandas dataframe object
        the above parameter contains the gdp_per_capita of all countries data gdp during pandemic .
        dataframe contains the columns '2020','2021' to check the data before pandemic with country column
    service_data_before_pandemic : pandas dataframe object
        the above parameter contains the imports , exports data of all countries ,dataframe contains the columns '2018','2019' to check the data before pandemic with country column.
    service_data_after_pandemic : pandas dataframe object
        the above parameter contians the imports , exports data of all countries ,dataframe contains the columns '2018','2019' to check the data before pandemic with country column.

    Returns
    -------
    summarize_agg_data : dataframe object
        this returns the aggregated data into single dataframe by considering each dataset from above and showed into single pandas dataframe .

    '''
    # creating a new list to append the data with each country
    country_code = data1['CODE'].unique().tolist()
    country = data1['COUNTRY'].unique().tolist()
    population = data1['Population'].unique().tolist()
    gdp_before_pandemic = gdp_data_before_pandemic['Gdp_per_capita'].unique().tolist()
    gdp_pandemic = gdp_data_after_pandemic['Gdp_per_capita'].unique().tolist()
    goods_service_before_pandemic = service_data_before_pandemic['Goods_and_service'].unique().tolist()
    goods_service_pandemic = service_data_after_pandemic['Goods_and_service'].unique().tolist()
    human_development_index = []
    total_cases = []
    total_deaths = []
    
    # calling each country and sum up the total values .
    ## as the data in not same at all the levels, so dividing the necessary columns with the mode value with the comman columns
    for each_country in country:
        human_development_index.append((data1.loc[data1['COUNTRY']==each_country, 'Human_Development_Index']).sum()/294)
        total_cases.append((data2.loc[data2['location']==each_country, "total_cases"]).sum())
        total_deaths.append((data2.loc[data2['location']==each_country, "total_deaths"]).sum())
        population.append((data1.loc[data1['COUNTRY']==each_country, "Population"]).sum()/294)
        # gdp.append((data1.loc[data1['COUNTRY']==each_country, 'Gdp_per_capita']).sum())
        # goods_and_service.append((service_data.loc[service_data['Country Name']==each_country, 'Goods_and_service']).sum())
      
        gdp_before_pandemic.append((gdp_data_before_pandemic.loc[gdp_data_before_pandemic['Country Name']==each_country, 'Gdp_per_capita']).sum())
        gdp_pandemic.append((gdp_data_after_pandemic.loc[gdp_data_after_pandemic['Country Name']==each_country, 'Gdp_per_capita']).sum())
        goods_service_before_pandemic.append((service_data_before_pandemic.loc[service_data_before_pandemic['Country Name']==each_country, 'Goods_and_service']).sum())
        goods_service_pandemic.append((service_data_after_pandemic.loc[service_data_after_pandemic['Country Name']==each_country, 'Goods_and_service']).sum())

    # aggregate the global economy data into single dataframe
    summarize_agg_data = pd.DataFrame(list(zip(country_code, country, total_cases, total_deaths, human_development_index,
                                              population, gdp_before_pandemic, gdp_pandemic, goods_service_before_pandemic, goods_service_pandemic)), columns = ['Country_code', 'Country', 'Total_cases', 'Total_deaths', 
                                                                      'Human_Development_Index', 'Population', 'GDP_before_pandemic', 'GDP_during_pandemic', 'GS_before_pandemic', 'GS_during_pandemic'])
                                                                                                                                                                 
    # return the aggregated variable                                                                                                                                                                 
    return summarize_agg_data                                                                                                                                                                                       
    
                                                                                                                                                                  
def show_infographic_dashboard(gc_bar_data, gc_data, pandemic_before_imports_exports_data, pandemic_imports_exports_data):
    '''
    

    Parameters
    ----------
    gc_bar_data : dataframe object
        this contains the dataframe which shows the top five countries total_Cases and total deaths during covid-19.
    gc_data : dataframe object
        this contains the dataframe which shows the top five countries sorted by total_Cases .
    pandemic_before_imports_exports_data : pandas dataframe object
        the pandemic_before_imports_exports_data contains the aggragated data informaiton that contains all the columns in a single dataframe
    pandemic_imports_exports_data: pandas dataframe object
        the gc_agg_data contains the aggragated data informaiton that contains all the columns in a single dataframe
    

    Returns
    -------
    None.

    '''
    
    # set style for seaborn plots
    sns.set_style("darkgrid")

    # create figure and subplot gridspec
    fig = plt.figure(figsize=(15, 19), dpi = 300)
    gs = fig.add_gridspec(9, 9)
    fig.suptitle("Showing the impact of covid-19 on Gloabl Economy \n Name: Raghavendhra Rao Devineni \n Student Id: 21072747", fontsize=22)
    
    # create subplots
    ax1 = fig.add_subplot(9,2,1,)
    ax6 = fig.add_subplot(9,2,2,)
    ax2 = fig.add_subplot(9,2,5)
    ax7 = fig.add_subplot(9,2,6,)
    ax3 = fig.add_subplot(9,2,7)
    ax8 = fig.add_subplot(9,2,8,)
    ax4 = fig.add_subplot(9,2,9)
    ax9 = fig.add_subplot(9,2,10,)
    ax5 = fig.add_subplot(9,2,13)
    ax10 = fig.add_subplot(9,2,14,)
    ax11 = fig.add_subplot(9,2,16,)
    ax12 = fig.add_subplot(9,2,17,)

    # show the bar plot
    gc_bar_data.plot(kind='bar',ax=ax1)
    # add the labels, title, legend to the plot
    ax1.set_xlabel('Country' , fontsize=20)
    ax1.set_ylabel('Total_Cases',fontsize=17)
    ax1.set_title(" top 5 countries Covid_19 total cases vs total deaths \n", fontsize=20)
    # plt.legend()
    # show the value text for each country in the bar plot
    for x, (tc, td) in enumerate(zip(gc_bar_data['total_cases'] , gc_bar_data['total_deaths'])):
        ax1.text(x-0.15, tc + 20000, "{:,}".format(tc), ha='center',)
        ax1.text(x+0.15, td + 20000, "{:,}".format(td), ha='center',)
    # set the text backgroung white
    ax6.patch.set_facecolor('white')
    # remove the spines and ticks to display only text
    ax6.spines['top'].set_visible(False)
    ax6.spines['right'].set_visible(False)
    ax6.spines['bottom'].set_visible(False)
    ax6.spines['left'].set_visible(False)
    ax6.set_xticks([])
    ax6.set_yticks([])
    # add the text
    ax6.text(0.5, 0.5, 'the bar plot shows the covid-19 cases. \n Graph shows the top five countries with highest number of cases  \n and the total deaths in these countries ', ha='center', va='center', fontsize=15, color='black')
    
    # summing up total_cases
    total_cases = gc_data['Total_cases'].sum()
    # summing up total_deaths
    total_deaths = gc_data['Total_deaths'].sum()
    # summing up population
    populaiton = gc_data['Population'].sum()
    
    # creating labels
    labels= ['Overall cases', 'Total deaths']
    # calling values to show in pie chart
    values = [total_cases, total_deaths]
    # show the data in a pie chart
    ax2.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    # display the overall population value in pie chart
    ax2.text(0, 0, f"Total Population: {gc_data['Population'].sum():,} " ,ha='center', fontsize=20)
    # indication axis
    plt.axis('equal')
    # creating title
    ax2.set_title("Overall rate of cases vs death between 2020-2021 for five countries \n", fontsize=20)
    # set the text background white
    ax7.patch.set_facecolor('white')
    # remove the spines and ticks to display only text
    ax7.spines['top'].set_visible(False)
    ax7.spines['right'].set_visible(False)
    ax7.spines['bottom'].set_visible(False)
    ax7.spines['left'].set_visible(False)
    ax7.set_xticks([])
    ax7.set_yticks([])
    # adding the text
    ax7.text(0.5, 0.5, 'the pie plot shows the overall covid-19 cases. \n Percentage shows the top five countries with overall cases  \n and the overall deaths percentage in these countries ', ha='center', va='center', fontsize=15, color='black')
    


    # showing recovered cases in pie chart
    # calculating the recoverd patients from all over the country
    recovered_percentages = gc_data['recovered_cases'] / gc_data['Total_deaths'] * 100

    # calling the pie plot
    ax3.pie(recovered_percentages, labels= gc_data['Country'], autopct='%1.1f%%')
    # creating the title
    ax3.set_title("Total number of recovered cases from each countries during 2020-2021 ", fontsize=20)
    # set the text background white
    ax8.patch.set_facecolor('white')
    # remove the spines and ticks to display only text
    ax8.spines['top'].set_visible(False)
    ax8.spines['right'].set_visible(False)
    ax8.spines['bottom'].set_visible(False)
    ax8.spines['left'].set_visible(False)
    ax8.set_xticks([])
    ax8.set_yticks([])
    # adding the text
    ax8.text(0.5, 0.5, 'the pie plot shows the recovered covid-19 cases. \n Percentage shows the top five countries recovered cases.  ', ha='center', va='center', fontsize=15, color='black')
    
    
    
    # show the bar plot
    pandemic_before_imports_exports_data.plot(kind='bar', ax=ax4)
    # add the labels, title and legend to the plot
    ax4.set_xlabel("Countries", fontsize=18)
    ax4.set_ylabel("values in billions \n (2018-2020)", fontsize=14)
    ax4.set_title("showing Population, GDP, Imports & Exports for top five countries(before pandemic)",fontsize=18 )
    # set the text background white
    ax9.patch.set_facecolor('white')
    # remove the spines and ticks to display only text
    ax9.spines['top'].set_visible(False)
    ax9.spines['right'].set_visible(False)
    ax9.spines['bottom'].set_visible(False)
    ax9.spines['left'].set_visible(False)
    ax9.set_xticks([])
    ax9.set_yticks([])
    # adding the text
    ax9.text(0.5, 0.5, 'the bar graph shows the population, gdp , \n exports & imports before covid pandemic. \n data shows the top five countries data where USA,\n Brazil and Russia has highest the gdp_per_capita and \n USA and Russia maintain same level of import & exports goods. ', ha='center', va='center', fontsize=15, color='black')
    
    
    
    # # creating a bar plot 
    pandemic_imports_exports_data.plot(kind='bar', ax=ax5)
    
    # give the plot lables, title, and legend
    ax5.set_xlabel("Countries", fontsize=18)
    ax5.set_ylabel("values in billions \n (2020-2021)", fontsize=14)
    ax5.set_title("Comparing population, GDP, imports & exports by countries (during pandemic)", fontsize=18)
    # set the text background white
    ax10.patch.set_facecolor('white')
    # remove the spines and ticks to display only text
    ax10.spines['top'].set_visible(False)
    ax10.spines['right'].set_visible(False)
    ax10.spines['bottom'].set_visible(False)
    ax10.spines['left'].set_visible(False)
    ax10.set_xticks([])
    ax10.set_yticks([])
    # adding the text
    ax10.text(0.5, 0.5, 'the bar graph shows the population, gdp , \n exports & imports during covid pandemic. \n data shows the top five countries data where \n Brazil and Russia has highest gdp_per_capita during pandemic and \n USA and india has low level of import & exports goods. ', ha='center', va='center', fontsize=15, color='black')
    
    # set the text background white
    ax11.patch.set_facecolor('white')
    # remove the spines and ticks to display only text
    ax11.spines['top'].set_visible(False)
    ax11.spines['right'].set_visible(False)
    ax11.spines['bottom'].set_visible(False)
    ax11.spines['left'].set_visible(False)
    ax11.set_xticks([])
    ax11.set_yticks([])
    # adding the text
    ax11.text(0.5, 0.5, '\n\n\n\n\n\n \n\n\n\Overall Covid19 has huge impact on the global economy \n and nearly 3% of the population from top five countries with \n  highest covid cases had died during the pandemic. \n Also GDP level for many countries effected badly which\n shows impact on jobs, increase in bills, grocery over the globe.', ha='center', va='center', fontsize=15, color='black')
      
    
    # # show the plot
    # plt.show()
    
    # save the figure
    fig.savefig('21072747.png')
    

def show_covid_19_total_cases_deaths(gc_agg_data):
    '''
    

    Parameters
    ----------
    gc_agg_data : pandas dataframe object
        the gc_agg_data ocntains the aggragated data informaiton that contains all the columns in a single dataframe
    
    Returns
    -------
    gc_bar_data : dataframe object
        this returns the dataframe which shows the top five countries total_Cases and total deaths during covid-19.
    gc_data : dataframe object
        this returns the dataframe which shows the top five countries sorted by total_Cases .

    '''                                                 
    # sorting the data
    gc_data = gc_agg_data.sort_values(by=['Total_cases'], ascending=False)
    
    # creating a new column for recoverd cases
    gc_data['recovered_cases'] = gc_data['Total_cases'] - gc_data['Total_deaths'] 
    
    # selecting top-5 countries with highest cases and comparing the data
    gc_data =gc_data.head(5)
    
    # creating a new dataframe which has columns country, total_cases, total_deaths
    gc_bar_data = pd.DataFrame({"country":gc_data['Country'], "total_cases":gc_data['Total_cases'],
                                "total_deaths":gc_data['Total_deaths']})
    
    # setting the country as index
    gc_bar_data.set_index('country', inplace=True)
    
    
    
    # return the bar graph dataframe and new dataframe
    return gc_bar_data, gc_data
            
    

def show_pop_gdp_imp_exp_data(gc_data):
    '''
    

    Parameters
    ----------
    gc_agg_data : pandas dataframe object
        the gc_agg_data contains the aggragated data informaiton that contains all the columns in a single dataframe
    
    Returns
    -------
    pandemic_before_imports_exports_data : pandas dataframe object
        the pandemic_before_imports_exports_data contains the aggragated data informaiton that contains all the columns in a single dataframe
    pandemic_imports_exports_data: pandas dataframe object
        the gc_agg_data contains the aggragated data informaiton that contains all the columns in a single dataframe
    

    '''
    # comparing goods and services from countries during and after pandemic
    
    # creating a new dataframe
    pandemic_before_imports_exports_data = pd.DataFrame({"country":gc_data['Country'], 
                                                         "population":gc_data['Population'], 
                                                         "GDP":gc_data['GDP_before_pandemic']/1000,
                                                         "goods_service_before_pandemic":gc_data['GS_before_pandemic']
                                                         })
    # setting index as country
    pandemic_before_imports_exports_data.set_index('country', inplace=True)
                                                                                                                                                              
                                                                                                                                                              
    # creating a dataframe during and after pandemic
    pandemic_imports_exports_data = pd.DataFrame({"country":gc_data['Country'], "population":gc_data['Population'], "gdp_pandemic":gc_data['GDP_during_pandemic']/1000, 
                                "goods_service_pandemic":gc_data['GS_during_pandemic']})
    # setting index as country
    pandemic_imports_exports_data.set_index('country', inplace=True)
    
    
    return pandemic_before_imports_exports_data, pandemic_imports_exports_data



if __name__ == "__main__":
    
    ### read and clean the data in csv file
    
    # Data-1 Covid-19 Pandemic on the Global Economy
    data1, data2 = read_covid_19_data()
    
    # Data-2 gdp_per_capita
    gdp_data_before_pandemic, gdp_data_after_pandemic = read_gdp_data()
    
    # Data-3 Imports_ exports_during covid-19
    service_data_before_pandemic,service_data_after_pandemic = read_goods_services_data()
    
    # group all the data and aggregate into one dataframe
    summarize_agg_data = summarize_and_show_data(data1, data2, gdp_data_before_pandemic, gdp_data_after_pandemic, service_data_before_pandemic,service_data_after_pandemic)
    
    # show the data in bar graph
    gc_bar_data, gc_data =  show_covid_19_total_cases_deaths(summarize_agg_data)
    
    # display the overall percentages in pie chart
    #show_covid_19_in_pie(gc_data)
    
    # compare and show population, gdp, imports & exports during and after covid-19 cases for each country
    pandemic_before_imports_exports_data, pandemic_imports_exports_data = show_pop_gdp_imp_exp_data(gc_data)
    
    # show the data into inforgraphic dashboard
    show_infographic_dashboard(gc_bar_data, gc_data, pandemic_before_imports_exports_data, pandemic_imports_exports_data)