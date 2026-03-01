from turtle import Turtle

FONT = ("Courier", 20, "bold")
FONT_GO = ("Bold Italic", 30 , "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-270,240)
        self.level = 1
        self.update()


    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def next_level(self):
        self.level += 1
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT_GO)
