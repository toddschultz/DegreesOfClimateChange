"""Unit test for grab_noaa.py

This Python module contains multiple unit test functions to verify the
execution of the grab_naoo.py module. Tests include verifying the number 
of columns, the exact column names, the data types in each column, and more.
Excceptions thrown for all failed tests.

(class) grab_noaa_UnitTests
    Python class for unit testing the Python function 
    grab_temperatures_noaa() in the  grab_noaa.py module.
Written by Todd Schultz
2018
"""
import unittest
import os
import grab_noaa

PATHNAME = '.'


class grab_naoo_UnitTests(unittest.TestCase):
    """Unit tests for validating grab_noaa module."""

    def test_column_names(self):
        """Test for exact 2 required column names.
        The required names are Date and Tanomaly_C"""
        df_test = grab_noaa.grab_temperatures_noaa()
        # if we test for the number of columns to match the number of exact
        #    column names, and that we have at least one column of each of the
        #    required names then we can conclude that we have only the exact
        #    columns required
        pass_test = True
        known_names = ('Date', 'Tanomaly_C')
        pass_test = pass_test & (df_test.shape[1] == len(known_names))
        col_names = df_test.columns

        def is_valid_column(cnames, testcname):
            """Test if column names are a member of the required names."""
            isvalid = False
            for x_column in enumerate(cnames):
                isvalid = isvalid | (x_column[1] == testcname)
            return isvalid

        for y_known_column in enumerate(known_names):
            pass_test = pass_test & (is_valid_column(
                col_names, y_known_column[1]))
        self.assertTrue(pass_test)

    def test_key_columns(self):
        """Test if 'video_id' and 'language' is a key."""
        data_table_test = hw3.create_dataframe(PATHNAME)
        teststr = (data_table_test['video_id'].map(str)
                   + data_table_test['language'])
        self.assertTrue(teststr.nunique() == data_table_test.shape[0])

    def test_invalid_path(self):
        """Test that ValueError exception thrown for invalid path."""
        invalidpath = os.path.join('.', 'no', 'path', 'should',
                                   'be', 'named', 'this')
        with self.assertRaises(ValueError):
            hw3.create_dataframe(invalidpath)


if __name__ == '__main__':
    unittest.main()
