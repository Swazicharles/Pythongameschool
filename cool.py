from ursina import *

#This is just to create the game development window we want
app = Ursina()


#player1 = Entity(model = 'sphere',color = color.green,scale_y =2)
#player2 = Entity(model = 'cube',color = color.orange,scale_y =4)
player = Entity(model = 'sphere',color= color.orange,scale_y =2)

#create the ground

ground = Entity(model = 'cube', color = color.magenta, z=-0.1, y=-3,
                origin = (0,0.5), scale = (50,1,10), colider = 'box')
#This function gets called by the engine every frame
#when d and a keys are presed there is movement on the screen

def update():
    player.x += held_keys['d'] * time.dt
    player.x -= held_keys['a'] * time.dt

#This part tells the player to move left or right based on your input

def input(key):
    if key =='space':
        player.y +=1
        invoke(setattr,player,'y',player.y-1, delay=0.25)
    if key =='b':
        player.y -=1
        invoke(setattr,player,'y',player.y-1, delay=0.25)
        

# We are telling the game to run over here
app.run()
