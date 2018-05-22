import player
import objectDriver

width  = 1000
height = 500
Player = player.Player(width=width, height=height)
driver = objectDriver.ObjectDriver(player = Player, width=width, height=height)

def setup():
    size(width, height)
    

def draw():
    translate(0,height/1.5)
    background(255,255,255)
    line(0,0,width,0)

    driver.move(Player)
    driver.collision(Player)
    driver.show(Player)
    
    if driver.coll:
        refresh()
        
def refresh():
        global Player, driver
        Player = player.Player(width=width, height=height)
        driver = objectDriver.ObjectDriver(player = Player, width=width, height=height)

def keyPressed():
    Player.callback()
