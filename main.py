"""
Draw Colorful Dots with Turtle

This Python script draws a grid of colorful dots using the Turtle module.
The dots are drawn in random colors from a predefined list.

Usage:
- Run the script.
- Click on the window to close it.
"""

import turtle
import random

# Create a screen object
screen = turtle.Screen()
# Set a screen to 800x600
screen.setup(width=800, height=600)

# Set color mode to use RGB values (0-255)
turtle.colormode(255)

# Create a turtle object named "timmy"
timmy = turtle.Turtle()
# Set the drawing speed to maximum
timmy.speed(0)
# Liftup the pen to prevent drawing
timmy.penup()
# Hide the turtle
timmy.hideturtle()

# Define a list of RGB color tuples
color_list = [(197, 165, 117), (142, 80, 56), (220, 201, 137), (59, 94, 119), (164, 152, 53), (136, 162, 181),
              (131, 34, 22), (69, 39, 32), (53, 117, 86), (192, 95, 78), (146, 177, 149), (19, 91, 68), (165, 143, 157),
              (31, 59, 76), (111, 75, 81), (228, 176, 164), (128, 29, 33), (179, 204, 177), (71, 34, 36), (25, 82, 89),
              (89, 146, 127), (18, 69, 57), (41, 66, 90), (219, 178, 182), (175, 94, 98), (179, 192, 205),
              (104, 129, 152), (67, 64, 59), (112, 135, 140), (175, 196, 206)]

# Set the initial heading of the turtle
timmy.setheading(225)
# Move the turtle forward
timmy.forward(300)
# Set the turtle heading to 0 (east)
timmy.setheading(0)

# Define the number of dots to draw
number_of_dots = 100

# Loop to draw dots
for dot_count in range(1, number_of_dots + 1):
    # Draw a dot with a random color from the color list
    timmy.dot(18, random.choice(color_list))

    # Move the turtle forward
    timmy.forward(50)

    # Check if it's time to move to the next row
    if dot_count % 10 == 0:
        # Turn the turtle to face upwards
        timmy.setheading(90)
        # Move the turtle upwards
        timmy.forward(50)
        # Turn the turtle to face left
        timmy.setheading(180)
        # Move the turtle to the left edge of the screen
        timmy.forward(500)
        # Turn the turtle to face right
        timmy.setheading(0)


# Close the screen when clicked
screen.exitonclick()
