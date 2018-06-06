# -*- coding: utf-8 -*-
"""plot_functions various functions to create graphs of temperature data

This python module contains a multiple Python functions to create different
visualizations of the average global temperature data from the various grab
functions in this project. The are designed to have a consistent input
interface, requiring only the dataframes. The outputis only the graphs
themselves.

Syntax
import plot_functions as pf
pf.plot_function_name() --> outputs matplotlib figure to the session

Written by Todd Schultz, Rahul Birmiwal, Abhishek Anand
2018
"""

import datetime
import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from functools import reduce


def valid_plotting_dataframe(df):
    """valid_plotting_dataframe is a function to test that _df_ is a valid
       dataframe that can be used in the plot_ functions. We use this function
       because unittesting is tricky/odd-behavior when applied to
       visualizations

    Inputs:
    - df (pandas Dataframe): df is a dataframe of date, data pairs i.e
                             df -> R(Date, TempData) where Date is a String;
                                                            TempData is a Float
    Output:
        - None
    Raises:
        - ValueError if df is not a valid dataframe to plot

    """

    if (not isinstance(df, pd.DataFrame)):
        raise ValueError("Arguments must be dataframe produced by a grab_ function!")
    cols = df.columns.values
    if len(cols) != 2:
        raise ValueError("Dataframe must have 2 columns")
    if (cols[0] != 'Date'):
        raise ValueError("First column must be date column ")
    if (df[cols[1]].dtype != 'float'):
        raise ValueError("Second column must be float type ")
    return


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


