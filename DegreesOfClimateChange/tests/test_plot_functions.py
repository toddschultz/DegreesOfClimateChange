"""Unit test for plot_functions.py

This Python module contains multiple unit test functions
to check if the plotting functions in plot_functions.py
return valid x and y axes 'handles'. For example in
plot_each_absolute_temperature(), if do_plot is set to False, we return
two dictionaries: one, a dictionary of <agency_name, x_linspace> pairs
where agency_name is NOAA, Berkeley, or WorldBank, and x_linspace
is a valid numerical x-axis that could be used for matplotlib.

The other dictionary is the analog for the y axis

Note we test only the 'data' used in plotting, not the
visualizations themselves

In particular, we test that the returned tuple of x,y axes 'dictionaries'
are valid sets for plotting. We also test that if there are invalid args
to plot_each_absolute_temperature, that it throws a ValueError

(class) TestPlotFunctions
    Python class for unit testing the Python functions in
    plot_functions.py

Written by Rahul Birmiwal
2018
"""



import sys
sys.path.append("..") # Adds higher directory to python modules path.
from DegreesOfClimateChange.plot_functions import plot_each_absolute_temperature
from DegreesOfClimateChange.plot_functions import plot_co2_against_temperature
from DegreesOfClimateChange.grab_worldbank import grab_worldbank
from DegreesOfClimateChange.grab_berkeley import grab_berkeley
from DegreesOfClimateChange.grab_noaa import grab_noaa
from DegreesOfClimateChange.grab_co2_scripps import grab_scripps_co2_data
import unittest
import datetime
import warnings
import pandas as pd


def raises_error(*args, **kwds):
    raise ValueError('Invalid value: %s%s' % (args, kwds))

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


