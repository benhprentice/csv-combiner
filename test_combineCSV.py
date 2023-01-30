import unittest  
from combineCSV import combineCsv

class TestCSVcombine(unittest.TestCase):

    def testIfNull(self):
        files = combineCsv(None)
        self.assertIsNone(files, 'There are no files to concatenate.')

if __name__ == '__main__':
    unittest.main()
