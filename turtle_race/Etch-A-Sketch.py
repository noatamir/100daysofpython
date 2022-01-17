from turtle import Turtle, Screen

tommy = Turtle()
tommy.pd()
tommy.width(2)


screen = Screen()


def move_forward():
    tommy.forward(50)


def move_backward():
    tommy.backward(50)


def turn_left():
    tommy.setheading(tommy.heading() + 50)


def turn_right():
    tommy.setheading(tommy.heading() - 50)


def clear_drawing():
    tommy.clear()
    tommy.penup()
    tommy.home()
    tommy.pendown()


screen.listen()

screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_drawing, "c")

screen.exitonclick()
