class Cell:
    def __init__(self,x,y,size,widthRes,heightRes):
        self.x=x
        self.y=y
        self.size=size
        self.widthRes=widthRes
        self.heightRes=heightRes

        self.gScore=0
        self.fScore=0
        self.cameFrom=None

        if x==-1 and y==-1:
            self.isVisited=True
        else:
            self.isVisited=False

        self.neighbors=[]
        self.walls=[True,True,True,True]
    
    def draw(self,app):
        if self.walls[0]:
            app.canvas.create_line(self.x,self.y,self.x+self.size,self.y,)
        if self.walls[1]:
            app.canvas.create_line(self.x,self.y+self.size,self.x+self.size,self.y+self.size)
        if self.walls[2]:
            app.canvas.create_line(self.x,self.y,self.x,self.y+self.size)
        if self.walls[3]:
            app.canvas.create_line(self.x+self.size,self.y,self.x+self.size,self.y+self.size)
    
    def setNs(self,i,j,maze):
        if i-1>=0:
            self.neighbors.append(maze[i-1][j])
        else:
            self.neighbors.append(Cell(-1,-1,self.size,self.widthRes,self.heightRes))
        if i+1<=self.heightRes-1:
            self.neighbors.append(maze[i+1][j])
        else:
            self.neighbors.append(Cell(-1,-1,self.size,self.widthRes,self.heightRes))
        if j-1>=0:
            self.neighbors.append(maze[i][j-1])
        else:
            self.neighbors.append(Cell(-1,-1,self.size,self.widthRes,self.heightRes))
        if j+1<=self.widthRes-1:
            self.neighbors.append(maze[i][j+1])
        else:
            self.neighbors.append(Cell(-1,-1,self.size,self.widthRes,self.heightRes))