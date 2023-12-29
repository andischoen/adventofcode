import day23.day23lib as lib
import unittest


class TestDay23(unittest.TestCase):
    def test_get_possible_dest(self):

        #0123456789012
         #############
         #.C.C.......#
         ###.#.#.#.###
           #.#.#.#.#  
           #########  
        map = dict()
        map[(2,1)] = lib.Amphipod('C')
        map[(4,1)] = lib.Amphipod('C')
        
        cave = lib.Cave(map, 0, list())
        dest = cave.get_possible_dest((2,1))
        self.assertEqual(dest, [])

        dest = cave.get_possible_dest((4,1))
        self.assertEqual(dest, [(7,3)])

    def test_done(self):
        #0123456789012
         #...........#
         ###A#B#C#D###
           #A#B#C#D#  
           #########  
        map = dict()
        map[(3,2)] = lib.Amphipod('A')
        map[(3,3)] = lib.Amphipod('A')
        
        map[(5,2)] = lib.Amphipod('B')
        map[(5,3)] = lib.Amphipod('B')
        
        map[(7,2)] = lib.Amphipod('C')
        map[(7,3)] = lib.Amphipod('C')
        
        map[(9,3)] = lib.Amphipod('D')
        map[(10,1)] = lib.Amphipod('D')
        
        cave = lib.Cave(map, 0, list())

        done = cave.is_done()
        self.assertEqual(done, False)

        cave.map[(9,2)] = lib.Amphipod('D')
        cave.map.pop((10,1)) 
        done = cave.is_done()
        self.assertEqual(done, True)

    def test_possible_movers(self):
       #0123456789012 
        #.C........C#
        ###A#B#.#D###
          #A#B#.#D#
          #########
        map = dict()
        map[(3,2)] = lib.Amphipod('A')
        map[(3,3)] = lib.Amphipod('A')
        
        map[(5,2)] = lib.Amphipod('B')
        map[(5,3)] = lib.Amphipod('B')
        
        map[(2,1)] = lib.Amphipod('C')
        map[(11,1)] = lib.Amphipod('C')
        
        map[(9,2)] = lib.Amphipod('D')
        map[(9,3)] = lib.Amphipod('D')
        
        cave = lib.Cave(map, 0, list())

        movers = cave.get_possible_movers()
        self.assertListEqual(movers, [(2,1),(11,1)])
        

if __name__ == '__main__':
    unittest.main()