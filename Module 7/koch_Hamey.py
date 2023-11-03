# Ross Hamey
# CSE163 - P7.3
# 10/29/2023
# https://github.com/Endeared

# importing Turtle class as trtl
from turtle import Turtle as trtl

# drawFractalLine function, which takes in a turtle object, distance
# angle, and level
def drawFractalLine(this_turtle, distance, angle, level):
    # if our level is 0, we move the given distance in our given
    # direction (angle)
    if level == 0:
        this_turtle.setheading(angle)
        this_turtle.forward(distance)
    # otherwise, we draw our four fractals with HALF the given distance, and
    # a given level MINUS one, and angles to produce our desired effect
    else:
        distance /= 3
        level -= 1
        drawFractalLine(this_turtle, distance, angle, level)
        drawFractalLine(this_turtle, distance, angle + 60, level)
        drawFractalLine(this_turtle, distance, angle - 60, level)
        drawFractalLine(this_turtle, distance, angle, level)

# main function
def main():
    # setting our initial vars
    width = 200
    height = 200
    size = 150
    level = 4

    # creating our new Turtle object, also hiding cursor this time to
    # see easier. release pen, move to top left of of fractal, and place
    # pen down
    new_turtle = trtl()
    new_turtle.speed(0)
    new_turtle.hideturtle()
    new_turtle.penup()
    new_turtle.goto(-width // 3, height // 4)
    new_turtle.pendown()

    # list of initial angles
    angles = [0, -120, 120]
    
    # iterate over list and call drawFractalLine func with our angle
    # (and other unchanged args)
    for angle in angles:
        drawFractalLine(new_turtle, size, angle, level)
    input()

if __name__ == "__main__":
    main()