import day11.day11lib as lib
import unittest


class TestDay11(unittest.TestCase):
    def test_getOccupiedSeatInDirection(self):
        seats = []
        seats.append(list("..."))
        seats.append(list(".L."))
        seats.append(list("..."))

        lib.setSeats(seats)
        count = lib.getOccupiedSeatInDirection(1,1,0,1)
        self.assertEqual(count, 0)
        count = lib.getOccupiedSeatInDirection(1,1,1,0)
        self.assertEqual(count, 0)
        count = lib.getOccupiedSeatInDirection(1,1,1,1)
        self.assertEqual(count, 0)
        count = lib.getOccupiedSeatInDirection(1,1,0,-1)
        self.assertEqual(count, 0)
        count = lib.getOccupiedSeatInDirection(1,1,-1,0)
        self.assertEqual(count, 0)
        count = lib.getOccupiedSeatInDirection(1,1,-1,-1)
        self.assertEqual(count, 0)
        count = lib.getOccupiedSeatInDirection(1,1,-1,1)
        self.assertEqual(count, 0)
        count = lib.getOccupiedSeatInDirection(1,1,1,-1)
        self.assertEqual(count, 0)

        seats = []
        seats.append(list("###"))
        seats.append(list("#L#"))
        seats.append(list("###"))

        lib.setSeats(seats)
        count = lib.getOccupiedSeatInDirection(1,1,0,1)
        self.assertEqual(count, 1)
        count = lib.getOccupiedSeatInDirection(1,1,1,0)
        self.assertEqual(count, 1)
        count = lib.getOccupiedSeatInDirection(1,1,1,1)
        self.assertEqual(count, 1)
        count = lib.getOccupiedSeatInDirection(1,1,0,-1)
        self.assertEqual(count, 1)
        count = lib.getOccupiedSeatInDirection(1,1,-1,0)
        self.assertEqual(count, 1)
        count = lib.getOccupiedSeatInDirection(1,1,-1,-1)
        self.assertEqual(count, 1)
        count = lib.getOccupiedSeatInDirection(1,1,-1,1)
        self.assertEqual(count, 1)
        count = lib.getOccupiedSeatInDirection(1,1,1,-1)
        self.assertEqual(count, 1)

        seats = []
        seats.append(list("............."))
        seats.append(list(".L.L.#.#.#.#."))
        seats.append(list("............."))

        lib.setSeats(seats)
        count = lib.getOccupiedSeatInDirection(1,1,0,1)
        self.assertEqual(count, 0)

    def test_getOccupiedVisualSeats(self):
        seats = []
        seats.append(list("..."))
        seats.append(list(".L."))
        seats.append(list("..."))

        lib.setSeats(seats)
        
        lib.setSeats(seats)
        count = lib.getOccupiedVisualSeats(1,1)
        self.assertEqual(count,0)
        
        seats = []
        seats.append(list("###"))
        seats.append(list("#L#"))
        seats.append(list("###"))

        lib.setSeats(seats)
        count = lib.getOccupiedVisualSeats(1,1)
        self.assertEqual(count,8)

if __name__ == '__main__':
    unittest.main()