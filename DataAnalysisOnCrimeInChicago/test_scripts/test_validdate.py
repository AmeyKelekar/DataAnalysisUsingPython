### Execute this test case using following command:
### "python -m test_scripts.test_validdate" from a directory above test_scripts 

import unittest
from datetime import datetime

from Chicago_Crime_DataCollection import valid_date

class MyTest(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(valid_date("2016-11-01"), datetime(2016, 11, 1, 0, 0))

    def test_notequal(self):
    	self.assertNotEqual(valid_date("2016-11-01"), '2016-01-11')

if __name__ == '__main__':
	unittest.main()