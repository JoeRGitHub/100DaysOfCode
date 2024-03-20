from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


with open("/Users/yossir-macos/git/python-files/100DaysOfCode/snake-game/test.txt", 'r') as f:
    content = f.read()

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.high_score = int(content)
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()

        if self.points >= self.high_score:
            self.write(f"Score: {self.points} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)
        else:
            self.write(f"Score: {self.points} High Score: {content}", move=False, align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.points += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(x=0, y=0)
        #self.write("GAME-OVER.", move=False, align=ALIGNMENT, font=('FONT', 30, 'normal'))
        self.write("GAME-OVER.", move=False, align=ALIGNMENT, font=FONT)

    def save_high_score(self):
        if self.points > self.high_score:
            self.high_score = self.points
        #self.points = 0

        # Save high_score to a file so it will show in the next time the game is used
        with open("test.txt", mode='w') as file:
            file.write(str(self.high_score))
        self.update_score()