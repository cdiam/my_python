#!/usr/bin/python

import turtle


# This draw_square creates a red window and creates a box and a circle
def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():       
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("blue")
    brad.speed(2)
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    
    window.exitonclick()

draw_art()