import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Starry Night with Twinkling Stars and Shooting Star")

# Function to draw a star
def draw_star(turtle_obj, size):
    turtle_obj.begin_fill()
    for _ in range(5):
        turtle_obj.forward(size)
        turtle_obj.right(144)
        turtle_obj.forward(size)
        turtle_obj.right(144)
    turtle_obj.end_fill()

# Function to create twinkling effect
def twinkle_star(turtle_obj, x, y, size):
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    turtle_obj.pendown()
    turtle_obj.color("white")
    draw_star(turtle_obj, size)
    time.sleep(0.1)
    turtle_obj.color("black")
    draw_star(turtle_obj, size)
    time.sleep(0.1)
    turtle_obj.color("white")
    draw_star(turtle_obj, size)

# Draw stars
star_turtle = turtle.Turtle()
star_turtle.speed(0)
star_turtle.hideturtle()

stars = []
for _ in range(50):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    size = random.randint(10, 20)
    stars.append((x, y, size))
    star_turtle.penup()
    star_turtle.goto(x, y)
    star_turtle.pendown()
    draw_star(star_turtle, size)

# Add a moon with beige color
moon_turtle = turtle.Turtle()
moon_turtle.color("#F5F5DC")  # Beige color
moon_turtle.penup()
moon_turtle.goto(200, 200)
moon_turtle.pendown()
moon_turtle.begin_fill()
moon_turtle.circle(50)
moon_turtle.end_fill()
moon_turtle.hideturtle()

# Function to draw clouds
def draw_cloud(turtle_obj, x, y):
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    turtle_obj.pendown()
    turtle_obj.color("gray")
    turtle_obj.begin_fill()
    for _ in range(6):
        turtle_obj.circle(20, 180)
        turtle_obj.right(120)
    turtle_obj.end_fill()

# Draw clouds around the moon
cloud_turtle = turtle.Turtle()
cloud_turtle.speed(0)
cloud_turtle.hideturtle()
draw_cloud(cloud_turtle, 150, 180)
draw_cloud(cloud_turtle, 250, 180)

# Function to animate shooting star
def shooting_star(turtle_obj):
    turtle_obj.color("yellow")
    turtle_obj.penup()
    turtle_obj.goto(-300, 200)
    turtle_obj.pendown()
    turtle_obj.speed(1)
    for _ in range(50):
        turtle_obj.forward(10)
        turtle_obj.right(1)
    turtle_obj.hideturtle()

# Animate twinkling stars and shooting star
while True:
    for x, y, size in stars:
        twinkle_star(star_turtle, x, y, size)
    shooting_star(star_turtle)

# Keep the window open
turtle.done()
