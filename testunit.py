import unittest
from train import *

class Test(unittest.TestCase):
    
    def setUp(self):
        self.railroad = Railroad()

    def test_calc_distance(self):
        # 5 tests to check calc_distance
        self.assertEqual(self.railroad.calc_distance('A-B-C'), 9)
        self.assertEqual(self.railroad.calc_distance('A-D'), 5)
        self.assertEqual(self.railroad.calc_distance('A-D-C'), 13)
        self.assertEqual(self.railroad.calc_distance('A-E-B-C-D'), 22)
        self.assertEqual(self.railroad.calc_distance('A-E-D'), 'NO SUCH ROUTE')

    def test_count_number_routes(self):
        # 2 tests to check number of possible routes between 2 towns
        self.assertEqual(self.railroad.count_number_routes('C', 'C', 3, '<'), 2)
        self.assertEqual(self.railroad.count_number_routes('A', 'C', 4, '='), 3)

    def test_shortest_route_display(self):
        # 2 tests to check the length of the shortest route between 2 towns
        self.assertEqual(self.railroad.shortest_route_display('A', 'C', 4, '<'), 9)
        self.assertEqual(self.railroad.shortest_route_display('B', 'B', 4, '<'), 9)

    def test_number_different_routes(self):
        # 1 test to check the number of possible routes between 2 towns
        self.assertEqual(self.railroad.number_different_routes('C', 'C', 10, '<'), 7)

if __name__ == '__main__':
    unittest.main()
