input_towns_string = 'AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7'

class Railroad:

    def __init__(self):
        self.routes_graph={}

    def check_input_string(self, string_distance):
        input_towns_list = string_distance.split(", ")
        length_input = len(input_towns_list)
        for l in range(0, length_input):
            input_distance = input_towns_list[l]
            print(input_distance)
            i = 0
            for char in input_distance:
                i += 1
                if (len(input_distance) > 3) or (len(input_distance) < 3):
                    raise Exception('input distance format should be 3 characters')
                elif (i == 1) and (char.isalpha() == True):
                    print('first character is a letter')
                    pass
                elif (i == 2) and (char.isalpha() == True):
                    print('second character is a letter')
                    pass
                elif (i == 3) and (char.isdigit() == True):
                    print('third character is a number')
                    pass
                else:
                    raise Exception('first and second characters should be letters and third a number')
        return input_towns_list

    def construct_graph(self, string_distance):
        railroad = Railroad()
        input_towns_list = railroad.check_input_string(input_towns_string)
        i = 0
        routes_graph = {}
        for l in range(0, len(input_towns_list)):
            for char in input_towns_list[l]:
                i += 1
                if i == 1:
                    char1 = char
                    if char1 not in routes_graph:
                        routes_graph[char1] = {}
                if i == 2:
                    char2 = char
                    routes_graph[char1][char2] = {}
                if i == 3:
                    char3 = char
                    routes_graph[char1][char2] = int(char3)
            i = 0
        return routes_graph
    
railroad = Railroad()
routes_graph = railroad.construct_graph(input_towns_string)
print(routes_graph)

#print(l)


