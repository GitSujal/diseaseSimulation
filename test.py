'''Testing people.py
'''

from  people import People
import random
import numpy as np
import matplotlib.pyplot as plt

population = []
INIT_POP = 1000
INIT_INFECTED = 50
NUM_COLS = 40
NUM_ROWS = 40
NUM_STEPS = 10

infection_probability = INIT_INFECTED/INIT_POP
numberOfInfected = 0;
infected_cells = []
total_infected = []

for i in range(0,INIT_POP):
	person=People(NUM_ROWS,NUM_COLS,infection = np.random.choice([0,1],p=[1-infection_probability,infection_probability]) ,infection_time=0)
	#person.print_out()
	if person.infected:
		infected_cells.append((person.xpos,person.ypos))

	population.append(person)
	#person.plot_people()

	if person.infected:
		numberOfInfected+=1


print(numberOfInfected)
total_infected.append(numberOfInfected)
#print(infected_cells)
# plt.show()
# plt.clf()
# plt.cla()
# plt.close()



for timestep in range(NUM_STEPS):
	print("\n###################### TIMESTEP", timestep, "#####################\n")
	print("Total Infected ", numberOfInfected)
	total_infected.append(numberOfInfected)
	for person in population:
		person.move_people(NUM_ROWS,NUM_COLS)
		numberOfInfected = person.check_infection(infected_cells,numberOfInfected)
		
		person.plot_people()
	filename="./Output/Outputfile"+str(timestep)+".png"
	plt.savefig(filename)
	plt.clf()
	plt.cla()
	plt.close()
	print("File saved as ",filename)
	plt.show()


plt.plot(range(0,NUM_STEPS+1),total_infected)
plt.savefig("growth.png")
plt.ylabel("Infected Population")
plt.xlabel("TIMESTEP")
plt.title("Growth of infected Population over time")
plt.show()