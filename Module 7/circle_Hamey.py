# Ross Hamey
# CSE163 - P7.1
# 10/29/2023
# https://github.com/Endeared

# our imports - renamed turtle and only imported pi
import turtle as trtl
from math import pi

# drawCircle func, takes in our Turtle object, center x, center y, and radius
def drawCircle(turtle, x, y, radius):
    # doing our calculations first for circumference, length of each
    # partition, and the angle
    circumference = 2.0 * pi * radius
    length = circumference / 120
    ang = 3

    # move turtle to center-right of circle, set our initial heading to 90
    # (to start going up), then place our pen down
    turtle.penup()
    turtle.goto(x + radius, y)
    turtle.setheading(90)
    turtle.pendown()

    # repeating our partitions 120 times by turning left 3 degrees and then
    # moving length of our partition
    for i in range(120):
        turtle.left(ang)
        turtle.forward(length)

# main func
def main():
    # creating new Turtle object then passing our arguments to
    # drawCircle func
    new_turtle = trtl.Turtle()
    drawCircle(new_turtle, 50, 75, 100)

if __name__ == "__main__":
    main()