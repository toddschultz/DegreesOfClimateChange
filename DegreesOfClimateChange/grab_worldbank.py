import wbpy
import pandas as pd
import sys
import numpy as np




def grab_worldbank(select_countries=None, start_date = None, end_date = None):
    """
    ################ FIX THIS DOCSTRING #####################
    Note: NEED to install wbpy <------- **
    - wbpy: https://github.com/mattduck/wbpy.
        * _not an official Python library for the world bank, but is well documented/used, and handles all the intricacies of interfacing with the World Bank RESTFUL API.
        * Our project will appropriately unittest any and all functions incorporating the wbpy library.

    Arguments:
        select_countries (list): List of countries from which to obtain temperature data.
                                Default 'None' means obtain from all countries
        start_date (int): Starting date in yyyy integer format for the historical data.
                          Default 'None' means 1901, the earliest available year on the World Bank dataset
        end_date (int): Ending date in yyyy integer format. Default 'None' means 2015.

    Returns:
    - Pandas DataFrame:

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

    """Read in country codes from World Bank website"""
    iso_codes_df = pd.read_csv('country_iso_codes.csv').dropna()
    codes_list = np.array(iso_codes_df['CODE'])
    country_list = np.array(iso_codes_df['COUNTRY'])

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

    """Create pandas dataframe of the data"""
    df = pd.DataFrame(columns=['Country','Year','Temperature'])

    count = 0
    for k in range(0,len(code_country_pairs)):
        c_name,c_code = code_country_pairs[k][0], code_country_pairs[k][1]
        if (c_code not in err_dict):
            country_data = dataset[c_code].as_dict()[c_code]
            for year_key in country_data.keys():
                if (int(year_key) >= start_date and int(year_key) <= end_date):
                    df.loc[count] = [c_name,int(year_key), country_data[year_key]]
                    count += 1



    temp_and_year_df = df.groupby(df['Year'])
    return temp_and_year_df


def test_output_grab_worldbank():
    """Get all data for all countries"""
    print("Get all data for all countries")
    wb_data_df = grab_worldbank()
    print(wb_data_df.tail(20))
    print("------------------------------------------------------------")

if __name__ == '__main__':
    test_output_grab_worldbank()
