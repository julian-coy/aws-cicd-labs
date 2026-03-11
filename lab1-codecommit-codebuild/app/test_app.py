import unittest
from app import suma, resta

class TestApp(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)

    def test_resta(self):
        self.assertEqual(resta(5, 2), 3)

if __name__ == "__main__":
    unittest.main()
