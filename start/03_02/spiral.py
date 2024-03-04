# Import the Turtle Graphics module
import turtle

# Create a window where we will do our drawing.
screen = turtle.Screen()
screen.setup(500, 500)  # Set the dimensions of the Turtle Graphics window.
screen.title("Colourful Spiral")
screen.bgcolor("black")

# Create a turtle called sally (with a lower case "s").
sally = turtle.Turtle()
sally.speed(10)  # Fastest possible speed.
sally.width(3)  # The width of sally's pen.

# Define some colours - Remember "Richard of York gave battle in vain"?
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Make a loop - it will run 100 times.
for x in range(100):
    # Cycle through the colours ("%" is the magic key).
    sally.pencolor(colors[x % 6])  # 6 keeps it hexagonal.
    # Move sally forward by an amount related to the loop counter.
    sally.forward(x * 2)
    # Rotate sally just less than 60% so we get the spiral effect.
    sally.left(59)

# Hide sally now her work is done.
sally.hideturtle()

# This statement (or an equivalent) is needed at the end of all your turtle programs.
turtle.done()
