import sys

from tkinter import *

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
        self.robotCoords = (50, 50, 70, 70)
        self.createMap(self.robotCoords)
        
        self.x1, self.y1, self.x2, self.y2 = self.zone.coords(self.robot)
        
        
    def createMap(self, crds):

        self.coords = crds
        # split each if into it's own seperate function: zone1(), zone2() etc...
        if self.robotLocation == 1:
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
          #  self.photo = PhotoImage(file="FUEL.png")
           # self.label = Label(self.zone, image=self.photo)
            #self.label.grid(padx=320, pady=250)
            self.initiateGameplay()

        if self.robotLocation == 2:
            self.zone.pack_forget()
            self.zone = Canvas(self.window, width=1000, height=600, bg='cyan')
            self.window.title("Zone 2")
            self.zone.pack(fill=BOTH, expand=1)
            self.teleport2 = self.zone.create_line(3, 270, 3, 310, fill ="green", width=2)
            self.teleport3 = self.zone.create_line(996, 270, 996, 310, fill="green", width=2)
            self.teleport7 = self.zone.create_line(500, 597, 450, 597, fill="green", width=2)
            self.zone.x_min = 0
            self.zone.y_min = 0
            self.zone.x_max = 991
            self.zone.y_max = 600
            self.robot = self.zone.create_rectangle(self.coords)
            self.canvas2(20,20,50,50)
            self.initiateGameplay()

        if self.robotLocation == 6:
            self.zone.pack_forget()
            self.zone = Canvas(self.window, width=1000, height=600, bg='cyan')
            self.window.title("Zone 4")
            self.zone.pack(fill=BOTH, expand=1)
            self.teleport1 = self.zone.create_line(500, 3, 450, 3, fill="green", width=2)
            self.teleport6 = self.zone.create_line(996, 270, 996, 310, fill ="green", width=2)
            self.zone.x_min = 0
            self.zone.y_min = 0
            self.zone.x_max = 991
            self.zone.y_max = 600
            self.robot = self.zone.create_rectangle(self.coords)
            self.canvas4(20,20,50,50)
            self.initiateGameplay()

        if self.robotLocation == 3:
            self.zone.pack_forget()
            self.zone = Canvas(self.window, width=1000, height=600, bg='cyan')
            self.window.title("Zone 3")
            self.zone.pack(fill=BOTH, expand=1)
            self.teleport3 = self.zone.create_line(3, 270, 3, 310, fill="green", width=2)
            self.teleport4 = self.zone.create_line(500, 597, 450, 597, fill="green", width=2)
            self.zone.x_min = 0
            self.zone.y_min = 0
            self.zone.x_max = 991
            self.zone.y_max = 600
            self.robot = self.zone.create_rectangle(self.coords)
            self.canvas3(20,20,50,50)
            self.initiateGameplay()

        if self.robotLocation == 4:
            self.zone.pack_forget()
            self.zone = Canvas(self.window, width=1000, height=600, bg='cyan')
            self.window.title("Zone 6")
            self.zone.pack(fill=BOTH, expand=1)
            self.teleport4 = self.zone.create_line(500, 3, 450, 3, fill="green", width=2)
            self.teleport5 = self.zone.create_line(3, 270, 3, 310, fill ="green", width=2)
            self.zone.x_min = 0
            self.zone.y_min = 0
            self.zone.x_max = 991
            self.zone.y_max = 600
            self.robot = self.zone.create_rectangle(self.coords)
            self.canvas6(20,20,50,50)
            self.initiateGameplay()

        if self.robotLocation == 5:
            self.zone.pack_forget()
            self.zone = Canvas(self.window, width=1000, height=600, bg='cyan')
            self.window.title("Zone 5")
            self.zone.pack(fill=BOTH, expand=1)
            self.teleport5 = self.zone.create_line(3, 270, 3, 310, fill ="green", width=2)
            self.teleport6 = self.zone.create_line(996, 270, 996, 310, fill ="green", width=2)
            self.teleport7 = self.zone.create_line(500, 3, 450, 3, fill="green", width=2)
            self.zone.x_min = 0
            self.zone.y_min = 0
            self.zone.x_max = 991
            self.zone.y_max = 600
            self.robot = self.zone.create_rectangle(self.coords)
            self.canvas5(20,20,50,50)
            self.initiateGameplay()
    def canvas1(self, topx,topy,botx,boty):
            room = open("MAP 1.txt","r")
            content = room.readlines()
            room.close()
            for i in range(len(content)):
                for symbol in content[i]:
                    if symbol == "W":
                        self.wall = self.zone.create_rectangle(topx,topy,botx,boty, fill="black")
                        botx += 50
                        topx +=20
                    elif symbol=="\n":
                        topy = boty
                        boty += 30
                        botx=50
                        topx=20
                    elif symbol=="0":
                       botx += 50
                       topx = botx - 30
                    elif symbol=="F":
                        self.photo = PhotoImage(file="FUEL.png")
                        self.label = Label(self.zone, image=self.photo)
                        self.label.grid(padx=topx, pady=topy)
                        botx += 50
                        topx = botx - 30
    def canvas2(self, topx,topy,botx,boty):
            room = open("MAP 2.txt","r")
            content = room.readlines()
            room.close()
            for i in range(len(content)):
                for symbol in content[i]:
                    if symbol == "W":
                        self.wall = self.zone.create_rectangle(topx,topy,botx,boty, fill="black")
                        botx += 50
                        topx +=20
                    elif symbol=="\n":
                        topy = boty
                        boty += 30
                        botx=50
                        topx=20
                    elif symbol=="0":
                       botx += 50
                       topx = botx - 30
                    elif symbol=="F":
                        self.photo = PhotoImage(file="FUEL.png")
                        self.label = Label(self.zone, image=self.photo)
                        self.label.grid(padx=topx, pady=topy)
                        botx += 50
                        topx = botx - 30
    def canvas3(self, topx,topy,botx,boty):
            room = open("MAP 3.txt","r")
            content = room.readlines()
            room.close()
            for i in range(len(content)):
                for symbol in content[i]:
                    if symbol == "W":
                        self.wall = self.zone.create_rectangle(topx,topy,botx,boty, fill="black")
                        botx += 50
                        topx +=20
                    elif symbol=="\n":
                        topy = boty
                        boty += 30
                        botx=50
                        topx=20
                    elif symbol=="0":
                       botx += 50
                       topx = botx - 30
    def canvas4(self, topx,topy,botx,boty):
            room = open("MAP 4.txt","r")
            content = room.readlines()
            room.close()
            for i in range(len(content)):
                for symbol in content[i]:
                    if symbol == "W":
                        self.wall = self.zone.create_rectangle(topx,topy,botx,boty, fill="black")
                        botx += 50
                        topx +=20
                    elif symbol=="\n":
                        topy = boty
                        boty += 30
                        botx=50
                        topx=20
                    elif symbol=="0":
                       botx += 50
                       topx = botx - 30
    def canvas5(self, topx,topy,botx,boty):
            room = open("MAP 5.txt","r")
            content = room.readlines()
            room.close()
            for i in range(len(content)):
                for symbol in content[i]:
                    if symbol == "W":
                        self.wall = self.zone.create_rectangle(topx,topy,botx,boty, fill="black")
                        botx += 50
                        topx +=20
                    elif symbol=="\n":
                        topy = boty
                        boty += 30
                        botx=50
                        topx=20
                    elif symbol=="0":
                       botx += 50
                       topx = botx - 30
    def canvas6(self, topx,topy,botx,boty):
            room = open("MAP 6.txt","r")
            content = room.readlines()
            room.close()
            for i in range(len(content)):
                for symbol in content[i]:
                    if symbol == "W":
                        self.wall = self.zone.create_rectangle(topx,topy,botx,boty, fill="black")
                        botx += 50
                        topx +=20
                    elif symbol=="\n":
                        topy = boty
                        boty += 30
                        botx=50
                        topx=20
                    elif symbol=="0":
                       botx += 50
                       topx = botx - 30

        
        
    def initiateGameplay(self):
        # Temporary movement for testing purposes
        # Refactor this code when the time comes
        
        def rightKey(event):
            self.x1, self.y1, self.x2, self.y2 = self.zone.coords(self.robot)
            
            
            if self.x2 >= self.zone.x_max or self.battery == 0:
                self.zone.coords(self.robot, self.x1, self.y1, self.x2, self.y2)
            else:
                self.zone.coords(self.robot, self.x1+10, self.y1, self.x2+10, self.y2)
