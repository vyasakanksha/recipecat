import unittest
from predictor import slow_predictor
from reader import recipe

class ReaderTestCase(unittest.TestCase):
    """Tests for `predictor.py`."""

    def test_slow_predictor(self):
        a = recipe(0, None, ['apple', 'cat', 'sky'])  
        b = recipe(450, None, ['boy', 'cat', 'empty']) 
        c = recipe(48, None, ['space', 'sky']) 

        cuisines = {'bunny': ['apple', 'cat', 'sky'], 'owl': ['space', 'sky']}

        o = slow_predictor([a, b, c], cuisines)
        self.assertEqual(o, [[0,'bunny'], [450, 'bunny'], [48, 'owl']])

if __name__ == '__main__':
    unittest.main()
