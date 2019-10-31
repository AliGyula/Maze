from gui import gui
from cell import Cell
from tkinter import Button

class levelEditor:
	def __init__(self,width,height,size):
		self.width=width
		self.height=height

		self.gui=gui(self.width,self.height,"Level editor")
		
		self.widthRes=int(self.gui.winWidth/size)
		self.heightRes=int(self.gui.winHeight/size)
		self.size=size
		self.maze=[]
		self.selectedCells=[]

		makeMaze(self.maze,self.widthRes,self.heightRes,self.size)
		self.drawMaze()

		btn=Button(self.gui.master,text='Done',command=self.gui.master.destroy)
		btn.pack()

		self.gui.master.bind('<Button-1>', self.placeCell)
		self.gui.master.bind('<B1-Motion>', self.placeCell)
		self.gui.master.bind('<Button-3>', self.removeCell)
		self.gui.master.bind('<B3-Motion>', self.removeCell)

		self.gui.mainloop()

		

	def placeCell(self,event):
		x,y=event.x,event.y

		if event.widget==self.gui.canvas:

			i=int(y/self.size)
			j=int(x/self.size)

			if self.maze[i][j].isVisited==False:
				self.maze[i][j].isVisited=True
				self.selectedCells.append(self.gui.canvas.create_rectangle(self.maze[i][j].x+1,self.maze[i][j].y+1,self.maze[i][j].x+self.size-1,self.maze[i][j].y+self.size-1,fill='black'))

	def removeCell(self,event):
		index=-1
		x,y=event.x,event.y

		if event.widget==self.gui.canvas:

			i=int(y/self.size)
			j=int(x/self.size)

			for u in range(len(self.selectedCells)):
				if [float(self.maze[i][j].x+1),float(self.maze[i][j].y+1),float(self.maze[i][j].x+self.size-1),float(self.maze[i][j].y+self.size-1)]==self.gui.canvas.coords(self.selectedCells[u]):
					index=u

			if self.maze[i][j].isVisited:
				self.maze[i][j].isVisited=False
				self.gui.canvas.delete(self.selectedCells[index])

	def drawMaze(self):
		for i in range(len(self.maze)):
			for j in range(len(self.maze[i])):
				self.maze[i][j].draw(self.gui)

def makeMaze(maze,widthRes,heightRes,size):
	for i in range(heightRes):
		maze.append([])
		for j in range(widthRes):
			maze[i].append(Cell(j*size+2,i*size+2,size,widthRes,heightRes))

	for i in range(heightRes):
		for j in range(widthRes):
			maze[i][j].setNs(i,j,maze)
		