# Trains stop
Training projects of AgilityFactory: trains

## Getting Started
Download train.py and gui.py.

To work with the graphical interface, execute: 

```
python gui.py
```

If you do not require the graphical interface, execute:

```
python train.py
```

### Prerequisites
python3.6 (2.7 should be fine)

pytest 

```
pip install pytest
```

tkinter

### Running the tests
To run tests, download test.py and execute: 

```
py.test test.py
```

Or if you prefer unittest:

```
python testunit.py
```

### Inputs
For the train.py code (without using the graphical interface gui.py):

Create an instance of Railroad with for example: railroad = Railroad()

To calculate distance between towns, evaluate: railroad.calc_distance('A-B-C'), if you want to calculate distance between town A and C going through B.

To count the number of routes between two towns, evaluate: railroad.count_number_routes('C', 'C', 3, '<') with the first two arguments being the starting and ending towns, the third and fourth arguments meaning "connect the two towns with a maximum of 3 stops". To look at the number of routes connecting the towns with exactly a given number of stops, replace the "<" sign with "=". 

To display the shortest route between two towns, evaluate: railroad.shortest_route_display('C', 'C', 3, '<')

To check the possible number of routes that have a length of less than 30, evaluate: railroad.number_different_routes('C', 'C', 10, '<') Giving the number of stops is mandatory.
