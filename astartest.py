import sys

from tkinter import *

import numpy

from heapq import *

import time



def heuristic(a, b):
    dx, dy = b[0] - a[0], b[1] - a[1]
    return abs(dx) + abs(dy)

def astar(array, start, goal):

    neighbors = [(0,1),(0,-1),(1,0),(-1,0)]

    close_set = set()
    came_from = {}
    gscore = {start:0}
    fscore = {start:heuristic(start, goal)}
    oheap = []

    heappush(oheap, (fscore[start], start))
    
    while oheap:

        current = heappop(oheap)[1]

        if current == goal:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            return data

        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j            
            tentative_g_score = gscore[current] + heuristic(current, neighbor)
            if 0 <= neighbor[0] < array.shape[0]:
                if 0 <= neighbor[1] < array.shape[1]:                
                    if array[neighbor[0]][neighbor[1]] == 1:
                        continue
                else:
                    # array bound y walls
                    continue
            else:
                # array bound x walls
                continue
                
            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue
                
            if  tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heappush(oheap, (fscore[neighbor], neighbor))
                
    return False

'''Here is an example of using my algo with a numpy array,
   astar(array, start, destination)
   astar function returns a list of points (shortest path)'''

nmap1 = numpy.array([
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1],
    [1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1],
    [1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1],
    [1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1],
    [1,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,1,0,1],
    [1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0],
    [1,0,1,1,0,1,1,1,1,0,1,1,1,0,0,0,1,0,0],
    [1,0,0,1,0,0,0,1,0,0,0,0,1,0,1,0,1,0,1],
    [1,0,0,1,0,0,0,1,0,0,0,0,1,1,1,0,0,0,1],
    [1,1,0,1,0,1,0,1,0,1,1,0,1,0,0,0,0,0,1],
    [1,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,1,1,1],
    [1,0,0,1,0,1,1,0,0,0,1,0,0,0,1,1,1,0,1],
    [1,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1],
    [1,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1]])

class userInterface():

    def __init__ (self, window):
        # Initializes the first window
         
        self.window = window
        self.menuCanvas = Canvas(self.window, width=300, height=300, bg='white')
        self.menuCanvas.pack(fill=BOTH, expand=1)

        self.buttonFrame = Frame(self.menuCanvas)
        self.buttonFrame.pack(side="top", pady=25)

        self.startButton = Button(self.menuCanvas, text="Play game", command = lambda: self.loadGameArena())
        self.startButton.pack()

        self.settingsButton = Button(self.menuCanvas, text="Settings")
        self.settingsButton.pack()

        self.exitButton = Button(self.menuCanvas, text="Exit", command = lambda: self.window.destroy())
        self.exitButton.pack()

    def settings(self):
        # Might need to edit this a little. 
        self.SettingsWindow = Tk()
        self.label = Label(self.SettingsWindow, text="There should be settings here. ")
        self.label.pack()
        self.SettingsWindow.mainloop()

    def loadGameArena(self):
        # Eventually this will have a new game/load game option prior to loading the actual game
        self.menuCanvas.pack_forget()
        theGame = theRobotGame(self.window)

class theRobotGame():

    
    def __init__(self, window):
        self.window = window
        self.window.geometry("1000x600+200+60")
        self.robotLocation = 1
        self.robotCoords = (50, 50, 80, 80)
        self.createMap(self.robotCoords)
        self.x1, self.y1, self.x2, self.y2 = self.zone.coords(self.robot)
        
        
    def createMap(self, crds):

        self.coords = crds
        # split each if into it's own seperate function: zone1(), zone2() etc...
        
        self.zone = Canvas(self.window, width=1000, height=600, bg='cyan')
        self.window.title("Zone 1")
        self.zone.pack(fill=BOTH, expand=1)
        self.teleport1 = self.zone.create_line(500, 597, 450, 597, fill="green", width=2)
        self.teleport2 = self.zone.create_line(996, 270, 996, 310, fill ="green", width=2)
        self.zone.x_min = 0
        self.zone.y_min = 0
        self.zone.x_max = 991
        self.zone.y_max = 600
        self.robot = self.zone.create_rectangle(self.coords)
        self.canvas1(20,20,50,50)
        self.initiateGameplay()
