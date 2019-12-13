import unittest

from sample import add

class SampleTest(unittest.TestCase):

    def test_add_integers(self):
        result = add(3, 5)
        self.assertEquals(8, result)

if __name__ == "__main__":
    unittest.main()