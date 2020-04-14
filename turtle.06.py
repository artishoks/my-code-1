import turtle as t
from random import randint, random

def draw_circle(size, col, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(col)
    t.speed('fastest')
    t.pensize(random())
    t.begin_fill()
    t.circle(size)
    t.end_fill()

#Основной код
t.Screen().bgcolor('dark blue')

choice = input('How many circles do you want? ')
print('you want ' + choice + ' circles')
choice = int(choice)
num = 0
while num < choice:
    num = num + 1
    ranSize = randint(20, 30)
    ranCol = (random(), random(), random())
    ranX = randint(-350, 300)
    ranY = randint(-250, 250)
    

    draw_circle(ranSize, ranCol, ranX, ranY)
    

    
