import unittest
from reader import init_data, build_cuisines, recipe

class ReaderTestCase(unittest.TestCase):
    """Tests for `reader.py`."""

    def test_build_cuisines(self):
        a = recipe(0, 'sweet', ['apple', 'cat', 'sky'])  
        b = recipe(450, 'this', ['boy', 'sky', 'empty']) 
        c, i = build_cuisines([a, b])
        self.assertEqual(c.keys(), ['this', 'sweet'])
        self.assertEqual(set(i), set(['apple', 'cat', 'sky', 'boy', 'empty']))

        self.assertNotEqual(i, ['apple', 'cat', 'sky', 'boy', 'sky', 'empty'])

if __name__ == '__main__':
    unittest.main()
