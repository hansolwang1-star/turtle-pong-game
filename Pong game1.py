# Write your code here :-)
import turtle

sc = turtle.Screen()
sc.title("Pong game")
sc.bgcolor("Black")
sc.setup(width=1000, height=600)
sc.tracer(0)

line = turtle.Turtle()
line.color("white")
line.hideturtle()
line.penup()
line.goto(0, 300)
line.setheading(270)
for i in range(30):
    line.pendown()
    line.forward(10)
    line.penup()
    line.forward(10)


lp = turtle.Turtle()
lp.color("white")
lp.shape("square")
lp.speed(0)
lp.shapesize(stretch_wid = 6, stretch_len = 1)
lp.penup()
lp.goto(-400.00,0.00)

rp = turtle.Turtle()
rp.color("white")
rp.shape("square")
rp.speed(0)
rp.shapesize(stretch_wid = 6, stretch_len = 1)
rp.penup()
rp.goto(400.00,0.00)

ball = turtle.Turtle()
ball.speed(0)
ball.color("red")
ball.shape("circle")
ball.shapesize(stretch_wid = 0.5 , stretch_len = 0.5)
ball.penup()
ball.goto(0.00,0.00)
ball.dx = 5
ball.dy = 5


def lp_up():
    y = lp.ycor()
    y= y+10
    lp.sety(y)
    if lp.ycor() > 220:
      lp.sety(lp.ycor()-10)

def lp_down():
    y=lp.ycor()
    y-=10
    lp.sety(y)
    if lp.ycor() < -220:
      lp.sety(lp.ycor()+10)

def rp_up():
    y = rp.ycor()
    y= y+10
    rp.sety(y)
    if rp.ycor() > 220:
      rp.sety(rp.ycor()-10)

def rp_down():
    y=rp.ycor()
    y-=10
    rp.sety(y)
    if rp.ycor() < -220:
      rp.sety(rp.ycor()+10)

def check_collision():
    if rp.xcor() - 20 < ball.xcor() < rp.xcor() + 20:
        if rp.ycor() - 60 < ball.ycor()  < rp.ycor() + 60:
            ball.dx *= -1
    if lp.xcor() - 20 < ball.xcor() < lp.xcor() + 20:
        if lp.ycor() - 60 < ball.ycor()  < lp.ycor() + 60:
            ball.dx *= -1


sc.listen()
sc.onkeypress(lp_up, key= "w")
sc.onkeypress(lp_down, key = "s")
sc.onkeypress(rp_up, key= "Up")
sc.onkeypress(rp_down, key = "Down")


p1=0
p2=0

score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)

score.write(f"Player 1: {p1}   Player 2: {p2}", align = "center" , font = ("courier", 24 , "normal"))

while True:
    sc.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor()+ball.dy)


    check_collision()

    if ball.ycor()>290:
        ball.dy=ball.dy*-1
    if ball.ycor()<-290:
        ball.dy*=-1

    if ball.xcor() < -490:
        ball.dx*=-1
        ball.goto(0,0)
        p2+=1

    if ball.xcor() > 490:
        ball.dx*=-1
        ball.goto(0,0)
        p1+=1

    score.clear()
    score.write(f"Player 1: {p1}   Player 2: {p2}", align = "center" , font = ("courier", 24 , "normal"))

    if p1 == 10:
        print("Player 1 Wins!")
        break

    elif p2==10:
        print("Player 2 Wins!")
        break

