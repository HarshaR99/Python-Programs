# Simple Pong game
# the turtle module allows us to create some basic graphics

import turtle
import winsound

# win is window variable
window = turtle.Screen()
# title for window
window.title('Pong Game')
# background colour
window.bgcolor('black')
# size of window
window.setup(width=800, height=600)
# to stop window from updating,window will be updated manually
window.tracer(0)

# Score
ScoreA = 0
ScoreB = 0

# Paddle A

paddleA = turtle.Turtle()
# speed of animation for the paddle, setting to maximum speed
paddleA.speed(0)
# Attributes for the paddle
paddleA.shape('square')
# By default the shape is 20px high and wide
paddleA.color('white')
# width = 20*4 px,height - 20*1 px
paddleA.shapesize(stretch_wid=5, stretch_len=1)
# To avoid lines being drawn due to motion of the Paddle
paddleA.penup()
# Starting co-ordinates of the Paddle
# The coordinates given are the mid point for the Paddle
paddleA.goto(-350, 0)

# Paddle B
# Attributes for paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape('square')
paddleB.color('white')
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350, 0)

# Code for the Ball

Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape('square')
Ball.color('white')
Ball.penup()
Ball.goto(0, 0)
# variable for x axis movement of ball
Ball.dx = 0.2
# variable for y axis movement of ball
Ball.dy = 0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
# try when penup is commented
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Player A :0  Player B :0', align='center', font=('Courier', 24, 'normal'))


# functions for motion

def paddleAUp():
    # Get y coordinate of Paddle A
    Y = paddleA.ycor()
    # Add 20 px to it , to mak it move upwards
    Y += 20
    # Setting new y coordinate
    paddleA.sety(Y)


def paddleADown():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)


def paddleBUp():
    Y = paddleB.ycor()
    Y += 20
    paddleB.sety(Y)


def paddleBDown():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)


# Keyboard binding

window.listen()
# When 'w' key is pressed by the user,the function paddleAUp is called
window.onkeypress(paddleAUp, 'w')
# When 's' key is pressed ,paddle goes down
window.onkeypress(paddleADown, 's')

window.onkeypress(paddleBUp, 'Up')
window.onkeypress(paddleBDown, 'Down')

# Main game loop
while True:
    window.update()

    # Motion of the Ball
    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    # Event when Ball collides with the border
    # For Upper and Lower borders
    if Ball.ycor() > 290:
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
        Ball.sety(290)
        Ball.dy *= -1

    if Ball.ycor() < -290:
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
        Ball.sety(-290)
        Ball.dy *= -1

    # For the Left and Right Borders
    if Ball.xcor() > 390:
        ScoreA += 1
        Ball.goto(0, 0)
        Ball.dx *= -1
        pen.clear()
        pen.write('Player A :{}  Player B :{}'.format(ScoreA, ScoreB), align='center', font=('Courier', 24, 'normal'))

    if Ball.xcor() < -390:
        ScoreB += 1
        Ball.goto(0, 0)
        Ball.dx *= -1
        pen.clear()
        pen.write('Player A :{}  Player B :{}'.format(ScoreA, ScoreB), align='center', font=('Courier', 24, 'normal'))

    # Paddle and Ball collisions

    if (340 < Ball.xcor() < 350) and (paddleB.ycor() + 40 > Ball.ycor() > paddleB.ycor() - 40):
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
        Ball.setx(340)
        Ball.dx *= -1

    if (-350 < Ball.xcor() < -340) and (paddleA.ycor() + 40 > Ball.ycor() > paddleA.ycor() - 40):
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
        Ball.setx(-340)
        Ball.dx *= -1
