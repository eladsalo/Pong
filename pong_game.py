
from turtle import Screen, Turtle
from scoreboard import Scoreboard
from rocket import Rocket
from ball import Ball
import time


def run():
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("pong game")

    screen.tracer(0)

    left_score = Scoreboard("left")
    right_score = Scoreboard("right")

    create_line()
    player1_rocket = Rocket("left")
    player2_rocket = Rocket("right")
    ball = Ball("right")
    screen.listen()
    screen.onkey(key="w", fun=player1_rocket.up)
    screen.onkey(key="s", fun=player1_rocket.down)
    screen.onkey(key="Up", fun=player2_rocket.up)
    screen.onkey(key="Down", fun=player2_rocket.down)
    screen.onkey(key="m", fun=ball.boom)
    speed_game = 0.05
    counter_rounds = 0
    in_double_round = False
    game_is_on = True

    while game_is_on:
        ball.move()

        speed_game = check_collision(ball, player1_rocket, player2_rocket, speed_game)
        if check_goal(ball, left_score, right_score, in_double_round):
            if in_double_round:
                screen.bgcolor("black")
                in_double_round = False
            speed_game = 0.05
            counter_rounds += 1
        if not in_double_round and counter_rounds % 3 == 0 and counter_rounds != 0:
            temp = ball.stop()
            double_round_massage(screen)
            ball.x_move = temp[0]
            ball.y_move = temp[1]
            in_double_round = True

        if left_score.score == 5 or right_score.score == 5:
            winner_massage(screen)
            game_is_on = False

        screen.update()
        time.sleep(speed_game)

    screen.exitonclick()


def check_collision(ball, player1_rocket, player2_rocket, speed_game):
    # collision with rockets
    if ball.move_to_side == "right":
        if ball.distance(player2_rocket) < 50 and ball.xcor() >= 320:
            ball.bounce_x()
            ball.move_to_side = "left"
            return speed_game * 0.9
    if ball.move_to_side == "left":
        if ball.distance(player1_rocket) < 50 and ball.xcor() <= -320:
            ball.bounce_x()
            ball.move_to_side = "right"
            return speed_game * 0.9

    # collision with walls
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()
    return speed_game


def check_goal(ball, left_score, right_score, in_double_round):
    # score a goal
    if ball.move_to_side == "right" and ball.xcor() >= 385:
        left_score.increase_score(in_double_round)
        ball.goto(0, 0)
        ball.move_to_side = "left"
        ball.bounce_x()
        return True
    if ball.move_to_side == "left" and ball.xcor() <= -385:
        right_score.increase_score(in_double_round)
        ball.goto(0, 0)
        ball.move_to_side = "right"
        ball.bounce_x()
        return True

    return False


def create_line():
    line = Turtle()
    line.color("white")
    line.penup()
    line.goto(0, 300)
    pen_up = False
    line.setheading(270)
    for _ in range(0, 600, 20):
        line.forward(20)
        if pen_up:
            line.penup()
            pen_up = False
        else:
            line.pendown()
            pen_up = True


def double_round_massage(screen):
    massage = Turtle()
    screen.bgcolor("green")
    massage.penup()
    massage.goto(0, 100)
    massage.color("black")
    massage.hideturtle()
    massage.write("Double round!", True, align="center", font=("Ariel", 30, "normal"))
    screen.update()
    time.sleep(2)
    massage.clear()


def winner_massage(screen):
    massage = Turtle()
    massage.penup()
    massage.goto(0, 100)
    massage.color("green")
    massage.hideturtle()
    massage.write(f"We have a winner!", True, align="center", font=("Ariel", 30, "normal"))
    screen.update()
    time.sleep(3)
    massage.clear()




