"""Unit test for grab_worldbank.py

This Python module contains multiple unit test functions to verify the
execution of the grab_worldbank.py module. Tests include verifying the number
of columns, the exact column names, the data types in each column. Furthermore,
this testing module ensures that exception handling of arguments to grab_worldbank()
is done correctly, and raises approrpriate errors if need be.

(class) test_grab_noaa
    Python class for unit testing the Python function
    grab_worldbank(arg1, arg2) in the  grab_worldbank.py module.

Written by Rahul Birmiwal
2018
"""


import sys
sys.path.append("..") # Adds higher directory to python modules path.
from DegreesOfClimateChange.grab_worldbank import grab_worldbank
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


class TestGrabWorldbank(unittest.TestCase):
    """ Unit tests for validating grab_worldbank.py module"""

    min_year = grab_worldbank.MIN_YEAR
    max_year = grab_worldbank.MAX_YEAR

    @ignore_warnings
    def setUp(self):
        """ natively called by the Python unittesting framework """
        print('In setUp()')
        self.fixture = grab_worldbank.grab_worldbank(2010,2012)

    @ignore_warnings
    def test_datatypes(self):
        """Test that column Date is a string data type
        A string in Pandas is actually an object."""
        self.assertTrue(self.fixture["Date"].dtypes == 'O')
        self.assertTrue(self.fixture["Tabsolute_C"].dtype == 'float')

    @ignore_warnings
    def test_column_names(self):
        """Test for exact 2 required column names.
        The required names are Date and Tabsolute_C"""
        #    Note: The WorldBank gives temperature averages in ABSOLUTE degrees
        #    if we test for the number of columns to match the number of exact
        #    column names, and that we have at least one column of each of the
        #    required names then we can conclude that we have only the exact
        #    columns required
        colnames = list(self.fixture.columns.values)
        self.assertTrue(len(colnames) == 2)
        self.assertTrue(colnames[0] == 'Date')
        self.assertTrue(colnames[1] == 'Tabsolute_C')

    @ignore_warnings
    def test_arguments(self):
        """ Various tests to ensure various forms of user-input to
            grab_worldbank(arg1, arg2) is appropriately handledself.

            The following cases are handled in this order:
            1) arbitrary string arguments
            2) blank arg1
            3) blank arg2
            4) arg1, arg2 are 'valid' dates passed incorrectly as strings
            5) arg2 is None/Null
            6) arg1 is None/Null
            7) arg1 accidentally negative, but otherwise valid
            8) arg2 is accidentally negative, but otherwise valid
            9) arg2 is the 'Current Time' of the computer, which is invalid
                            because exceeds the year 2012
        """

        self.assertRaises(ValueError, grab_worldbank.grab_worldbank, 'foo', 'baz')
        self.assertRaises(ValueError, grab_worldbank.grab_worldbank, '', 'baz')
        self.assertRaises(ValueError, grab_worldbank.grab_worldbank, 'foo', '')
        self.assertRaises(ValueError, grab_worldbank.grab_worldbank, '1901', '2012')
        self.assertRaises(ValueError, grab_worldbank.grab_worldbank, '$&', None)
        self.assertRaises(ValueError, grab_worldbank.grab_worldbank, None, '$&')
        self.assertRaises(ValueError, grab_worldbank.grab_worldbank, -TestGrabWorldbank.min_year, TestGrabWorldbank.max_year)
        self.assertRaises(ValueError, grab_worldbank.grab_worldbank, TestGrabWorldbank.min_year, -TestGrabWorldbank.max_year)
        self.assertRaises(ValueError, grab_worldbank.grab_worldbank, 0, 0)
        self.assertRaises(ValueError, grab_worldbank.grab_worldbank, None, datetime.datetime.now().year)

    def tearDown(self):
        """ natively called by the Python unittesting framework """
        print('In tearDown()')
        del self.fixture

if __name__ == '__main__':
    unittest.main()
