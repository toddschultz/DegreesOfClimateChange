import wbpy
import pandas as pd
import sys
import numpy as np




def grab_worldbank(select_countries=None, start_date = None, end_date = None):
    """
    ################ FIX THIS DOCSTRING #####################

    Arguments:
        select_countries (list): List of countries from which to obtain temperature data.
                                Default 'None' means obtain from all countries
        start_date (int): Starting date in yyyy integer format for the historical data.
                          Default 'None' means 1901, the earliest available year on the World Bank dataset
        end_date (int): Ending date in yyyy integer format. Default 'None' means 2015.

    Returns:
    - Pandas DataFrame:

    """

    """Argument/type checking"""
    if (  (select_countries is not None and not isinstance(select_countries,list)) or
          (start_date is not None and not isinstance(start_date,int)) or
           (end_date is not None and not isinstance(end_date, int))
        ) :
        raise ValueError("Error: Arguments are of incorrect datatype!")


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


    """Run data collections"""
    if (select_countries is not None):
        try:
            code_country_pairs = [(country_list[k],codes_list[k]) for k in range(0,len(codes_list)) if country_list[k] in select_countries]
            #country_codes = iso_codes_df['CODE']
        except Exception as e:
            print(e)
            sys.exit(0)
    else:
        code_country_pairs = [(country_list[k],codes_list[k]) for k in range(0,len(codes_list))]
    data_len = len(code_country_pairs)
    dataset = {}
    for k in range(0,data_len):
        code = code_country_pairs[k][1]
        try:
            dataset[code]=climate_api.get_instrumental(data_type='tas',interval='year',locations=[code])
        except Exception as e:
            print("Warning: Data Does Not Exist for Country Code: {}".format(code))
            # Add erroneous country to error dictionary
            err_dict[code] = 1
            continue

    """Create pandas dataframe of the data"""

    df = pd.DataFrame(columns=['Country','Code','Year','Temperature'])

    count = 0
    for k in range(0,data_len):
        c_name,c_code = code_country_pairs[k][0], code_country_pairs[k][1]
        if (c_code not in err_dict):
            country_data = dataset[c_code].as_dict()[c_code]
            for year_key in country_data.keys():
                if (int(year_key) >= start_date and int(year_key) <= end_date):
                    df.loc[count] = [c_name, c_code,year_key, country_data[year_key]]
                    count += 1
    return df


def test_output_grab_worldbank():
    """Get all data for only United States"""
    print("Get all data for only United States")
    select = ['United States']
    wb_data_df = grab_worldbank(select_countries=select)
    print(wb_data_df.head(30))
    print("------------------------------------------------------------")

    """Get all data for only United States, Burkina Faso, and Georgia"""
    print("Get all data for only United States, Burkina Faso, and Georgia")
    select = ['United States','Burkina Faso', 'Georgia']
    wb_data_df = grab_worldbank(select_countries=select)
    print(wb_data_df.head(30))
    print("------------------------------------------------------------")

    """Get only year 2000-ending date data for only United States, Burkina Faso, and Georgia"""
    print("Get only year 2000-ending date data for only United States, Burkina Faso, and Georgia")
    select = ['United States','Burkina Faso', 'Georgia']
    wb_data_df = grab_worldbank(select_countries=select, start_date = 2000)
    print(wb_data_df.head(30))
    print("------------------------------------------------------------")

    """Get only 1910-1915 date data for only United States, Burkina Faso, and Georgia"""
    print("Get only 1910-1915 date data for only United States, Burkina Faso, and Georgia")
    select = ['United States','Burkina Faso', 'Georgia']
    wb_data_df = grab_worldbank(select_countries=select, start_date = 1910, end_date=1915)
    print(wb_data_df.head(30))
    print("------------------------------------------------------------")

    """Get all data for all countries"""
    print("Get all data for all countries")
    wb_data_df = grab_worldbank()
    print(wb_data_df.tail(20))
    print("------------------------------------------------------------")

if __name__ == '__main__':
    #test_output_grab_worldbank()
