
import sys
import grab_worldbank as grab_worldbank
import unittest
import datetime
import warnings


def ignore_warnings(test_func):
    """Decorator to ignore specific warnings during unittesting"""

    def do_test(self, *args, **kwargs):
        with warnings.catch_warnings():

            """File I/O is known to raise ResourceWarning in unittest so ignore it"""
            warnings.simplefilter("ignore", ResourceWarning)
            test_func(self, *args, **kwargs)
    return do_test


class TestGrabWorldbank(unittest.TestCase):
    min_year = grab_worldbank.MIN_YEAR
    max_year = grab_worldbank.MAX_YEAR

    @ignore_warnings
    def setUp(self):
        print('In setUp()')
        self.fixture = grab_worldbank.grab_worldbank(2010,2012)


    @ignore_warnings
    def test_column_names(self):
        colnames = list(self.fixture.columns.values)
        self.assertTrue(len(colnames) == 2)
        self.assertTrue(colnames[0] == 'Date')
        self.assertTrue(colnames[1] == 'Tabsolute_C')

    @ignore_warnings
    def test_arguments(self):
        self.assertRaises(ValueError, grab_worldbank.grab_worldbank, 'foo','baz')
        self.assertRaises(ValueError, grab_worldbank.grab_worldbank, '','baz')
        self.assertRaises(ValueError, grab_worldbank.grab_worldbank, 'foo','')
        self.assertRaises(ValueError, grab_worldbank.grab_worldbank, '1901','2012')
        self.assertRaises(ValueError, grab_worldbank.grab_worldbank, '$&', None)
        self.assertRaises(ValueError, grab_worldbank.grab_worldbank, None,'$&')
        self.assertRaises(ValueError, grab_worldbank.grab_worldbank, -TestGrabWorldbank.min_year, TestGrabWorldbank.max_year)
        self.assertRaises(ValueError, grab_worldbank.grab_worldbank, TestGrabWorldbank.min_year, -TestGrabWorldbank.max_year)
        self.assertRaises(ValueError, grab_worldbank.grab_worldbank, 0,0)
        self.assertRaises(ValueError, grab_worldbank.grab_worldbank, None, datetime.datetime.now().year)

    def tearDown(self):
        print('In tearDown()')
        del self.fixture

if __name__ == '__main__':
    unittest.main()
