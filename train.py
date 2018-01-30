input_towns_string = 'AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7'

class Railroad:

    def __init__(self):
        self.routes_graph={}
    
    def build(self, input_towns_string):
        self.check_input_string(input_towns_string)
        input_towns_list = input_towns_string.split(", ")
        for e in input_towns_list:
            self.construct_graph(e)

    def construct_graph(self, input_towns_list):
        if input_towns_list[0] not in self.routes_graph:
            self.routes_graph[input_towns_list[0]] = {}
        if input_towns_list[1]:
            self.routes_graph[input_towns_list[0]][input_towns_list[1]] = {}
        if input_towns_list[2]:
            self.routes_graph[input_towns_list[0]][input_towns_list[1]] = int(input_towns_list[2])

    def calc_distance(self, route_string):
        self.build(input_towns_string)
        route_string = route_string.split("-")
        l = 0
        distance = 0
        while l != len(route_string) - 1:
#           Try important here to avoid KeyError Exception
            try:
                if route_string[l+1] in self.routes_graph[route_string[l]]:
                    distance += self.routes_graph[route_string[l]][route_string[l+1]]
                else:
                    distance = str('NO SUCH ROUTE')
                l += 1
#           KeyError appears when unknown key is inputed then capture the Exception
            except KeyError:
                distance = str('NO SUCH ROUTE')
                l += 1
        print(distance)

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
#               First character must be a letter
                elif (i == 1) and (char.isalpha() == True):
                    pass
#               Second character but be a letter
                elif (i == 2) and (char.isalpha() == True):
                    pass
#               Third character and fourth and so on can be digits (so combined are a number)
                elif ( 3 <= i <= len(input_distance)) and (char.isdigit() == True):
                    pass
                else:
                    raise Exception('first and second characters should be letters and the following a number')


    def display_all_routes(self, start, end, number_stops, method, path=[]):
        global l
        path = path + [start]
        if start not in self.routes_graph:
            return None
        for node in self.routes_graph[start]:
            if len(path) < number_stops + 1: 
                newpath = self.display_all_routes(node, end, number_stops, method, path)
                if newpath:
                    if method == '=':
                        if len(newpath) == number_stops + 1 and newpath[-1] == end: 
                            l += 1
                    else:
                        if len(newpath) < number_stops + 2 and newpath[-1] == end:
                            l += 1
        return path

    def shortest_route(self, start, end, number_stops, method, path=[]):
        global q
        path = path + [start]
        if start not in self.routes_graph:
            return None
        for node in self.routes_graph[start]:
            if len(path) < number_stops + 1:
                newpath = self.shortest_route(node, end, number_stops, method, path)
                if newpath:
                    if method == '=':
                        if len(newpath) == number_stops + 1 and newpath[-1] == end:
                            q += newpath
                    else:
                        if len(newpath) < number_stops + 2 and newpath[-1] == end:
                            q += [newpath]
        return path

    def count_number_routes(self, start, end, number_stops, method):
        global l
        l = 0
        self.display_all_routes(start, end, number_stops, method)
        print(l)
        return None

    def shortest_route_display(self, start, end, number_stops, method):
        global q
        q = []
        shortest_distance = []
        self.shortest_route(start, end, number_stops, method)
        for e in q:
            distance = 0
            for f,g in zip(e,e[1:]):
                distance += self.routes_graph[f][g]
            shortest_distance += [distance]
        shortest_distance_sorted = sorted(shortest_distance)
        print(shortest_distance_sorted[0]) 
        return None
    
    def number_different_routes(self, start, end, number_stops, method):
        global q
        q = []
        shortest_distance = []
        self.shortest_route(start, end, number_stops, method)
        for e in q:
            distance = 0
            for f,g in zip(e,e[1:]):
                distance += self.routes_graph[f][g]
            shortest_distance += [distance]
        newlist = [e for e in shortest_distance if e<30]
        print(len(newlist))
        return None


    '''
    def count_all_routes(self, start_end_string):
        self.build(input_towns_string)
        start_end_list = start_end_string.split(":")
        start_town = start_end_list[0]
        end_town = start_end_list[1]
        method = start_end_list[2]
        number_stops = int(start_end_list[3])
        count_stops = 0


        for l in range(1,len(list(self.routes_graph.keys()))+1):
            print(l)
            route = ''
            while count_stops != number_stops + 1:
                temp = self.make_connection(start_town, **self.routes_graph)
                route += temp.split("-")[0] + '-'
                start_town = temp.split("-")[1]
                count_stops += 1
#            if l < len(list(self.routes_graph.keys()))
            print(route)
            route = ''
            count_stops = 0
            print('changing start town')
            if l < len(list(self.routes_graph.keys())):
                start_town = list(self.routes_graph.keys())[l]

    def make_connection(self, start_town, **dictionary):
        for i in range(0,len(list(self.routes_graph[start_town].keys()))):
            print(list(self.routes_graph[start_town].keys())[i])
            route = start_town + '-' + list(self.routes_graph[start_town].keys())[i]
            return route    
    '''

railroad = Railroad()
route = railroad.calc_distance('A-B-C')
route = railroad.calc_distance('A-D')
route = railroad.calc_distance('A-D-C')
route = railroad.calc_distance('A-E-B-C-D')
route = railroad.calc_distance('A-E-D')
route = railroad.count_number_routes('C', 'C', 3, '<')
route = railroad.count_number_routes('A', 'C', 4, '=')
route = railroad.shortest_route_display('A', 'C', 4, '<')
route = railroad.shortest_route_display('B', 'B', 4, '<')
route = railroad.number_different_routes('C', 'C', 10, '<')
