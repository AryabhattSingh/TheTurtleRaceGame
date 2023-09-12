import turtle

screen = turtle.Screen()
screen.setup(500, 400)

valid_inputs = ["v", "i", "b", "g", "y", "o", "r"]
user_bet = ""
while user_bet not in valid_inputs:
    user_bet = turtle.textinput(title="Make your bet.", prompt="There are 7 turtles in the race with colors matching "
                                                               "with VIBGYOR.\nWhich turtle will win the race? Valid "
                                                               "inputs are V, I, B, G, Y, O, R.\nEnter a color: ")


screen.exitonclick()
