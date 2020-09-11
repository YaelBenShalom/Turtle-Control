class BSP:
    def __init__(self, M, N, maze, start, goal):
        self.M = M
        self.N = N
        self.maze = maze
        self.start = start
        self.goal = goal
        self.solution = maze
        self.nos = 0