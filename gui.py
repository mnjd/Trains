from tkinter import *


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

        shortest_route_button = Button(self.centerframe, text="Shortest route between 2 towns", command=self.shortest_route_window)
        shortest_route_button.pack(side = LEFT)

        number_routes_length_button = Button(self.bottomframe, text="Number of routes having a length smaller than 30", command=self.number_routes_length_window)
        number_routes_length_button.pack(side = BOTTOM)

    def entry_user(self):
        string  = self.entry.get()
        print(string)

    def two_commands(self):
        self.entry_user()
        self.window.destroy()

    def calc_distance_window(self):
        self.window = Toplevel(self.master)
        label = Label(self.window, text="Enter route as A-B")
        label.pack()
        self.entry = Entry(self.window)
        self.entry.pack()
        button = Button(self.window, text='OK', command=self.two_commands)
        button.pack(side = BOTTOM)

    def count_number_routes_window(self):
        self.window = Toplevel(self.master)
        label = Label(self.window, text="Enter input as: 'C', 'C', 3, '<')")
        label.pack()
        self.entry = Entry(self.window)
        self.entry.pack()
        button = Button(self.window, text='OK', command=self.two_commands)
        button.pack(side = BOTTOM)

    def shortest_route_window(self):
        self.window = Toplevel(self.master)
        label = Label(self.window, text="Enter input as: 'A', 'C', 4, '<')")
        label.pack()
        self.entry = Entry(self.window)
        self.entry.pack()
        button = Button(self.window, text='OK', command=self.two_commands)
        button.pack(side = BOTTOM)

    def number_routes_length_window(self):
        self.window = Toplevel(self.master)
        label = Label(self.window, text="Enter input as: 'C', 'C', 10, '<')")
        label.pack()
        self.entry = Entry(self.window)
        self.entry.pack()
        button = Button(self.window, text='OK', command=self.two_commands)
        button.pack(side = BOTTOM)


root = Tk()
gui = GraphicalInterface(root)
root.mainloop()