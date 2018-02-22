from tkinter import *
from train import Railroad


class GraphicalInterface:

    def __init__(self, master):
        '''
        Creating 3 frames to display buttons
        and calling method to create buttons
        '''
        self.master = master
        self.topframe = Frame(master)
        self.topframe.pack(side = TOP)
        self.centerframe = Frame(master)
        self.centerframe.pack()
        self.bottomframe = Frame(master)
        self.bottomframe.pack(side = BOTTOM)
        self.buttons(master)

    def buttons(self, master):
        '''
        Creating the main 4 buttons
        '''
        calc_distance_button = Button(self.topframe, text="Distance between 2 towns", command=self.calc_distance_window)
        calc_distance_button.pack(side = LEFT)

        count_number_routes_button = Button(self.topframe, text="Number of routes between 2 towns", command=self.count_number_routes_window)
        count_number_routes_button.pack(side = LEFT)

        shortest_route_button = Button(self.centerframe, text="Shortest route between 2 towns", command=self.shortest_route_display_window)
        shortest_route_button.pack(side = LEFT)

        number_routes_length_button = Button(self.bottomframe, text="Number of routes having a length smaller than 30", command=self.number_different_routes_window)
        number_routes_length_button.pack(side = BOTTOM)
        
    def calc_distance_window(self):
        '''
        Method called when user wants to compute distance 
        '''
        self.window = Toplevel(self.master)
        label = Label(self.window, text="Enter route in the format A-B or A-B-C or A-B-C-D etc...")
        label.pack()
        self.entry = Entry(self.window)
        self.entry.pack()
        button = Button(self.window, text='OK', command=self.show_calc_distance)
        button.pack(side = BOTTOM)

    def count_number_routes_window(self):
        '''
        Method called when user wants to compute the number of 
        routes between two towns given the number of stops.
        '''
        self.entry_fields()
        button = Button(self.window, text='OK', command=self.show_count_number_routes)
        button.grid(row=5, column=1)

    def shortest_route_display_window(self):
        '''
        Method called when user wants to compute the length of
        the shortest route between two towns given the number
        of stops.
        '''
        self.entry_fields()
        button = Button(self.window, text='OK', command=self.show_shortest_route_display)
        button.grid(row=5, column=1)

    def number_different_routes_window(self):
        '''
        Method called when user wants to compute the number
        of different routes having a length smaller than 30
        between 2 towns.
        '''
        self.entry_fields()
        button = Button(self.window, text='OK', command=self.show_number_different_routes)
        button.grid(row=5, column=1)

    def entry_fields(self):
        '''
        Fields used to get the input
        '''
        self.window = Toplevel(self.master)
        label_start = Label(self.window, text="Starting town")
        label_start.grid(row=1, column=0)
        self.entry_start = Entry(self.window)
        self.entry_start.grid(row=1, column=2)
        label_end = Label(self.window, text="Ending town")
        label_end.grid(row=2, column=0)
        self.entry_end = Entry(self.window)
        self.entry_end.grid(row=2, column=2)
        label_stops = Label(self.window, text="# of stops")
        label_stops.grid(row=3, column=0)
        self.entry_number_stops = Entry(self.window)
        self.entry_number_stops.grid(row=3, column=2)
        # User must click on one of the following button 
        # to say whether one wants to make the trip
        # in less than a given number of stops
        # or exactly within a given number of stops
        button_max_stops = Button(self.window, text='max stops (<)', command = self.max_stops_method)
        button_max_stops.grid(row=4, column=0)
        button_finite_stops = Button(self.window, text='finite stops (=)', command = self.finite_stops_method)
        button_finite_stops.grid(row=4, column=2)

    def max_stops_method(self):
        '''
        Less than a given number of stops
        '''
        self.gui_method = '<'

    def finite_stops_method(self):
        '''
        Equal to a given number of stops
        '''
        self.gui_method = '='

    def show_calc_distance(self):
        '''
        call the train code and compute the distance
        '''
        self.string = self.entry.get()
        railroad = Railroad()
        print(railroad.calc_distance(self.string))
        self.window.destroy()

    def show_count_number_routes(self):
        self.get_entry()
        railroad = Railroad()
        print(railroad.count_number_routes(self.string_start, self.string_end, self.string_number_stops, self.string_method))
        self.window.destroy()

    def show_shortest_route_display(self):
        self.get_entry()
        railroad = Railroad()
        print(railroad.shortest_route_display(self.string_start, self.string_end, self.string_number_stops, self.string_method))
        self.window.destroy()

    def show_number_different_routes(self):
        self.get_entry()
        railroad = Railroad()
        print(railroad.number_different_routes(self.string_start, self.string_end, self.string_number_stops, self.string_method))
        self.window.destroy()

    def get_entry(self):
        '''
        Method which get the input given by the user.
        '''
        self.string_start = self.entry_start.get()
        self.string_end = self.entry_end.get()
        self.string_number_stops = self.entry_number_stops.get()
        self.check_entry()
        self.string_method = self.gui_method

    def check_entry(self):
        '''
        Method that check if the entry given by the user is valid
        If it is not, an exception is raised and the code waits
        until a correct input is given
        '''
        if not self.string_start.isalpha():
            raise Exception('Starting town should be a string')
        if not self.string_end.isalpha():
            raise Exception('Ending town should be a string')
        if self.string_number_stops.isdigit():
            self.string_number_stops = int(self.string_number_stops)
        else:
            raise Exception('Number of stops should be a number')


root = Tk()
gui = GraphicalInterface(root)
root.mainloop()
