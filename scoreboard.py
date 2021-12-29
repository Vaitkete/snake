from turtle import Turtle
ALIGNEMT = "center"
FONT = ("Arial", 16, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("White")
        self.goto(0, 270)
        with open("data.txt") as result:
            self.high_score = int(result.read())
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High score: {self.high_score}", align=ALIGNEMT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as new_result:
                new_result.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="Game over", align=ALIGNEMT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()








