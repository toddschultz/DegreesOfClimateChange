# -*- coding: utf-8 -*-
"""
grab_berekely retrieves global average temperatures from berkeley.
Written by Abhishek Anand
2018
"""

import pandas as pd

def grab_berekely():
    url="http://berkeleyearth.lbl.gov/auto/Global/Complete_TAVG_complete.txt"
    c=pd.read_csv(url,delim_whitespace = True,index_col=None, skiprows=34, header=None, lineterminator='\n')
    c.columns = ['Year', 'Month','Monthly Anomaly','Annual Anomaly',
                'Five-year Anomaly', 'Ten-year Anomaly',
                'Twenty-year Anomaly','8','9','10','11','12']
    #print(c.head())
    c.drop(c.columns[[3,4,5,6,7,8,9,10,11]], axis=1, inplace=True)
    #print(c.head())


    # clean up dataframe
    c = c.sort_values(["Year", "Month"])
    c["Date"] = (c["Year"].astype("str") + "-" +
                        c["Month"].astype("str") + "-01")
    c["Tanomaly_C"] = c["Monthly Anomaly"]
    c.drop(c.columns[[0,1,2]], axis=1, inplace=True)
    #c = c.reset_index()
    #print(c.head())

    return c

df = grab_berekely()
print(df.head())    