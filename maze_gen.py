import numpy
import random

class Maze:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.frontier_list = []
        self.init_matrix = []

    def maze_generator(self):
    # creating an initial matrix of ones
        self.init_matrix = numpy.ones((self.m,self.n), dtype=int)

    #randomly selecting a starting position and adding 2-hop neigbors to frontier_list
        start_array = (random.randrange(self.m), random.randrange(self.n))
        self.init_matrix[start_array] = 0
#        print("initial matrix:")
#        print (self.init_matrix)
        self.update_frontier_list(start_array[0], start_array[1])
#        print ("frontier_list:")
#        print (self.frontier_list)

    # iterating through the frontier_list
        while self.frontier_list:
            # randomly selecting from the frontier_list, 
            # randomly selecting a free (non-blocked) neighbor
            # removing the wall of the random frontier
            # updating the frontier_list
            random_frontier = random.choice(self.frontier_list)
            frontier_neighbor = self.choose_neighbor(random_frontier[0], random_frontier[1], 0)
            self.init_matrix[random_frontier[0]][random_frontier[1]] = 0
            self.update_frontier_list(random_frontier[0], random_frontier[1])

            #breaking the wall; choosing a random blocked neighbor
            self.init_matrix[self.middle_cell(random_frontier, frontier_neighbor)[0]][self.middle_cell(random_frontier, frontier_neighbor)[1]] = 0
            add_to_frontier_list = self.choose_neighbor(random_frontier[0], random_frontier[1], 1)

            if add_to_frontier_list and add_to_frontier_list not in self.frontier_list:
                self.frontier_list.append(add_to_frontier_list)
            self.frontier_list.remove(random_frontier)
#            print("adding to the frontier list:")   
#            print (self.frontier_list)
        print (self.init_matrix)

    def middle_cell(self, first_array, second_array): 
        #finding the middle cell between the frontier cell and the neighbor cell
        middle_array = [int((first_array[0] + second_array[0])/2), int((first_array[1] + second_array[1])/2)]
        return middle_array

    def update_frontier_list(self, xcell, ycell):
        #updating the frontier list with the frontier cells
        if xcell-2 >= 0 and self.init_matrix[xcell-2, ycell] and [xcell-2, ycell] not in self.frontier_list:
            self.frontier_list.append([xcell-2, ycell])
        if xcell+2 < self.m and self.init_matrix[xcell+2, ycell] and [xcell+2, ycell] not in self.frontier_list:
            self.frontier_list.append([xcell+2, ycell])
        if ycell-2 >= 0 and self.init_matrix[xcell, ycell-2] and [xcell, ycell-2] not in self.frontier_list:
            self.frontier_list.append([xcell, ycell-2])
        if ycell+2 < self.n and self.init_matrix[xcell, ycell+2] and [xcell, ycell+2] not in self.frontier_list:
            self.frontier_list.append([xcell, ycell+2])

    def choose_neighbor(self, xneighbor, yneighbor, value):
        #returning a randon neighbor from the list of all possible neighbors
        neighbors_list = []
        if xneighbor-2 >= 0 and self.init_matrix[xneighbor-2,yneighbor] == value:
            neighbors_list.append([xneighbor-2,yneighbor])
        if xneighbor+2 < self.m and self.init_matrix[xneighbor+2,yneighbor] == value:
            neighbors_list.append([xneighbor+2,yneighbor])
        if yneighbor-2 >= 0 and self.init_matrix[xneighbor,yneighbor-2] == value:
            neighbors_list.append([xneighbor,yneighbor-2])
        if yneighbor+2 < self.n and self.init_matrix[xneighbor,yneighbor+2] == value:
            neighbors_list.append([xneighbor,yneighbor+2])
        if  neighbors_list:
            return random.choice(neighbors_list)


def main():
    maze = Maze(11, 31)
    maze.maze_generator()
    # print(maze)


if __name__ == "__main__":
    main()



# All cells are walls.
# Randomly choose a cell B and mark it as free. 
# Add that cell's neighbors to the wall list.
# While the frontier list is not empty:
#     Randomly choose a wall C from the wall list
#     The wall divides two cells, A and B.
#     If either A or B is a wall
#        Let D be whichever of A and B that is the wall
#        Make C free
#        Make D free
#        Add the walls of D to the wall list
#     Remove C from the wall list