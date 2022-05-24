# by Ellie G, last visited:24/05/2022
# the module we are using pythons turtle module to write a program with objects
from turtle import Turtle
from random import randint

# --------------------- create 4 turtles -------------------- #
laura = Turtle('turtle')
laura.color('red')
laura.penup()
laura.goto(-160,100)
laura.pendown()

bob = Turtle('turtle')
bob.color('blue')
bob.penup()
bob.goto(-160,60)
bob.pendown()


rick = Turtle('turtle')
rick.color('green')
rick.penup()
rick.goto(-160,20)
rick.pendown()

hannah = Turtle('turtle')
hannah.color('purple')
hannah.penup()
hannah.goto(-160,-20)
hannah.pendown()
# ----------------------------------------------------------- #

for i in range(100):
    laura.forward(randint(1,5))
    bob.forward(randint(1,5))
    rick.forward(randint(1,5))
    hannah.forward(randint(1,5))

