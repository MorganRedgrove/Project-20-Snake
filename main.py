from turtle import Turtle,Screen
from random import randint
from time import sleep
from sys import exit

def up():
    if snake_block.heading() != 270:
        snake_block.setheading(90)
def down():
    if snake_block.heading() != 90:
        snake_block.setheading(270)
def left():
    if snake_block.heading() != 0:
        snake_block.setheading(180)
def right():
    if snake_block.heading() != 180:
        snake_block.setheading(0)

def cull_cord():
    if len(stamp_cord) > snake_length:
        stamp_cord.__delitem__(0)

def cull_stamp():
    if len(stamp_list) > snake_length:
        snake_block.clearstamp(stamp_list[0])
        stamp_list.__delitem__(0)

def draw_food():
    food_block.setx((-240 + (10* randint(1,48))))
    food_block.sety(-240 + (10* randint(1,48)))
    food_list.append(food_block.stamp())
    food_cord.append(food_block.pos())

def cull_food():
    food_block.clearstamp(food_list[0])
    food_list.__delitem__(0)

screen = Screen()
screen.setup(width=495, height=495)

snake_block = Turtle(shape="square")
snake_block.shapesize(0.45,0.45)
snake_block.penup()

food_block = Turtle(shape="circle")
food_block.shapesize(0.45,0.45)
food_block.penup()
food_block.hideturtle()

snake_length = 5
score = snake_length - 5


stamp_list = []
stamp_cord = []

food_list = []
food_cord = []

draw_food()

screen.listen()
screen.onkeypress(fun=up, key="w")
screen.onkeypress(fun=down, key="s")
screen.onkeypress(fun=left, key="a")
screen.onkeypress(fun=right, key="d")

game_over = False
while game_over == False:
    snake_block.forward(10)

    if snake_block.pos() in stamp_cord:
        print("GAME OVER!")
        game_over = True
    if snake_block.xcor() >240 or snake_block.xcor() <-240:
        print("GAME OVER!")
        game_over = True
    if snake_block.ycor() >240 or snake_block.ycor() <-240:
        print("GAME OVER!")
        game_over = True
    if snake_block.distance(food_block) <10:
        draw_food()
        cull_food()
        snake_length += 1

    stamp_list.append(snake_block.stamp())
    stamp_cord.append(snake_block.pos())

    cull_stamp()
    cull_cord()
    sleep(0.1)


screen.exitonclick()