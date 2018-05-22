"""
Unit test for grab_berkeley.py
This Python module contains multiple unit test functions to verify the
execution of the grab_berkeley.py module. Tests include verifying the number
of columns, the exact column names, the data types in each column, and more.
Excceptions thrown for all failed tests.
(class) grab_berkeley.py
    Python class for unit testing the Python function
    grab_noaa() in the  grab_berkeley.py module.

Written by Abhishek Anand

2018
"""

import sys
sys.path.append("../")
from DegreesOfClimateChange.grab_berkeley import grab_berkeley
import unittest


dfberkeley = grab_berkeley()

class test_grab_berkeley(unittest.TestCase):
    """Unit tests for validating grab_berkeleymodule."""

    def test_checkRowSize(self):
        """Check Row Size  with at least 12"""
        self.assertTrue(dfberkeley.shape[0] >= 12)

    def test_checkColumnSize(self):
        """Check Row Size """
        self.assertTrue(dfberkeley.shape[1] == 2)
    
    def test_checkColumnName(self):
        """Check if column Names are 'Date', 'Tanomaly_C' """
        self.assertTrue(set(['Date', 'Tanomaly_C']).issubset(set(list(dfberkeley))))
        
    def test_datatypes(self):
        """Test that column Date is a string data type
        A string in Pandas is actually an object."""
        self.assertTrue(dfberkeley["Date"].dtypes == 'O')
        self.assertTrue(dfberkeley["Tanomaly_C"].dtype == 'float')


if __name__ == '__main__':
    unittest.main()
