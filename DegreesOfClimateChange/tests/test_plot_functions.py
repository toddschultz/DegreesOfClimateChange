# -*- coding: utf-8 -*-
"""Unit test for plot_functions.py

This Python module contains multiple unit test functions to verify the
execution of the grab_noaa.py module. Tests include verifying the number
of columns, the exact column names, the data types in each column, and more.
Excceptions thrown for all failed tests.

(class) test_plot_functions
    Python class for unit testing the functions in the
    plot_functions.py module.

Written by Todd Schultz
2018
"""

from DegreesOfClimateChange.grab_berkeley import grab_berkeley
from DegreesOfClimateChange.grab_noaa import grab_noaa
from DegreesOfClimateChange.grab_worldbank import grab_worldbank
import DegreesOfClimateChange.plot_functions as pf
import unittest


df_berkeley = grab_berkeley()
df_noaa = grab_noaa()
df_wb = grab_worldbank()

class test_plot_functions(unittest.TestCase):
    """Unit tests for validating grab_noaa module."""
    
    def test_plot_each_temperature(self):
        """Test error free execution of plot_each_temperature"""
        raised = False
        try:
            hf = pf.plot_each_temperature(df_noaa, df_berkeley, df_wb)
        except:
                raised = True
        self.assertFalse(raised, 'Exception raised')
        self.assertTrue(hf)


if __name__ == '__main__':
    unittest.main()
