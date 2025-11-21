import turtle as d
def draw_branch(length):
    if length > 5:
        for i in range(3):
            d1.forward(length)
            draw_branch(length / 3)
            d1.backward(length)
            d1.right(60)

d1 = d.Turtle()
d1.speed(0)
d1.color('#99ccff')
d1.penup()
d1.teleport(0,0)
d1.pendown()

for i in range(6):
    draw_branch(100)
    d1.right(60)

d1.hideturtle()
d.done()