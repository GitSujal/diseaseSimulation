'''
This is a people class which represents a person in the world
'''
import uuid
import random
import matplotlib.pyplot as plt
import numpy as np

class People:
	area = (5)**2
	def __init__(self, num_rows,num_cols, infection= True, resistance= random.random(), infection_time =  0):
		self.ID = uuid.uuid4()
		self.xpos = random.randint(0,num_rows)
		self.ypos = random.randint(0,num_cols)
		self.infected = infection
		self.resistance = resistance
		self.probability_of_Infection = 0.0
		self.infection_time = infection_time
	
	def calculate_infection(self):
		if self.resistance<0.5:
			infected = True

	def de_infection(self):
		infected = False

	def time_step(self):
		if infected:
			infection_time+=1
		else:
			infection_time=0

	def print_out(self):
		if self.infected:
			print("Peope ID:", self.ID, " At location (", self.xpos, ",", self.ypos, ") is infected for: ",self.infection_time," time step")
		else:
			print("Peope ID:", self.ID, " At location (", self.xpos, ",", self.ypos, ") is not infected")

	def plot_people(self):
		if self.infected:
			plt.scatter(self.xpos,self.ypos,s=self.area,marker='o',alpha=0.2,c='red')
		else:
			plt.scatter(self.xpos,self.ypos,s=self.area,marker='o',alpha=0.2,c='blue')

	def move_people(self,NUM_ROWS,NUM_COLS):
		rMove = random.randint(-1,1)
		cMove = random.randint(-1,1)
		if  (self.xpos + rMove) > (NUM_ROWS-1) or ( self.xpos + rMove)<0:
			rMove = 0
		if (self.ypos + cMove) > (NUM_COLS-1) or (self.ypos + cMove)<0:
			cMove =0
		self.xpos+=rMove
		self .ypos+=cMove

	def check_infection(self,infected_cells,numberOfInfected):
		if self.infected == False:
			if (self.xpos,self.ypos) in infected_cells:
				self.probability_of_Infection +=0.10
			if self.resistance < self.probability_of_Infection:
				self.infected = True
				numberOfInfected+=1
		return numberOfInfected

	
