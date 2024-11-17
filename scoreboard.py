from turtle import Turtle

FONT = ("Gothic", 70, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0

        self.hideturtle()
        self.update_scoreboard()

    # def draw_boundary(self):
    #     self.goto(0, 280)
    #     self.setheading(270)
    #     for _ in range(28):
    #         self.pendown()
    #         self.forward(10)
    #         self.penup()
    #         self.forward(10)

    def update_scoreboard(self):
        self.clear()
        self.goto(-180, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(180, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
