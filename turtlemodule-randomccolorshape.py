
from turtle import Turtle, Screen
import random

joni = Turtle ()

screen = Screen()
screen.colormode(255)

joni.shape("turtle")
joni.width(10)
joni.speed("fastest")

def randomwalk(steps = 1000):
    for _ in range(steps):
        joni.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0,255))
        joni.setheading(random.choice([0,90,180,270]))
        joni.forward(30)


randomwalk()



#make shapes with diff colors.
#for sides in range (3,11):
    #joni.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0,255))

    #for _ in range(sides):
        #joni.fd(100)
        #joni.right(360/sides)







screen.exitonclick()