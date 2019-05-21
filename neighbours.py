'''
neighbours.py This program has two functions
vou_neuman_neighbour and moore_neighbour
Each neighbour function takes an array of cells
and for each cell returns the respective neighbours cells
'''


def vou_neuman_neighbour(Cells):
	'''
	vou_neuman_neighbour takes arguments of cells
	cells is a array of (x,y) co-ordinates
	For each (x,y) coordinate in the cells
	the function returns all vouneuman neighbours
	Vou neuman neighbours are the cells
	that are exactly on
	North,South,East and West of the cell
	including the cell itself.
	'''
	vou_neuman_neibhbour_cells = []
	for (x, y) in Cells:
 		vou_neuman_neibhbour_cells.append((x, y))
 		vou_neuman_neibhbour_cells.append((x+1, y))
 		vou_neuman_neibhbour_cells.append((x, y+1))
 		vou_neuman_neibhbour_cells.append((x-1, y))
 		vou_neuman_neibhbour_cells.append((x, y-1))

	return vou_neuman_neibhbour_cells


def moore_neighbour(Cells):
	'''
	moore_neighbour takes arguments of cells
	cells is a array of (x,y) co-ordinates
	For each (x,y) coordinate in the cells
	the function returns all moore neighbours
	moore neighbours consists of
	all the cells in vou_neuman_cell 
	plus cells on Northeast, Northwest, Southeast
	and southwest of the cell
	'''
	moore_neighbour_cells = vou_neuman_neighbour(Cells)
	for (x, y) in Cells:
		moore_neighbour_cells.append((x+1, y+1))
		moore_neighbour_cells.append((x-1, y+1))
		moore_neighbour_cells.append((x+1, y-1))
		moore_neighbour_cells.append((x-1, y-1))
	return moore_neighbour_cells


'''
Testing the module.
'''


if __name__ == "__main__":
	test_cells  = [(3, 3)]
	print("Test cell is(3,3)")
	for (x, y) in vou_neuman_neighbour(test_cells):
		print("Vou nueman neighbour = (", x, " , ", y, ")\n")
	print() 
	for (x, y) in moore_neighbour(test_cells):
		print("Moore neighbour = (", x, " , ", y, ")\n")
	print()
