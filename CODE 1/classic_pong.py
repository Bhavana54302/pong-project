# Team 94

import turtle
import winsound

a_wins = False
b_wins = False

# set up screen
wn = turtle.Screen()
wn.title("Pong by Team 94")
wn.bgpic("pongbg.gif")
wn.setup(width=800, height=600)
wn.tracer(0)

# score
score_a = 0
score_b = 0
score_limit = 11

# Paddle A
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.penup()
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.goto(-350, 0)

# Paddle B
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.3

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 20, "normal"))

# function
def left_paddle_up():
    y = left_paddle.ycor()
    y += 20
    left_paddle.sety(y)

def left_paddle_down():
    y = left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)

def right_paddle_up():
    y = right_paddle.ycor()
    y += 20
    right_paddle.sety(y)

def right_paddle_down():
    y = right_paddle.ycor()
    y -= 20
    right_paddle.sety(y)

# keyboard binding
wn.listen()
wn.onkeypress(left_paddle_up, "w")
wn.onkeypress(left_paddle_down, "s")
wn.onkeypress(right_paddle_up, "p")
wn.onkeypress(right_paddle_down, "l")

# Main loop
while True:
    wn.update()

    # Moving the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("borders.wav", winsound.SND_ASYNC)

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("borders.wav", winsound.SND_ASYNC)

    elif ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))

    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < right_paddle.ycor() + 40 and ball.ycor() > right_paddle.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("ballsound3.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < left_paddle.ycor() + 40 and ball.ycor() > left_paddle.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("ballsound3.wav", winsound.SND_ASYNC)

    if score_a == score_limit:
        turtle.clearscreen()
        a_wins = True
        winsound.PlaySound("bgsound2.wav", winsound.SND_ASYNC)
        break

    elif score_b == score_limit:
        turtle.clearscreen()
        b_wins = True
        winsound.PlaySound("bgsound2.wav", winsound.SND_ASYNC)
        break

while True:
    if a_wins:
        wn.bgcolor("black")
        pen.goto(0,0)
        pen.write("--GAME OVER--\nPlayer A wins", align="center", font=("Courier", 50, "normal"))

    elif b_wins:
        wn.bgcolor("black")
        pen.goto(0,0)
        pen.write("--GAME OVER--\nPlayer B wins", align="center", font=("Courier", 50, "normal"))

