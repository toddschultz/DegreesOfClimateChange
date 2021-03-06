# -*- coding: utf-8 -*-
"""grab_berkeley retrieves global average temperatures from Berekeley Earth.

This python module contains a single function, grab_berekely, that
retrieves the global average temperature anomaly estimates from Berekely. This
is the climate data that is used to evaluate global climate change.

Syntax
import grab_berekely
df_berekely = grab_berekely.grab_berekely()

An overview of the data access available from Berkeley Earth is at:
http://berkeleyearth.lbl.gov/auto/Global/Raw_TAVG_complete.txt

The data is provided as a delimited, plain text webpage that can be easily
read by various text interpreters. This module uses the Pandas package and
the Pandas.read_csv function to retrieve the data into a Pandas DataFrame.

Written by Abhishek Anand
2018
"""


import pandas as pd


def grab_berkeley():
    """
    Returns a dataframe of (Date, Tanomaly_C) tuples with data
    from the Berkeley Earth.
    Note: Temperatures are in Celsius and reported as anomalies
            relative to the Jan 1951-Dec 1980 average.
            Estimated Jan 1951-Dec 1980 absolute temperature (C): 8.64

    Args:
        None
    Returns:
        pandas dataframe: Dataframe pointing to the temperature measurement
                          on monthly basis
    Examples:
        >>> df_Berekely = grab_berkeley()
        >>>  print(df_Berekely.head())
                    Date  Tanomaly_C
            0  1750-1-01       0.382
            1  1750-2-01       0.539
            2  1750-3-01       0.574
            3  1750-4-01       0.382
            4  1750-5-01         NaN
    """
    url = "http://berkeleyearth.lbl.gov/auto/Global/Complete_TAVG_complete.txt"
    df_berkeley = pd.read_csv(url, delim_whitespace=True, index_col=None,
                              skiprows=34, header=None, lineterminator='\n')
    df_berkeley.columns = ['Year', 'Month', 'Monthly Anomaly',
                           'Annual Anomaly', 'Five-year Anomaly',
                           'Ten-year Anomaly', 'Twenty-year Anomaly',
                           '8', '9', '10', '11', '12']
    df_berkeley.drop(df_berkeley.columns[[3, 4, 5, 6, 7, 8, 9, 10, 11]],
                     axis=1, inplace=True)
    # clean up dataframe
    df_berkeley["Date"] = (df_berkeley["Year"].astype("str") + "-" +
                           df_berkeley["Month"].astype("str") + "-01")
    df_berkeley["Tanomaly_C"] = df_berkeley["Monthly Anomaly"]
    df_berkeley.drop(df_berkeley.columns[[0, 1, 2]], axis=1, inplace=True)

    return df_berkeley
