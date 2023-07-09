from turtle import Turtle
from random import randint

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.setheading(90)
        self.x_move=10
        self.y_move=10
        self.move_speed=0.07
        self.lives=4
        self.spawn_point()
        
    def spawn_point(self):
        self.x_move=10
        self.y_move=10
        self.lives-=1
        self.goto((50, -200))
        
    def move(self):
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x, new_y)
        
    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed*=0.9
        
        
    
        