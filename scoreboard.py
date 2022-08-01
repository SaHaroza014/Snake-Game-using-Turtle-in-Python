from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = int(0)
        self.goto(0, 260)
        self.color('white')
        self.write(f'Score: {self.score}', align='center', font=('Calibre', 24, 'normal'))
        self.hideturtle()
        self.penup()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', align='center', font=('Calibre', 24, 'normal'))

    def end_game(self):
        self.goto(0, 0)
        self.write(f'Game over!', align='center', font=('Calibre', 24, 'normal'))
        self.goto(0, -40)
