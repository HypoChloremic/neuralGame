import baseObject

class ObjectDriver:
    def __init__(self, player, width, height):    
        self.obstacleTimer = 0
        self.obstacles = []
        
        
    
        # constants
        self.minObsInterval = 100
        self.width  = width
        self.height = height
        
    def show(self,player):
        player.show()
        
        for obs in self.obstacles:
            if obs:
                obs.show()
    
    def move(self, player):
        self.obstacleTimer += 1        
        
        if self.obstacleTimer > self.minObsInterval + random(10):
            self.addObstacle()
        
        player.move()
        
        for obsInd in range(len(self.obstacles)):
            if self.obstacles[obsInd]:
                self.obstacles[obsInd].move()
                
                if self.obstacles[obsInd].pos.x < 0:
                    self.obstacles[obsInd] = None
                
    def addObstacle(self):
        obj = baseObject.BaseObject(width=self.width, height=self.height, bool=random(3))
                
        if self.obstacles:
            for i in range(len(self.obstacles)):
                if self.obstacles[i] == None:
                    self.obstacles[i] = obj
                    self.obstacleTimer = 0
                
                elif self.obstacles[i] and i != len(self.obstacles)-1:
                    pass
                
                else:
                    self.obstacles.append(obj)
                    self.obstacleTimer = 0
        else:
            self.obstacles.append(obj)
            self.obstacleTimer = 0
