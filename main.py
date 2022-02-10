import turtle as t
import random


# import colorgram


def change_direction_random(turtle):
    angles = [0, 90, 180, 270]
    turtle.setheading(random.choice(angles))


def change_color_random(turtle):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    turtle.color(r, g, b)


def draw_shape(turtle, side_num):
    change_color_random(turtle)
    for _ in range(side_num):
        turtle.forward(100)
        # calculate the angle of rotation based on shape
        turtle.right(360 / side_num)


t.colormode(255)

tim = t.Turtle()
tim.shape("turtle")
tim.color("red")

# Drawing a square ***************************************************************************************
# for _ in range(0, 4):
#     tim.forward(100)
#     tim.right(90)

# Drawing a dashed line **********************************************************************************
# for _ in range(0, 10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# Drawing different geometrical shapes *******************************************************************
# for num_of_sides in range(3, 10):
#     draw_shape(tim, num_of_sides)

# Drawing a Random Walk
# tim.pensize(15)
# tim.speed("fastest")
# for _ in range(200):
#     change_direction_random(tim)
#     change_color_random(tim)
#     tim.forward(30)

# Drawing a Spirograph
# tim.speed("fastest")
# angle = 10
# for _ in range(int(360 / angle)):
#     change_color_random(tim)
#     tim.circle(100, None, 100)
#     tim.left(angle)

# Find colors contained in an image
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
              (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]

tim.penup()
tim.speed("fastest")
tim.hideturtle()

tim.setx(-250)
tim.sety(-250)

for x in range(10):
    for y in range(10):
        tim.dot(20, random.choice(color_list))
        tim.setx(tim.xcor() + 50)

    # return the turtle to the beginning of the new row
    tim.sety(tim.ycor() + 50)
    tim.setx(-250)

screen = t.Screen()
screen.exitonclick()
