from tkinter import *
from train import Railroad
import sys

class GraphicalInterface:

    def __init__(self, master):
        self.master = master
        self.topframe = Frame(master)
        self.topframe.pack(side = TOP)
        self.centerframe = Frame(master)
        self.centerframe.pack()
        self.bottomframe = Frame(master)
        self.bottomframe.pack(side = BOTTOM)
        self.buttons(master)

    def buttons(self, master):
        calc_distance_button = Button(self.topframe, text="Distance between 2 towns", command=self.calc_distance_window)
        calc_distance_button.pack(side = LEFT)

        count_number_routes_button = Button(self.topframe, text="Number of routes between 2 towns", command=self.count_number_routes_window)
        count_number_routes_button.pack(side = LEFT)

        shortest_route_button = Button(self.centerframe, text="Shortest route between 2 towns", command=self.shortest_route_display_window)
        shortest_route_button.pack(side = LEFT)

        number_routes_length_button = Button(self.bottomframe, text="Number of routes having a length smaller than 30", command=self.number_different_routes_window)
        number_routes_length_button.pack(side = BOTTOM)

    def show_calc_distance(self):
        self.string = self.entry.get()
        railroad = Railroad()
        print(railroad.calc_distance(self.string))
        self.window.quit()

    def show_count_number_routes(self):
        self.string_start = self.entry_start.get()
        self.string_end = self.entry_end.get()
        self.string_number_stops = int(self.entry_number_stops.get())
        self.string_method = self.gui_method
        railroad = Railroad()
        print(railroad.count_number_routes(self.string_start, self.string_end, self.string_number_stops, self.string_method))
        self.window.quit()

    def show_shortest_route_display(self):
        self.string_start = self.entry_start.get()
        self.string_end = self.entry_end.get()
        self.string_number_stops = int(self.entry_number_stops.get())
        self.string_method = self.gui_method
        railroad = Railroad()
        print(railroad.shortest_route_display(self.string_start, self.string_end, self.string_number_stops, self.string_method))
        self.window.quit()

    def show_number_different_routes(self):
        self.string_start = self.entry_start.get()
        self.string_end = self.entry_end.get()
        self.string_number_stops = int(self.entry_number_stops.get())
        self.string_method = self.gui_method
        railroad = Railroad()
        print(railroad.number_different_routes(self.string_start, self.string_end, self.string_number_stops, self.string_method))
        self.window.quit()

    def max_stops_method(self):
        self.gui_method = '<'

    def finite_stops_method(self):
        self.gui_method = '='

    def calc_distance_window(self):
        self.window = Toplevel(self.master)
        label = Label(self.window, text="Enter route as A-B")
        label.pack()
        self.entry = Entry(self.window)
        self.entry.pack()
        button = Button(self.window, text='OK', command=self.show_calc_distance)
        button.pack(side = BOTTOM)

    def count_number_routes_window(self):
        self.window = Toplevel(self.master)
        label = Label(self.window, text="Enter route as: 'C', 'C', 3, '<'")
        label.pack()
        self.entry_start = Entry(self.window)
        self.entry_start.pack()
        self.entry_end = Entry(self.window)
        self.entry_end.pack()
        self.entry_number_stops = Entry(self.window)
        self.entry_number_stops.pack()
        button_max_stops = Button(self.window, text='max stops (<)', command = self.max_stops_method)
        button_max_stops.pack(side = LEFT)
        button_finite_stops = Button(self.window, text='finite stops (=)', command = self.finite_stops_method)
        button_finite_stops.pack(side = LEFT)
        button = Button(self.window, text='OK', command=self.show_count_number_routes)
        button.pack(side = BOTTOM)

    def shortest_route_display_window(self):
        self.window = Toplevel(self.master)
        label = Label(self.window, text="Enter route: 'C', 'C', 3, '<'")
        label.pack()
        self.entry_start = Entry(self.window)
        self.entry_start.pack()
        self.entry_end = Entry(self.window)
        self.entry_end.pack()
        self.entry_number_stops = Entry(self.window)
        self.entry_number_stops.pack()
        button_max_stops = Button(self.window, text='max stops (<)', command = self.max_stops_method)
        button_max_stops.pack(side = LEFT)
        button_finite_stops = Button(self.window, text='finite stops (=)', command = self.finite_stops_method)
        button_finite_stops.pack(side = LEFT)
        button = Button(self.window, text='OK', command=self.show_shortest_route_display)
        button.pack(side = BOTTOM)

    def number_different_routes_window(self):
        self.window = Toplevel(self.master)
        label = Label(self.window, text="Enter route as: 'C', 'C', 3, '<'")
        label.pack()
        self.entry_start = Entry(self.window)
        self.entry_start.pack()
        self.entry_end = Entry(self.window)
        self.entry_end.pack()
        self.entry_number_stops = Entry(self.window)
        self.entry_number_stops.pack()
        button_max_stops = Button(self.window, text='max stops (<)', command = self.max_stops_method)
        button_max_stops.pack(side = LEFT)
        button_finite_stops = Button(self.window, text='finite stops (=)', command = self.finite_stops_method)
        button_finite_stops.pack(side = LEFT)
        button = Button(self.window, text='OK', command=self.show_number_different_routes)
        button.pack(side = BOTTOM)


root = Tk()
gui = GraphicalInterface(root)
root.mainloop()
