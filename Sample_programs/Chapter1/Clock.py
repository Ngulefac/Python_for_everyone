#(Turtle: display a clock) This program  displays a clock that shows the time 9:15:00
import turtle

turtle.penup()
turtle.goto(0, -150)
turtle.pendown()
turtle.circle(180) 

turtle.penup()
turtle.goto(-10, 200)
turtle.goto(-10, 180)
turtle.pendown()
turtle.write("12")

turtle.penup()
turtle.goto(-10, -200)
turtle.goto(-10, -140)
turtle.pendown()
turtle.write("6")

turtle.penup()
turtle.goto(-180, 20)
turtle.goto(-160, 20)
turtle.pendown()
turtle.write("9")
