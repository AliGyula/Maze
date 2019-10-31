class mazeSolver:
    def __init__(self,maze):
        self.maze=maze
        self.start=self.maze[0][0]
        self.end=self.maze[len(self.maze)-1][len(self.maze[0])-1]
        self.path=[]
        self.cameFrom=[]
        self.openSet=[]
        self.closedSet=[]
        self.solveMaze()

    def heuristic(self,current,goal):
        return abs(current.x-goal.x)+abs(current.y-goal.y)

    def makePath(self,current):
        self.path.append(current)

        while current.cameFrom!=None:
            current=current.cameFrom
            self.path.append(current)

    def lowestFScore(self):
        index=0
        minF=self.openSet[0].fScore
        for i in range(1,len(self.openSet)):
            if minF>self.openSet[i].fScore:
                minF=self.openSet[i].fScore
                index=i
        return index

    def solveMaze(self):
        self.openSet.append(self.start)
        self.start.gScore=0
        self.start.fScore=self.heuristic(self.start,self.end)

        while len(self.openSet)>0:
            current=self.openSet[self.lowestFScore()]

            if current == self.end:
                self.makePath(current)
                return
            
            self.openSet.remove(current)
            self.closedSet.append(current)

            neighbors=[current.neighbors[i] for i in range(len(current.neighbors)) if current.walls[i]==False]

            for neighbor in neighbors:
                if neighbor in self.closedSet:
                    continue

                tempGScore=current.gScore+1

                if neighbor not in self.openSet:
                    self.openSet.append(neighbor)
                elif tempGScore>=neighbor.gScore:
                    continue
                
                neighbor.cameFrom=current
                neighbor.gScore=tempGScore
                neighbor.fScore=neighbor.gScore+self.heuristic(neighbor,self.end)