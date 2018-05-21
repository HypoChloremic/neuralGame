# the player object

class Player:
    def __init__(self, width, height, baseSpeed=5):
        # The constants declarations
        self.pos = PVector(0, 0)
        self.vel = PVector(0,0)
        self.gravity = PVector(0,-1)
        self.vZero = PVector(1,0)
        self.jump  = PVector(0,15)
        self.call  = 0
        self.collide = False
        self.spaceTimer = 0
        
        # Dimensions of the player object, we havent done any sprites
        # yet here. 
        self.playerWidth  = 50
        self.playerHeight = 100
        
    
    def show(self):
        fill(150)
        rect(self.pos.x, self.pos.y, self.playerWidth, self.playerHeight)
    
    
    def move(self):
        self.pos.add(self.vel)
        if self.pos.y > 0:
            self.vel.y = self.vel.y + self.gravity.y
        elif self.pos.y < 0:
            self.pos.y = 0
        else:
            self.vel.y = 0
            
    def callback(self):
        self.vel.add(self.jump)
        
