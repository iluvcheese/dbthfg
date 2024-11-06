import pgzrun
import random

HEIGHT = 720
WIDTH = 1180

skor = 0
leifs = 3
fire_exclemationmark = False
you = Actor("tottally not killing da bees with a spaceship")
fire_allcaps_exclemationmark = Actor("tottally not promoting to shoot bees or smth")
bee = Actor("hotdoggg")
kaboom = Actor("fireisgud")

you.pos = 590, 670
kaboom.pos = you.pos



boelet = []

bees = []

helth = 10
gaemover = False

idk = random.randint(5,54547)

for i in range(idk):
    bees.append(Actor("hotdoggg"))
    xpos = random.randint(1, 1180)
    bees[-1].pos = xpos, -100


    

def draw():
    global gaemover
    screen.clear()
    screen.fill("SteelBlue3")
    you.draw()
    for i in boelet:
        i.draw()
    for a in bees:
        a.draw()
    if gaemover:
        kaboom.pos = you.pos
        kaboom.draw()
        fire_allcaps_exclemationmark.pos = 2000000,388876786

    screen.draw.text(str(helth),center = (590, 360))



imfastasfluf = random.randint(1,1)

def update():
    global bees, you, gaemover, helth, boelet
    for bwee in bees:
        bwee.y=bwee.y+random.randint(1, 4)
        for bOOlet in boelet:
            if bwee.colliderect(bOOlet):
                helth=helth-1
                bees.remove(bwee)
    for bewlvuhub in boelet:
        if bewlvuhub.y<-19:
            boelet.remove(bewlvuhub)
        else:
            bewlvuhub.y=bewlvuhub.y-10
    if keyboard.a:
        you.x-=3
    if keyboard.d:
        you.x+=3
    if keyboard.s:
        gaemover = True
    for i in bees:
        if i.y==670:
            helth-=1
    if helth<=0:
        gaemover = True
    
def on_key_down(key):
    if key ==keys.SPACE:
        boelet.append(fire_allcaps_exclemationmark)
        boelet[-1].x=you.x
        boelet[-1].y=you.y

    

pgzrun.go()