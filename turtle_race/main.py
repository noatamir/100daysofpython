from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
guess = screen.textinput(title="The Rainbow Turtle Race",
                         prompt="Pick the winning Turtle: \n (red, orange, yellow, green, blue, purple, brown, black, "
                                "pink")

num_turtles = 9
colors = ["red2", "OrangeRed", "goldenrod1", "ForestGreen", "DodgerBlue4", "DarkMagenta", "brown4", "grey10", "magenta"]
color_names = {-160 : "red",
               -120 : "orange",
               -80 : "yellow",
               -40 : "green",
               0 : "blue",
               40 : "purple",
               80 : "brown",
               120 : "black",
               160 : "pink",
               }

tommies = []
for t in range(num_turtles):
    tommies.append(Turtle())
    tommies[t].shape("turtle")
    tommies[t].penup()
    tommies[t].color(colors[t])
    tommies[t].setposition(-240, -160 + (t * 40))


def move_forward():
    random.shuffle(tommies)
    for t in tommies:
        t.forward(random.randint(1, 10))
        if t.xcor() >= 225:
            return False
    return True


def winning_turtle():
    x = 0.0
    winner_y = 0
    for t in tommies:
        if t.xcor() > x:
            x = t.xcor()
            winner_y = t.ycor()
            # print(t.xcor(),t.ycor(),t.color())
            # print(winner_y)
    the_winner = color_names[winner_y]
    return the_winner


racing = True

while racing:
    racing = move_forward()

the_winner_is = winning_turtle()

if guess.lower() == the_winner_is.lower():
    print(f"Congrats! {guess} won The Rainbow Turtle Race!")
else:
    print(f"{guess} lost! {the_winner_is} has won The Rainbow Turtle Race this time!")

screen.exitonclick()
