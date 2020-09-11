from pygame.locals import *
import pygame
import time

class Maze:
    def __init__(self, M, N, start, goal, maze, solution, nos):
        self.M = M
        self.N = N
        self.maze = maze
        self.start = start
        self.goal = goal
        self.solution = solution
        self.nos = nos

        self.robotX = start[0]
        self.robotY = start[1]

    def draw(self, display, robotImage, blockImage, startImage, goalImage, step):
        x = 0
        y = 0
        for i in range(0, self.M*self.N):
            if self.solution[y][x] == -1:
                display.blit(blockImage, (x*50, y*50))
            else:
                # draw start cell and goal cell
                if (x,y) == self.start:
                    display.blit(startImage, (x*50, y*50))
                elif (x,y) == self.goal:
                    display.blit(goalImage, (x*50, y*50))
                # draw robot by step
                if step > self.nos:
                    if self.solution[y][x] == self.nos:
                        display.blit(robotImage, (x*50, y*50))
                else:
                    if self.solution[y][x] == step:
                        display.blit(robotImage, (x*50, y*50))

            x += 1
            if x > self.M-1:
                x = 0 
                y = y + 1

class App: 
    def __init__(self, M, N, start, goal, maze, solution, nos):
        self._running = True
        self._automatic = False
        self._interactive = False
        self._display = None
        self.robotImage = None
        self.blockImage = None
        self.startImage = None
        self.goalImage = None
        self.windowWidth = M*50
        self.windowHeight = N*50
        self.maze = Maze(M, N, start, goal, maze, solution, nos)
 
    def on_init(self):
        pygame.init()
        self._display = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
        self._running = True
        self.robotImage = pygame.image.load("robot.png").convert_alpha()
        self.blockImage = pygame.image.load("block.png").convert_alpha()
        self.startImage = pygame.image.load("start.png").convert_alpha()
        self.goalImage = pygame.image.load("goal.png").convert_alpha()
    
    def render(self, step):
        self._display.fill((0,0,0))
        self.maze.draw(self._display, self.robotImage, self.blockImage, self.startImage, self.goalImage, step)
        pygame.display.flip()
 
    def cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        startTime = time.time()

        if self.on_init() == False:
            self._running = False
 
        while(self._running):
            pygame.event.pump()
            keys = pygame.key.get_pressed()
 
            if (keys[K_ESCAPE]):
                self._running = False

            step = int((time.time() - startTime)*2) + 1
            
            self.render(step)

        self.cleanup()

def convert(src, dst):
    pygame.init()
    pygame.display.set_mode()
    image = pygame.image.load(src).convert_alpha()
    for x in range(image.get_width()):
        for y in range(image.get_height()):
            if image.get_at((x,y)) == (255, 255, 255, 255):
                image.set_at((x,y), (255, 255, 255, 0))
    pygame.image.save(image, dst)

# if __name__ == "__main__":

#     theApp = App()
#     theApp.on_execute()