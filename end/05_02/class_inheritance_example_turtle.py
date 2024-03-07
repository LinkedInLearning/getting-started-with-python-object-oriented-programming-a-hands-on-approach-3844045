import turtle
import random


class RainbowTurtle(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(x, y)
        self.color = random.choice(colors)
        self.onclick(self.change_color)
        self.fillcolor(random.choice(colors))

    def change_color(self, x, y):
        same_color = True
        while same_color:
            new_color = random.choice(colors)
            if new_color != self.fillcolor():
                self.fillcolor(new_color)
                same_color = False


colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

my_turtle1 = RainbowTurtle(-200, 200)
my_turtle2 = RainbowTurtle(200, -200)
my_turtle3 = RainbowTurtle(200, 200)
my_turtle4 = RainbowTurtle(-200, -200)

turtle.done()
