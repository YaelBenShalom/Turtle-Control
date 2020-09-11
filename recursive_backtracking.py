class RBT:
    def __init__(self, M, N, maze, start, goal):
        self.M = M
        self.N = N
        self.maze = maze
        self.start = start
        self.goal = goal
        self.solution = maze
        self.nos = 0

    def isFree(self, cell):
        x = cell[0]
        y = cell[1]
        if x >= 0 and x < self.M and y >=0 and y < self.N and self.maze[y][x] == 0:
            return True
        return False

    def findNeighbour(self, cell):
        x = cell[0]
        y = cell[1]
        return [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]

    def recursiveBT(self, cell, step):
        x = cell[0]
        y = cell[1]
        self.solution[y][x] = step

        for neighbour in self.findNeighbour(cell):
            n_x = neighbour[0]
            n_y = neighbour[1]

            if self.isFree(neighbour) and self.solution[n_y][n_x] == 0:
                if neighbour == self.goal:
                    self.solution[n_y][n_x] = step+1
                    self.nos = step+1
                    return True
                elif self.recursiveBT(neighbour, step+1):
                    return True

        self.solution[y][x] = 0

        return False

    def execute(self):
        self.recursiveBT(self.start, 1)