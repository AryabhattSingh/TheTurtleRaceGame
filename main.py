import turtle

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


def get_set_ready(turtle_object, color, x_position, y_position):
    pass


for i in range(0, 7):
    turtle_obj = turtle.Turtle()
    get_set_ready(turtle_object=turtle_obj, color=colors[i], x_position=x_pos, y_position=y_pos)
    y_pos -= 50
    turtles.append(turtle_obj)


screen.exitonclick()
