#!/usr/bin/env python3

from art import logo
from random import randint

def game_run():
    def intro(hint_number):
        print(logo)
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100.")
        print(f"HINT: Its {hint_number}.")

        # Choose difficulty, if input does not equal easy or hard keep asking for difficulty.
        checkDifficultLoop = True
        while checkDifficultLoop:
            chosen_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
            if chosen_difficulty == "easy" or chosen_difficulty == "hard":
                checkDifficultLoop = False
            else:
                print('It looks like you did not select easy or hard. Please select again.')

        # Return number of guesses for the game
        if chosen_difficulty == "easy":
            print("You have chosen easy mode. You will have 10 guess to find the number.")
            return 10
        elif chosen_difficulty == "hard":
            print("You have chosen hard mode. You will have 5 guess to find the number.")
            return 5
    
    # Introduction
    TARGET_NUMBER = randint(1,100)
    guess_count = intro(TARGET_NUMBER)
    game_running = True

    # Player guessing phase
    while game_running:
        player_guess = int(input("Make a guess: "))

        # Deterime if the guess was to low, to high, or correct.
        if player_guess < TARGET_NUMBER:
            print(f"The number {player_guess} is to low.")
            guess_count -= 1
        elif player_guess > TARGET_NUMBER:
            print(f"The number {player_guess} is to high.")
            guess_count -= 1
        elif player_guess == TARGET_NUMBER:
            print(f"You got it! The answer was {TARGET_NUMBER}.")
            game_running = False
        
        if guess_count == 0:
            game_running = False
            print("You've run out of guesses, you lose.")
        elif guess_count > 0 and game_running:
            print("Guess again.")
            print(f"You have {guess_count} guesses left.")

    # Check to see if player wants to play another gaame or not
    checkPlayAgainLoop = True
    while checkPlayAgainLoop:
        play_again = input("Would you like to play again? Type 'y' or 'n': ").lower()
        if play_again == "y" or play_again == 'n':
            checkPlayAgainLoop = False
        else:
            print("It looks like you did not select y or n. Please try again.")
    if play_again == "y":
        game_run()

if __name__ == "__main__":
    game_run()