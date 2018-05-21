# BaseObject
# used to generate objects

class BaseObject:
    def __init__(self, width, height, bool=0):
        # Dimensions of the obj object, we havent done any sprites
        # yet here. 
        if bool < 1:
            self.objWidth  = 50
            self.objHeight = 50
        elif bool < 2:
            self.objWidth  = 100
            self.objHeight = 50
        else:
            self.objWidth  = 25
            self.objHeight = 20

        # The constants declarations
        self.pos = PVector(width+self.objWidth, 0)
        self.vel = PVector(-1,0)
        self.vZero = PVector(1,0)
        self.jump  = PVector(0,10)
        self.gravity = PVector(0,-5)
        
        self.color = random(100)


    def show(self):
        fill(100,self.color,100)
        rect(self.pos.x, self.pos.y, self.objWidth, self.objHeight)
    
    def move(self):
        self.pos.add(self.vel)