##                self.battery -= 0.5

            if self.robotLocation == 1:

                self.teleportTuple2 = self.zone.find_overlapping(996, 270, 996, 310)
                
                if self.robot in self.teleportTuple2:
                    self.robotLocation = 2
                    self.zone.pack_forget()
                    self.robotCoords = (4, 280, 24, 300)
                    self.createMap(self.robotCoords)
                else:
                    pass

            if self.robotLocation == 2:

                self.teleportTuple3 = self.zone.find_overlapping(990,280,996,300)

                if self.robot in self.teleportTuple3:
                    self.robotLocation = 3
                    self.robotCoords = (4, 280, 24, 300)
                    self.createMap(self.robotCoords)
                else:
                    pass

            if self.robotLocation == 5:

                self.teleportTuple5 = self.zone.find_overlapping(990, 280, 996, 310)
                
                if self.robot in self.teleportTuple5:
                    self.robotLocation = 4
                    self.zone.pack_forget()
                    self.robotCoords = (4, 280, 24, 300)
                    self.createMap(self.robotCoords)
                else:
                    pass

            if self.robotLocation == 6:

                self.teleportTuple6 = self.zone.find_overlapping(996, 270, 996, 310)

                if self.robot in self.teleportTuple6:
                    self.robotLocation = 5
                    self.zone.pack_forget()
                    self.robotCoords = (4, 280, 24, 300)
                    self.createMap(self.robotCoords)
                else:
                    pass

                
        def leftKey(event):
            self.x1, self.y1, self.x2, self.y2 = self.zone.coords(self.robot)
            
            
            if self.x1 <= self.zone.x_min or self.battery == 0:
                self.zone.coords(self.robot, self.x1, self.y1, self.x2, self.y2)
            else:
                self.zone.coords(self.robot, self.x1-10, self.y1, self.x2-10, self.y2)
