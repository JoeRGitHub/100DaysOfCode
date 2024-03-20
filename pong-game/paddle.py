from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position_x, position_y):
        super().__init__()
        self.shape("square")
        self.color('white')
        self.shapesize(5, 1)  # 1 = 20
        self.penup()
        self.goto(position_x, position_y)

    def go_up(self):
        y_new_up = self.ycor() + 20
        self.goto(self.xcor(), y_new_up)

    def go_down(self):
        y_new_down = self.ycor() - 20
        self.goto(self.xcor(), y_new_down)
