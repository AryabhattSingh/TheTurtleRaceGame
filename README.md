# Project - The Turtle Race Game

## Overview

The Turtle Race Game is a fun Python project that utilizes the turtle module to create a graphical interface for an exciting turtle race. In this game, users can make guess on which of the seven colorful turtles will win the race. The game features an interactive interface, random turtle movement, and congratulatory or condolence messages based on the user's guess.

## Features

### Canvas Setup

- We start by setting up a race canvas with a specified height and width to provide a visually engaging environment for the turtle race.

### User Instructions

- Upon launching the game, instructions are displayed on the screen, guiding the user on how to place bets on the turtles.
- The instructions will remain on the screen until the user provides valid input following the displayed guidelines.

### Turtle Racing

- The game creates seven instances of the Turtle class, each representing one of the seven turtles participating in the race.
- To initiate the race, we use the `get_set_ready()` function to position each turtle at the left edge of the screen, separated by a fixed distance.
- Each turtle is assigned a unique color from VIBGYOR, making the race visually appealing.

### Gameplay

- The race continues until one of the turtles reaches the right edge of the screen.
- To determine how far each turtle moves in each step, we use the `random.randint()` function to generate a random number between 0 and 5, simulating the unpredictable nature of the race.

### Outcome

- After the race concludes, the user is informed whether their bet was successful or not.
- If the user's chosen color matches the color of the winning turtle, a congratulatory message is displayed on the race canvas, along with the color of the victorious turtle.
- In case the user's guess doesn't win, a condolence message is shown on the race canvas, accompanied by the color of the turtle that won.

### Game Closure

- To exit the game, simply click anywhere within the race canvas.
- The `screen.exitonclick()` event listener is used to detect clicks and gracefully close the race canvas.

## Installation

To run the Turtle Race Game, ensure you have Python installed on your system. This project uses the Python turtle module, which is a standard library, so there's no need for additional installations.

1. Clone this repository to your local machine.
   
   ```bash
   git clone https://github.com/AryabhattSingh/TheTurtleRaceGame.git
   ```

2. Navigate to the project directory.

   ```bash
   cd TheTurtleRaceGame
   ```

3. Run the game script.

   ```bash
   python main.py
   ```

## Gameplay

1. Follow the on-screen instructions to place your bet on one of the seven turtles.
2. Watch the exciting race unfold as the turtles dash towards the finish line.
3. After the race, check the screen for the outcome of your guess.
4. Click anywhere on the race canvas to close the game.

Have a great time playing the Turtle Race Game! Good luck, and may your chosen turtle be the winner!
