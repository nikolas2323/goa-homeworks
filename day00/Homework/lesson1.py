from turtle import *

#we want to paint a house

#step1: draw a square
speed(7)
width(7)
color("blue")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
forward(70)
color("yellow")
begin_fill()
left(90)
forward(100)
right(90)
forward(70)
right(90)
forward(100)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

color("black")
penup()
goto(140, 120)
pendown()
left(120)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(25)
left(90)
forward(50)
left(180)
forward(25)
left(90)
forward(25)
left(180)
forward(50)

penup()
goto(60,120)
pendown()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(25)
right(90)
forward(50)
right(180)
forward(25)
right(90)
forward(25)
right(180)
forward(50)

exitonclick()