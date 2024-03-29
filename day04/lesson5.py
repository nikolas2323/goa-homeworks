from turtle import *

#we want to paint a house

#step1: draw a square
speed(100)
width(7)
color("blue")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#door
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

#roof
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#window
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

#window
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

#grass
penup()
goto(-3, -3)
pendown()
color("green")
begin_fill()
forward(370)
right(90)
forward(300)
right(90)
forward(750)
right(90)
forward(300)
right(90)
forward(400)
end_fill()
penup()
color("white")
goto(-3,200)
pendown()

#chimney
color("black")
begin_fill()
penup()
goto(200,200)
left(120)
forward(60)
right(30)
pendown()
forward(50)
right(90)
forward(30)
right(90)
forward(100)
end_fill()

#second house
color("blue")
penup()
goto(-50,0)
right(90)
pendown()
begin_fill()
forward(160)
right(90)
forward(240)
right(90)
forward(160)
right(90)
forward(240)
end_fill()

#door orange
color("orange")
begin_fill()
right(90)
penup()
forward(50)
pendown()
forward(60)
right(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

#third house
penup()
begin_fill()
right(90)
forward(150)
pendown()
forward(100)
right(90)
forward(200)
right(90)
forward(100)
right(90)
forward(200)
end_fill()
right(90)
forward(25)
#door
color("pink")
begin_fill()
pendown()
forward(40)
right(90)
forward(70)
right(90)
forward(40)
right(90)
forward(70)
end_fill()

exitonclick()
