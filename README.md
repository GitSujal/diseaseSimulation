#### Author: Sujal Dhungana
#### Student ID: 19302779
#### Program: Master of Predictive Analytics
#### Unit: Fundamentals of Programming COMP5006
#### Assignment Title: Disease Simulation

# Disease Simulation

## Dependencies
The diseaseSimulation program requires following dependencies:

1. [numpy](https://www.numpy.org/): NumPY is a python package for mathematical computations. It is used for generating random numbers and handling higher dimensional numerical arrays.
2. [matplotlib](https://matplotlib.org/): Matplotlib is a python package for generating plots. Matplotlib is used to plot the scatter plot and line graph for this program.
3. [random](https://docs.python.org/2/library/random.html): random module in python is used for generating random float or random integer.
4. [uuid](https://www.npmjs.com/package/uuid): UUID module for python used for generating unique id for each people.
5. [sys](https://docs.python.org/3/library/sys.html): sys module to access system arguments in python.
6. [neighbours](https://github.com/GitSujal/diseaseSimulation/blob/master/neighbours.py): Neighbours program to get Vou Neumann and Moore neighbours for each cell. Can be found along with the diseaseSimulation program.
7. [people](https://github.com/GitSujal/diseaseSimulation/blob/master/people.py): People class that holds all the information about the people in the world and functions to make changes on the world. Can be found along with the diseaseSimulation program.

### To install other modules except ones found along the program.

1. Using pip
```
pip3 install numpy
pip3 install matplotlib
pip3 install uuid
```

2.  Using Anaconda 

Download Anaconda for your operating system and install it globally on your system.

* [Download Anaconda](https://www.anaconda.com/distribution/#download-section)

## Directory Overview 
The directory consists of following files.

1.  diseaseSimulation.py
2. people.py
3. neighbours.py
4. parametersweep.sh

The output from the simulation conducted via parameter sweep can be found in directory named Simulation_Timestamp. The directory contains separate folder with outputs from separate simulations.

If a simulation is run directly from diseaseSimulation.py the output can be found at Output directory in the same directory.


##Running the Program

There are two ways of running this program.

## 1. Without Parameter Sweep 
To run the program without parameter sweep please follow the commands below:

### Running program with system arguments 
```
python3 diseaseSimulation.py INIT_POP INIT_INFECTED NUM_ROWS NUM_COLS TIME_STEPS NEIGHBOURHOOD_CHOICE  
```

* INIT_POP is the initial population of the world 
* INIT_INFECTED is the number of initially infected people in the world
* NUM_ROWS is the number of rows in the world map
* NUM_COLS is the number of columns in the world map
* TIME_STEPS is the number of time steps the simulation runs for.
* NEIGHBOURHOOD_CHOICE This is the choice for choosing the neighbourhood. (1) for Vou Neumann neighbours and (2)  for Moore neighbours

If no values are give the program used default values for the variables and runs the program the default values for the variables are as follows:
 
* INIT_POP  = 500
* INIT_INFECTED = 20
* NUM_ROWS = 20
* NUM_COLS = 20
* TIME_STEPS = 15
* NEIGHBOURHOOD_CHOICE = 1 (Vou neumann neighbour)

### Running the program with default values.

```
python3 diseaseSimulation.py
```


## 2. Running program with parameter Sweep

To run the program with parameter sweep please follow following commands:

```
sh parametersweep.sh LOW_INIT_POP HI_INIT_POP STEP_INIT_POP LOW_INIT_INFECTED HI_INIT_INFECTED STEP_INIT_INFECTED NUM_ROWS NUM_COLS NUM_STEPS
```
Each system arguments corresponds to following value:

* LOW\_INIT\_POP is lowest value of population you want to start the simulation with
* HI\_INIT\_POP is the highest value of population you want the simulation to go
* STEP\_INIT\_POP is the step increment you want in the population
* LOW\_INIT\_INFECTED is the lowest value of number of infected people in population simulation runs with
* HI\_INIT\_INFECTED is the highest value of number of infected people in population simulation runs with
* STEP\_INIT\_INFECTED is the step increment you want in the initial infected population.
* NUM\_ROWS is the number of rows in the world
* NUM\_COLS is the number of columns in the world
* NUM\_STEPS is the number of time step each simulation n runs.

The parameter sweep will run each simulation two times. One time taking Vou Neumann neighbourhood and next time with Moore neighbourhood. Output from each simulation can be found in separate folder under directory Simulation_timestamp.


