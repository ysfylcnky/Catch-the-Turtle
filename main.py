import sys
import turtle
import time
from random import randint

#SCREEN
win = turtle.Screen()
win.title("Catch the Turtle")
win.bgcolor("light blue")
win.setup(width=800,height=600)

#SCORE TURTLE
skor = 0
skor_yazisi = turtle.Turtle()
skor_yazisi.color("green")
skor_yazisi.hideturtle()
skor_yazisi.penup()
skor_yazisi.goto(-375, 250)
skor_yazisi.write(f"SCORE: {skor}", align="left", font=("Arial", 20, "normal"))

#TURTLE TURTLE
t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.shapesize(2)
t.penup()
t.hideturtle()

#COUNTER TURTLE
counter = turtle.Turtle()
counter.hideturtle()
counter.penup()
counter.color("green")
counter.goto(-25, 200)

#GAME
game_over = False

#FUNCTIONS
def countdown(time_left):
    global game_over
    if time_left > 0:
        counter.clear()
        counter.write(f"{time_left}", align="center", font=("Arial", 40, "normal"))
        win.ontimer(lambda: countdown(time_left - 1), 1000)  # Her saniyede bir azalt
    else:
        game_over = True
        counter.clear()
        counter.write("Bitti!", align="center", font=("Arial", 40, "normal"))
def skor_guncelle(x,y):
    global skor
    if not game_over:
        skor += 10
        skor_yazisi.clear()
        skor_yazisi.write(f"SCORE: {skor}", align="left", font=("Arial", 20, "normal"))
def randomPlace():
    if not game_over:
        t.hideturtle()
        x = randint(-200,200)
        y = randint(-200,200)
        t.goto(x,y)
        t.showturtle()
        win.ontimer(randomPlace,600)
    else:
        t.hideturtle()

countdown(5)
t.onclick(skor_guncelle)
randomPlace()


win.mainloop()


