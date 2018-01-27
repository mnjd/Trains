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
        railroad = Railroad()
        if input_towns_list[0] not in self.routes_graph:
            self.routes_graph[input_towns_list[0]] = {}
        if input_towns_list[1]:
            self.routes_graph[input_towns_list[0]][input_towns_list[1]] = {}
        if input_towns_list[2]:
            self.routes_graph[input_towns_list[0]][input_towns_list[1]] = int(input_towns_list[2])

    def calc_distance(self, route_string):
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
#           If KeyError shout out if unknown key is inputed then capture the Exception
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
    
railroad = Railroad()
routes_graph = railroad.build(input_towns_string)
route = railroad.calc_distance('A-B-C')
route = railroad.calc_distance('A-D')
route = railroad.calc_distance('A-D-C')
route = railroad.calc_distance('A-E-B-C-D')
route = railroad.calc_distance('A-E-D')


