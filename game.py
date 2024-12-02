import turtle
import random
import time

# Creating screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.setup(width=800, height=800)
screen.bgcolor("#000000")
screen.tracer(0)

# Code for border
border = turtle.Turtle()
border.speed(5)
border.pensize(5)
border.penup()
border.goto(-350, 300)
border.pendown()
border.color("red")
for _ in range(2):
    border.forward(700)
    border.right(90)
    border.forward(600)
    border.right(90)
border.penup()
border.hideturtle()

# Score
score = 0
delay = 0.1

# Creating snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("pink")
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"

# Creating food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("white")
food.penup()
food.goto(random.randint(-350, 350), random.randint(-300, 300))

# List to store segments
old = []

# Score display
scor = turtle.Turtle()
scor.speed(0)
scor.color("white")
scor.penup()
scor.hideturtle()
scor.goto(0, 350)
scor.write("Score: 0", align="center", font=("Courier", 24, "normal"))

# Defining movement functions
def move_up():
    if snake.direction != "down":
        snake.direction = "up"

def move_down():
    if snake.direction != "up":
        snake.direction = "down"

def move_left():
    if snake.direction != "right":
        snake.direction = "left"

def move_right():
    if snake.direction != "left":
        snake.direction = "right"

# Move function
def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

# Binding keypress
screen.listen()
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

#setting up game over
def game_over():
    scor.clear()
    scor.goto(0, 0)
    scor.write("Game Over! Final Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
    screen.ontimer(screen.bye, 2000)

# Game loop
def game_loop():
    global score, delay

    screen.update()

    # Collision with food
    if snake.distance(food) < 20:
        food.goto(random.randint(-350, 350), random.randint(-300, 300))
        scor.clear()
        score += 1
        scor.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
        delay = max(0.1, delay - 0.001)  # Ensure delay doesn't go negative

        # Add new segment for the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("red")
        new_segment.penup()
        old.append(new_segment)

    # Move the segments
    for i in range(len(old) - 1, 0, -1):  # Start from the last segment
        a = old[i - 1].xcor()
        b = old[i - 1].ycor()
        old[i].goto(a, b)

    if len(old) > 0:
        a = snake.xcor()
        b = snake.ycor()
        old[0].goto(a, b)

    move()  # Call the move function to update the snake's position

    # Border collision check
    if (snake.xcor() < -350 or snake.xcor() > 350 or snake.ycor() < -300 or snake.ycor() > 300):
        game_over()

    # Snake collision with itself
    for segment in old:
        if segment.distance(snake) < 20:
            game_over()

    # Call game_loop again after delay
    screen.ontimer(game_loop, int(delay * 1000))  # Convert to milliseconds

# Start the game loop
game_loop()

# Keep the window open until it's closed by the user
turtle.mainloop()
