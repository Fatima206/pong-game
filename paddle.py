from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        # paddle = Turtle()
        # can get rid of this line as our paddle class is now same as turtle class
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)  # every turtle starts out as 20 by 20 pixels
        self.penup()
        self.speed("fastest")
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)  # to its current xcor not changing it

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
