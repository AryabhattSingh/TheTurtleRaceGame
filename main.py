import random
import turtle


def get_set_ready(turtle_object, color, x_position, y_position):
    """This function sets the shape and color of the turtle, and it positions a turtle to the starting point of the
    race i.e. left edge of the canvas. It takes 4 arguments - turtle object, color name, x position and y position."""
    turtle_object.shape("turtle")
    turtle_object.color(color)
    turtle_object.penup()
    turtle_object.goto(x=x_position, y=y_position)


screen = turtle.Screen()
screen.setup(500, 400)

valid_inputs = ["v", "i", "b", "g", "y", "o", "r"]
user_bet = ""
while user_bet not in valid_inputs:
    user_bet = turtle.textinput(title="Make your bet.", prompt="There are 7 turtles in the race with colors matching "
                                                               "with VIBGYOR.\nWhich turtle will win the race? Valid "
                                                               "inputs are V, I, B, G, Y, O, R.\nEnter a color: ")

turtles = []
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
x_pos = -240
y_pos = 150

for i in range(0, 7):
    turtle_obj = turtle.Turtle()
    get_set_ready(turtle_object=turtle_obj, color=colors[i], x_position=x_pos, y_position=y_pos)
    y_pos -= 50
    turtles.append(turtle_obj)

is_game_on = True
while is_game_on:
    for turtle_obj in turtles:
        random_distance = random.randint(0, 5)
        turtle_obj.forward(random_distance)

        if turtle_obj.xcor() >= 222:
            turtle.hideturtle()
            turtle.penup()
            turtle.goto(x=-30, y=0)
            if turtle_obj.pencolor()[0] == user_bet:
                turtle.write(f"\nCongratulations!\nYour turtle won.\nThe winner is {turtle_obj.pencolor()} turtle.")
            else:
                turtle.write(f"\nBetter luck next time!\nYour turtle lost.\nThe winner is {turtle_obj.pencolor()} turtle.")
            is_game_on = False

screen.exitonclick()
