'''
3 people following each other with steplength of 1px 
'''
from turtle import Screen, Turtle
import time
from math import sqrt

screen = Screen()
screen.setup(800, 800)
t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t1.hideturtle()
t2.hideturtle()
t3.hideturtle()

def setup(sidelength):
    h = sqrt(sidelength**2 - (sidelength/2)**2)
    a = ((sidelength/2)**2 + h**2)/(2*h)
    t1.penup()
    t2.penup()
    t3.penup()
    t1.right(30)
    t1.forward(a)
    t1.setheading(270)
    t1.forward(100)
    t2.right(150)
    t2.forward(a)
    t2.setheading(270)
    t2.forward(100)
    t3.right(270)
    t3.forward(a)
    t3.setheading(270)
    t3.forward(100)
    t1.pendown()
    t2.pendown()
    t3.pendown()


def follow():
    t1.pensize(3)
    t2.pensize(3)
    t3.pensize(3)
    t1pos = t1.position()
    t2pos = t2.position()
    t3pos = t3.position()
    print(t1pos, t2pos, t3pos)
    t1.setheading(t1.towards(t2pos))
    t2.setheading(t2.towards(t3pos))
    t3.setheading(t3.towards(t1pos))
    t1.fd(1)
    t2.fd(1)
    t3.fd(1)
    screen.update()


def run():
    setup(750)
    for i in range(100000):

        screen.update()
        follow()
        time.sleep(0.01)

screen.tracer(False)
run()
screen.tracer(True)
screen.mainloop()
