from turtle import Turtle
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-290,265)
        self.update_level()

    def update_level(self):
        self.write(f"level:{self.level}", align= "left", font= FONT)   

    def increase_level(self):
        self.level += 1   
        self.clear() 
        self.update_level()

    def game_over(self):
        self.goto(0,0)
        self.write(f"game over!", align= "center", font= FONT)    