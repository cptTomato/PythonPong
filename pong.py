import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800,height=800)
wn.tracer(0)




#Paddle

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("gold")
paddle_a.shapesize(stretch_wid=1,stretch_len=6)
paddle_a.penup()
paddle_a.goto(-350,-350)

#Ball
ball= turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("gold")
ball.shapesize(stretch_wid=2,stretch_len=2)
ball.penup()
ball.goto(0,0)
ball.dx = 2.5
ball.dy = 2.5

# score
score = 0
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)



#Ball bewegen
def moveLinks():
    x = paddle_a.xcor()
    x -= 30
    paddle_a.setx(x)

def moveRechts():
    x = paddle_a.xcor()
    x += 30
    paddle_a.setx(x)

#eingabe
wn.listen()
wn.onkeypress(moveLinks,"a")
wn.onkeypress(moveRechts,"d")



while True:
    wn.update()
    #ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor()>390:
        ball.sety(390)
        ball.dy += -1

    if ball.ycor()<-390:
        ball.sety(-390)
        ball.dy += +1

    if ball.xcor()>390:
        ball.setx(390)
        ball.dx += -1

    if ball.xcor()<-390:
        ball.setx(-390)
        ball.dx += +1

    #bounce

    if ball.ycor() < -340 and ball.xcor() < paddle_a.xcor() + 50 and ball.xcor() > paddle_a.xcor() - 50:
        ball.dy *= -1
        score = score + 1
        pen.clear()
        pen.write("Score {} ".format(score), align="center", font=("Courier", 24, "normal"))

    elif ball.ycor() <-380:
        score = 0
        pen.clear()
        pen.write("Score {} ".format(score), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

