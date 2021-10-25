# Team 94

import turtle
import winsound


a_wins = False
b_wins = False

# set up screen
wn = turtle.Screen()
wn.title("Pong by Team 94")
wn.bgcolor("black")

wn.setup(width=800, height=600)
wn.tracer(0)

# score
score_a = 0
score_b = 0
score_limit = 2

# Paddle A
leftpad_a = turtle.Turtle()
leftpad_a.speed(0)
leftpad_a.shape("square")
leftpad_a.color("white")
leftpad_a.shapesize(stretch_wid=5, stretch_len=1)
leftpad_a.penup()
leftpad_a.goto(-350, 0)

# Paddle B
rightpad_b = turtle.Turtle()
rightpad_b.speed(0)
rightpad_b.shape("square")
rightpad_b.color("white")
rightpad_b.shapesize(stretch_wid=5, stretch_len=1)
rightpad_b.penup()
rightpad_b.goto(350, 0)

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
def paddle_a_up():
    y = leftpad_a.ycor()
    y += 20
    leftpad_a.sety(y)

def paddle_a_down():
    y = leftpad_a.ycor()
    y -= 20
    leftpad_a.sety(y)

def paddle_b_up():
    y = rightpad_b.ycor()
    y += 20
    rightpad_b.sety(y)

def paddle_b_down():
    y = rightpad_b.ycor()
    y -= 20
    rightpad_b.sety(y)

# keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "p")
wn.onkeypress(paddle_b_down, "l")

# Main loop
while True:
    wn.update()

    # Moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

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
    if (ball.xcor() > 340 and ball.xcor() < 350) and (
            ball.ycor() < rightpad_b.ycor()+40 and ball.ycor()>rightpad_b.ycor()-40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("ballsound.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (
            ball.ycor() < leftpad_a.ycor()+40 and ball.ycor()>leftpad_a.ycor()-40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("ballsound.wav", winsound.SND_ASYNC)

    if score_a == score_limit:
        turtle.clearscreen()
        a_wins = True
        break

    elif score_b == score_limit:
        turtle.clearscreen()
        b_wins = True
        break

while True:
    if a_wins:
        wn.bgcolor("black")
        pen.goto(0, 0)
        pen.write("--GAME OVER--\nPlayer A wins", align="center", font=("Courier", 50, "normal"))
    elif b_wins:
        wn.bgcolor("black")
        pen.goto(0, 0)
        pen.write("--GAME OVER--\nPlayer B wins", align="center", font=("Courier", 50, "normal"))