import unittest  
from readCSV import readCsv

class TestCSVreader(unittest.TestCase):

    def testNotNone(self):
        CSV = readCsv()
        self.assertIsNotNone(CSV, 'There are files to concatenate.')

if __name__ == '__main__':
    unittest.main()

