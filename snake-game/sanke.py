from turtle import Screen, Turtle

SQUARE_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

screen = Screen()


class Snake:
    def __init__(self):
        self.square_list = []
        self.create_snake()
        self.head = self.square_list[0]

    def create_snake(self):
        for position in SQUARE_POS:
            square = Turtle("square")
            square.penup()
            square.color("white")
            square.goto(position)
            self.square_list.append(square)

    def move(self):
        global new_segment_x, new_segment_y
        for seg_num in range(len(self.square_list)-1, 0, -1):  # the -1 is for the square_list[0-2]
            #print(seg_num)
            new_segment_x = self.square_list[seg_num - 1].xcor()  # use the -1 to start form the end
            new_segment_y = self.square_list[seg_num - 1].ycor()
            self.square_list[seg_num].goto(new_segment_x, new_segment_y)
            #print(new_segment_x, new_segment_y)
        self.head.forward(MOVE_DISTANCE)

    # Extend snake tail
    def snake_extend(self):
        new_square = Turtle("square")
        new_square.penup()
        new_square.color("white")
        new_square.goto(new_segment_x, new_segment_y)
        self.square_list.append(new_square)

    # Prevent snake from going backward
    def up(self):
        if self.head.heading() != DOWN:  # Heading() is a method
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def home(self):
        self.head.home()

    def pause(self):
        self.head.pause()


