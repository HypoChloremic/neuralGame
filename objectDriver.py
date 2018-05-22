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
        self.score = 0
        


    def show(self,player):
        player.show()
        for obs in self.obstacles:
            if obs:
                obs.show()
    

    def drawSprite(self):
        pass
                
    def move(self, player):
        self.obstacleTimer += 1
        self.score += 1
        print(self.score)        
        
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
            objVertex = [(obj.pos.x, obj.pos.y), ]
            plaVertex = [(player.pos.x, player.pos.y),]
            
            objVx = obj.pos.x + obj.objWidth
            objVy = obj.pos.y + obj.objHeight
            
            plaVx = player.pos.x + player.playerWidth
            plaVy = player.pos.y + player.playerHeight
            
            if player.pos.x < obj.pos.x and plaVx > obj.pos.x and player.pos.y <= obj.pos.y and player.pos.y >= obj.pos.y:
                self.coll = True
            
            elif player.pos.x > obj.pos.x and player.pos.x < objVx and player.pos.y > objVy:
                self.coll = True
