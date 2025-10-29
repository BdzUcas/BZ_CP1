#BZ 1st Turtle Race

#Import Libraries
import turtle as d
import random as r
import time as t
#Create functions for various things
#Function for generating random turtle movement
def dmove():
    #Return a random number between 5 and 30
    return r.randint(5,30)
#function for checking who won
def checkwin():
    #Check if each turtle has passed finish line. If they have, display "(turtle color) turtle won!" and return true
    if d1.xcor() >= 450:
        print('Red turtle won!')
        return True
        
    elif d2.xcor() >= 450:
        print('Orange turtle won!')
        return True
        
    elif d3.xcor() >= 450:
        print('Yellow turtle won!')
        return True
        
    elif d4.xcor() >= 450:
        print('Green turtle won!')
        return True
        
    elif d5.xcor() >= 450:
        print('Blue turtle won!')
        return True
    #if none have crossed finish line
    else:
        #return false
        return False
#Create Screen
screen = d.Screen()
#Set screen size
screen.setup(1000,400)
#Give screen a name
screen.title("Racing Turtles")

#Pen Setup
pen = d.Turtle()
pen.speed(0)
pen.hideturtle()

#Create 5 turtles
d1 = d.Turtle()
d2 = d.Turtle()
d3 = d.Turtle()
d4 = d.Turtle()
d5 = d.Turtle()
#Set turtles shapes to turtle
d1.shape('turtle')
d2.shape('turtle')
d3.shape('turtle')
d4.shape('turtle')
d5.shape('turtle')
#Give unique colors to each turtle
d1.color('red')
d2.color('orange')
d3.color('yellow')
d4.color('green')
d5.color('blue')
#Set turtle speed to instant
d1.speed(0)
d2.speed(0)
d3.speed(0)
d4.speed(0)
d5.speed(0)
#Remove turtle trails
d1.penup()
d2.penup()
d3.penup()
d4.penup()
d5.penup()
#Make each turtle go to starting postition
d1.goto(-450,160)
d2.goto(-450,80)
d3.goto(-450,0)
d4.goto(-450,-80)
d5.goto(-450,-160)
#Set turtle speed to normal
d1.speed(10)
d2.speed(10)
d3.speed(10)
d4.speed(10)
d5.speed(10)
#Start turtle trails
d1.pendown()
d2.pendown()
d3.pendown()
d4.pendown()
d5.pendown()
#Remove pen trail
pen.penup()
#Set pen size
pen.pensize(20)
#Move pen to top of finish line
pen.goto(450,200)
#Start pen trail
pen.pendown()
#Face pen down
pen.right(90)
#Loop ten times
for i in range(0,10):
    #Set pen color to white
    pen.color("#FFFFF0")
    #Move pen down 1/20 of the screen
    pen.forward(20)
    #Set pen color to black
    pen.color("#000000")
    #Move pen down 1/20 of the screen
    pen.forward(20)
#Start Game Loop
while not False:
    #Move each turtle forward
    d1.forward(dmove())
    d2.forward(dmove())
    d3.forward(dmove())
    d4.forward(dmove())
    d5.forward(dmove())
    #Check if any turtles have won
    if checkwin():
        #if yes, break loop
        break
#Make screen stay open 2 seconds
t.sleep(2)