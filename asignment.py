import turtle
turtle.Screen().bgcolor("red")
square = turtle.Turtle()

num_sides = 4
sides_length = 100
angle = 90.0

for i in range(num_sides):
    square.forward(sides_length)
    square.left(angle)