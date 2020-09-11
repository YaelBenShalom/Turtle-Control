import copy

class WFP:
    def __init__(self, M, N, maze, start, goal):
        self.M = M
        self.N = N
        self.maze = maze
        self.start = start
        self.goal = goal
        self.checked = copy.deepcopy(maze)
        self.solution = copy.deepcopy(maze)
        self.nos = 0

        self.dx = [1, 0, -1, 0]
        self.dy = [0, 1, 0, -1]

    def check(self, x, y):
        if (x < 0 or x >= self.M or y < 0 or y >= self.N):
            return False
        if (self.checked[y][x]):
            return False
        if (self.maze[y][x]):
            return False
        else:
            return True


    def generate_map(self):
        curX = self.goal[0]
        curY = self.goal[1]
        curS = 1  # curS is the current number for the cell
        current = [curX, curY, curS]
        self.checked[curY][curX] = curS
        cellist = []
        cellist.append(current)
        while (cellist):
            cur = cellist.pop(0)
            if (cur[0] == self.start[0] and cur[1] == self.start[1]):
                return True
            for i in range(4):
                nX = cur[0] + self.dx[i]
                nY = cur[1] + self.dy[i]
                if not self.check(nX, nY):
                    continue
                self.checked[nY][nX] = cur[2] + 1
                next = [nX, nY, cur[2] + 1]
                cellist.append(next)


    def generate_route(self):
        route = []
        curP = [self.start[0],self.start[1]]
        route.append(curP[:])
        while (not (curP[0] == self.goal[0] and curP[1] == self.goal[1])):
            pstate = []
            for i in range(4):
                nX = curP[0] + self.dx[i]
                nY = curP[1] + self.dy[i]
                if (nX < 0 or nX >= self.M or nY < 0 or nY >= self.N or self.maze[nY][nX] == -1):
                    pstate.append(1024)
                    continue
                pstate.append(self.checked[nY][nX])
            p = pstate.index(min(pstate))
            curP[0] = curP[0] + self.dx[p]
            curP[1] = curP[1] + self.dy[p]
            route.append(curP[:])
        
        for step in route:
            self.nos += 1
            self.solution[step[1]][step[0]] = self.nos

    
    def execute(self):
        self.generate_map()
        self.generate_route()
        