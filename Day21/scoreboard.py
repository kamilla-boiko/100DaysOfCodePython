from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Garamond", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        with open("data.txt") as file:
            self.high_score = int(file.read())

        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()
