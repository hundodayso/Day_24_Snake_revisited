from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.set_score(0)

    def set_score(self, score):
        self.score = score
        self.clear()
        self.penup()
        self.speed("fastest")
        self.hideturtle()
        self.color(255, 255, 255)
        self.setpos(0, 270)
        self.write(f"Score = {self.score}", True, align="center",font=('Courier', 20, 'normal'))

    def get_score(self):
        return self.score

    def game_over(self):
        self.hideturtle()
        self.color(255, 255, 255)
        self.setpos(0, 0)
        self.write(f"GAME OVER", True, align="center", font=('Courier', 20, 'normal'))


