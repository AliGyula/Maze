import random

class mazeGenerator:

	def __init__(self,maze,start):
		self.maze=maze
		self.finalMaze=[]
		self.stack=[]
		self.start=start
		self.mazeGenerator(self.maze,self.stack)

	def notAllVisited(self,maze):
		for i in range(len(maze)):
			for j in range(len(maze[i])):
				if maze[i][j].isVisited==False:
					return True
		return False

	def mazeGenerator(self,maze,stack):
		current=self.start
		while (self.notAllVisited(maze)):
			n=[]
			for i in range(len(current.neighbors)):
				if current.neighbors[i].isVisited==False:
					n.append(current.neighbors[i])

			if len(n)>0:
				a=random.randrange(0,len(current.neighbors))

				while current.neighbors[a].isVisited==True:
					a=random.randrange(0,len(current.neighbors))
				stack.append(current)

				if a==0:
					current.walls[0]=False
					current.neighbors[a].walls[1]=False
				elif a == 1:
					current.walls[1]=False
					current.neighbors[a].walls[0]=False
				elif a==2:
					current.walls[2]=False
					current.neighbors[a].walls[3]=False
				elif a == 3:
					current.walls[3]=False
					current.neighbors[a].walls[2]=False

				current=current.neighbors[a]
				current.isVisited=True

			elif len(stack)>0:
				current = stack[len(stack)-1]
				del stack[len(stack)-1]
			elif len(stack)==0:
				return

			self.finalMaze.append(current)