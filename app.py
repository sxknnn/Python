//Description: if you run this code, it prints out a red flower with black background

import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("red")
t.speed(0)
for i in range(150):
    t.circle(190-1,90)
    t.lt(90)
    t.circle(190-i,90)
    t.lt(18)
