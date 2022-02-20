from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(-290, 260)
        self.color("black")
        self.penup()
        self.hideturtle()
        self.player_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level:{self.player_score}", font=FONT)

    def player_point(self):
        self.player_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
