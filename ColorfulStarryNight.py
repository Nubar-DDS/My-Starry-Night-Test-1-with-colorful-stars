import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Starry Night with Shiny and Twinkling Colorful Stars and a Moon")

# Create a turtle object for stars
star_turtle = turtle.Turtle()
star_turtle.speed(0)
star_turtle.hideturtle()

# Create a turtle object for the moon
moon_turtle = turtle.Turtle()
moon_turtle.speed(0)
moon_turtle.hideturtle()

# Function to draw a star
def draw_star(x, y, color, size):
    star_turtle.penup()
    star_turtle.goto(x, y)
    star_turtle.pendown()
    star_turtle.color(color)
    star_turtle.begin_fill()
    for _ in range(5):
        star_turtle.forward(size)
        star_turtle.right(144)
    star_turtle.end_fill()

# Function to draw the moon with a bit of roughness
def draw_moon(x, y, size):
    moon_turtle.penup()
    moon_turtle.goto(x, y)
    moon_turtle.pendown()
    moon_turtle.color("beige")
    moon_turtle.begin_fill()
    moon_turtle.circle(size)
    moon_turtle.end_fill()
    # Adding roughness
    for _ in range(10):
        moon_turtle.penup()
        moon_turtle.goto(x + random.randint(-size, size), y + random.randint(-size, size))
        moon_turtle.pendown()
        moon_turtle.color("darkgray")
        moon_turtle.begin_fill()
        moon_turtle.circle(random.randint(1, 5))
        moon_turtle.end_fill()

# Draw the moon
draw_moon(200, 200, 50)

# Generate random stars
num_stars = 100
stars = []
for _ in range(num_stars):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    color = (random.random(), random.random(), random.random())
    size = random.randint(10, 20)
    stars.append((x, y, color, size))
    draw_star(x, y, color, size)

# Function to make stars twinkle
def twinkle_stars():
    while True:
        for star in stars:
            x, y, color, size = star
            draw_star(x, y, "black", size)  # Erase the star
            time.sleep(0.1)
            draw_star(x, y, color, size)  # Redraw the star
            time.sleep(0.1)

# Start twinkling stars
twinkle_stars()

# Keep the window open
turtle.done()
