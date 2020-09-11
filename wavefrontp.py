class WFP:
    def __init__(self, M, N, maze, start, goal):
        self.M = M
        self.N = N
        self.maze = maze
        self.start = start
        self.goal = goal
        self.checked = maze
        self.checked[goal[1]][goal[0]] = -2
        self.solution = maze
        self.nos = 1

        self.dx = [1, 0, -1, 0]
        self.dy = [0, 1, 0, -1]

    def isFree(self, x, y):
        if (x < 0 or x >= self.M or y < 0 or y >= self.N or self.maze[y][x] == -1):
            return False

        return True
    
    def isChecked(self, x, y):
        if self.checked[y][x] != 0:
            return True
        # if (maze[x][y]):
        #     return False
        return False

    def getNeighbour(self, x, y):
        return [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]

    def generate_map(self):
        # curX = self.goal[0]
        # curY = self.goal[1]
        # curS = 0  # curS is the current number for the cell
        # curCell = [curX, curY, curS]
        for row in self.checked:
            print(row)

        cellist = []
        cellist.append([self.goal[0], self.goal[1], 0])
        while (cellist):
            cur = cellist.pop(0)
            # print("cur",cur)
            if (cur[0] == self.start[0] and cur[1] == self.start[1]):
                return True
            for neighbour in self.getNeighbour(cur[0], cur[1]):
                nX = neighbour[0]
                nY = neighbour[1]
                if not self.isFree(nX, nY):
                    continue
                    if self.isChecked(nY, nX):
                        continue
                self.checked[nY][nX] = cur[2] + 1
                next = [nX, nY, cur[2] + 1]
                cellist.append(next)
                # print("next",next)
        
        print("generate_map")
        for row in self.checked:
            print(row)

        print("solution")

    def generate_route(self):
        # route= []
        curP = list(self.start)
        # route.append(curP[:])
        while (not (curP[0] == self.goal[0] and curP[1] == self.goal[1])):
            pstate = []
            neighbours = self.getNeighbour(curP[0], curP[1])
            for neighbour in neighbours:
                nX = neighbour[0]
                nY = neighbour[1]
                if not self.isFree(nX, nY):
                # if (nX < 0 or nX >= M or nY < 0 or nY >= N or maze[nX][nY]):
                    pstate.append(1024)
                    continue
                pstate.append(self.checked[nY][nX])

            p = pstate.index(min(pstate))
            curP[0] = neighbours[p][0]
            curP[1] = neighbours[p][1]
            # print("curP", curP)
            self.solution[curP[1]][curP[0]] = self.nos
            self.nos += 1
                  
        self.solution[curP[1]][curP[0]] = self.nos
        # return route
    def execute(self):
        self.generate_map()
        self.generate_route()


# if __name__ == "__main__":
#     maze = [[0, 0, 0, 0, 0, 1, 0, 0], [1, 1, 1, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0]]  # 1 for block
#     M = len(maze)
#     N = len(maze[0])
#     # used to avoid double check
#     # checked = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
#     endpoint = [3, 7]
#     # checked[endpoint[0]][endpoint[1]]=-1

#     startpoint = [0, 0]
#     #  up,left,down,right
#     # dy = [0, 1, 0, -1]
#     # dx = [1, 0, -1, 0]
#     # check if this cell need to be processed
#     generate_map()
#     print(checked)
#     r = generate_route()
#     print(r)

