import time
from turtle import *
from score import Board
from player import Player
from ball import Ball
from bricks import Bricks


screen = Screen()
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.bgcolor("black")
screen.tracer(0)

player=Player()
brick_wall=Bricks()
ball=Ball()
board=Board()

#Move paddle/player
screen.listen()
screen.onkeypress(player.move_left,"Left")
screen.onkeypress(player.move_right,"Right")

heart=Turtle()
heart.penup()
heart.hideturtle()
heart.setheading(90)
heart.color('white')

game_on=True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    #Sense collision between ball and brick
    for brick in brick_wall.all_bricks:
        if ball.distance(brick) < 40:
            brick_wall.destroy_brick(brick)
            ball.bounce_y()
            board.update_score()
                  
    if player.distance(ball) < 50 and ball.ycor() < -220 :
        ball.bounce_y()
        
    if ball.ycor() > 580:
        ball.bounce_y()
    
    if ball.xcor() > 370 or ball.xcor() < -370:
        ball.bounce_x()
        
    if ball.ycor() < -290:
        ball.spawn_point()
        if ball.lives == 0:
            board.game_over()
            break
        
    hearts=''
    for life in range(0,ball.lives):
        hearts+='❤'
    heart.clear()
    heart.goto(-350,-230)
    heart.write(f"{hearts}",align="center",font=("Courier", 20, "normal"))
        
    
screen.exitonclick()