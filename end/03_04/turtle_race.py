import turtle
import random

screen = turtle.Screen()
screen.title("Python is fun!")
screen.bgcolor("cyan")
screen.setup(600, 600)

# Chequered flag
pen = turtle.Turtle(visible=False)
pen.shape("square")
pen.color("black")
pen.speed(10)
pen.penup()
pen.goto(200, 200)
pen.pendown()
pen.setheading(270)


for i in range(20):
    pen.stamp()
    pen.forward(20)
    if i % 2 == 0:
        pen.color("white")
    else:
        pen.color("black")

# First contestant
james = turtle.Turtle()
james.shape("turtle")
james.color("red")
james.penup()
james.goto(-200, -100)

for i in range(10):
    james.right(36)

# Second contestant
sou = turtle.Turtle()
sou.shape("turtle")
sou.color("green")
sou.penup()
sou.goto(-200, 100)

for i in range(10):
    sou.right(36)

# The race!
while james.xcor() < 200 and sou.xcor() < 200:
    james.forward(random.randint(1, 10))
    sou.forward(random.randint(1, 10))


turtle.done()
