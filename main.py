from game.game_logic import NumberGuessingGame
from game.player import Player

def main():
    player = Player()
    game = NumberGuessingGame()
    
    print("Welcome to the Number Guessing Game!")
    
    while True:
        game.start_new_game()
        while not game.is_game_over():
            guess = player.make_guess()
            result = game.check_guess(guess)
            print(result)
        
        if not player.play_again():
            break
    
    print("Thanks for playing!")

if __name__ == "__main__":
    main()