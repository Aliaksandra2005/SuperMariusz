<<<<<<< HEAD
value = 255
clr = 127 

def setup():
    size(600, 600)
    text_size = 40
    textSize(text_size)
    background(0)  

def draw():
    global value, clr 
    fill(value)
    rect(170, 330, 250, 100)
    text("       WELCOME \nTO SUPERMARIUSZ!",width/4-40, height/3)
    fill(clr, 0, 0)
    text("START", 235, 395)
    
def mouseClicked(): 
    global value, clr
    if value == 255:
        value = 0
    if clr == 127:
        clr = 0
        

=======
def setup():
    size (1000, 500) #do zmiany

    #Mariusz chodzi i ladowanie tla
    global pos_x, pos_y, sm_Stand, sm_Walk, is_walk, bg
    pos_x=0
    pos_y=0
    sm_Stand = loadImage("SuperMariuszSpriteStand.png")
    sm_Walk = loadImage("SuperMariuszSpriteWalk.png")
    bg = loadImage("bg.jpg")
    is_walk = False
    
def draw():
    global pos_x, pos_y, sm_Stand, sm_Walk, is_walk, bg
    clear()
    image(bg,0,0)
    def sm_walk():
        global is_walk
        if pos_x%17==0:
            is_walk = not is_walk
        if is_walk:
            image(sm_Walk, pos_x, pos_y)
        else:
            image(sm_Stand, pos_x, pos_y)
        #https://py.processing.org/reference/rotateY.html
        
    if keyPressed:
        if key == 'd': #prawo
            sm_walk()
            pos_x+=5
        if key == 'a': #lewo
            sm_walk()
            pos_x-=5
    else:
        image(sm_Stand, pos_x, pos_y)
            
>>>>>>> 69d69604079bc2dc67ba06c59d55e8fb1b4798c1
