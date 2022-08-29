import unittest
from funciones.suma import suma


class MyTestCase(unittest.TestCase):
    def test_suma(self):
        assert suma(2, 2) == 4


if __name__ == '__main__':
    unittest.main()
