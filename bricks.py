from turtle import Turtle
import random
COLORS = ["red","orange", "yellow", "green", "blue", "purple"]

class Bricks():
    def __init__(self):
        self.all_bricks=[]
        self.color_number=0
        self.starting_y=280
        while self.color_number != 6:
            random_var=0
            self.current_x=0
            while self.current_x < 360:
                brick=Turtle()
                brick.penup()
                brick.shape('square')
                brick.shapesize(stretch_wid=1.5,stretch_len=3)
                brick.color(COLORS[self.color_number])
                
                if self.color_number%2 == 0:
                    self.starting_x=-390
                else:
                    self.starting_x=-426
                
                
                brick.goto(self.starting_x+(random_var*66), self.starting_y-(self.color_number)*33)
                self.current_x=brick.xcor()        
                self.all_bricks.append(brick)
                random_var+=1
                
            self.color_number+=1
            
    def destroy_brick(self, brick):
        brick.goto(10000,10000)
        
            
        