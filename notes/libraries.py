import turtle as d
import time as t
import random as r
colors = ['red','orange','yellow','green','blue']
d.speed(100)
for shape in range(0,r.randint(1,200)):
    d.color(r.choice(colors))
    d.fillcolor(r.choice(colors))
    d.begin_fill()
    d.penup()
    d.goto(r.randint(-500,500),r.randint(-300,300))
    d.pendown()
    sides = r.randint(3,12)
    for turtle in range(0,sides):
        d.forward(600/sides)
        d.right(360/sides)
    d.end_fill()

d.done()