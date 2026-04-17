import turtle as t


t.pencolor("white")
t.bgcolor("black")
t.pencolor("white")
t.hideturtle()
t.fillcolor("red")

def heart (x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.left(45)
    t.forward(160)
    t.circle(70,200)
    t.left(230)
    t.circle(70,200)
    t.forward(160)
    t.end_fill()

    


heart(-70,-180)
t.penup()
t.home()
t.pendown
heart(70,-90)

t.done()