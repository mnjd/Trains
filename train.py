#from gui import GraphicalInterface
#from tkinter import *

input_towns_string = 'AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7'

class Railroad:

    def __init__(self):
        '''
        Initialisation with definition of:
        _ a dictionary: routes_graph
        _ an int counting the number of routes between two towns
        _ a list containing possible routes between two towns.
        '''
        self.routes_graph = {}
        self.number_routes = 0
        self.possible_routes = []

    def calc_distance(self, route_string):
        '''
        Method to calculate distance between two towns.
        '''
        self.build(input_towns_string)
        # Input is given as 'A-B-C'
        route_string = route_string.split("-")
        counter = 0
        distance = 0
        # len(route_string) - 1 is the definition of number of stops
        number_stops = len(route_string) - 1
        while counter != number_stops:
        # Try/Except important here to avoid KeyError Exception.
            try:
                if route_string[counter+1] in self.routes_graph[route_string[counter]]:
                    distance += self.routes_graph[route_string[counter]][route_string[counter+1]]
                else:
                    distance = str('NO SUCH ROUTE')
                counter += 1
                # KeyError appears when non-existing key in the graph is inputed.
            except KeyError:
                distance = str('NO SUCH ROUTE')
                counter += 1
        return(distance)

    def build(self, input_towns_string):
        '''
        Method to check the input given to create the graph with "check_input_string method" 
        and calls "construct_graph" method to create the dictionary containing the graph.
        '''
        self.check_input_string(input_towns_string)
        input_towns_list = input_towns_string.split(", ")
        for e in input_towns_list:
            self.construct_graph(e)

    def check_input_string(self, string_distance):
        input_towns_list = string_distance.split(", ")
        length_input = len(input_towns_list)
        for l in range(0, length_input):
            input_distance = input_towns_list[l]
            i = 0
            for char in input_distance:
                i += 1
                if (len(input_distance) < 3):
                    raise Exception('input distance format should be at least 3 characters')
                # First character must be a letter
                elif (i == 1) and (char.isalpha() == True):
                    pass
                # Second character but be a letter
                elif (i == 2) and (char.isalpha() == True):
                    pass
                # Third character and fourth and so on can be digits (so combined are a number)
                elif ( 3 <= i <= len(input_distance)) and (char.isdigit() == True):
                    pass
                else:
                    raise Exception('first and second characters should be letters and the following a number')

    def construct_graph(self, input_towns_list):
        '''
        Method to construct the graph.
        '''
        # If starting town is not in the graph add it.
        if input_towns_list[0] not in self.routes_graph:
            self.routes_graph[input_towns_list[0]] = {}
        # Town connected to starting one is added to graph
        if input_towns_list[1]:
            self.routes_graph[input_towns_list[0]][input_towns_list[1]] = {}
        # Distance between the 2 towns is added to the graph. 
        if input_towns_list[2]:
            self.routes_graph[input_towns_list[0]][input_towns_list[1]] = int(input_towns_list[2:])

    def display_all_routes(self, start, end, number_stops, method, path=[]):
        '''
        Method to display all possible routes given the starting, ending town 
        and maximum number of stops. We check with variable method that we need 
        a maxmimum number of stops "<" or exactly a number of stops "=".
        '''
        path = path + [start]
        # "If" important here to display "0" if starting town is not in the graph
        if start not in self.routes_graph:
            return None
        for node in self.routes_graph[start]:
            # Check if we have made enough steps
            if len(path) < number_stops + 1:
                newpath = self.display_all_routes(node, end, number_stops, method, path)
                if newpath:
                    # We want exactly a given number of stops.
                    if method == '=':
                        if len(newpath) == number_stops + 1 and newpath[-1] == end:
                            self.number_routes += 1
                            self.possible_routes += newpath
                    # We want a maximum number of stops.
                    else:
                        if len(newpath) < number_stops + 2 and newpath[-1] == end:
                            self.number_routes += 1
                            self.possible_routes += [newpath]
        # Returning path is important as this method is recursively called.
        return path

    def count_number_routes(self, start, end, number_stops, method):
        '''
        Method calling the main method (display_all_routes) and outputing the number of routes.
        '''
        self.build(input_towns_string)
        self.number_routes = 0
        self.display_all_routes(start, end, number_stops, method)
        return self.number_routes

    def shortest_route_display(self, start, end, number_stops, method):
        '''
        Method calling the main method (display_all_routes) and for all possible
        routes computing the total distance between starting and ending towns.
        '''
        self.build(input_towns_string)
        self.possible_routes = []
        all_distances = []
        self.display_all_routes(start, end, number_stops, method)
        # For each route of the list
        for e in self.possible_routes:
            distance = 0
            # This is a way to select AB, BC, CD
            for f,g in zip(e,e[1:]):
                # Compute the distance for each couple using the graph
                distance += self.routes_graph[f][g]
            # Save distances in a list
            all_distances += [distance]
        # Sort distances 
        all_distances.sort()
        # Shortest distance is the first one.
        shortest_distance = all_distances[0]
        return shortest_distance

    def number_different_routes(self, start, end, number_stops, method):
        '''
        Method calling the main method (display_all_routes) and counting the number
        of different routes having a length smaller than 30.
        '''
        self.build(input_towns_string)
        self.possible_routes = []
        all_distances = []
        self.display_all_routes(start, end, number_stops, method)
        for e in self.possible_routes:
            distance = 0
            for f,g in zip(e,e[1:]):
                distance += self.routes_graph[f][g]
            all_distances += [distance]
        # We use here the index correspondance between possible.routes and all_distances.
        newlist = [e for e in all_distances if e<30]
        return len(newlist)

railroad = Railroad()
#root = Tk()
#gui = GraphicalInterface(root)
#root.mainloop()
#string = gui.entry_user()

if __name__ == "__main__":
    print(railroad.calc_distance('A-B-C'))
    print(railroad.calc_distance('A-D'))
    print(railroad.calc_distance('A-D-C'))
    print(railroad.calc_distance('A-E-B-C-D'))
    print(railroad.calc_distance('A-E-D'))
    print(railroad.count_number_routes('C', 'C', 3, '<'))
    print(railroad.count_number_routes('A', 'C', 4, '='))
    print(railroad.shortest_route_display('A', 'C', 4, '<'))
    print(railroad.shortest_route_display('B', 'B', 4, '<'))
    print(railroad.number_different_routes('C', 'C', 10, '<'))
