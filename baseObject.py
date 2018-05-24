# BaseObject
# used to generate objects
import config
con = config.config()

class BaseObject:
    def __init__(self, width, height, bool=0):
        # Dimensions of the obj object, we havent done any sprites
        # yet here. 
        
        # assets
        self.cactus = loadImage(con.parent + "\\cactus.png")
        
        # booleans
        if bool < 1:
            self.objWidth  = 25
            self.objHeight = 50

        elif bool < 2:
            self.objWidth  = 10
            self.objHeight = 50

        else:
            self.objWidth  = 25
            self.objHeight = 20

        # The constants declarations
        self.pos = PVector(width+self.objWidth, -self.objHeight)
        self.vel = PVector(-5,0)
        self.vZero = PVector(1,0)
        self.jump  = PVector(0,10)
        self.gravity = PVector(0,-5)
        
        self.color = random(100)


    def show(self):
        #fill(100,self.color,100)
        #rect(self.pos.x, self.pos.y, self.objWidth, self.objHeight)
        image(self.cactus, self.pos.x, self.pos.y, self.objWidth, self.objHeight)
    
    def move(self):
        self.pos.add(self.vel)
