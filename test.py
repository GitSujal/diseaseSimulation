'''Testing people.py
'''

from  people import People
import random
import numpy as np
import matplotlib.pyplot as plt


'''
Making scatterplot based on either a person is dead, infected or healthy
'''
def scatterplot_people(person,numberOfInfected,numberOfDead):
	#Getting data from each person for plotting.
	(xpos,ypos,infected,dead) = person.plot_people()
	if dead:
		plt.scatter(xpos,ypos,s=area,marker='x',alpha=0.2,c='black')
		numberOfDead+=1
		numberOfInfected+=1
	elif infected:
		plt.scatter(xpos,ypos,s=area,marker='o',alpha=0.2,c='red')
		infected_cells.append((xpos,ypos))
		numberOfInfected+=1
	elif infected ==False:
		plt.scatter(xpos,ypos,s=area,marker='o',alpha=0.2,c='blue')
	return (numberOfInfected,numberOfDead)	

def print_detail(INIT_POP,numberOfHealthyPeople,numberOfInfected,numberOfDead):
	print("Total Population Number of Healthy People Number of Infected People Dead People")
	print("    ",INIT_POP, "\t  ",numberOfHealthyPeople, "\t   ", numberOfInfected, "  \t  ",numberOfDead)

'''
Initialising the world with population.
Populating the world with specified population and sepecific number of initially infected people.
'''	

population = []
INIT_POP = 200
INIT_INFECTED = 20
NUM_COLS = 20
NUM_ROWS = 20
NUM_STEPS = 14
area = (5)**2

infection_probability = INIT_INFECTED/INIT_POP
numberOfInfected = 0
infected_cells = []
total_infected = []
numberOfDead =0
total_dead =[]
numberOfHealthyPeople=0
total_Healthy=[]

for i in range(0,INIT_POP):
	person=People(NUM_ROWS,NUM_COLS,infection = np.random.choice([0,1],p=[1-infection_probability,infection_probability]) ,infection_time=0)		
	population.append(person)
	numberOfInfected,numberOfDead = scatterplot_people(person,numberOfInfected,numberOfDead)
	numberOfHealthyPeople = INIT_POP - numberOfInfected - numberOfDead

'''
Printing information regarding total healthy, infected and dead people.
'''
print_detail(INIT_POP,numberOfHealthyPeople,numberOfInfected,numberOfDead)
plt.show()

# total_infected.append(numberOfInfected)
# total_Healthy.append(numberOfHealthyPeople)
# total_dead.append(numberOfDead)


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
for timestep in range(NUM_STEPS):
	numberOfHealthyPeople=0
	numberOfInfected=0
	numberOfDead=0

	for person in population:
		person.each_timestep(NUM_ROWS,NUM_COLS,infected_cells)
		# person.move_people(NUM_ROWS,NUM_COLS)
		# numberOfInfected = person.check_infection(infected_cells,numberOfInfected)
		# person.plot_people()
		numberOfInfected,numberOfDead = scatterplot_people(person,numberOfInfected,numberOfDead)
		numberOfHealthyPeople = INIT_POP - numberOfInfected - numberOfDead
	
	total_infected.append(numberOfInfected)
	total_Healthy.append(numberOfHealthyPeople)
	total_dead.append(numberOfDead)

	print("\n######################### TIMESTEP: ", timestep, "#########################\n")
	print_detail(INIT_POP,numberOfHealthyPeople,numberOfInfected,numberOfDead)

	filename="./Output/Outputfile"+str(timestep)+".png"
	plt.savefig(filename)
	plt.clf()
	plt.cla()
	plt.close()
	print("File saved as ",filename)
	# plt.show()


xAxis = range(0,NUM_STEPS)
# print(xAxis)
# print(total_Healthy)

plt.plot(xAxis,total_Healthy,'b-',xAxis,total_infected,'r-',xAxis,total_dead,'k-')
plt.show()
# plt.plot(range(0,NUM_STEPS),total_infected)
# plt.savefig("growth.png")
# plt.ylabel("Infected Population")
# plt.xlabel("TIMESTEP")
# plt.title("Growth of infected Population over time")
# plt.show()