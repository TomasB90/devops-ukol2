import unittest
from skript import scitani

class TestScitani(unittest.TestCase):
    def test_scitani(self):
        self.assertEqual(scitani(2, 3), 5)

if __name__ == '__main__':
    unittest.main()
