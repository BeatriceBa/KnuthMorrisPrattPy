import unittest

import src.knuthMorrisPratt

class testKMP(unittest.TestCase):
    def testSearchKnuthMorrisPatternIsString(self):
        pattern = 1
        text = "text"
        with self.assertRaises(Exception):
            self.searchKnuthMorris(pattern,text)

    def testSearchKnuthMorrisTextIsString(self):
        pattern = "pattern"
        text = 1
        with self.assertRaises(Exception):
            self.searchKnuthMorris(pattern,text)
    
    def testSearchKnuthMorrisCheckEmptyString(self):
        pattern = ""
        text = "test"
        with self.assertRaises(Exception):
            self.searchKnuthMorris(pattern,text)
    
    def testcomputeLPSArrayPatternIsString(self):
        pattern = 1
        text = "text"
        with self.assertRaises(Exception):
            self.computeLPSArray(pattern)

if __name__ == '__main__':
    unittest.main()