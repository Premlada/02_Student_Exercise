import turtle
from polygon_shape import Polygon

# Create drawing screen
screen = turtle.Screen()
screen.title("My Static Polygon Artwork")
screen.setup(900, 700)
screen.bgcolor("black")
screen.tracer(0)


# Create 20 Polygon objects
polygons = [
    Polygon(-350, 200, 3, 65, "cyan", 3, 10),
    Polygon(-230, 180, 4, 70, "magenta", 4, 15),
    Polygon(-100, 220, 5, 60, "yellow", 3, 25),
    Polygon(50, 190, 6, 65, "orange", 4, 10),
    Polygon(200, 210, 7, 55, "lime", 3, 20),

    Polygon(320, 100, 3, 80, "pink", 5, 30),
    Polygon(-350, 30, 5, 75, "white", 3, 0),
    Polygon(-200, 40, 6, 60, "red", 4, 15),
    Polygon(-50, 50, 4, 90, "cyan", 3, 30),
    Polygon(100, 30, 7, 55, "violet", 4, 10),

    Polygon(250, -30, 5, 80, "gold", 3, 20),
    Polygon(350, -150, 4, 65, "orange", 5, 0),
    Polygon(-300, -170, 6, 70, "magenta", 3, 25),
    Polygon(-150, -180, 3, 85, "lime", 4, 10),
    Polygon(0, -170, 5, 65, "cyan", 3, 15),

    Polygon(150, -200, 7, 60, "pink", 4, 30),
    Polygon(-250, -50, 4, 75, "yellow", 3, 20),
    Polygon(0, 180, 3, 70, "white", 5, 0),
    Polygon(180, 100, 6, 55, "red", 3, 15),
    Polygon(300, 200, 5, 70, "violet", 4, 25)
]

# Draw all polygons
for polygon in polygons:
    polygon.draw()


screen.update()
screen.mainloop()