from train import *

#def setUp(self):
    #string ="AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7"
    #self.railroad = Railroad()

def test_calc_distance():
    # 5 tests to check calc_distance
	assert railroad.calc_distance('A-B-C') == 9
	assert railroad.calc_distance('A-D') == 5
	assert railroad.calc_distance('A-D-C') == 13
	assert railroad.calc_distance('A-E-B-C-D') == 22
	assert railroad.calc_distance('A-E-D') == 'NO SUCH ROUTE'

def test_count_number_routes():
    # 2 tests to check number of possible routes between 2 towns
    assert railroad.count_number_routes('C', 'C', 3, '<') == 2
    assert railroad.count_number_routes('A', 'C', 4, '=') == 3

def test_shortest_route_display():
    # 2 tests to check the length of the shortest route between 2 towns
    assert railroad.shortest_route_display('A', 'C', 4, '<')  == 9
    assert railroad.shortest_route_display('B', 'B', 4, '<') == 9

def test_number_different_routes():
    # 1 test to check the number of possible routes between 2 towns
    assert railroad.number_different_routes('C', 'C', 10, '<') == 7
