import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.title("Geometric Transformations with Turtle")
screen.bgcolor("white")

# Create a turtle to draw the original square
t = turtle.Turtle()

def draw_square(t, vertices, color):
    t.penup()
    t.goto(vertices[0])
    t.pendown()
    t.color(color)
    for vertex in vertices[1:]:
        t.goto(vertex)
    t.goto(vertices[0])

def translate(vertices, tx, ty):
    return [(x + tx, y + ty) for x, y in vertices]

def rotate(vertices, angle):
    theta = math.radians(angle)
    return [(x * math.cos(theta) - y * math.sin(theta), x * math.sin(theta) + y * math.cos(theta)) for x, y in vertices]

def scale(vertices, sx, sy):
    return [(x * sx, y * sy) for x, y in vertices]

# Define the original square vertices
square_vertices = [(50, 50), (150, 50), (150, 150), (50, 150)]

# Draw the original square
draw_square(t, square_vertices, "black")

# Translate the square
translated_vertices = translate(square_vertices, 200, 100)
draw_square(t, translated_vertices, "blue")

# Rotate the square
rotated_vertices = rotate(square_vertices, 45)
draw_square(t, rotated_vertices, "red")

# Scale the square
scaled_vertices = scale(square_vertices, 0.5, 0.5)
draw_square(t, scaled_vertices, "green")

# Hide the turtle and display the window
t.hideturtle()
turtle.done()
