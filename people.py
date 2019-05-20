'''
This is a people class which represents a person in the world. 
Each people have an unique identifier or ID, it's location as xpos and ypos, information about whether it is infected or not, resistance in range of (0,1) and infection time.
'''

import uuid
import random
import numpy as np
from neighbours import *



class People:   
	
	def __init__(self, num_rows=20,num_cols=20, infection= False, resistance= random.random(), infection_time =  0):
		'''
		Initialising people. 
		People class instance gets following parameter upon initialisation:
		1. a unique ID
		2. a random xpos and ypos
		3. a bool value infected representing whether it is infected or  not
		4. a value ranging between 0-1 representing the resistance power against infection of that people.
		5. a timer ranging from 0-10 representing how long has the person been infected. Once it reaches 10 the person dies.
		6. a bool value dead representing whether the person is dead or not.
		7. probability of death meaning the chances of person being dead after being infected. For non infected it would be zero.
		'''
		self.ID = uuid.uuid4()
		self.xpos = random.randint(0,num_rows)
		self.ypos = random.randint(0,num_cols)
		self.infected = infection
		self.resistance = resistance
		self.probability_of_Infection = 0.0
		self.infection_time = infection_time
		self.dead = False
		self.probability_of_death = 0.0

	def gets_deinfection(self):
		'''
		when people get deinfected the bool value for infected would be False. 
		'''
		self.infected = False

	def gets_infected(self):
		'''
		when people get infected the bool value for infected would be True. 
		'''
		self.infected = True

	def time_step(self):
		'''
		This function runs for each timestep.
		For each timestep the infection time for infected is increased by 1.
		'''
		if infected:
			infection_time+=1
		else:
			infection_time=0

	def print_out(self):
		'''
		Printing out people information. Useful for debugging and assessing individual values of people.
		'''
		if self.infected:
			print("Peope ID:", self.ID, " At location (", self.xpos, ",", self.ypos, ") is infected for: ",self.infection_time," time step")
		else:
			print("Peope ID:", self.ID, " At location (", self.xpos, ",", self.ypos, ") is not infected")


	def plot_people(self):
		'''
		This functions returns required values (xpos,ypos,infercted,dead) values required for plottingp people into the world.
		'''
		return (self.xpos,self.ypos,self.infected,self.dead)


	def move_people(self,NUM_ROWS,NUM_COLS,Airport_Cells,Boundary_Cells):
		'''
		This function is used to move people by one position either in x direction or y direction or by 1 step on both direction.

		'''
		if self.dead:
			'''
			Dead people don't move.
			'''
			rMove=0
			cMove=0

		else:	
			if (self.xpos,self.ypos) in Airport_Cells:
				#Teleporting to random airport if a person is at any airport
				self.xpos,self.ypos = Airport_Cells[np.random.randint(len(Airport_Cells))]
				rMove=0
				cMove=0
			else:
				rMove = random.randint(-1,1)
				cMove = random.randint(-1,1)

				#Checking if the movement takes the people out of Xlim and Ylim.
				if  ((self.xpos + rMove) > (NUM_ROWS-1) or ( self.xpos + rMove)<0):
					rMove = 0
				if (self.ypos + cMove) > (NUM_COLS-1) or (self.ypos + cMove)<0:
					cMove =0
		
				#Stopping person from getting through the boundary wall.
				if ((self.xpos + rMove),( self.xpos + rMove)) in Boundary_Cells:
					# print("Someone hit the boundary")
					rMove=0
					cMove=0
		
		self.xpos+=rMove
		self .ypos+=cMove

	def check_infection(self,infected_cells,Neighbour_Choice):
		if self.dead:
			'''
			Dead ones cannot infect healthy people
			'''
		else:
			if (self.xpos,self.ypos) in (infected_cells):
				'''
				If a people is in infected cell it increases the chance of infection by 5%
				'''
				self.probability_of_Infection +=0.05

			if (self.xpos,self.ypos) in vou_neuman_neighbour(infected_cells) and (self.xpos,self.ypos) not in infected_cells :
				'''
				If a people is in vou neuman neighbour of infected cell it increases chance of infection by 2.5%
				'''
				self.probability_of_Infection +=0.025
			
			if Neighbour_Choice == 2:
				if (self.xpos,self.ypos) in moore_neighbour(infected_cells) and (self.xpos,self.ypos) not in infected_cells and (self.xpos,self.ypos) not in vou_neuman_neighbour(infected_cells):
					'''
					If a people is in Moore neighbour of infected cell it increases the chance of infection by 2%
					'''
					self.probability_of_Infection +=0.02

			if self.resistance < self.probability_of_Infection:
				self.gets_infected()
			
	def check_dead(self,numberOfDead,infected_cells):
		'''
		Check if the people is dead.
		'''

		if self.infection_time>0:
			'''
			If person is infected for longer than 1 timestamp the probabiltiy of death increase by 0.3*certain random value between 0-1.
			'''
			self.probability_of_death += 0.1*np.random.choice([0,1],p=[1/self.infection_time,1-1/self.infection_time])
			
			if self.probability_of_death>=1:
				self.dead = True

			if self.dead:
				numberOfDead+=1
		else:
		 	self.dead=False

		return numberOfDead

	def each_timestep(self,NUM_ROWS,NUM_COLS,infected_cells,numberOfInfected,numberOfDead,Airport_Cells,Boundary_Cells,Neighbour_Choice):
		'''
		This function repeats every time a timestamp is passed by a people. People move randomly, gets infected randomly and dies randomly based on parameters defined.
		'''

		self.move_people(NUM_ROWS,NUM_COLS,Airport_Cells,Boundary_Cells)

		if self.infected:
				self.infection_time+=1
				numberOfInfected+=1
				numberOfDead =  self.check_dead(numberOfDead,infected_cells)

		elif self.infected == False:
				self.check_infection(infected_cells,Neighbour_Choice)

		return(numberOfInfected,numberOfDead)	

'''
Testing the class
'''
if __name__ == "__main__" :
	for i in range(0,5):
		#Creating 5 people instances and printing the details.
		person = People()
		person.print_out()






