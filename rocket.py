from turtle import Turtle

MOVE_DISTANCE = 45


class Rocket(Turtle):
    def __init__(self, player_side):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        if player_side == "right":
            self.goto(350, 0)
        else:
            self.goto(-350, 0)

    def up(self):
        self.goto(self.xcor(), self.ycor()+MOVE_DISTANCE)

    def down(self):
        self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)




