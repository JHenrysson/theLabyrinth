# coding=utf-8
import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("The One with a Labyrinth")
wn.setup(700,700)

class Pen( turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
print(
    '''
    You have been placed in a pitch-black labyrinth, without knowing if there is a way out or not.
    Maybe there are traps? The only option available is to walk in a random direction and hope 
    for the best, hope that you do not walk into a wall, or even worse,that you walk in circles. 
    But hurry up, you only have so many moves…''')
print(
    '''
    To move around use:
    w = up 
    a = left 
    s = down 
    d = right 
    '''
)

direction = input("Enter direction: ")
