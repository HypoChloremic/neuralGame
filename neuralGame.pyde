import player

width  = 500
height = 500
Player = player.Player(width=width, height=height)

def setup():
    size(width, height)
    scale(-1,1)
    

def draw():
    scale(-1,1)
    background(255,255,255)
    line(0,0,width,0)
    Player.move()
    Player.show()
    
    if keyPressed:
        Player.callback()
        print("hello")