class TestPlotFunctions(unittest.TestCase):
    """ Unit tests for validating plot_functions.py module"""

    # Override super class init, so we can define an instance
    # attribute for grab_worldbank() and cache the computations...
    def __init__(self, *args, **kwargs):
        super(TestPlotFunctions, self).__init__(*args, **kwargs)
        self.df_wb = grab_worldbank(2009, 2010) # arbitrary dates chosen in
                                                # tight range for speed
        self.df_noaa = grab_noaa()
        self.db_berkeley = grab_berkeley()
        self.df_co2 = grab_scripps_co2_data()

    @ignore_warnings
    def setUp(self):
        """ natively called by the Python unittesting framework """
        print('In setUp()')

        # dataframes used in plotting
        df_noaa = self.df_noaa
        df_berkeley = self.db_berkeley
        df_worldbank = self.df_wb # using the cached dataframe
        df_co2 = self.df_co2
        # Define the testing unit
        (self.ydata, self.xdata) = plot_each_absolute_temperature(df_noaa,
                                    df_berkeley, df_worldbank, do_plot=False,
                                    fig_num=None)
        (self.ydata_wco2, self.xdata_wco2) = plot_co2_against_temperature(
                                    df_co2, df_noaa,
                                    df_berkeley, df_worldbank, do_plot=False,
                                    fig_num=0)





    @ignore_warnings
    def test_valueError(self):
        """ test_valueError tests that plot_each_absolute_temperature propagates
        a ValueError if one of the corresponding argument that was expected to
        be a Pandas DataFrame, was not a pandas dataframe
        """
        try:
            # Testing plot_each_absolute_temperature
            raises_error(plot_each_absolute_temperature(None, None, None,
                                            False, None))
            raises_error(plot_each_absolute_temperature(pd.DataFrame(), None, None,
                                            False, None))
            raises_error(plot_each_absolute_temperature(None, pd.DataFrame(), None,
                                            False, None))
            raises_error(plot_each_absolute_temperature(None, None, pd.DataFrame(),
                                            False, None))


            # Testing plot_co2_against_temperature
            raises_error(plot_co2_against_temperature(None, None, None, None))
            raises_error(plot_co2_against_temperature(None, pd.DataFrame(), None, None))
            raises_error(plot_co2_against_temperature(None, None, pd.DataFrame(), None))
            raises_error(plot_co2_against_temperature(None, None, None, pd.DataFrame()))


        except ValueError:
            pass
        else:
            self.fail('Did not see ValueError')


    @ignore_warnings
    def test_x_axis(self):
        """test_x_axis tests that the x-axes returned by
        plot_each_absolute_temperature is a valid set of axes"""

        self.assertIsInstance(self.xdata, dict)
        keys = list(self.xdata.keys())
        keys.sort()

        # test that the correct agency names are in the x-axis dictionary
        # and we only have our three main data sources
        self.assertTrue(keys[0] == 'Berkeley')
        self.assertTrue(keys[1] == 'NOAA')
        self.assertTrue(keys[2] == 'WorldBank')
        self.assertTrue(len(keys) == 3)

        vals = self.xdata.values()
        # test that each agency_name points to a list of numeric values
        # that could be used on the x-axis
        for v in vals:
            self.assertTrue(all(isinstance(elem, int) for elem in v) or
                            all(isinstance(elem, float) for elem in v))


    @ignore_warnings
    def test_y_axis(self):
        """test_y_axis tests that the y-axes returned by
        plot_each_absolute_temperature is a valid set of axes"""

        self.assertIsInstance(self.ydata, dict)
        keys = list(self.ydata.keys())
        keys.sort()

        # test that the correct agency names are in the x-axis dictionary
        # and we only have our three main data sources
        self.assertTrue(keys[0] == 'Berkeley')
        self.assertTrue(keys[1] == 'NOAA')
        self.assertTrue(keys[2] == 'WorldBank')
        self.assertTrue(len(keys) == 3)

        vals = self.ydata.values()
        # test that each agency_name points to a list of numeric values
        # that could be used on the x-axis
        for v in vals:
            self.assertTrue(all(isinstance(elem, int) for elem in v) or
                            all(isinstance(elem, float) for elem in v))

    @ignore_warnings
    def test_y_axis_co2plot(self):
        """test_y_axis_co2plot tests that the y-axes returned by
        plot_co2_against_temperature is a valid set of axes"""

        self.assertIsInstance(self.ydata_wco2, dict)
        keys = list(self.ydata_wco2.keys())
        keys.sort()

        # test that the correct agency names are in the x-axis dictionary
        # and we only have our three main data sources
        self.assertTrue(keys[0] == 'Berkeley')
        self.assertTrue(keys[1] == 'NOAA')
        self.assertTrue(keys[1] == 'Scripps')
        self.assertTrue(keys[3] == 'WorldBank')
        self.assertTrue(len(keys) == 4)

        vals = self.ydata_wco2.values()
        # test that each agency_name points to a list of numeric values
        # that could be used on the x-axis
        for v in vals:
            self.assertTrue(all(isinstance(elem, int) for elem in v) or
                            all(isinstance(elem, float) for elem in v))


    @ignore_warnings
    def test_x_axis_co2plot(self):
        """test_x_axis_co2plot tests that the x-axes returned by
        plot_co2_against_temperature is a valid set of axes"""

        self.assertIsInstance(self.xdata_wco2, dict)
        keys = list(self.xdata_wco2.keys())
        keys.sort()

        # test that the correct agency names are in the x-axis dictionary
        # and we only have our three main data sources
        self.assertTrue(keys[0] == 'Berkeley')
        self.assertTrue(keys[1] == 'NOAA')
        self.assertTrue(keys[1] == 'Scripps')
        self.assertTrue(keys[3] == 'WorldBank')
        self.assertTrue(len(keys) == 4)

        vals = self.xdata_wco2.values()
        # test that each agency_name points to a list of numeric values
        # that could be used on the x-axis
        for v in vals:
            self.assertTrue(all(isinstance(elem, int) for elem in v) or
                            all(isinstance(elem, float) for elem in v))


    def tearDown(self):
        """ natively called by the Python unittesting framework """
        print('In tearDown()')
        del self.xdata
        del self.ydata
        del self.ydata_wco2
        del self.xdata_wco2

if __name__ == '__main__':
    unittest.main()
