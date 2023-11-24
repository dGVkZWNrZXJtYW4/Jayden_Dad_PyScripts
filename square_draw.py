import turtle

# Create a turtle screen and a turtle
screen = turtle.Screen()
my_turtle = turtle.Turtle()

# Draw a square
for _ in range(4):
    my_turtle.forward(100)  # Move the turtle forward by 100 units
    my_turtle.right(90)     # Turn the turtle right by 90 degrees

# Close the turtle graphics window when clicked
screen.exitonclick()
