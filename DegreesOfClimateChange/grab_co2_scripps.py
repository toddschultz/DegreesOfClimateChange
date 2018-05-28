# -*- coding: utf-8 -*-
"""grab_co2_scripps retrieves carbon dioxide (CO2) measurements in
   parts-per-million (ppm) from various measurement sites sanctioned
   by Scripps Institute of Oceanography at the University of California, San Diego

   The Scripps CO2 program was initiated in 1956 by Charles David Keeling,
   an American scientist whose research measuring CO2 levels at the
   Moana Loa observatory, Hawaii, is considered the first real 'alert'
   to the world of the consequences of greenhouse gases and high CO2 levels and
   its affects on (detrimental) climate changeself.

   This function pulls data from various sampling stations of the Scripps Institute

   ALERT, NWT, CANADA
   LA JOLLA, CA, USA
   CHRISTMAS ISLAND, AUSTRALIA
   AMERICAN SAMOA
   SOUTH POLE, ANTARCTICA

http://scrippsco2.ucsd.edu/data/atmospheric_co2/sampling_stations

This python module contains a single function, grab_co2_scripps().
This is the climate data that is used to evaluate global climate change.
CO2 measurements are computed per annum from various geographic locations
dating back to the mid-late 20th century (exact start date varies from site-to-site)

Usage:

    function usage is then simple:
    >>> df = grab_co2_scripps()

Output:
    Relation/Dataframe -> R(Date, CO2 (ppm)),
    where 'CO2 (ppm)' is the average CO2 measurement averaged across the sampling
           stations defined above

Dependencies:
    numpy
    pandas

Written by Rahul Birmiwal
2018
"""

import numpy as np
import pandas as pd


def grab_scripps_co2_data():
    """Returns a dataframe of (Year, Mean CO2 Level (ppm)) tuples with data
       from the Scripps Institute sampling stations.
       Note: Scripps uses the mnemonic '-99.99' to represent missing data!!

    Args:
        None
    Returns:
        pandas dataframe: Dataframe pointing to the CO2 measurement per annum
    Examples:
        >>> df = grab_co2_scripps()
        >>> print(df.head())
                  Date         CO2
        0   1957-01-01  313.625000
        1   1958-01-01  314.706667
        2   1959-01-01  315.635000
        3   1960-01-01  316.616667
        4   1961-01-01  317.387500
        5   1962-01-01  317.364444
    """
    # url links to data
    links = ['http://scrippsco2.ucsd.edu/assets/data/atmospheric/stations/flask_co2/monthly/monthly_flask_co2_alt.csv',
            'http://scrippsco2.ucsd.edu/assets/data/atmospheric/stations/flask_co2/monthly/monthly_flask_co2_ljo.csv',
            'http://scrippsco2.ucsd.edu/assets/data/atmospheric/stations/flask_isotopic/monthly/monthly_flask_c13_chr.csv',
            'http://scrippsco2.ucsd.edu/assets/data/atmospheric/stations/flask_co2/monthly/monthly_flask_co2_sam.csv',
            'http://scrippsco2.ucsd.edu/assets/data/atmospheric/stations/merged_in_situ_and_flask/monthly/monthly_merge_co2_spo.csv']

    # labels
    locations = ['Alert_CAN','LaJolla_USA','ChristmasIsland_AUS','AmericanSamoa_ASM','SouthPole_ANT']

    # dataframe to store results
    master_df = pd.DataFrame(dtype=float)
    count = 0
    for link in links:
        station_df = pd.read_csv(link,comment = '"',delimiter=",",header=None) #read in a dataframe for _this_ station

        #Add column denoting _this_ substation location
        station_df['Location'] = locations[count]
        count += 1

        #only get the columns we care about...
        station_df = station_df.iloc[:,[0,4,10]]
        master_df = master_df.append(station_df)

    master_df = master_df.iloc[5:] #get rid of garbage at the top of the frame
    master_df.columns = ['Date', 'CO2', 'Location'] #rename columns
    master_df = master_df[master_df.Date.apply(lambda x: x.isnumeric())] #get rid of non-numeric Dates
    master_df['Date'] = pd.to_numeric(master_df['Date']) #convert Date column to numeric
    master_df['CO2'] = pd.to_numeric(master_df['CO2']) #convert CO2 col to numeric
    master_df = master_df[master_df.CO2 != -99.99] #remove missing values
    master_df = master_df[master_df.Date != -99.99] #remove missing values

    # Average by year across all locations
    master_df = master_df.groupby('Date').mean()
    master_df = master_df.reset_index() #convert dataframe back to two columns

    ### Convert DATE columns to yyyy-mm-dd format!
    master_df['Date'] = master_df['Date'].astype(str) + '-01-01'
    return master_df

if __name__ == '__main__':
    df = grab_scripps_co2_data()
    print(df.head(30))