##                self.battery -= 0.5

            if self.robotLocation == 2:

                self.teleportTuple1 = self.zone.find_overlapping(3, 270, 3, 310)

                if self.robot in self.teleportTuple1:
                    self.robotLocation = 1
                    self.zone.pack_forget()
                    self.robotCoords = (976, 270, 996, 290)
                    self.createMap(self.robotCoords)

            if self.robotLocation ==3:

                self.teleportTuple3 = self.zone.find_overlapping(3, 270, 3, 310)

                if self.robot in self.teleportTuple3:
                    self.robotLocation = 2
                    self.zone.pack_forget()
                    self.robotCoords = (976, 270, 996, 290)
                    self.createMap(self.robotCoords)
                else:
                    pass

            if self.robotLocation == 4:

                self.teleportTuple5 = self.zone.find_overlapping(3, 270, 3, 310)

                if self.robot in self.teleportTuple5:
                    self.robotLocation = 5
                    self.zone.pack_forget()
                    self.robotCoords = (976, 270, 996, 290)
                    self.createMap(self.robotCoords)
                else:
                    pass

            if self.robotLocation == 5:

                self.teleportTuple6 = self.zone.find_overlapping(3, 270, 3, 310)

                if self.robot in self.teleportTuple6:
                    self.robotLocation = 6
                    self.zone.pack_forget()
                    self.robotCoords = (976, 270, 996, 290)
                    self.createMap(self.robotCoords)
                else:
                    pass
                    
        def upKey(event):
            self.x1, self.y1, self.x2, self.y2 = self.zone.coords(self.robot)
            

            if self.y1 <= self.zone.y_min or self.battery == 0:
                self.zone.coords(self.robot, self.x1, self.y1, self.x2, self.y2)
            else:
                self.zone.coords(self.robot, self.x1, self.y1-10, self.x2, self.y2-10)
##                self.battery -= 0.5

           

            if self.robotLocation == 6:

                self.teleportTuple1 = self.zone.find_overlapping(470, 1, 495, 1)

                if self.robot in self.teleportTuple1:
                    self.robotLocation = 1
                    self.zone.pack_forget()
                    self.robotCoords = (447, 627, 470, 605)
                    self.createMap(self.robotCoords)
                else:
                    pass

            if self.robotLocation == 4:

                self.teleportTuple4 = self.zone.find_overlapping(470,1, 495, 1)

                if self.robot in self.teleportTuple4:
                    self.robotLocation = 3
                    self.zone.pack_forget()
                    self.robotCoords = (447, 627, 470, 605)
                    self.createMap(self.robotCoords)
                else:
                    pass

            if self.robotLocation == 5:

                self.teleportTuple7 = self.zone.find_overlapping(470, 1, 495, 1)

                if self.robot in self.teleportTuple7:
                    self.robotLocation = 2
                    self.zone.pack_forget()
                    self.robotCoords = (447, 627, 470, 605)
                    self.createMap(self.robotCoords)
                else:
                    pass
                      
        def downKey(event):
            self.x1, self.y1, self.x2, self.y2 = self.zone.coords(self.robot)
            
            
            if self.y2 >= self.zone.y_max or self.battery == 0:
                self.zone.coords(self.robot, self.x1, self.y1, self.x2, self.y2)

            else:
                self.zone.coords(self.robot, self.x1, self.y1+10, self.x2, self.y2+10)
##                self.battery -= 0.5

            if self.robotLocation == 1:

                self.teleportTuple1 = self.zone.find_overlapping(500, 597, 450, 597)
                
                if self.robot in self.teleportTuple1:
                    self.robotLocation = 6
                    self.robotCoords = (460, 3, 480, 23)
                    self.createMap(self.robotCoords)
                else:
                    pass
            if self.robotLocation == 3:

                self.teleportTuple4 = self.zone.find_overlapping(510, 605, 450, 597)
                
                if self.robot in self.teleportTuple4:
                    self.robotLocation = 4
                    self.robotCoords = (460, 3, 480, 23)
                    self.createMap(self.robotCoords)
                else:
                    pass

            if self.robotLocation == 2:

                self.teleportTuple7 = self.zone.find_overlapping(510, 605, 450, 597)

                if self.robot in self.teleportTuple7:
                    self.robotLocation = 5
                    self.robotCoords= (460, 3, 480, 23)
                    self.createMap(self.robotCoords)
                else:
                    pass

        self.battery = 100.0
        self.zone.focus_set()
        self.zone.bind("<Right>", rightKey)
        self.zone.bind("<Left>", leftKey)
        self.zone.bind("<Up>", upKey)
        self.zone.bind("<Down>", downKey)
        
def main():
    window = Tk()
    window.geometry("400x200+450+300") # Window needs to be centered on each PC screen 
    game = userInterface(window)
    window.mainloop()

if __name__=='__main__':
    sys.exit(main())
