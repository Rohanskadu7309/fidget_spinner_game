from turtle import *

state = {'turn': 0}

def spinner():
    clear()
    angle = state['turn'] / 10
    right(angle)
    forward(100)
    dot(120, 'red')
    back(100)
    right(120)
    forward(100)
    dot(120, 'green')
    back(100)
    right(120)
    forward(100)
    dot(120, 'blue')
    back(100)
    right(120)
    update()

def animate():
    if state['turn'] > 0:
        state['turn'] -= 1

    spinner()
    ontimer(animate, 20)

# The mouse click passes 'x' and 'y' coordinates, 
# so we add them as arguments even if we don't use them.
def flick(x, y):
    state['turn'] += 10

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
width(20)

# Changed from onkey to onscreenclick
onscreenclick(flick) 

listen()
animate()
done()