import turtle as t

def draw_axes(pen, x_min, x_max, y_min, y_max, t=1):
    pen.color("gray")
    pen.pensize(1)
    pen.penup()

    pen.goto(x_min, 0); pen.pendown(); pen.goto(x_max, 0); pen.penup()
    for x in range(int(x_min), int(x_max) + 1, t):
        pen.goto(x, 0); pen.dot(3)

    pen.goto(0, y_min); pen.pendown(); pen.goto(0, y_max); pen.penup()
    for y in range(int(y_min), int(y_max) + 1, t):
        pen.goto(0, y); pen.dot(3)

def parabol(x, a=1, b=0, c=0):
    return a*x*x + b*x + c

def plot_function(pen, f, x_min, x_max, dx):
    pen.color("blue")
    pen.pensize(2)
    pen.penup()

    x = x_min
    y = f(x)
    pen.goto(x, y)
    pen.pendown()

    while x <= x_max:
        y = f(x)
        pen.goto(x, y)
        x += dx

screen = t.Screen()
x_min, x_max = -10, 10
y_min, y_max = -10, 100
screen.setworldcoordinates(x_min, y_min, x_max, y_max)

pen = t.Turtle(visible=False)
pen.speed(0)
pen.hideturtle()

draw_axes(pen, x_min, x_max, y_min, y_max, t=1)

dx = 0.1
a, b, c = 1, 0, 0
plot_function(pen, lambda x: parabola(x, a, b, c), x_min, x_max, dx)

screen.exitonclick()