##
##        if self.robotLocation == 2:
##            self.zone.pack_forget()
##            self.zone = Canvas(self.window, width=1000, height=600, bg='cyan')
##            self.window.title("Zone 2")
##            self.zone.pack(fill=BOTH, expand=1)
##            self.teleport2 = self.zone.create_line(3, 270, 3, 310, fill ="green", width=2)
##            self.teleport3 = self.zone.create_line(996, 270, 996, 310, fill="green", width=2)
##            self.teleport7 = self.zone.create_line(500, 597, 450, 597, fill="green", width=2)
##            self.zone.x_min = 0
##            self.zone.y_min = 0
##            self.zone.x_max = 991
##            self.zone.y_max = 600
##            self.robot = self.zone.create_rectangle(self.coords)
##            self.canvas2(20,20,50,50)
##            self.initiateGameplay()
##
##        if self.robotLocation == 6:
##            self.zone.pack_forget()
##            self.zone = Canvas(self.window, width=1000, height=600, bg='cyan')
##            self.window.title("Zone 6")
##            self.zone.pack(fill=BOTH, expand=1)
##            self.teleport1 = self.zone.create_line(500, 3, 450, 3, fill="green", width=2)
##            self.teleport6 = self.zone.create_line(996, 270, 996, 310, fill ="green", width=2)
##            self.zone.x_min = 0
##            self.zone.y_min = 0
##            self.zone.x_max = 991
##            self.zone.y_max = 600
##            self.robot = self.zone.create_rectangle(self.coords)
##            self.canvas6(20,20,50,50)
##            self.initiateGameplay()
##
##        if self.robotLocation == 3:
##            self.zone.pack_forget()
##            self.zone = Canvas(self.window, width=1000, height=600, bg='cyan')
##            self.window.title("Zone 3")
##            self.zone.pack(fill=BOTH, expand=1)
##            self.teleport3 = self.zone.create_line(3, 270, 3, 310, fill="green", width=2)
##            self.teleport4 = self.zone.create_line(500, 597, 450, 597, fill="green", width=2)
##            self.zone.x_min = 0
##            self.zone.y_min = 0
##            self.zone.x_max = 991
##            self.zone.y_max = 600
##            self.robot = self.zone.create_rectangle(self.coords)
##            self.canvas3(20,20,50,50)
##            self.initiateGameplay()
##
##        if self.robotLocation == 4:
##            self.zone.pack_forget()
##            self.zone = Canvas(self.window, width=1000, height=600, bg='cyan')
##            self.window.title("Zone 4")
##            self.zone.pack(fill=BOTH, expand=1)
##            self.teleport4 = self.zone.create_line(500, 3, 450, 3, fill="green", width=2)
##            self.teleport5 = self.zone.create_line(3, 270, 3, 310, fill ="green", width=2)
##            self.zone.x_min = 0
##            self.zone.y_min = 0
##            self.zone.x_max = 991
##            self.zone.y_max = 600
##            self.robot = self.zone.create_rectangle(self.coords)
##            self.canvas4(20,20,50,50)
##            self.initiateGameplay()
##
##        if self.robotLocation == 5:
##            self.zone.pack_forget()
##            self.zone = Canvas(self.window, width=1000, height=600, bg='cyan')
##            self.window.title("Zone 5")
##            self.zone.pack(fill=BOTH, expand=1)
##            self.teleport5 = self.zone.create_line(3, 270, 3, 310, fill ="green", width=2)
##            self.teleport6 = self.zone.create_line(996, 270, 996, 310, fill ="green", width=2)
##            self.teleport7 = self.zone.create_line(500, 3, 450, 3, fill="green", width=2)
##            self.zone.x_min = 0
##            self.zone.y_min = 0
##            self.zone.x_max = 991
##            self.zone.y_max = 600
##            self.robot = self.zone.create_rectangle(self.coords)
##            self.canvas5(20,20,50,50)
##            self.initiateGameplay()
        
    def canvas1(self, topx,topy,botx,boty):
            room = open("MAP 1.txt","r")
            content = room.readlines()
            room.close()
            for i in range(len(content)):
                for symbol in content[i]:
                    if symbol == "W":
                        self.wall = self.zone.create_rectangle(topx,topy,botx,boty, fill="black")
                        botx += 30
                        topx +=20
                    elif symbol=="\n":
                        topy = boty
                        boty += 30
                        botx=50
                        topx=20
                    elif symbol=="0":
                       botx += 30
                       topx = botx - 30
                       
