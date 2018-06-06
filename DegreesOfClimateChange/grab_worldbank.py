# -*- coding: utf-8 -*-
"""grab_worldbank retrieves global average temperatures from the Worldbank
https://data.worldbank.org/topic/climate-change

This python module contains a single function, grab_worldbank, that
retrieves the global average temperature estimates from the Worldbank dataset
(Celsius). This is the climate data that is used to evaluate global climate
change. Global averages are computed using yearly data from all countries on
earth between the years 1901 and 2012.

Usage:
    To use, one will need to install the 'wbpy' Python packageself.
    https://github.com/mattduck/wbpy
    'wbpy' is the recommended directly by the WorldBank as a wrapper library
    to access its databases. It supports and ensures clean, correct
    data access, as well as legacy ISO country code formats
    Install via any standard method, i.e.:
        pip install wbpy

    function usage is then simple:
    >>> df = grab_worldbank()

Dependencies:
    wbpy
    numpy
    pandas

Written by Rahul Birmiwal
2018
"""


import wbpy
import pandas as pd
import sys
import numpy as np


MIN_YEAR = 1901  # constant defining minimum year value in WorldBank dataset
MAX_YEAR = 2012  # likewise maximum


def grab_worldbank(start_date=1901, end_date=2012):
    """Returns a dataframe of (Year, GlobalAverageTemperature) tuples with data
       from the WorldBank database.
       https://data.worldbank.org/topic/climate-change
    Args:
        start_date (int): Starting year for data retrieval; minimum 1901.
                          Defaults to 1901
        end_date (int): End year for data retrieval; maximum 2012.
                        Defaults to 2012
    Returns:
        pandas dataframe: Dataframe pointing to the results from the worldbank
                          Columns are of type Date (yyyy-mm-dd string);
                          Tabsolute_C (float)
                          NOTE: January 1st chosen as a dummy month-date
                                for each year
    Examples:
        >>> df = grab_worldbank()
        >>> print(df.head())
           Date          Tabsolute_C
        0  1901-01-01    19.002034
        1  1902-01-01    18.882094
        2  1903-01-01    18.925365
        3  1904-01-01    18.835930
        4  1905-01-01    18.877793

        >>> df = grab_worldbank(2011,2012)
        >>> print(df.head())
           Date  Tabsolute_C
        0  2011-01-01    19.002201
        1  2012-01-01    19.026535

    """
    if (start_date is not None and not isinstance(start_date, int) or
        end_date is not None and not isinstance(end_date, int)):
        raise ValueError("Error: Invalid argument type. Must be integer")
        sys.exit(0)
    if (start_date is not None and (start_date < MIN_YEAR or start_date > MAX_YEAR)):
        raise ValueError("Error: Starting date cannot precede 1901")
        sys.exit(0)
    if (end_date is not None and (end_date > MAX_YEAR or end_date < MIN_YEAR)):
        raise ValueError("Error: Ending date cannot exceed 2012")
        sys.exit(0)

    """Dictionary to store countries who do NOT HAVE DATA"""
    err_dict = {}

    """Instantiate API Interface using wbpy package"""
    climate_api = wbpy.ClimateAPI()

    """Obtain ISO country codes for ALL countries in the world"""
    iso_df = pd.read_csv('https://raw.githubusercontent.com/datasets/country-codes/master/data/country-codes.csv',
                         delimiter=',')
    codes_list = np.array(iso_df['ISO3166-1-Alpha-3'])  # i.e. [DEU, GHA, GIB,...]
    country_list = np.array(iso_df['official_name_en'])  # i.e. [Germany, Ghana, Gibraltar, ...]

    codes_list = list(filter(lambda v: v == v, codes_list))
    country_list = list(filter(lambda v: v == v, country_list))

    """
        Create a 'temporary' _dataset_ of (country, year, average annual
        temperature) triples. To do this, we will need to use the
        climate_api.get_instrumental() wrapper function,
        and store the wrapper results into a dictionary called _dataset_
    """
    code_country_pairs = [(country_list[k],codes_list[k]) for k in range(0,len(codes_list))]
    dataset = {}
    for k in range(0, len(code_country_pairs)):
        code = code_country_pairs[k][1]
        try:
            dataset[code] = climate_api.get_instrumental(data_type='tas',
                                             interval='year', locations=[code])
        except Exception as e:
            print("Warning: Data Does Not Exist for Country Code: {}".format(code))
            # Add erroneous country to error dictionary
            err_dict[code] = 1
            continue

    """
        Create a pandas dataframe from the dataset dictionary
        by parsing the content of the calls to climate_api.get_instrumental(),
        stored in dataset
    """
    df = pd.DataFrame(columns=['Country', 'Date', 'Tabsolute_C'])
    count = 0
    # For all countries
    for k in range(0, len(code_country_pairs)):
        c_name, c_code = code_country_pairs[k][0], code_country_pairs[k][1]

        # if is a valid country
        if (c_code not in err_dict):

            # convert the get_instrumental() content to dictionary and access 
            # it's 'subdictionary' using the appropriate country code
            country_data = dataset[c_code].as_dict()[c_code]

            # for all years that are in the valid time window
            for year_key in country_data.keys():
                if (int(year_key) >= start_date and int(year_key) <= end_date):
                    # Append to dataframe
                    df.loc[count] = [c_name,int(year_key), country_data[year_key]]
                    count += 1

    """
        At this point, df points to a relation df -> R(Country, Year,
        Temperature). Since we need to return global average temperature,
        we compute the mean of all countries per given year, and store the
        results in a new dataframe
    """
    print(".......computing worldwide averages across all years...hang on!!!")
    df_worldbank = df.groupby(df['Date']).mean()
    df_worldbank = df_worldbank.reset_index()

    # Convert DATE columns to yyyy-mm-dd format!
    df_worldbank['Date'] = df['Date'].astype(str) + '-01-01'

    return df_worldbank


if __name__ == '__main__':
    df = grab_worldbank(2011, 2012)
    print(df.head())
