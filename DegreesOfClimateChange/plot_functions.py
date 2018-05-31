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

def plot_each_absolute_temperature(df_noaa, df_berkeley, db_wb, do_plot, figNum):
    yearly_noaa = df_noaa.groupby(df_noaa['Date'].map(lambda x: pd.to_datetime(x).year)).mean()
    yearly_noaa = yearly_noaa.reset_index()
    yearly_noaa['Date'] = yearly_noaa['Date'].astype(str) + '-01-01' #reset Date to proper format

    yearly_ber = df_berkeley.groupby(df_berkeley['Date'].map(lambda x: pd.to_datetime(x).year)).mean()
    yearly_ber = yearly_ber.reset_index()
    yearly_ber['Date'] = yearly_ber['Date'].astype(str) + '-01-01' #reset Date to proper format

    BASELINE_TEMP = np.mean( df_wb['Tabsolute_C'])

    noaa_2_absolute = list(map(lambda x: x + BASELINE_TEMP, yearly_noaa['Tanomaly_C']))
    berkeley_2_absolute = list(map(lambda x: x + BASELINE_TEMP, yearly_ber['Tanomaly_C']))

    # Get new yearly dates
    dates_yearly_noaa = matplotlib.dates.date2num(pd.to_datetime(yearly_noaa['Date']))
    dates_yearly_ber = matplotlib.dates.date2num(pd.to_datetime(yearly_ber['Date']))
    dateswb = matplotlib.dates.date2num(pd.to_datetime(df_wb['Date']))

    if (do_plot == False):
        plot_data = {'NOAA':noaa_2_absolute, 'Berkeley':berkeley_2_absolute,
                     'WorldBank':df_wb['Tabsolute_C']
                    }
        x_linspace = {'NOAA':dates_yearly_noaa, 'Berkeley':dates_yearly_ber,
                     'WorldBank':'dateswb'
                     }
        return (plot_data, x_linspace)
    else:
        # Now plot the temperatures from the 3 sources using
        # the same units (absolute degrees Celsius)
        hf = plt.figure(figNum)
        #fig, ax1 = plt.subplots()

        color1 = 'tab:blue'
        color2 = 'tab:red'
        plt.xlabel('Date')
        plt.ylabel('Absolute Global Avg. Temp (deg C)', color=color1)
        plt.plot_date(dates_yearly_noaa, noaa_2_absolute, color=color1, label='NOAA',linestyle='solid', alpha = 0.8, marker='None')
        plt.plot_date(dates_yearly_ber, berkeley_2_absolute, color='green', label='Berkeley',alpha = 0.5, linestyle='dashed', marker='None')
        plt.plot_date(dateswb, df_wb["Tabsolute_C"], color=color2, label='WorldBank',linestyle='solid', alpha = 0.7, marker='None')
        plt.tick_params(axis='y', labelcolor=color1)
        plt.legend()

        plt.tight_layout()  # otherwise the right y-label is slightly clipped
        return hf

def plot_co2_against_temperature(df_co2, df_noaa, df_berkeley, df_wb, figNum):
    """
    def intersection(lst1, lst2):
        lst3 = [value for value in lst1 if value in lst2]
        return lst3
    """
    (temp_plot_data, x_linspace) = plot_each_absolute_temperature(df_noaa, df_berkeley, db_wb, False, 0)
    noaa_data = temp_plot_data['NOAA']
    berkeley_data = temp_plot_data['Berkeley']
    wb_data = temp_plot_data['WorldBank']

    noaa_xs = x_linspace['NOAA']
    berkeley_xs = x_linspace['Berkeley']
    wb_xs = x_linspace['WorldBank']
    co2_xs = pd.to_datetime(df_co2['Date'])

    all_dates = [noaa_xs, berkeley_xs, wb_xs, co2_xs]
    common_dates = list(reduce(set.intersection, [set(elem) for elem in all_dates ]))

    # convert to matplotlib required formatting
    dates  = matplotlib.dates.date2num(common_dates)
    # Create comparison graph
    hf = plt.figure(figNum)
    fig, ax1 = plt.subplots()

    color1 = 'tab:blue'
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Global Avg. Temperature (deg C)', color=color1)
    ax1.plot_date(dates, wb_data, color='24D3E5', label='WorldBank'linestyle='solid',alpha=0.5, marker='.')
    ax1.plot_date(dates, noaa_data, color='218EE2', label='NOAA'linestyle='solid',alpha=0.5, marker='.')
    ax1.plot_date(dates, berkeley_data, color='213CE2', label='Berkeley'linestyle='solid',alpha=0.5, marker='.')
    ax1.tick_params(axis='y', labelcolor=color1)
    ax2 = ax1.twinx()  # second axes that shares the same x-axis

    color2 = 'tab:red'
    ax2.set_ylabel('CO2 (ppm)', color=color2)
    ax2.plot_date(dates, co2_dataframe["CO2"], color=color2, linestyle='dashed', marker='o')
    ax2.tick_params(axis='y', labelcolor=color2)

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    return hf
