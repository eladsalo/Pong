from turtle import Turtle
FONT = 50
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self, side):
        self.score = 0
        super().__init__()
        self.penup()
        self.side = side
        if side == "left":
            self.goto(-40, 220)
        else:
            self.goto(40, 220)
        self.color("white")
        self.hideturtle()
        self.write(f"{0}", True, align=ALIGNMENT, font=("Ariel", FONT, "normal"))

    def increase_score(self, in_double_round):
        if in_double_round:
            self.score += 2
        else:
            self.score += 1
        self.clear()
        if self.side == "left":
            self.goto(-40, 220)
        else:
            self.goto(40, 220)

        self.write(f"{self.score}", True, align=ALIGNMENT, font=("Ariel", FONT, "normal"))


