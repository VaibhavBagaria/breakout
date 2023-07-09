from turtle import Turtle
import time

class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.hideturtle()
        self.setheading(90)
        self.color('white')
        
    def scoreboard(self):
        self.goto(0,0)
        time.sleep(1)
        self.write(f"Score:{self.score}",align="center",font=("Courier", 20, "normal"))
        
    def update_score(self):
        self.score+=3
        self.clear()
        self.scoreboard()
    
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over\nYour score is {self.score}",align="center",font=("Courier", 20, "normal"))
        

        