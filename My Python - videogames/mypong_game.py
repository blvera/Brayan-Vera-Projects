import turtle #We are going to use this instead of pygame

#Creating window
window = turtle.Screen()
window.title("Pong game created by 'Brayan Vera'")
window.bgcolor("black")
window.setup(width = 800, height= 600)
window.tracer(0) #this command helps with the animation.

#Scoring
score_a = 0
score_b = 0

#Player A: creating player 1 shape on the left side of the screen.
player_a = turtle.Turtle()
player_a.speed(0) #to appear instant mode when opening the window
player_a.shape("square") #assigning shape 
player_a.color("white")  #assigning color white
player_a.penup() #to avoid tracing line on screen
player_a.goto(-350,0)  #Default, the square is created in the center, but we want it to create on the left.
player_a.shapesize(stretch_wid = 5, stretch_len = 1)

#Player b: creating player 1 shape on the left side of the screen.
player_b = turtle.Turtle()
player_b.speed(0) #to appear instant mode when opening the window
player_b.shape("square") #assigning shape 
player_b.color("white")  #assigning color white
player_b.penup() #to avoid tracing line on screen
player_b.goto(350,0)  #Default, the square is created in the center, but we want it to create on the left.
player_b.shapesize(stretch_wid = 5 ,stretch_len = 1)


#Making the ball
ball = turtle.Turtle()
ball.speed(0) #to appear instant mode when opening the window
ball.shape("circle") #assigning shape 
ball.color("blue")  #assigning color white
ball.penup() #to avoid tracing line on screen
ball.goto(0,0)
ball.dx = 0.3 #move ball every 3 pixels
ball.dy = 0.3


#Create line division
division = turtle.Turtle()
division.color("white")
division.goto(0,400)
division.goto(0,-400)


#Scoreboard code
pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("PlayerA:        PlayerB: ", align = "center", font=("Times",24, "normal"))



#create movement to the pong player up and down
#doing it in functions
def player_a_up():
    y = player_a.ycor()
    y += 60 #updating it to 40 px to move up
    player_a.sety(y) #updating the coordinate
def player_a_down():
    y = player_a.ycor()
    y -= 60 #updating it to 40 px to move up
    player_a.sety(y) #updating the coordinate

def player_b_up():
    y = player_b.ycor()
    y += 60 #updating it to 40 px to move up
    player_b.sety(y) #updating the coordinate
def player_b_down():
    y = player_b.ycor()
    y -= 60 #updating it to 40 px to move up
    player_b.sety(y) #updating the coordinate

#keyboard controls implementation. telling the keyboard what is happenning 
# and what to do when a key is pressed.
#Providing movement to the players
window.listen()
window.onkeypress(player_a_up, "w")
window.onkeypress(player_a_down, "s")
window.onkeypress(player_b_up, "Up") #up key arrow
window.onkeypress(player_b_down, "Down") #down key arrow

while True:
    window.update()

    #applied ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Borderlines handling
    # applying some math,basically if the ball goes down or up and touches 
    # the borders then it should bouce the opposite way.
    if ball.ycor() > 290:
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.dy *= -1

    #Borderlines Left and Right
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("PlayerA: {}       PlayerB: {}".format(score_a,score_b), align = "center", font=("Times",24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("PlayerA: {}       PlayerB: {}".format(score_a,score_b), align = "center", font=("Times",24, "normal"))

    #Making collision (ball with player) and bounce back
    #checking whether the ball is found in the x-axis of player a and player b
    # also checking if the ball is in the y-axis of the player
    if ((ball.xcor() > 340 and ball.xcor() < 350)
            and (ball.ycor() < player_b.ycor() + 50
            and ball.ycor() > player_b.ycor() - 50)):
        ball.dx *= -1 #reverting the axis when it gets to player b
    if ((ball.xcor() < -340 and ball.xcor() > -350)
            and (ball.ycor() < player_a.ycor() + 50
            and ball.ycor() > player_a.ycor() - 50)):
        ball.dx *= -1 #reverting the axis when it gets to player a

