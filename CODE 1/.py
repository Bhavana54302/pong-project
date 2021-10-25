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

# Main loop
while True:
    wn.update()


