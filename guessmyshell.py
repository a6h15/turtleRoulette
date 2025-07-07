import random
from turtle import Turtle , Screen
import random

window = Screen()
is_race_on = False
window.setup(width=500,height=400)
user_guess = window.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter color(red,yellow,green,blue,purple,orange): ")


colors = ["red","yellow","green","blue","purple","orange"]
y_positions = [-70,-40,-10,20,50,80]           # list of y position as all turtle would be on the same place
all_t = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_t.append(new_turtle)


if user_guess:
    is_race_on = True               #done as so the while loop doesnt start when the user is making their guess.

while is_race_on:
    for turtle in all_t:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_guess.lower():
                print(f"You won , the {winning_color} turtle is the winner!")
            else:
                print(f"You lost , the {winning_color} turtle is the winner!")

        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)

# def move_for():
#     diddy.forward(10)
#
# def move_back():
#     diddy.backward(10)
#
# def turn_left():
#     new_heading = diddy.heading() + 10              #adding 10 degrees to the current heading
#     diddy.setheading(new_heading)
#
# def turn_right():
#     new_heading = diddy.heading() - 10
#     diddy.setheading(new_heading)
#
# def clear():
#     diddy.clear()
#     diddy.penup()
#     diddy.home()
#     diddy.pendown()
#
# window.listen()
# window.onkey(key="w",fun=move_for)
# window.onkey(key="s",fun=move_back)
# window.onkey(key="a",fun=turn_left)
# window.onkey(key="d",fun=turn_right)
# window.onkey(key="c",fun=clear)
window.exitonclick()
