# -*- coding: utf-8 -*-
"""grab_noaa retrieves global average temperatures from NOAA.

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
    Doc String
    """
    url = "http://berkeleyearth.lbl.gov/auto/Global/Complete_TAVG_complete.txt"
    df = pd.read_csv(url, delim_whitespace=True, index_col=None, skiprows=34, header=None, lineterminator='\n')
    df.columns = ['Year', 'Month', 'Monthly Anomaly', 'Annual Anomaly', 'Five-year Anomaly', 'Ten-year Anomaly', 'Twenty-year Anomaly', '8', '9', '10', '11', '12']
    df.drop(df.columns[[3, 4, 5, 6, 7, 8, 9, 10, 11]], axis=1, inplace=True)
    # clean up dataframe
    # df = df.sort_values(["Year", "Month"])
    df["Date"] = (df["Year"].astype("str") + "-" + df["Month"].astype("str") + "-01")
    df["Tanomaly_C"] = df["Monthly Anomaly"]
    df.drop(df.columns[[0, 1, 2]], axis=1, inplace=True)

    return df

#df_Berekely = grab_berekely()
#print(df_Berekely.head())
