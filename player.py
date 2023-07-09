from turtle import Turtle

STARTING_POSITION = (10, -250)

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1,stretch_len=5)
        self.color("white")
        self.goto(STARTING_POSITION)
    
    def move_left(self):
        if self.xcor() >= -300:
            self.goto(self.xcor()-25, self.ycor())
        
    def move_right(self):
        if self.xcor() <= 300:
            self.goto(self.xcor()+25, self.ycor())
            