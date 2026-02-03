# Magical Number Guessing Game (Python):

A fun command-line based number guessing game written in Python where the player must find a hidden “magical” number between 1 and 1000 within a limited number of guesses.

## Description:
The Magical Number Guessing Game is a Python program that randomly generates a secret number using Python’s built-in random module. The player is given 10 chances to guess the correct number.
After every incorrect guess, the program provides smart hints to guide the player, indicating whether the guessed number is too high or too low and suggesting how much the player should increase or decrease their next guess.

The game ends when:

-The player guesses the number correctly, or

-The player runs out of available guesses

## Features:

-Random number generation between 1 and 1000

-Maximum of 10 guesses

-Helpful hints based on how close the guess is

-Tracks number of attempts taken to win

-Displays the correct number if the player loses

-Beginner-friendly logic and structure

## Concepts Used:

-random module

-Loops (while)

-Conditional statements (if / elif / else)

-User input handling

-Counters and game logic

-Console output formatting

## Dependencies:

-Python 3.10 or later

-Any operating system that supports Python:

.Windows

.Linux

.macOS

-Built-in Python modules only:

.random

-No external libraries are required

## How the Game Works:

-A random number between 1 and 1000 is generated.

-The player starts with 10 available guesses.

-After each guess:

.The program checks if the guess is correct.

.If incorrect, a hint is displayed:

.“Add a number…” if the guess is too low

.“Subtract a number…” if the guess is too high

-The number of remaining guesses decreases after every attempt.

-The game ends when:

.The player finds the magical number, or

.All guesses are exhausted

## Installation:

-Clone the repository:

   ### git clone https://github.com/Immortal-code-creator/number-guessing-game-python.git

-Navigate to the project directory.

-Ensure Python is installed on your system.

## Executing the Program:

-Open a terminal or command prompt.

-Navigate to the project folder.

-Run the program:

   ### python number_guessing_game.py

Enter your guesses when prompted and follow the hints.

## Help:

-If the program does not run:

 .Make sure Python 3.10 or later is installed.
 
-Verify Python installation:

   ### python --version

-Ensure you are running the file from the correct directory.

## Author:

Aeshan Chowdhury

   ### GitHub: https://github.com/Immortal-code-creator
