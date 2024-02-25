import turtle

turtle.pencolor('white')


def sector(angle, radius):
    turtle.begin_fill()
    turtle.forward(radius)
    turtle.left(90)
    turtle.circle(radius, angle)
    turtle.right(90 + angle)
    turtle.goto(0, 0)
    turtle.end_fill()


def a_lttr(x, y):
    turtle.penup()
    turtle.setposition(x, y)
    turtle.pendown()
    turtle.left(75)
    turtle.forward(12)
    turtle.right(150)
    turtle.forward(6)
    turtle.right(105)
    turtle.forward(3.1)
    turtle.right(180)
    turtle.forward(3.1)
    turtle.right(75)
    turtle.forward(6)
    turtle.left(75)


def b_lttr(x, y):
    turtle.penup()
    turtle.setposition(x, y)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(12)
    turtle.left(90)
    turtle.forward(3)
    turtle.circle(3, 180)
    turtle.forward(3)
    turtle.left(180)
    turtle.forward(3)
    turtle.circle(3, 180)
    turtle.forward(3)
    turtle.right(180)


def c_lttr(x, y):
    turtle.penup()
    turtle.setposition(x, y)
    turtle.pendown()
    turtle.left(150)
    turtle.circle(6, 250)
    turtle.right(40)


def d_lttr(x, y):
    turtle.penup()
    turtle.setposition(x, y)
    turtle.pendown()
    turtle.circle(6, 180)
    turtle.left(90)
    turtle.forward(12)
    turtle.left(90)


def e_lttr(x, y):
    turtle.penup()
    turtle.setposition(x, y)
    turtle.pendown()
    turtle.forward(6)
    turtle.goto(x, y)
    turtle.right(90)
    turtle.forward(6)
    turtle.left(90)
    turtle.forward(6)
    turtle.goto(x, y - 6)
    turtle.right(90)
    turtle.forward(6)
    turtle.left(90)
    turtle.forward(6)


turtle.right(30)
turtle.fillcolor('#4684EE')
turtle.begin_fill()
sector(120, 100)
turtle.end_fill()
turtle.right(100)

turtle.fillcolor('#DC3912')
turtle.begin_fill()
sector(100, 100)
turtle.end_fill()
turtle.right(70)

turtle.fillcolor('#FF9900')
turtle.begin_fill()
sector(70, 100)
turtle.end_fill()
turtle.right(50)

turtle.fillcolor('#008000')
turtle.begin_fill()
sector(50, 100)
turtle.end_fill()
turtle.right(20)

turtle.fillcolor('#4942CC')
turtle.begin_fill()
sector(20, 100)
turtle.end_fill()
turtle.right(90)

turtle.pencolor('black')
a_lttr(90, 78)
b_lttr(15, -110)
c_lttr(-100, -50)
d_lttr(-85, 90)
e_lttr(-20, 125)

turtle.penup()
turtle.forward(30)

turtle.done()
