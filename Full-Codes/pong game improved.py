import turtle
import time

#Assigns players and initialises their points

p1=0
p2=0

#Creates a graphic window for the game

sc = turtle.Screen()
sc.bgcolor("black")
sc.title("Pong game")
sc.setup(width=1000,height=600)

#for smoother game play -- need to manually update graphics
sc.tracer(0)


#Creates a new turtle for seperation line in the middle of the screen

line = turtle.Turtle()
line.color("white")
line.hideturtle()
line.penup()
line.goto(0,300)
line.setheading(270)

#Draws the actual seperation line -- penup() is used for Dashed line
for i in range(30):
    line.pendown()
    line.forward(10)
    line.penup()
    line.forward(10)


#Creates the ball and initialise its location

ball = turtle.Turtle()
ball.color("red")
ball.shape("circle")
ball.shapesize(stretch_wid=0.5, stretch_len=0.5)
ball.penup()
ball.goto(0,0)

#Gives values for dx and dy -- magnitude of ball movement, difference of x and difference of y
#can change to make ball faster
ball.dx = 1
ball.dy = 1

#left paddle code
lp = turtle.Turtle()
lp.shape("square")
lp.shapesize(stretch_wid=6,stretch_len=1)
lp.color("white")
lp.penup()
lp.goto(-400,0)

#right paddle code
rp = turtle.Turtle()
rp.shape("square")
rp.shapesize(stretch_wid=6,stretch_len=1)
rp.color("white")
rp.penup()
rp.goto(400,0)

#ball movement function. magnitude of speed set by ball.dx and ball.dy above
def ball_move():
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

#defines paddle moving function
def lp_up():
    y=lp.ycor()
    y+=10
    lp.sety(y)


def lp_down():
    y=lp.ycor()
    y-=10
    lp.sety(y)

def rp_up():
    y=rp.ycor()
    y+=10
    rp.sety(y)

def rp_down():
    y=rp.ycor()
    y-=10
    rp.sety(y)

#collision for upper and lower walls -- so that the ball doesnt exit the screen
def ball_limit():
    if ball.ycor()<-290 or ball.ycor()>290:
        ball.dy*=-1

#collision detection for paddles
#only inverts dx if it is within paddle x-range and y-range
def check_collision():
    if rp.xcor() -20 < ball.xcor() < rp.xcor() +20:
        if rp.ycor() -60 < ball.ycor() < rp.ycor() +60:
            ball.dx*=-1
    if lp.xcor() -20 < ball.xcor() < lp.xcor() +20:
        if lp.ycor() -60 < ball.ycor() < lp.ycor() +60:
            ball.dx*=-1

#detects when a specific key is pressed and performs a function
sc.listen()
sc.onkeypress(lp_up,key="w")
sc.onkeypress(lp_down,key="s")
sc.onkeypress(rp_up,key="Up")
sc.onkeypress(rp_down,key="Down" )

#Create new turtle used later
score = turtle.Turtle()
score.hideturtle()
score.color("white")
score.penup()
score.goto(0,260)

#Function: Indicates the start of the game and clears starting screen
def startgame():
    global game_started
    game_started = True
    ssc.clear()


#defines starting screen
def startsc():
    global ssc #global function ssc (starting screen). when the game is started will be erased
    ssc = turtle.Turtle()
    ssc.hideturtle()
    ssc.color("white")
    ssc.penup()
    ssc.goto(0,0)
    ssc.write("Welcome to Pong! \n PRESS SPACE TO START",align="center",font = ("Courier",40,"normal"))

    sc.listen()
    sc.onkeypress(startgame,key="space")


game_started = False
startsc()

#updates the screen manually as "tracer(0)" for a smoother gameplay
while not game_started:
    sc.update()

#repeats all the functions and checks for scoring, win detection and display the winner
while True:
    sc.update() #continously updates screen
    ball_move()
    ball_limit()
    check_collision()
    if ball.xcor() > 490:
        ball.dx*=-1
        ball.goto(0,0)
        p1+=1

    if ball.xcor() <-490:
        ball.dx*=-1
        ball.goto(0,0)
        p2+=1

    score.clear()
    #Scoreboard
    score.write(f"Player 1: {p1}           Player 2: {p2}", align = "center", font = ("Arial", 24, "normal"))
    if lp.ycor()>220:
        lp.sety(lp.ycor()-10)

    if lp.ycor()<-220:
        lp.sety(lp.ycor()+10)

    if rp.ycor()>220:
        rp.sety(rp.ycor()-10)

    if rp.ycor()<-220:
        rp.sety(rp.ycor()+10)


    if p1 == 10:
        P1Win = turtle.Turtle()
        P1Win.color("Green")
        P1Win.hideturtle()
        P1Win.penup()
        P1Win.goto(0,0)
        P1Win.write("PLAYER 1 Wins!",align="center", font= ("Courier", 50, "normal"))

        time.sleep(5)
        break

    elif p2 == 10:
        P2Win = turtle.Turtle()
        P2Win.color("Green")
        P2Win.hideturtle()
        P2Win.penup()
        P2Win.goto(0,0)
        P2Win.write("PLAYER 2 Wins!",align="center", font= ("Courier", 50, "normal"))

        time.sleep(5)
        break
    startgame()
