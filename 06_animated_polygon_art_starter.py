import turtle
import math
import time
from polygon_shape import Polygon

# Create screen
screen = turtle.Screen()
screen.title("My Animated Polygon Artwork")
screen.setup(900, 700)
screen.bgcolor("black")
screen.tracer(0)


# Create 8 polygon objects
polygons = [
    Polygon(-250, 150, 3, 55, "cyan", 4, 0),
    Polygon(-100, 150, 4, 55, "magenta", 4, 15),
    Polygon(50, 150, 5, 55, "yellow", 4, 25),
    Polygon(200, 150, 6, 55, "orange", 4, 10),
    Polygon(-250, -100, 7, 45, "lime", 4, 20),
    Polygon(-100, -100, 3, 65, "pink", 4, 30),
    Polygon(50, -100, 5, 55, "white", 4, 0),
    Polygon(200, -100, 4, 65, "red", 4, 15)
]


# Save original positions
start_positions = [
    (-250, 150),
    (-100, 150),
    (50, 150),
    (200, 150),
    (-250, -100),
    (-100, -100),
    (50, -100),
    (200, -100)
]


# Draw the first frame
for polygon in polygons:
    polygon.draw()

screen.update()


# Animation: 80 frames
for frame in range(80):

    for i, polygon in enumerate(polygons):

        start_x, start_y = start_positions[i]

        x = start_x + 60 * math.sin(frame * 0.08 + i)
        y = start_y + 40 * math.cos(frame * 0.08 + i)

        polygon.move_to(x, y)

    screen.update()
    time.sleep(0.05)

screen.mainloop()