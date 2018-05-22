# the player object
import os

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
        
        # config    
        # sprites
        #self.playerSprite = createGraphics(self.playerWidth, self.playerHeight, path="sprite.png")
        #self.playerImg = loadImage("C:\\Users\\Ali Rassolie\\Documents\\prwork\\python\\processing\\neuralGame\\sprite.png")
        #self.playerDino = loadImage("C:\\Users\\Ali Rassolie\\Documents\\prwork\\python\\processing\\neuralGame\\dino.png")
        
        #self.playerImg = loadImage("{}\\sprite.png".format(os.getcwd()))
        #self.playerDino = loadImage("{}\\dino.png".format(os.getcwd()))
        
    def show(self):
        noFill()
        stroke(2, 55)
        rect(self.pos.x, self.pos.y, self.playerWidth, self.playerHeight)
        image(self.playerDino, self.pos.x,self.pos.y, self.playerWidth, self.playerHeight)
        
    def move(self):
        self.pos.add(self.vel)
        if self.pos.y < -self.playerHeight:
            self.vel.y = self.vel.y + self.gravity.y
        elif self.pos.y > -self.playerHeight:
            self.pos.y = -self.playerHeight
        else:
            self.vel.y = 0
            
    def callback(self):
        self.vel.add(self.jump)
        
