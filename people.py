'''

This is a people class which represents a person in the world. 
Each people have an unique identifier or ID, it's location as xpos and ypos, information about whether it is infected or not, resistance in range of (0,1) and infection time.
'''
import uuid
import random
import numpy as np
class People:   
	
	def __init__(self, num_rows,num_cols, infection= False, resistance= random.random(), infection_time =  0):
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
		self.infected = False

	def gets_infected(self):
		self.infected = True

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

	# def plot_people(self):
	# 	if self.infected:
	# 		plt.scatter(self.xpos,self.ypos,s=self.area,marker='o',alpha=0.2,c='red')
	# 	else:
	# 		plt.scatter(self.xpos,self.ypos,s=self.area,marker='o',alpha=0.2,c='blue')

	def plot_people(self):
		return (self.xpos,self.ypos,self.infected,self.dead)


	def move_people(self,NUM_ROWS,NUM_COLS):

		#Teleporting to random airport if a person is at any airport
		if (self.xpos,self.ypos) in Airport_Cells:
			self.xpos,self.ypos = Airport_Cells[np.random.randint(len(Airport_Cells))]

			#For Debugging
			print("Someone just passed through an airport.")

		rMove = random.randint(-1,1)
		cMove = random.randint(-1,1)

		#Checking if the movement takes the people out of Xlim and Ylim.
		if  ((self.xpos + rMove) > (NUM_ROWS-1) or ( self.xpos + rMove)<0):
			rMove = 0
		
		if (self.ypos + cMove) > (NUM_COLS-1) or (self.ypos + cMove)<0:
			cMove =0
		
		#Stopping person from getting through the boundary wall.
		if ((self.xpos + rMove),( self.xpos + rMove)) in Boundary_Cells:
			print("Someone hit the boundary")
			rMove=0
			cMove=0
		
		self.xpos+=rMove
		self .ypos+=cMove

		




	def check_infection(self,infected_cells,):
		if (self.xpos,self.ypos) in infected_cells:
			self.probability_of_Infection +=0.10
		if self.resistance < self.probability_of_Infection:
			self.gets_infected()
			
	def check_dead(self,numberOfDead):
		if self.infection_time>0:
			self.probability_of_death += np.random.choice([0,1],p=[1/self.infection_time,1-1/self.infection_time])
			
			if self.probability_of_death>=1:
				self.dead = True
			if self.dead:
				numberOfDead+=1
		else:
		 	self.dead=False

		return numberOfDead

	def each_timestep(self,NUM_ROWS,NUM_COLS,infected_cells,numberOfInfected,numberOfDead,Airport_Cells,Boundary_Cells):
		
		self.move_people(NUM_ROWS,NUM_COLS,Airport_Cells,Boundary_Cells)

		if self.infected:
				self.infection_time+=1
				numberOfInfected+=1
				numberOfDead =  self.check_dead(numberOfDead)

		elif self.infected == False:
				self.check_infection(infected_cells)

		return(numberOfInfected,numberOfDead)	
			
