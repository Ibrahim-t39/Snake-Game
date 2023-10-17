from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial",24,"normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        with open("my_file.txt") as data:
            self.high_score = int(data.read())
        
    def draw(self):
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(x = 0,y = 260)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align= ALIGNMENT, font=FONT)
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("my_file.txt", mode="w") as data:
                data.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()    
            
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        