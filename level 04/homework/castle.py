from turtle import*


width(5)
speed(20)

 # grass

penup()
goto(-950, -200)
pendown()


begin_fill()
color("black", "green")

forward(1950)
right(90)
forward(500)
right(90)
forward(2250)

end_fill()

# walls
penup()
goto(700, -200)
pendown()

begin_fill()
color("black", "grey")

right(90)
forward(350)
left(90)

forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
right(90)
forward(50)
left(90)
forward(350)

end_fill()

#wall2
penup()
goto(450, 150)
pendown()

begin_fill()
color("Black", "grey")

left(180)
forward(225)


left(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
right(90)
forward(50)
left(90)
forward(225)

end_fill()

left(180)
forward(50)

right(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

right(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

right(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

right(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

right(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

right(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

right(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

right(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

right(90)
forward(50)
right(90)
forward(50)

#flag_goa

penup()

backward(225)
right(90)
forward(425)
right(90)

pendown()

begin_fill()
color("Black", "dark green")

forward(125)
right(90)
forward(100)
right(90)
forward(50)
right(90)
forward(100)

end_fill()

#door_chad

penup()
goto(700, -200)
pendown()

begin_fill()
color("black", "brown")

forward(450)

right(90)
forward(300)
left(90)
forward(450)
left(90)
forward(300)

end_fill()


backward(300)
left(90)
forward(225)
right(90)
forward(300)

#window1

penup()

right(90)

forward(375)
right(90)
forward(125)

pendown()


begin_fill()
color("black", "skyblue")

forward(125)
left(90)
forward(125)
left(90)
forward(125)
left(90)
forward(125)
left(90)

forward(64)
left(90)
forward(125)
backward(64)
left(90)
forward(64)
backward(125)

end_fill()


#window2
penup()
goto(700, -200)


right(90)
forward(150)
right(90)
forward(125)

pendown()

begin_fill()
color("black", "skyblue")

forward(125)
left(90)
forward(125)
left(90)
forward(125)
left(90)
forward(125)
left(90)

forward(64)
left(90)
forward(125)
backward(64)
left(90)
forward(64)
backward(125)

end_fill()
















































exitonclick()