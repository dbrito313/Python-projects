import turtle
from turtle import Turtle, Screen
import random

# Create turtles
blue = Turtle()
yellow = Turtle()
red = Turtle()
purple = Turtle()
green = Turtle()
black = Turtle()

# Set colors
blue.color("blue")
yellow.color("yellow")
red.color("red")
purple.color("purple")
green.color("green")
black.color("black")

# Set shapes
blue.shape("turtle")
yellow.shape("turtle")
red.shape("turtle")
purple.shape("turtle")
green.shape("turtle")
black.shape("turtle")

finish_line_x = 198


for turtle in [blue, yellow, red, purple, green, black]:
    turtle.penup()


screen = Screen()
screen.setup(width=500, height=400)
player_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color:").lower()

turtles = [blue, yellow, red, purple, green, black]


blue.goto(-200, 80)
yellow.goto(-200, 50)
red.goto(-200, 20)
purple.goto(-200, -10)
green.goto(-200, -40)
black.goto(-200, -70)




finish_line_turtle = Turtle()
finish_line_turtle.penup()
finish_line_turtle.goto(finish_line_x, 200)
finish_line_turtle.pendown()
finish_line_turtle.pensize(5)
finish_line_turtle.right(90)

for _ in range(12):
    finish_line_turtle.forward(25)
    finish_line_turtle.penup()
    finish_line_turtle.forward(25)
    finish_line_turtle.pendown()

finish_line_turtle.hideturtle()


def move():
    return random.randint(10, 20)

def racing():
    while True:
        for turtle in turtles:
            turtle.forward(move())
            if turtle.xcor() >= finish_line_x:
                winner = turtle.pencolor()
                announce_winner(winner)
                return


def announce_winner(winner):
    winner_turtle = Turtle()
    winner_turtle.hideturtle()
    winner_turtle.penup()
    winner_turtle.goto(-200, -180)
    winner_turtle.color("black")
    if winner == player_bet:
        winner_turtle.write(f"{winner.capitalize()} turtle won. You won the bet!!!", font=("Arial", 12, "bold"))
    else:
        winner_turtle.write(f"{winner.capitalize()} turtle won. You lost the bet!!!", font=("Arial", 12, "bold"))


racing()
screen.exitonclick()