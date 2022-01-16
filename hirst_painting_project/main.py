# import colorgram
from turtle import Turtle, Screen, colormode
import random

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     # new_color = (r, g, b)
#     rgb_colors.append((r, g, b))
# print(rgb_colors)

rgb_colors = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73),
              (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
              (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19),
              (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

# rgb_colors = [(241, 229, 215), (189, 157, 123), (77, 99, 121), (128, 78, 89), (131, 92, 76), (138, 157, 170),
#               (239, 224, 229), (81, 108, 91), (179, 143, 153), (222, 228, 235), (140, 166, 155), (222, 232, 226),
#               (169, 101, 114), (221, 198, 141), (176, 104, 91), (144, 144, 89), (61, 41, 50), (42, 46, 64),
#               (90, 49, 59), (59, 45, 38), (53, 57, 86), (105, 142, 125), (218, 180, 172), (98, 139, 149),
#               (214, 178, 185), (112, 124, 150), (41, 56, 48), (95, 50, 46), (47, 75, 64), (178, 199, 190)]

art = Turtle()
art.hideturtle()
art.width(3)
colormode(255)
art.speed(0)


def new_color():
    return random.choice(rgb_colors)


art.penup()

for x_pos in range(-5, 6):
    for y_pos in range(-5, 6):
        art.color(new_color())
        art.setposition((x_pos * 50, y_pos * 50))
        art.dot(20)

screen = Screen()
screen.exitonclick()
