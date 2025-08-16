STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto_start()
        self.setheading(90)

    def move_distance(self):
        self.forward(MOVE_DISTANCE)

    def move_left (self):
        x = self.xcor() - 10
        self.setx(x)     
    
    def move_right (self):
        x = self.xcor() + 10
        self.setx(x) 

    def goto_start (self):
        self.goto(STARTING_POSITION)    

    def finish_line (self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else :
            return False        