from day5.day5lib import getBinarySeat
import unittest


class TestDay5(unittest.TestCase):
    def test_getBinarySeat(self):
        seat = getBinarySeat("FFFFFFB", 0, 127)
        self.assertEqual(seat, 1)

if __name__ == '__main__':
    unittest.main()