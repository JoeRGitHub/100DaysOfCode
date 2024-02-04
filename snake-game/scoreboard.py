from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"Score: {self.points}", move=False, align=ALIGNMENT, font=FONT)
    def increase_score(self):
        self.points += 1
        self.clear()
        self.update_score()
        print(self.points)