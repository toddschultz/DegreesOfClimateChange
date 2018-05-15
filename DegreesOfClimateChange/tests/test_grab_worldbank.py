
import sys
from grab_worldbank import grab_worldbank
import unittest
import datetime



class TestGrabWorldbank(unittest.TestCase):
    min_year = 1901
    max_year = 2015
    def test_arguments(self):

        self.assertRaises(ValueError, grab_worldbank, 'foo','baz')
        self.assertRaises(ValueError, grab_worldbank, '','baz')
        self.assertRaises(ValueError, grab_worldbank, 'foo','')
        self.assertRaises(ValueError, grab_worldbank, '1901','2015')
        self.assertRaises(ValueError, grab_worldbank, '$&', None)
        self.assertRaises(ValueError, grab_worldbank, None,'$&')
        self.assertRaises(ValueError, grab_worldbank, -TestGrabWorldbank.min_year, TestGrabWorldbank.max_year)
        self.assertRaises(ValueError, grab_worldbank, TestGrabWorldbank.min_year, -TestGrabWorldbank.max_year)
        self.assertRaises(ValueError, grab_worldbank, 0,0)
        self.assertRaises(ValueError, grab_worldbank, None, datetime.datetime.now().year)

if __name__ == '__main__':
    unittest.main()

