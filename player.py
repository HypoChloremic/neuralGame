# the player object
import config
con = config.config()

class Player:
    def __init__(self, width, height, baseSpeed=5):

        # Dimensions of the player object, we havent done any sprites
        # yet here. 
        self.playerWidth  = 50
        self.playerHeight = 50 

        # The constants declarations
        self.pos = PVector(100, -self.playerHeight)
        self.vel = PVector(0,0)
        self.jump  = PVector(0,-15)
        self.call  = 0
        self.gravity = PVector(0,1)
        self.collide = False
        self.spaceTimer = 0
        self.color = random(0,150)
        self.trav = 0
    
        # sprites           
        self.playerDino = [loadImage(con.parent + "\\dino{}.png".format(i)) for i in range(5)]
        self.lengthDino = len(self.playerDino)
        self.ind = 0
        
        
    def show(self):
        #noFill()
        #stroke(2, 55)
        #rect(self.pos.x, self.pos.y, self.playerWidth, self.playerHeight)
        if self.trav%5 == 0:
            self.ind += 1
            self.ind = self.ind % self.lengthDino
            image(self.playerDino[self.ind], self.pos.x,self.pos.y, self.playerWidth, self.playerHeight)
            
        else:
            image(self.playerDino[self.ind], self.pos.x,self.pos.y, self.playerWidth, self.playerHeight)

        
    def move(self):
        self.trav += 1
        self.pos.add(self.vel)
        if self.pos.y < -self.playerHeight:
            self.vel.y = self.vel.y + self.gravity.y
        elif self.pos.y > -self.playerHeight:
            self.pos.y = -self.playerHeight
        else:
            self.vel.y = 0
            
    def callback(self):
        if self.pos.y == -self.playerHeight:
            self.vel.add(self.jump)
        
