def vou_neuman_neighbour(Cells):
	vou_neuman_neibhbour_cells=[]
	for (x,y) in Cells:
		vou_neuman_neibhbour_cells.append((x,y))
		vou_neuman_neibhbour_cells.append((x+1,y))
		vou_neuman_neibhbour_cells.append((x,y+1))
		vou_neuman_neibhbour_cells.append((x-1,y))
		vou_neuman_neibhbour_cells.append((x,y-1))

	return vou_neuman_neibhbour_cells

def moore_neighbour(Cells):
	moore_neighbour_cells = vou_neuman_neighbour(Cells)
	for (x,y) in Cells:
		moore_neighbour_cells.append((x+1,y+1))
		moore_neighbour_cells.append((x-1,y+1))
		moore_neighbour_cells.append((x+1,y-1))
		moore_neighbour_cells.append((x-1,y-1))
	return moore_neighbour_cells
