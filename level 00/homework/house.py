from turtle import*
 
width(5)
speed(10)

#building
begin_fill()
color("black", "grey")

forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
end_fill()


#window
penup()
goto (20, 170)
pendown()

begin_fill()
color("black", "skyblue")

forward(50)
left(90)
forward(40)
left(90)
forward(50)
left(90)
forward(40)
backward(20)
left(90)
forward(50)
backward(25)
right(90)
forward(20)
backward(40)

end_fill()

#window_2
penup()
goto(140, 170)
pendown()

begin_fill()
color("black", "skyblue")

left(90)
forward(50)
left(90)
forward(40)
left(90)
forward(50)
left(90)
forward(40)
backward(20)
left(90)
forward(50)
backward(25)
right(90)
forward(20)
backward(40)
end_fill()

#door
penup()
goto(0, 0)
pendown()

begin_fill()
color("black", "brown")

backward(80)
right(90)
forward(80)
right(90)
forward(40)
right(90)
forward(80)

end_fill()

#roof
penup()
goto(0, 200)
pendown()

begin_fill()
color("black", "red")

left(135)
forward(140)
right(90)
forward(140)

end_fill()

#grass
penup()
goto(200, 0)
pendown()

begin_fill()
color("black", "green")
left(45)
forward(270)
right(90)
forward(397)
right(90)
forward(949)
right(90)
forward(397)
right(90)
forward(730)


end_fill()


exitonclick()