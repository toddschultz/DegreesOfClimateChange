# -*- coding: utf-8 -*-
"""grab_noaa retrieves global average temperatures from NOAA.

This python module contains a single function, grab_temperatures_NOAA, that
retrieves the global average temperature estimets from NOAA. This is the
climate data that is used to evaluate global climate change.

An overview of the data access available from NOAA is at:
https://www.ncdc.noaa.gov/data-access

The documentation for the NOAA RESTful Web Services v2 API is at:
https://www.ncdc.noaa.gov/cdo-web/webservices/v2

Reference documents from NOAA can be found at:
ftp://ftp.ncdc.noaa.gov/pub/data/noaa/

Instructions for obtaining an API key:
1. Go to <https://www.ncdc.noaa.gov/cdo-web/token> and
   submit a token request.
2. Open the "NOAAtokenTemplate.txt" file and enter the email
   address used to obtain the NOAA API token and the token
   itself into the second line of the file.
3. Save the file as "NOAAtoken.txt" in the same directory with
   the template file and the python module.

Written by Todd Schultz
2018
"""

import datetime
import pandas as pd
import requests


def grab_temperatures_noaa():
    """Retrieves global average temperatures from NOAA."""
    
    # NOAA Global average temperature time series
    start_year = 1880
    this_year = datetime.datetime.now().year
    base_url = "https://www.ncdc.noaa.gov/cag/global/time-series/globe/land_ocean/1/"
    end_url = "/" + str(start_year) + "-" + str(this_year) + ".csv"
    header_skip = [0, 1, 2, 3]
    df_noaa = pd.DataFrame(columns=['Year', 'Value', 'Month'])
    
    for imonth in range(1, 13):
        month = str(imonth)
        noaa_url = base_url + month + end_url
        data_df = pd.read_csv(noaa_url, skiprows=header_skip)
        data_df["Month"] = imonth
        df_noaa = df_noaa.append(data_df)
        
    # check length of dataframe
    assert (df_noaa.shape[0] >= (this_year - start_year)*12), \
           "Error retrieving data, not enough rows"
    
    # clean up dataframe
    df_noaa = df_noaa.sort_values(["Year","Month"])
    df_noaa["Date"] = df_noaa["Year"].astype("str") + "-" + df_noaa["Month"].astype("str") + "-01"
    df_noaa["Tanomaly_C"] = df_noaa["Value"]
    df_noaa = df_noaa.reset_index()
    df_noaa = df_noaa.drop(columns=["Year", "Value", "Month", "index"])
    
    return df_noaa
