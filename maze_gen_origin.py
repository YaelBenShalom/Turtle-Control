def check(x, y):
    if (x < 0 or x >= M or y < 0 or y >= N):
        return False
    if (checked[x][y]):
        return False
    if (maze[x][y]):
        return False
    else:
        return True

def generate_map():
    curX = endpoint[0]
    curY = endpoint[1]
    curS = 0  # curS is the current number for the cell
    current = [curX, curY, curS]
    cellist = []
    cellist.append(current)
    while (cellist):
        cur = cellist.pop(0)
        # print("cur",cur)
        if (cur[0] == startpoint[0] and cur[1] == startpoint[1]):
            return True
        for i in range(4):
            nX = cur[0] + dx[i]
            nY = cur[1] + dy[i]
            if not check(nX, nY):
                continue
            checked[nX][nY] = cur[2] + 1
            next = [nX, nY, cur[2] + 1]
            cellist.append(next)
            # print("next",next)


def generate_route():
    route = []
    curP = [startpoint[0],startpoint[1]]
    route.append(curP)
    while (not (curP[0] == endpoint[0] and curP[1] == endpoint[1])):
        pstate = []
        for i in range(4):
            nX = curP[0] + dx[i]
            nY = curP[1] + dy[i]
            if (nX < 0 or nX >= M or nY < 0 or nY >= N or maze[nX][nY]):
                pstate.append(1024)
                continue
            pstate.append(checked[nX][nY])
        p = pstate.index(min(pstate))
        curP[0] = curP[0] + dx[p]
        curP[1] = curP[1] + dy[p]
        print("curP", curP)
        route.append(curP)
    return route


if __name__ == "__main__":
    #maze = [[0, 0, 0, 0, 0, 1, 0, 0], [1, 1, 1, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0],
     #       [0, 0, 0, 0, 0, 0, 0, 0, 0]]  # 1 for block
    maze = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, 0, 0, 0, 0, 0, 0, 0, 0, -1],
            [-1, 0, 0, 0, 0, 0, 0, 0, 0, -1],
            [-1, 0, -1, -1, -1, -1, -1, -1, 0, -1],
            [-1, 0, -1, 0, 0, 0, 0, -1, 0, -1],
            [-1, 0, -1, 0, -1, -1, -1, -1, 0, -1],
            [-1, 0, 0, 0, 0, 0, 0, -1, 0, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]
    M = len(maze)
    N = len(maze[0])
    # used to avoid double check
    checked = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
    endpoint = [6, 4]
    checked = maze

    startpoint = [1, 1]

    #  up,left,down,right
    dy = [0, -1, 0, 1]
    dx = [-1, 0, 1, 0]
    # check if this cell need to be processed
    generate_map()
    for i in range(len(checked)):
        print(checked[i])
    #print(checked)
    #r = generate_route()
    #print(r)


