from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
    def text_box(self):
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.color("white")
        self.write("Score:", move=False, align='center', font=('Ariel', 20, 'normal'))

class Increase_score(Scoreboard):
    def __init__(self):
        super().__init__()
        self.points = 0

    def dot_box(self):
        self.penup()
        self.goto(x=40, y=270)
        self.hideturtle()
        self.color("white")
        self.write("0", move=False, align='center', font=('Ariel', 18, 'normal'))

    def score(self):
        super().text_box()
        self.penup()
        self.goto(x=40, y=270)
        self.hideturtle()
        self.color("white")
        self.clear()
        self.points += 1
        self.write(self.points, move=False, align='center', font=('Ariel', 18, 'normal'))
        #self.write(self.points)
        print(self.points)