def plot_all_temperature(df_noaa, df_berkeley, df_wb):
    """plot_all_temperature plots all temperature estimates on one plot

    Create a simple line graph of the provided temperatures in the input
    dataframes where all temperature estimate sources are plotted on a single
    set of plot axes. The plot contains two set of y axies to allow for the
    absolute and anomaly temperatures to be plotted together. Each dataframe
    should contain only two columns named Data and Tanomaly_C for NOAA and
    Berkeley, and Date and Tabsolute_C for World Bank.

    Syntax
    plot_all_temperature(df_noaa, df_berkeley, df_wb)

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

    # Create comparison graph
    fig, ax1 = plt.subplots()
    color1 = 'tab:blue'
    ax1.set_xlabel('Date')
    ax1.set_ylabel('T_anomaly (deg C)', color=color1)
    ax1.plot_date(datesnoaa, df_noaa["Tanomaly_C"], color=color1,
                  linestyle='solid', marker='None')
    ax1.plot_date(datesberkeley, df_berkeley["Tanomaly_C"], color='green',
                  alpha=0.5, linestyle='dashed', marker='None')
    ax1.tick_params(axis='y', labelcolor=color1)

    ax2 = ax1.twinx()  # second axes that shares the same x-axis
    color2 = 'tab:red'
    ax2.set_ylabel('T_absolute (deg C)', color=color2)
    ax2.plot_date(dateswb, df_wb["Tabsolute_C"], color=color2,
                  linestyle='solid', marker='None')
    ax2.tick_params(axis='y', labelcolor=color2)
    
    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.show()


def plot_each_absolute_temperature(df_noaa, df_berkeley, df_wb, do_plot, fig_num=None):
    """plot_each_absolute_temperature plots each agency's temperture estimates
       on a single plot, colored by agency; if the agency's data is in Anomaly
       format, then we convert to absolute temperature via by using the
       reference temperature as the mean global average temperature 1901-2012.
       This function returns a plot handle, and/or the data used to plot
       (see do_plot argument)

    Each dataframe should contain only two columns
    named Data and Tanomaly_C for NOAA and Berkeley, and Date and Tabsolute_C
    for World Bank.

    do_plot specifies whether to return the plotting (x,y) data, or to generate
    the plot fig_num, if provided, is the figure numbered in the Jupyter
    Notebook

    Syntax
    hf = plot_each_absolute_temperature(df_noaa, df_berkeley, df_wb, True, 1)
        ...generates a plot in Jupyter Notebook as Figure Number 1
    (y_data, x_data) = plot_each_absolute_temperature(df_noaa, df_berkeley,
                                                      df_wb, False)

    Inputs
    - df_noaa (Pandas Dataframe): NOAA dataframe from grab_noaa
    - df_berkeley (Pandas Dataframe): Berkeley dataframe from grab_berkeley
    - df_wb (Pandas Dataframe): World Bank dataframe from grab_worldbank
    - do_plot (boolean): True if to plot; False to return plot data
    - fig_num (int): Figure number to use in the output plotting

    Output
        if (do_plot is True), outputs
            - Graph
            - hf = figure handle (if do_plot )
        if (do_plot is False), outputs
            - (y_data, x_data) tuple where
            y_data is a Python Dictionary of {agency_name, temperature_data}
            x_data is a Python Dictionary of {agency_name, x-axis dates}

            i.e:

            y_data = {'NOAA': [0.00, -0.12, -0.13...],
                      'WorldBank': [19.002324., 18.882094., ...], etc.}
            x_data = {'WorldBank': [693961. 694326. 694691., ....],
                      'NOAA: [.....etc.]', etc.}

            That is, the _values_ in x_data are matplotlib ready dates;
            and the _values_ in y_data are respective second columns in
            the dataframes (Tabsolute_C or Tanomaly_C)

         Written By Rahul Birmiwal
    """

    # check efficacy of arguments
    [valid_plotting_dataframe(elem) for elem in [df_noaa, df_berkeley, df_wb]]

    # annualize the data
    yearly_noaa = df_noaa.groupby(df_noaa['Date'].map(lambda x: pd.to_datetime(x).year)).mean()
    yearly_noaa = yearly_noaa.reset_index()
    yearly_noaa['Date'] = yearly_noaa['Date'].astype(str) + '-01-01' #reset Date to proper format

    yearly_ber = df_berkeley.groupby(df_berkeley['Date'].map(lambda x: pd.to_datetime(x).year)).mean()
    yearly_ber = yearly_ber.reset_index()
    yearly_ber['Date'] = yearly_ber['Date'].astype(str) + '-01-01' #reset Date to proper format

    # baseline temperature for conversion
    baseline_temp = np.mean(df_wb['Tabsolute_C'])

    # convert Anomaly data to Absolute
    noaa_2_absolute = list(map(lambda x: x + baseline_temp, yearly_noaa['Tanomaly_C']))
    berkeley_2_absolute = list(map(lambda x: x + baseline_temp, yearly_ber['Tanomaly_C']))

    # Get new yearly dates
    dates_yearly_noaa = matplotlib.dates.date2num(pd.to_datetime(yearly_noaa['Date']))
    dates_yearly_ber = matplotlib.dates.date2num(pd.to_datetime(yearly_ber['Date']))
    dateswb = matplotlib.dates.date2num(pd.to_datetime(df_wb['Date']))

    if (not do_plot):
        plot_data = {'NOAA':noaa_2_absolute, 'Berkeley':berkeley_2_absolute, 'WorldBank':df_wb['Tabsolute_C']}
        x_linspace = {'NOAA':dates_yearly_noaa, 'Berkeley':dates_yearly_ber, 'WorldBank':dateswb}
        return (plot_data, x_linspace)
    else:
        # Now plot the temperatures from the 3 sources using
        # the same units (absolute degrees Celsius)
        if (fig_num is None):
            fig_num = 0
        hf = plt.figure(fig_num)

        color1 = 'tab:blue'
        color2 = 'tab:red'
        plt.xlabel('Date')
        plt.ylabel('Absolute Global Avg. Temp (deg C)', color=color1)
        plt.plot_date(dates_yearly_noaa, noaa_2_absolute, color=color1, label='NOAA', linestyle='solid', alpha = 0.8, marker='None')
        plt.plot_date(dates_yearly_ber, berkeley_2_absolute, color='green', label='Berkeley', alpha=0.5, linestyle='dashed', marker='None')
        plt.plot_date(dateswb, df_wb["Tabsolute_C"], color=color2, label='WorldBank', linestyle='solid', alpha=0.7, marker='None')
        plt.tick_params(axis='y', labelcolor=color1)
        plt.legend()
        plt.tight_layout()  # otherwise the right y-label is slightly clipped
        return hf


def plot_co2_against_temperature(df_co2, df_noaa, df_berkeley, df_wb, fig_num):
    """plot_co2plot_co2_against_temperature plots the aforementioned absolute
       global avg. temperature from our agencies, as well as CO2 data from the
       Scripps Institute of Oceanography, on the same plot

      do_plot specifies whether to return the plotting (x,y) data, or to
      generate the plot fig_num, if provided, is the figure numbered in the
      Jupyter Notebook

      Syntax
      >>> plot_each_absolute_temperature(df_noaa, df_berkeley, df_wb, 4)

      Arguments
      - df_noaa (Pandas Dataframe): NOAA dataframe from grab_noaa
      - df_berkeley (Pandas Dataframe): Berkeley dataframe from grab_berkeley
      - df_wb (Pandas Dataframe): World Bank dataframe from grab_worldbank
      - do_plot (boolean): True if to plot; False to return plot data
      - fig_num (int): Figure number to use in the output plotting

      Returns
      - None

      Outputs
      - matplotlib graph of that described above

      Written By Rahul Birmiwal
    """
    # argument checking for CO2 dataframe
    valid_plotting_dataframe(df_co2)

    # Get the data source dictionary and their respective x-axes
    (data_dict, axes_dict) = plot_each_absolute_temperature(df_noaa, df_berkeley, df_wb, False, 0)
    co2_data = df_co2["CO2"] #store CO2 in this dictionary
    data_dict['Scripps'] = co2_data #add co2 data to the 'data source dictionary'

    co2_xs = matplotlib.dates.date2num(pd.to_datetime(df_co2['Date']))
    axes_dict['Scripps'] = co2_xs #likewise for the x-axes

    # compute the common dates across all data sources
    common_dates = np.asarray(list(map(int, (list(reduce(lambda x, y: x&y, [set(xs) for xs in axes_dict.values()]))))), dtype=float)

    # sort them in chronological order for plotting
    common_dates = np.sort(common_dates)

    # get the data correspondong to _common_dates_, and restore in data dictionary
    for agency_name, data in data_dict.items():
        mask = np.isin(axes_dict[agency_name], common_dates)
        masked_data = [data[i] for i in range(len(data)) if mask[i]]
        data_dict[agency_name] = masked_data

    # Create comparison graph
    fig, ax1 = plt.subplots()
    with plt.style.context('Solarize_Light2'):
        color1 = 'tab:blue'
        ax1.set_xlabel('Date')
        ax1.set_ylabel('Global Avg. Temperature (deg C)')
        ax1.plot_date(common_dates, data_dict['WorldBank'], label='WorldBank',linestyle=':', color=color1, alpha=0.4, marker=None)
        ax1.plot_date(common_dates, data_dict['NOAA'], label='NOAA',linestyle='-', color=color1, alpha=0.4, marker=None)
        ax1.plot_date(common_dates, data_dict['Berkeley'], label='Berkeley',linestyle='-.', color=color1, alpha=0.4, marker=None)
        ax1.tick_params(axis='y')
        ax1.legend()
        ax2 = ax1.twinx()  # second axes that shares the same x-axis

        color2 = 'tab:red'
        ax2.set_ylabel('CO2 (ppm)')
        ax2.plot_date(common_dates, data_dict['Scripps'], color=color2, label='CO2', linewidth=2.0, linestyle='solid', marker=None)
        ax2.tick_params(axis='y')

        fig.tight_layout()  # otherwise the right y-label is slightly clipped
        ax2.legend(loc=3)

        plt.show()
