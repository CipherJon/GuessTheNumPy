class Player:
    def make_guess(self):
        while True:
            try:
                guess = int(input("Enter your guess: "))
                return guess
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def play_again(self):
        while True:
            answer = input("Do you want to play again? (y/n): ").lower()
            if answer in ['y', 'n']:
                return answer == 'y'
            print("Invalid input. Please enter 'y' or 'n'.")