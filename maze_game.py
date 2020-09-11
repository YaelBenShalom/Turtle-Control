import recursive_backtracking
import visualization
import wavefrontp

M = 10
N = 8
maze = [[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1, 0, 0, 0, 0, 0, 0, 0, 0,-1],
        [-1, 0, 0, 0, 0, 0, 0, 0, 0,-1],
        [-1, 0,-1,-1,-1,-1,-1,-1, 0,-1],
        [-1, 0,-1, 0, 0, 0, 0,-1, 0,-1],
        [-1, 0,-1, 0,-1,-1,-1,-1, 0,-1],
        [-1, 0, 0, 0, 0, 0, 0,-1, 0,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]
start = (1,1)
goal = (6,4)

if __name__ == "__main__":

    # theRBT = recursive_backtracking.RBT(M, N, maze, start, goal)
    # theRBT.execute()

    theWFP = wavefrontp.WFP(M, N, maze, start, goal)
    theWFP.execute()

    for row in theWFP.solution:
        print(row)

    theApp = visualization.App(M, N, start, goal, maze, theRBT.solution, theRBT.nos)
    theApp.on_execute()