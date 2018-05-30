# -*- coding: utf-8 -*-
"""plot_functions.py various functions to create visualizations of temperature data

This python module contains a multiple Python functions to create different visualizations
of the average global temperature data from the various grab functions in this project. The
are designed to have a consistent input interface, requiring only the dataframes. The output
is only the graphs themselves. 

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

def plot_each_temperature(df_noaa, df_berkeley, df_worldbank):
