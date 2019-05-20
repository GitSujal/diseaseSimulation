# Author: Sujal Dhungana
# Student ID: 19302779
# Unit: Fundamentals of Programming COMP5005
# Program: Master of Predictive Analytics
#Unit Co ordinator: Dr. Valerie Maxville
#Assignment Title: Disease Simulation
#Submission Date: 21 May 2019

'''
diseaseSimulation.py
This program simulates spread of diesease over population in a world. World consists of barrier where people can't pass through.
Airports allow people to travel randomly from one place to another. 
Program can be run with or without system arguments. If no system arguments provided it runs with default values. 

The System Arguments should follow this order.
INIT_POPULATION,INIT_INFECTED,NUM_ROWS,NUM_COLS,NUM_STEPS,Neighbours_choice

'''

from  people import People
import random
import numpy as np
import matplotlib.pyplot as plt
import sys
from neighbours import *

# Setting seed for reproducibility
random.seed(19302657) 
np.random.seed(19302659)


def scatterplot_people(person):
	'''
	Function to plot scatterplot based on either a person is dead, infected or healthy
	'''
	#Getting data from each person for plotting.

	(xpos,ypos,infected,dead) = person.plot_people()
	if dead:
		plt.scatter(xpos,ypos,s=area,marker='x',alpha=0.2,c='black')

	elif infected:
		plt.scatter(xpos,ypos,s=area,marker='o',alpha=0.2,c='red')
		infected_cells.append((xpos,ypos))
	elif infected ==False:
		plt.scatter(xpos,ypos,s=area,marker='o',alpha=0.2,c='blue')


def print_detail(INIT_POP,numberOfHealthyPeople,numberOfInfected,numberOfDead):
	'''
	Function to print detail about the population, including number of people living, infected and dead.
	Arguments needed: Initial population, number of healthy people, number of infected, number of Dead.
	'''
	print("Alive Population| Healthy People| Infected People| Dead People")
	print("    ",INIT_POP - numberOfDead , "\t      ",numberOfHealthyPeople, "\t  \t", numberOfInfected, " \t \t  ",numberOfDead)


def plot_cells(Cells,size,color='yellow',label="default"):
	'''
	Function to plot Airport cells takes the Airport cells coordinates as argument.
	'''
	x_array= []
	y_array=[]
	for x,y in Cells:
		x_array.append(x)
		y_array.append(y)
	plt.scatter(x_array,y_array,s=size*area,marker='s',c=color,alpha=0.75)


'''
Defining intial variables and setting them to some default vales.
'''

Initial_Values_Names= ["INIT_POPULATION","INIT_INFECTED","NUM_ROWS","NUM_COLS,NUM_STEPS","Neighbours Choice"]
Initial_Values_Array = [500,20,20,20,15,1]
area = (5)**2

''''
Getting the system argument and initialising population with the values provided.
'''

if len(sys.argv) == 1:
	print("No arguments passed initialising with default values\n")

if len(sys.argv)<=7:
	for i in range(1,len(sys.argv)) :
		#Checking that the provided arguments are numerical values
		if sys.argv[i].isnumeric():
			Initial_Values_Array[i-1] = int(sys.argv[i])
		else:
			print("Non Numeric Character provided for ",Initial_Values_Names[i-1], "at argument position \n", i+1)
			print("Default values used for the non numeric arguments\n")
else:
	print("More arguments passed than required. Please enter upto 6 arguments. Initialising with default values")

INIT_POP,INIT_INFECTED,NUM_ROWS,NUM_COLS,NUM_STEPS,Neighbours_Choice = Initial_Values_Array


'''
Adding some airports and boundaries.
'''	
Airport_Cells = [(NUM_COLS/4,0),(NUM_COLS,NUM_ROWS/4),(0,3*NUM_ROWS/4),(NUM_COLS,3*NUM_ROWS/4)]
Boundary_Cells = []

for i in range(0,(NUM_ROWS+1),1):
	Boundary_Cells.append((NUM_COLS/2,i))
for i in range(0,(NUM_COLS+1),1):
	Boundary_Cells.append((i,NUM_ROWS/2))


#Making few doors at the boundaries to allow people movement through them.
random_index = np.random.randint(0,len(Boundary_Cells)-10,size=4)
for i in random_index:
	del Boundary_Cells[i-1]
	del Boundary_Cells[i]
	del Boundary_Cells[i-2]


