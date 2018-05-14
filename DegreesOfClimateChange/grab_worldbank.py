import wbpy
import pandas as pd
import sys
import numpy as np


import wbpy
import pandas as pd
import sys
import numpy as np




def grab_worldbank(start_date = None, end_date = None):
    """
    ################ FIX THIS DOCSTRING #####################
    Note: NEED to install wbpy <------- **
    - wbpy: https://github.com/mattduck/wbpy.
        * _not an official Python library for the world bank, but is well documented/used, and handles all the intricacies of interfacing with the World Bank RESTFUL API.
        * Our project will appropriately unittest any and all functions incorporating the wbpy library.

    Arguments:
        start_date (int): Starting date in yyyy integer format for the historical data.
                          Default 'None' means 1901, the earliest available year on the World Bank dataset
        end_date (int): Ending date in yyyy integer format. Default 'None' means 2015.

    Returns:
        pandas dataframe: Columns are (Year, Mean Temperature)

    """

    if (end_date is not None and end_date > 2015):
        raise ValueError("Error: Starting date cannot exceed 2015")

    if (start_date is None):
        start_date = 1901
    if (end_date is None):
        end_date = 2015

    """Dictionary to store countries who do NOT HAVE DATA"""
    err_dict = {}

    """Instantiate API Interface using wbpy package"""
    climate_api = wbpy.ClimateAPI()

    """Obtain ISO country codes for ALL countries in the world"""
    iso_df = pd.read_csv('https://raw.githubusercontent.com/datasets/country-codes/master/data/country-codes.csv',
                  delimiter=',')
    codes_list = np.array(iso_df['ISO3166-1-Alpha-3'])#i.e. [..., DEU, GHA, GIB,...]
    country_list = np.array(iso_df['official_name_en'])#i.e. [...Germany, Ghana, Gibraltar, ...]


    """
        Create a 'temporary' _dataset_ of (country, year, average annual temperature) triples.
        To do this, we will need to use the climate_api.get_instrumental() wrapper function,
        and store the wrapper results into a dictionary called _dataset_
    """
    code_country_pairs = [(country_list[k],codes_list[k]) for k in range(0,len(codes_list))]
    dataset = {}
    for k in range(0,len(code_country_pairs)):
        code = code_country_pairs[k][1]
        try:
            dataset[code]=climate_api.get_instrumental(data_type='tas',interval='year',locations=[code])
        except Exception as e:
            print("Warning: Data Does Not Exist for Country Code: {}".format(code))
            # Add erroneous country to error dictionary
            err_dict[code] = 1
            continue

    """
        Create a pandas dataframe from the dataset dictionary
        by parsing the content of the calls to climate_api.get_instrumental(), stored in dataset
    """
    df = pd.DataFrame(columns=['Country','Year','Temperature'])
    count = 0
    #For all countries
    for k in range(0,len(code_country_pairs)):
        c_name,c_code = code_country_pairs[k][0], code_country_pairs[k][1]

        #if is a valid country
        if (c_code not in err_dict):

            #convert the get_instrumental() content to dictionary and access it's
            # 'subdictionary' using the appropriate country code
            country_data = dataset[c_code].as_dict()[c_code]

            #for all years that are in the valid time window
            for year_key in country_data.keys():
                if (int(year_key) >= start_date and int(year_key) <= end_date):
                    #Append to dataframe
                    df.loc[count] = [c_name,int(year_key), country_data[year_key]]
                    count += 1

    """
        At this point, df points to a relation df -> R(Country, Year, Temperature).
        Since we need to return global average temperature, we compute the mean of all
        countries per given year, and store the results in a new dataframe
    """

    temp_and_year_df = df.groupby(df['Year']).mean()
    return temp_and_year_df




def test_output_grab_worldbank():
    """Get global average temperature across all countries worldwide, for
    1901-2015"""
    print("Print getting data")
    wb_data_df = grab_worldbank()
    print("Now printing (Year, AverageTemperature) tuples ")
    print(wb_data_df.head())
    print("------------------------------------------------------------")
    print(wb_data_df.tail())

if __name__ == '__main__':
    test_output_grab_worldbank()
