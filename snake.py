# Simple Snake Game in Python 3
# By ToykyoEdTech

import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0


# Setup the screen

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("maroon")
wn.setup(width=600, height=600)
# Prevent animation and turns off screen updates
wn.tracer(0)



# Make snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("lime")
# turtles draw lines, dont draw the line
food.penup()
food.goto(0,100)



# Make snake head
head = turtle.Turtle()
head.speed(0)
head.shape("turtle")
head.color("aqua")
# turtles draw lines, dont draw the line
head.penup()
head.goto(0,0)
head.direction = "stop"



# Make snake body
segments = []


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))


# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"
    
def go_down():
    if head.direction != "up":
        head.direction = "down"
    
def go_left():
    if head.direction != "right":
        head.direction = "left"
    
def go_right():
    if head.direction != "left":
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

    # Check for collision with border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear segments list
        segments.clear()

        # Reset the score if it hits the border
        score = 0

        # Reset the delay
        #delay = 0.01

        # Update the score 
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

            
    

    # Check for collision with food
    if head.distance(food) < 20:
        # move food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("cyan")
        new_segment.penup()
        segments.append(new_segment)

        #shorten the delay
        #delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


    # Move the end segments first - reverse order
    for index in range(len(segments) -1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
        
        
    move()

    # Check for head collisions with the body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear segments list
            segments.clear()

            # Reset the score if it hits the border
            score = 0

            # Reset the delay
            #delay = 0.01

            # Update the score
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


    
    time.sleep(delay)
    

# Keep window open
wn.mainloop()
