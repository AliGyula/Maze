from gui import gui
from settingsGUI import settings
from mazeGenerator import mazeGenerator
from mazeSolver import mazeSolver
from levelEditor import levelEditor,makeMaze
from cell import Cell

import time

maxSpeed=101
maze=[]

settings=settings()
settings.mainloop()

width=int(settings.width)
height=int(settings.height)
size=int(settings.cell)
speed=int(settings.speed)
isLaunching=settings.isLaunching

if isLaunching:
        levelEditor=levelEditor(width,height,size)
        maze=levelEditor.maze

gui = gui(width,height,"Maze")

widthRes=int(gui.winWidth/size)
heightRes=int(gui.winHeight/size)

if len(maze)==0:
        makeMaze(maze,widthRes,heightRes,size)

mazeGenerator=mazeGenerator(maze,maze[0][0])

point=gui.canvas.create_rectangle(mazeGenerator.finalMaze[0].x,mazeGenerator.finalMaze[0].y,mazeGenerator.finalMaze[0].x+size,mazeGenerator.finalMaze[0].y+size,fill='red',outline='')

for i in range(len(mazeGenerator.finalMaze)):
        gui.canvas.coords(point,mazeGenerator.finalMaze[i].x,mazeGenerator.finalMaze[i].y,mazeGenerator.finalMaze[i].x+size,mazeGenerator.finalMaze[i].y+size)
        mazeGenerator.finalMaze[i].draw(gui)
        time.sleep((maxSpeed-speed)/1000.0)
        gui.update()

gui.canvas.delete(point)
gui.update()

mazeSolver = mazeSolver(maze)

offSet=int(size*0.7)

for i in range(len(mazeSolver.path)):
        index=(len(mazeSolver.path)-1-i)
        gui.canvas.create_oval(mazeSolver.path[index].x+offSet,mazeSolver.path[index].y+offSet,mazeSolver.path[index].x+size-offSet,mazeSolver.path[index].y+size-offSet,fill='green',outline='')
        time.sleep((maxSpeed-speed)/1000.0)
        gui.update()

gui.mainloop()