import turtle

window = turtle.Screen()
window.title('Pong')
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

score_a = 0
score_b = 0

box_a = turtle.Turtle()
box_a.speed(0)
box_a.shape("square")
box_a.color("white")
box_a.shapesize(stretch_wid=5, stretch_len=1)
box_a.penup()
box_a.goto(-350,0)

box_b = turtle.Turtle()
box_b.speed(0)
box_b.shape("square")
box_b.color("white")
box_b.shapesize(stretch_wid=5, stretch_len=1)
box_b.penup()
box_b.goto(350,0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.35
ball.dy = 0.35

score = turtle.Turtle()
score.speed(0)
score.color('white')
score.penup()
score.hideturtle()
score.goto(0, 250)
score.write("Player A: 0  Player B: 0", align="center", font=("Courier", 25, "normal"))

def box_a_up():
    y = box_a.ycor()
    y += 25
    box_a.sety(y)

def box_a_down():
    y = box_a.ycor()
    y -= 25
    box_a.sety(y)

def box_b_up():
    y = box_b.ycor()
    y += 25
    box_b.sety(y)

def box_b_down():
    y = box_b.ycor()
    y -= 25
    box_b.sety(y)

window.listen()
window.onkeypress(box_a_up, "w")
window.onkeypress(box_a_down, "s")
window.onkeypress(box_b_up, "Up")
window.onkeypress(box_b_down, "Down")
while True:
    window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        score.clear()
        score.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 25, "normal"))
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        score.clear()
        score.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 25, "normal"))
    
    if (ball.xcor() > 340 and ball.xcor() <350) and (ball.ycor() < box_b.ycor() + 40 and ball.ycor() > box_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1 
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < box_a.ycor() + 40 and ball.ycor() > box_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
     