# Team 94

import turtle


# set up screen
wn = turtle.Screen()
wn.title("Pong by Team 94")
wn.bgcolor("light pink")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0, 0)

# function
def left_pad_up():
    y = left_pad.ycor()
    y += 20
    left_pad.sety(y)

# keyboard binding
wn.listen()
wn.onkeypress(left_pad_up, "w")

# Main loop
while True:
    wn.update()