##    def canvas2(self, topx,topy,botx,boty):
##            room = open("MAP 2.txt","r")
##            content = room.readlines()
##            room.close()
##            for i in range(len(content)):
##                for symbol in content[i]:
##                    if symbol == "W":
##                        self.wall = self.zone.create_rectangle(topx,topy,botx,boty, fill="black")
##                        botx += 50
##                        topx +=20
##                    elif symbol=="\n":
##                        topy = boty
##                        boty += 30
##                        botx=50
##                        topx=20
##                    elif symbol=="0":
##                       botx += 50
##                       topx = botx - 30
##    def canvas3(self, topx,topy,botx,boty):
##            room = open("MAP 3.txt","r")
##            content = room.readlines()
##            room.close()
##            for i in range(len(content)):
##                for symbol in content[i]:
##                    if symbol == "W":
##                        self.wall = self.zone.create_rectangle(topx,topy,botx,boty, fill="black")
##                        botx += 50
##                        topx +=20
##                    elif symbol=="\n":
##                        topy = boty
##                        boty += 30
##                        botx=50
##                        topx=20
##                    elif symbol=="0":
##                       botx += 50
##                       topx = botx - 30
##    def canvas4(self, topx,topy,botx,boty):
##            room = open("MAP 4.txt","r")
##            content = room.readlines()
##            room.close()
##            for i in range(len(content)):
##                for symbol in content[i]:
##                    if symbol == "W":
##                        self.wall = self.zone.create_rectangle(topx,topy,botx,boty, fill="black")
##                        botx += 50
##                        topx +=20
##                    elif symbol=="\n":
##                        topy = boty
##                        boty += 30
##                        botx=50
##                        topx=20
##                    elif symbol=="0":
##                       botx += 50
##                       topx = botx - 30
##    def canvas5(self, topx,topy,botx,boty):
##            room = open("MAP 5.txt","r")
##            content = room.readlines()
##            room.close()
##            for i in range(len(content)):
##                for symbol in content[i]:
##                    if symbol == "W":
##                        self.wall = self.zone.create_rectangle(topx,topy,botx,boty, fill="black")
##                        botx += 50
##                        topx +=20
##                    elif symbol=="\n":
##                        topy = boty
##                        boty += 30
##                        botx=50
##                        topx=20
##                    elif symbol=="0":
##                       botx += 50
##                       topx = botx - 30
##    def canvas6(self, topx,topy,botx,boty):
##            room = open("MAP 6.txt","r")
##            content = room.readlines()
##            room.close()
##            for i in range(len(content)):
##                for symbol in content[i]:
##                    if symbol == "W":
##                        self.wall = self.zone.create_rectangle(topx,topy,botx,boty, fill="black")
##                        botx += 50
##                        topx +=20
##                    elif symbol=="\n":
##                        topy = boty
##                        boty += 30
##                        botx=50
##                        topx=20
##                    elif symbol=="0":
##                       botx += 50
##                       topx = botx - 30

        
        
    def initiateGameplay(self):
        self.zone.focus_set()
        
        pa,pb = 1,1
        l = len(astar(nmap1, (1,1), (17,9))) - 1
        while l >= 0:
            self.zone.update()
            self.x1, self.y1, self.x2, self.y2 = self.zone.coords(self.robot)
            a,b = astar(nmap1, (1,1), (17,9)).pop(l)
            print("step %d" %l)
            print(a - pa)
            print(b - pb)
            #print(pa)
            #print(pb)
            ##down
            if a - pa == 1 and b - pb == 0:
                self.zone.coords(self.robot, self.x1, self.y1+30, self.x2, self.y2+30)
                self.x1, self.y1, self.x2, self.y2 = self.zone.coords(self.robot)
                time.sleep(1)
                print("down")
                
            ##up
            if a - pa == -1 and b - pb == 0:
                self.zone.coords(self.robot, self.x1, self.y1-30, self.x2, self.y2-30)
                self.x1, self.y1, self.x2, self.y2 = self.zone.coords(self.robot)
                time.sleep(1)
                print("up")
            ##right
            if a - pa == 0 and b - pb == 1:
                self.zone.coords(self.robot, self.x1+30, self.y1, self.x2+30, self.y2)
                self.x1, self.y1, self.x2, self.y2 = self.zone.coords(self.robot)
                time.sleep(1)
                print("right")
            ##left
            if a - pa == 0 and b - pb == -1:
                self.zone.coords(self.robot, self.x1-30, self.y1, self.x2-30, self.y2)
                self.x1, self.y1, self.x2, self.y2 = self.zone.coords(self.robot)
                time.sleep(1)
                print("left")
            l = l - 1
            pa,pb = a,b
            
        
def main():
    window = Tk()
    window.geometry("400x200+450+300") # Window needs to be centered on each PC screen 
    game = userInterface(window)
    window.mainloop()

if __name__=='__main__':
    sys.exit(main())
