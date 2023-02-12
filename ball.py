from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self, side):
        super().__init__()
        self.move_to_side = side
        self.penup()
        self.color("white")
        self.shape("circle")
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move = -self.y_move

    def bounce_x(self):
        self.x_move = -self.x_move

    def stop(self):
        tuple_pos = (self.x_move, self.y_move)
        self.x_move = 0
        self.y_move = 0
        return tuple_pos


    def boom(self):
        b1 = Ball(self.move_to_side)
        b1.x_move = self.x_move
        b1.y_move = self.y_move
        b1.goto(self.xcor(), self.ycor()-30)

        b2 = Ball(self.move_to_side)
        b2.x_move = self.x_move
        b2.y_move = self.y_move
        b2.goto(self.xcor(), self.ycor()+30)



