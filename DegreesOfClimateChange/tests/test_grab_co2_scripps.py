"""Unit test for grab_co2_scripps.py

This Python module contains multiple unit test functions to verify the
execution of the grab_co2_scripps.py module. Tests include verifying the number
of columns, the exact column names, the data types in each column. Furthermore,
this testing module ensures that exception handling of arguments to grab_co2_scripps()
is done correctly, and raises approrpriate errors if need be.

(class) TestGrab_CO2_Scripps
    Python class for unit testing the Python function
    grab_co2_scripps() in the  grab_co2_scripps.py module.

Written by Rahul Birmiwal
2018
"""

import sys
sys.path.append("..") # Adds higher directory to python modules path.
from DegreesOfClimateChange.grab_co2_scripps import grab_scripps_co2_data
#from grab_co2_scripps import grab_scripps_co2_data
import unittest
import datetime
import warnings


def ignore_warnings(test_func):
    """Decorator to ignore specific warnings during unittesting"""

    """
    Returns:
        do_test: The input function 'test_func' in decorated form to
                 approrpriately handle resource warnings
    """
    def do_test(self, *args, **kwargs):
        with warnings.catch_warnings():
            """File I/O is known to raise ResourceWarning in
            unittest so ignore it"""
            warnings.simplefilter("ignore", ResourceWarning)
            test_func(self, *args, **kwargs)
    return do_test


class TestGrab_CO2_Scripps(unittest.TestCase):
    """ Unit tests for validating grab_co2_scripps.py module"""

    @ignore_warnings
    def setUp(self):
        """ natively called by the Python unittesting framework """
        print('In setUp()')
        self.fixture = grab_scripps_co2_data()

    @ignore_warnings
    def test_datatypes(self):
        """Test that column Date is a string data type
        A string in Pandas is actually an object."""
        self.assertTrue(self.fixture["Date"].dtypes == 'O')
        self.assertTrue(self.fixture["CO2"].dtype == 'float')

    @ignore_warnings
    def test_column_names(self):
        """Test for exact 2 required column names.
        The required names are Date and Tabsolute_C"""
        #    if we test for the number of columns to match the number of exact
        #    column names, and that we have at least one column of each of the
        #    required names then we can conclude that we have only the exact
        #    columns required
        colnames = list(self.fixture.columns.values)
        self.assertTrue(len(colnames) == 2)
        self.assertTrue(colnames[0] == 'Date')
        self.assertTrue(colnames[1] == 'CO2')

    @ignore_warnings
    def test_valid_data(self):
        """Test that the CO2 data present 'makes sense', i.e
           the CO2 levels in ppm are all positive, an issue
           that could have arisen due to the mnemonic of -99.99
           for missing values """
        self.assertTrue( (self.fixture['CO2'] > 0).all() )

    def tearDown(self):
        """ natively called by the Python unittesting framework """
        print('In tearDown()')
        del self.fixture

if __name__ == '__main__':
    unittest.main()
