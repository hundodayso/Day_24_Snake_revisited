from turtle import Turtle, Screen
import random

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.rev_segments = []
        self.head = self.segments[0]


    def create_snake(self):
        for position in START_POSITIONS:
#            self.add_segment(position[0], position[0])
            new_segment = Turtle(shape="square")
            new_segment.up()
            new_segment.color(Snake.colour_randomiser())
            new_segment.setpos(position)
            self.segments.append(new_segment)

    def add_segment(self, xpos, ypos):
        new_segment = Turtle(shape="square")
        new_segment.up()
        new_segment.color(Snake.colour_randomiser())
        new_segment.setpos(xpos, ypos)
        self.segments.append(new_segment)

    def move(self):
        snake_length = len(self.segments)
        self.rev_segments.clear()
        rev_segments = list(reversed(self.segments))
        for index, seg in enumerate(rev_segments):
            if index <= snake_length - 2:
                next_posx = rev_segments[index + 1].xcor()
                next_posy = rev_segments[index + 1].ycor()
                seg.setpos(x=next_posx, y=next_posy)
                # time.sleep(0.5)
        self.head.forward(MOVE_DISTANCE)

    def check_tail(self):
        snake_length = len(self.segments)
        for seg_num in range(1, snake_length, 1):
            if round(self.segments[seg_num].xcor()) == round(self.head.xcor()) and round(self.segments[seg_num].ycor()) == round(self.head.ycor()):
                print("HEAD")
                return True

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def colour_randomiser():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return r, g, b




