import random

class NumberGuessingGame:
    def __init__(self):
        self.number_to_guess = None
        self.max_attempts = 5
        self.attempts = 0
        self.game_over = False

    def start_new_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.game_over = False
        print("\nA new game has started! Guess the number between 1 and 100.")

    def check_guess(self, guess):
        self.attempts += 1
        if guess < self.number_to_guess:
            result = "Too low!"
        elif guess > self.number_to_guess:
            result = "Too high!"
        else:
            self.game_over = True
            result = "Congratulations! You guessed the right number."
        
        if self.attempts >= self.max_attempts and not self.game_over:
            self.game_over = True
            result = f"Game Over! The correct number was {self.number_to_guess}."
        
        return result

    def is_game_over(self):
        return self.game_over