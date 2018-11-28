# Space Invaders
import turtle
import math
import os
import random

# Set up screen
mainScreen = turtle.Screen()
mainScreen.bgcolor("black")
mainScreen.title("Space Invaders")
mainScreen.bgpic("space_invaders_background.gif")

# Register the shapes
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")

# Create game border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("White")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)

for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)

border_pen.hideturtle()

# Set score to 0
score = 0

# Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align = "left", font = ("Arial", 14, "normal"))
score_pen.hideturtle()
                
# Create the player
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

# Choose a number of enemies
numEnemies = 5

# Create an empty list of enemies
enemies = []

# Add enemies to list
for i in range(numEnemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemyspeed = 2

# Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

# Define bullet state
# ready = ready to fire
# fire = bullet is firing (moving)
bulletstate = "ready"

# Use arrow keys to move player left and right
def move_left():
   x = player.xcor()
   x -= playerspeed
   if x < -280:
       x = -280
   player.setx(x)

def move_right():
   x = player.xcor()
   x += playerspeed
   if x > 280:
       x = 280
   player.setx(x)

def fire_bullet():
    #Declare bulletstate as a global if it needs to be changed
    global bulletstate
    if bulletstate == "ready":
        os.system("afplay laser.wav&")
        bulletstate = "fire"
        # Move the bullet to above player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) + math.pow(t1.ycor()-t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False

# Create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

# Main game loop
while True:

    for enemy in enemies:
        # Move enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        # Reverse direction and move down
        if enemy.xcor() > 280:
            # Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # Change enemy direction
            enemyspeed *= -1

        if enemy.xcor() < -280:
            # Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # Change enemy direction
            enemyspeed *= -1
            
        # Check for collision between bullet and enemy
        if isCollision(bullet, enemy):
            os.system("afplay explosion.wav&")
            # Reset bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            # Reset enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            # Update the score
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align = "left", font = ("Arial", 14, "normal"))

        # Check for collision between player and enemy
        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break
    
    # Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    # Check to see if the bullet is at the top border
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bullet.sety(-240)
        bulletstate = "ready"

    
