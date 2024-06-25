#Imports
from tphysics import *
from random import randint
import time
import turtle as t
from time import sleep
import random
import tkinter

print("""$~ READMEDon't get hit by the enemy! Try to eat as many candies as you can to gain more points.

This project was made to demonstrate my proficiency with Python programming and the syntax used, and to show my understanding of game-based logic and fundamentals behind
programming games. Uses a library tPhysics made my by old Computer Science teacher Billy Rebecchi, and was able to utilize the simplicity of the library to program this game.""")



colours = ["red","lime","green","purple","indigo","yellow","","","","blue","orange"]
backs = ["back.gif","back.gif"]

#Create a new game
game = Game('Dungeon Crawler', 600, 600, 'black')
t.write("LOADING", align="center", font=("Aharoni", 46, "normal")) 
t.hideturtle()
t.clear()

# Create a player and add them to the game
player = Rectangle(randint(-300,300), randint(-300,300), 32, 32)
player.fill_colour = random.choice(colours)
game.add_shape(player)

# Custom BG
screen = turtle.Screen()
screen.setup(950,850)
screen.bgpic(backs[1])

# Create a LEFT side 
walls = [
    Rectangle(0, -400, 900, 4),
    Rectangle(0, 400, 900,4),
    Rectangle(-450,0,4,800),
    Rectangle(450,0,4,800)
    ]

colourRandom = "grey"

# Add the walls to the game and set fill colour
for w in walls:
    w.fill_colour = colourRandom
    game.add_shape(w)

# Create a enemy and add them to the game
enemy = Circle(randint(-300, 300), randint(-300, 300), 15)
enemy.fill_colour = 'red'
game.add_shape(enemy)

# Bad powerups
pu2 = Rectangle(randint(-300,300), randint(-300,100), 20,20)
pu2.fill_colour = 'lavender'
game.add_shape(pu2)


# speed Power-Ups 
pu = Rectangle(randint(-300,300), randint(-300,100), 16,16)
pu.fill_colour = 'light sky blue'
game.add_shape(pu)


    
# Set the physics
playerSpeed = 7
enemySpeed = 4

#scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(150, 350)
pen.write("""Score: 0        High Score: 0""", align="left", font=("Cascadia Code", 12, "normal"))
score = 0
highScore = 0

try:
    f = open("highScore.txt")
    highScore = int(f.read())
except FileNotFoundError:
    highScore = "{ERROR - Not found}"  


running = False


    
#Game loop
while True:
    pen.clear()
    pen.write("""Score: {}    High Score: {}""".format(score, highScore), align="LEFT", font=("Cascadia Code", 12, "normal")) 
    
    
    
    if score == highScore:
        highScore = score
        f = open("highScore.txt", "w")
        f.write(str(highScore))
        f.close()
         
            
    if 0 > score:
        playerSpeed = 7
        enemySpeed = 4.25
        score = 0
        

    if score > highScore:
        highScore = score
        
    


    if running:

        if pu.collide(pu2):
            pu2.x = randint(-300 , 300)
            pu2.y = randint(-300 , 300)
            
            

        # Check for movement

        if game.ispressed('Left') or game.ispressed('a'):
            player.x += playerSpeed

        if game.ispressed('Right') or game.ispressed('d'):
            player.x -= playerSpeed

        if game.ispressed('Up') or game.ispressed('w'):
            player.y += playerSpeed

        if game.ispressed('Down') or game.ispressed('s'):
            player.y-= playerSpeed

        if player.x >= enemy.x:
            enemy.x += enemySpeed

        if player.x <= enemy.x:
            enemy.x -= enemySpeed


        if player.y >= enemy.y:
            enemy.y += enemySpeed

        if player.y <= enemy.y:
            enemy.y -= enemySpeed
            

        if player.collide(enemy):
            
            player.x = randint(-300, 300)
            player.y = randint(-300, 300)
            
            running = False
            


        
            

        if player.collide(pu):
            playerSpeed = playerSpeed + 0.9
            pu.x = randint(-300, 300)
            pu.y = randint(-300, 300)
            enemySpeed = enemySpeed + 0.64
            score = score + 10
            game.add_shape(enemy)


        if player.collide(pu2):
            playerSpeed = playerSpeed + 1.8
            pu2.x = randint(-300, 300)
            pu2.y = randint(-300, 300)
            enemySpeed = enemySpeed + 1.28
            score = score + 15


        if player.collide(pu2):
            playerSpeed = playerSpeed + 1.8
            pu2.x = randint(-300, 300)
            pu2.y = randint(-300, 300)
            enemySpeed = enemySpeed + 1.28
            score = score + 20



        if player.x - player.width / 2 < -450:
            player.x = 450 - player.width / 2
        if player.x + player.width / 2 > 450:
            player.x = -450 + player.width / 2


        if player.y - player.width / 2 < -400:
            player.y = 400 - player.width / 2
        if player.y + player.width / 2 > 400:
            player.y = -400 + player.width / 2
   

# To resetz game 

    else:

        if game.ispressed("space"):
            t.clear
            playerSpeed = 7
            running = True
            enemySpeed = 4.25
            pen.clear()
            pen.write("""Score: {}    High Score: {}""".format(score, highScore), align="LEFT", font=("Cascadia Code", 12, "normal")) 
            score = 0

            enemy.x = randint(-300 , 300)
            enemy.y = randint(-300 , 300)


            
    # Update the game
    game.update()