'''
Initialising population and factors associated with population and each people
'''
infection_probability = INIT_INFECTED/INIT_POP
numberOfInfected = 0
numberOfDead =0
numberOfHealthyPeople=0
total_dead =[]
infected_cells = []
total_infected = []
total_Healthy=[]
population = []

'''
Initialising the world with population.
Populating the world with specified population and sepecific number of initially infected people.
'''	
for i in range(0,INIT_POP):
	person=People(NUM_ROWS,NUM_COLS,infection = np.random.choice([0,1],p=[1-infection_probability,infection_probability]) ,infection_time=0)		
	population.append(person)
	scatterplot_people(person)
	plot_cells(Airport_Cells,4,"yellow","Airporti")
	plot_cells(Boundary_Cells,2,"black","Boundary")
	#plot_Airport(Airport_Cells)
	#plot_Airport(moore_neighbour(Airport_Cells),"green")
	#plot_Airport(vou_neuman_neibhbour(Airport_Cells),"red")
	#plot_boundary(Boundary_Cells)
title_string = "Simualtion for "+ str(INIT_POP) + " People with " +str(INIT_INFECTED) +" Infected ones" 
plt.xlim(0,NUM_ROWS)
plt.ylim(0,NUM_COLS)
plt.title(title_string)
plt.clf()
plt.cla()
plt.close()


#plt.show()


'''
	Disease simulation for each timestep. Following things occur on each timestep.
	1. Each people move randomly one cell either by row or by 1 column.
	2. If a people is in cell with an infected person, the infection probability of the healthy people increases by 20%
	3. If the infection probability is greater than person's resistance, the person gets infected
	4. The infection time increases by 1 for each timestep for an infected person.
	5. If a people is infected for more than 10 timestep it dies.
'''


total_infected=[]
total_Healthy=[]
total_dead=[]
Neighbours_Choice_array=["Vou Neuman Neighbour"," Moore Neighbour"]

for timestep in range(NUM_STEPS):
	numberOfInfected=0
	numberOfDead=0
	for person in population:
		numberOfInfected,numberOfDead = person.each_timestep(NUM_ROWS,NUM_COLS,infected_cells,numberOfInfected,numberOfDead,Airport_Cells,Boundary_Cells,Neighbours_Choice)
		scatterplot_people(person)
	
	'''
	Calculating number of healthy, unhealthy and dead population after each timestep and printing it. 
	'''
	numberOfHealthyPeople = INIT_POP - numberOfInfected

	total_infected.append(numberOfInfected)
	total_Healthy.append(numberOfHealthyPeople)
	total_dead.append(numberOfDead)

	print("\n######################### TIMESTEP: ", timestep, "#########################\n")
	print_detail(INIT_POP,numberOfHealthyPeople,numberOfInfected,numberOfDead)
	plt.xlim(0,NUM_ROWS)
	plt.ylim(0,NUM_COLS)
	plot_cells(Airport_Cells,4,"yellow","Airport")
	plot_cells(Boundary_Cells,2,"black","Boundary")

	filename="./Output/Image"+str(timestep)+".png"

	title_string_timestep = "Simulation for " +str(timestep)+ " timestep "+"using"+Neighbours_Choice_array[Neighbours_Choice-1]

	subtitle_string = 'Not Infected: '+ str(numberOfHealthyPeople),' Infected: '+ str(numberOfInfected) +' Dead: ' +str(numberOfDead)
	plt.suptitle(title_string_timestep)
	plt.title(subtitle_string)
	plt.savefig(filename)
	plt.clf()
	plt.cla()
	plt.close()
	print("File saved as ",filename)
	#plt.show()

'''
Plotting the overall growth of population over time for whole experiment.
'''
xAxis = range(0,NUM_STEPS)
plt.plot(xAxis,total_Healthy,'b-',label='Healthy Population')
plt.plot(xAxis,total_infected,'r-',label='Infected Population')
plt.plot(xAxis,total_dead,'k-',label='Dead Population')
plt.xlim(0,NUM_STEPS)
plt.ylim(0,INIT_POP)
plt.xlabel("TIMESTEP")
plt.title("Growth of Healthy,Infected and Dead Population over time")
plt.legend()
plt.savefig("FinalResult.png")
print("File saved as FinalResult.png")
plt.clf()
plt.cla()
plt.close()

