# Simple Snake Game in Python 3
# By ToykyoEdTech

import turtle
import time
import random

delay = 0.1

# Setup the screen

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("green")
wn.setup(width=600, height=600)
# Prevent animation and turns off screen updates
wn.tracer(0)



# Make snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("blue")
# turtles draw lines, dont draw the line
food.penup()
food.goto(0,100)



# Make snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("orange")
# turtles draw lines, dont draw the line
head.penup()
head.goto(0,0)
head.direction = "stop"



# Functions
def go_up():
    head.direction = "up"
    
def go_down():
    head.direction = "down"
    
def go_left():
    head.direction = "left"
    
def go_right():
    head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
        
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
        
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
        
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard Bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")


# Main Game Loop
while True:
    wn.update()

    if head.distance(food) < 20:
        # move food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)
    
    move()
    time.sleep(delay)
    

# Keep window open
wn.mainloop()
