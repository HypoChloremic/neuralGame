import baseObject
import player

class ObjectDriver:
    def __init__(self, player, width, height):    
        self.obstacleTimer = 0
        self.obstacles = []
            
        # constants
        self.minObsInterval = 100
        self.width  = width
        self.height = height
        self.coll = False
        
    def show(self,player):
        player.show()
        
        for obs in self.obstacles:
            if obs:
                obs.show()
    
    def move(self, player):
        self.obstacleTimer += 1        
        
        if self.obstacleTimer > self.minObsInterval + random(50,100):
            self.addObstacle()
        
        player.move()
        
        for obsInd in range(len(self.obstacles)):
            try:
                if self.obstacles[obsInd]:
                    self.obstacles[obsInd].move()
                
                    if self.obstacles[obsInd].pos.x+self.obstacles[obsInd].objWidth < 0:
                        del(self.obstacles[obsInd])
            except IndexError as e:
                pass

        
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
    
    def collision(self, player): 
        for obj in self.obstacles:
            objVertex = [(obj.pos.x, obj.pos.y), (obj.pos.x+obj.objWidth, obj.pos.y+obj.objHeight)]
            plaVertex = [(player.pos.x, player.pos.y),(player.pos.x+player.playerWidth,player.pos.y+player.playerHeight)]
            
            if plaVertex[0][0] < objVertex[0][0] and plaVertex[1][0] > objVertex[0][0] and plaVertex[0][1] <= objVertex[0][1]:
                self.coll = True
            
            elif plaVertex[0][0] > objVertex[0][0] and plaVertex[0][1] < objVertex[1][1]:
                self.coll = True

    def refresh(self, play):
        play = player.Player(width=width, height=height)
        
            
            
            
            
            
            
            
