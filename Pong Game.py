import turtle
import time

# Screen setup
sc = turtle.Screen()
sc.title("Pong Game")
sc.bgcolor("White")
sc.setup(width=1000, height=600)
sc.tracer(0)  # Turns off the screen updates for better performance

# Paddle setup
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("black")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)

right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("black")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)

# Ball setup
hit_ball = turtle.Turtle()
hit_ball.speed(40)  # You can leave this as is; it affects drawing speed, not movement speed
hit_ball.shape("circle")
hit_ball.color("blue")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 3  # Adjusted ball speed
hit_ball.dy = -3  # Adjusted ball speed

# Score
left_player = 0
right_player = 0

sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("blue")
sketch.penup()
sketch.goto(0, 260)
sketch.hideturtle()
sketch.write("Left_player: 0 Right_player: 0", align="center", font=("Courier", 24, "normal"))

# Pause flag
paused = False

# Paddle movement functions
def paddleaup():
    y = left_pad.ycor()
    y += 20
    if y < 250:
        left_pad.sety(y)

def paddleadown():
    y = left_pad.ycor()
    y -= 20
    if y > -240:
        left_pad.sety(y)

def paddlebup():
    y = right_pad.ycor()
    y += 20
    if y < 250:
        right_pad.sety(y)

def paddlebdown():
    y = right_pad.ycor()
    y -= 20
    if y > -240:
        right_pad.sety(y)

# Toggle pause function
def toggle_pause():
    global paused
    paused = not paused
    if paused:
        sketch.goto(0, 0)
        sketch.write("Paused", align="center", font=("Courier", 36, "normal"))
    else:
        sketch.clear()
        sketch.write("Left_player: {} Right_player: {}".format(left_player, right_player), align="center", font=("Courier", 24, "normal"))

# Keyboard bindings
sc.listen()
sc.onkeypress(paddleaup, "e")
sc.onkeypress(paddleadown, "x")
sc.onkeypress(paddlebup, "Up")
sc.onkeypress(paddlebdown, "Down")
sc.onkeypress(toggle_pause, "p")  # 'p' key to toggle pause

# Main game loop
while True:
    sc.update()
    
    if not paused:
        # Move the ball
        hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
        hit_ball.sety(hit_ball.ycor() + hit_ball.dy)

        # Border collision
        if hit_ball.ycor() > 290:
            hit_ball.sety(290)
            hit_ball.dy *= -1
        
        if hit_ball.ycor() < -290:
            hit_ball.sety(-290)
            hit_ball.dy *= -1

        # Ball out of bounds (scoring)
        if hit_ball.xcor() > 490:
            hit_ball.goto(0, 0)
            hit_ball.dx *= -1
            left_player += 1
            sketch.clear()
            sketch.write("Left_player: {} Right_player: {}".format(left_player, right_player), align="center", font=("Courier", 24, "normal"))

        if hit_ball.xcor() < -490:
            hit_ball.goto(0, 0)
            hit_ball.dx *= -1
            right_player += 1
            sketch.clear()
            sketch.write("Left_player: {} Right_player: {}".format(left_player, right_player), align="center", font=("Courier", 24, "normal"))

        # Improved Paddle collision detection
        # Right paddle collision
        if (hit_ball.dx > 0) and (hit_ball.xcor() > 360) and (hit_ball.xcor() < 370) and (hit_ball.ycor() < right_pad.ycor() + 60) and (hit_ball.ycor() > right_pad.ycor() - 60):
            hit_ball.setx(360)
            hit_ball.dx *= -1

        # Left paddle collision
        if (hit_ball.dx < 0) and (hit_ball.xcor() < -360) and (hit_ball.xcor() > -370) and (hit_ball.ycor() < left_pad.ycor() + 60) and (hit_ball.ycor() > left_pad.ycor() - 60):
            hit_ball.setx(-360)
            hit_ball.dx *= -1

    # Adding a small delay
    time.sleep(0.01)
