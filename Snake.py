import turtle
import time
import random

delay = 0.1

#Score
score = 0
high_score = 0

# Hier wird die Oberfläche/Spielfeld eingestellt. (Farbe, titel, größe etc.)
fenster = turtle.Screen()
fenster.title("Snake Spiel von Dominik")
fenster.bgcolor("azure")
fenster.setup(620, 620)
fenster.tracer(0) #schaltet screen uptdates aus

#Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Hier wird das Essen erstellt
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

#Körper von der Schlange
körper = []

#pen / Also der schriftzug von dem Score etc.
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 270)
pen.write("score: 0 High Score: 0", align= "center", font=("Courier", 24, "normal"))

#Functions
#Bewegen / richtungen
def goup():
    if head.direction != "down":
        head.direction = "up"
def godown():
    if head.direction != "up":
        head.direction = "down"
def goright():
    if head.direction != "left":
        head.direction = "right"
def goleft():
    if head.direction != "right":
        head.direction = "left"

#Bewegen
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

#Tastatur einbinden
fenster.listen()
fenster.onkeypress(goup, "w")
fenster.onkeypress(godown, "s")
fenster.onkeypress(goright, "d")
fenster.onkeypress(goleft, "a ")

#Main game loop
while True:
    fenster.update()

#checken ob schlange mit grenze kolidiert
    if head.xcor()>280 or head.xcor()<-280 or head.ycor()>280 or head.ycor()<-280:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

#Körper weg, wenn gegen grenze
        for k in körper:
            k.goto(1000, 1000)
        körper.clear()

#reset score
        score = 0
        pen.clear()
        pen.write("Score:  {}   High Score:   {}".format(score, high_score), align="center",font=("Courier", 24, "normal"))

# delay reset
        delay = 0.1

    #ob die schlange das essen berührt
    if head.distance(food) < 20:

#Essen geht an einen zufälligen punkt
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

#körperteil hinzufügen
        new_körper = turtle.Turtle()
        new_körper.speed(0)
        new_körper.shape("square")
        new_körper.color("lightgreen")
        new_körper.penup()
        körper.append(new_körper)

#Zeit kürzen
        delay = delay - 0.005

#Score erhöhen
        score = score + 1

        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score:  {}   High Score:   {}".format(score, high_score), align= "center", font=("Courier", 24, "normal"))

#Körper bewegt sich mit head: Letzter Körper wird zu erst weiter nachvorne bewegt
    for index in range(len(körper)-1, 0, -1):
        x = körper[index-1].xcor()
        y = körper[index-1].ycor()
        körper[index].goto(x, y)

#Körper 0 bewegen
    if len(körper) > 0:
        x = head.xcor()
        y = head.ycor()
        körper[0].goto(x, y)

    move()

# Ob Schlange eigenen Körper berührt
    for k in körper:
        if k.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

#Delay reset
            delay = 0.1

# reset score
            score = 0
            pen.clear()
            pen.write("Score:  {}   High Score:   {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))

# Körper weg, wenn gegen grenze
            for koe in körper:
                koe.goto(1000, 1000)

            körper.clear()

    time.sleep(delay)

fenster.mainloop()