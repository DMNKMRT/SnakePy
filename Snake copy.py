import turtle
import time
import random
import tkinter

from tkinter import *
from tkinter.ttk import *
from time import strftime

delay = 0.1

# Hier wird die Oberfläche/Spielfeld eingestellt. (Farbe, titel, größe etc.)






fenster = tkinter.Tk()
fenster.title("Snake spiel von Dominik")
fenster.geometry("600x600")
fenster.configure(background="azure")


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

# Functions
#Bewegen
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

# Körper weg, wenn gegen grenze
            for koe in körper:
                koe.goto(1000, 1000)

            körper.clear()

    time.sleep(delay)


fenster.mainloop()