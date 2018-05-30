# -*- coding: utf-8 -*-
"""plot_functions various functions to create graphs of temperature data

This python module contains a multiple Python functions to create different
visualizations of the average global temperature data from the various grab
functions in this project. The are designed to have a consistent input
interface, requiring only the dataframes. The outputis only the graphs
themselves.

Syntax
import plot_functions as pf
pf.plot_function_name()

Written by Todd Schultz, Rahul Birmiwal, Abhishek Anand
2018
"""

import datetime
import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def plot_each_temperature(df_noaa, df_berkeley, df_wb):
    """plot_each_temperature plots each temperature estimate on seperate plots
    
    Create a simple line graph of the provided temperatures in the input
    dataframes where each temperature estimate source is plotted seperately
    on its own subplot axes. Each dataframe should contain only two columns
    named Data and Tanomaly_C for NOAA and Berkeley, and Date and Tabsolute_C
    for World Bank.
    
    Syntax
    plot_each_temperature(df_noaa, df_berkeley, df_wb)
    
    Inputs
    df_noaa = NOAA dataframe from grab_noaa
    df_berkeley = Berkeley dataframe from grab_berkeley
    df_wb = World Bank dataframe from grab_worldbank
    
    Output
    graph
    hf = figure handle (optional)
    """
    # Prepare data for plotting
    # NOAA Data
    tnoaa = pd.to_datetime(df_noaa['Date'])
    datesnoaa = matplotlib.dates.date2num(tnoaa)
    # Berkeley Data
    tberkeley = pd.to_datetime(df_berkeley['Date'])
    datesberkeley = matplotlib.dates.date2num(tberkeley)
    # World Bank Data
    twb = pd.to_datetime(df_wb['Date'])
    dateswb = matplotlib.dates.date2num(twb)
    
    # Find plotting limits
    datemin = min([datesnoaa.min(), datesberkeley.min(), dateswb.min()])
    datemax = max([datesnoaa.max(), datesberkeley.max(), dateswb.max()])
    datelims = [datemin, datemax]
    ymin = math.floor(min([df_noaa["Tanomaly_C"].min(),
                           df_berkeley["Tanomaly_C"].min()]))
    ymax = math.ceil(max([df_noaa["Tanomaly_C"].max(),
                          df_berkeley["Tanomaly_C"].max()]))
    yanomalylims = [ymin, ymax]
    ymin = math.floor(min([df_wb["Tabsolute_C"].min()]))
    ymax = math.ceil(max([df_wb["Tabsolute_C"].max()]))
    yabsolutelims = [ymin, ymax]
    
    # Create comparison plot
    hf = plt.figure(1)
    # Subplot 1
    plt.subplot(3, 1, 1)
    plt.plot_date(datesnoaa, df_noaa["Tanomaly_C"], color="blue",
                  linestyle='solid', marker='None')
    # plt.xlabel("Date")
    plt.ylabel("T_anomaly (deg C)")
    plt.xlim(datelims)
    plt.ylim(yanomalylims)
    plt.text(0.999*datelims[1], 0.99*yanomalylims[0], 'NOAA',
             verticalalignment='bottom', horizontalalignment='right')
    # Subplot 2
    plt.subplot(3, 1, 2)
    plt.plot_date(datesberkeley, df_berkeley["Tanomaly_C"],
                  color="blue", linestyle='solid', marker='None')
    # plt.xlabel("Date")
    plt.ylabel("T_anomaly (deg C)")
    plt.xlim(datelims)
    plt.ylim(yanomalylims)
    plt.text(0.999*datelims[1], 0.99*yanomalylims[0], 'Berkeley',
             verticalalignment='bottom', horizontalalignment='right')
    # Subplot 3
    plt.subplot(3, 1, 3)
    plt.plot_date(dateswb, df_wb["Tabsolute_C"], color="blue",
                  linestyle='solid', marker='None')
    plt.xlabel("Date")
    plt.ylabel("T_absolute (deg C)")
    plt.xlim(datelims)
    plt.ylim(yabsolutelims)
    plt.text(0.999*datelims[1], 1.005*yabsolutelims[0], 'World Bank',
             verticalalignment='bottom', horizontalalignment='right')
    return hf

# next plot function
