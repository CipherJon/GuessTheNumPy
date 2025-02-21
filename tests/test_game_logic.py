import unittest
from game.game_logic import NumberGuessingGame

class TestNumberGuessingGame(unittest.TestCase):
    def setUp(self):
        self.game = NumberGuessingGame()

    def test_start_new_game(self):
        self.game.start_new_game()
        self.assertIsNotNone(self.game.number_to_guess)
        self.assertEqual(self.game.attempts, 0)
        self.assertFalse(self.game.game_over)

    def test_check_guess_correct(self):
        self.game.start_new_game()
        self.game.number_to_guess = 50
        result = self.game.check_guess(50)
        self.assertEqual(result, "Congratulations! You guessed the right number.")
        self.assertTrue(self.game.game_over)

    def test_check_guess_too_low(self):
        self.game.start_new_game()
        self.game.number_to_guess = 50
        result = self.game.check_guess(25)
        self.assertEqual(result, "Too low!")
        self.assertFalse(self.game.game_over)

    def test_check_guess_too_high(self):
        self.game.start_new_game()
        self.game.number_to_guess = 50
        result = self.game.check_guess(75)
        self.assertEqual(result, "Too high!")
        self.assertFalse(self.game.game_over)

    def test_game_over_after_max_attempts(self):
        self.game.start_new_game()
        self.game.number_to_guess = 50
        for _ in range(self.game.max_attempts):
            self.game.check_guess(25)
        self.assertTrue(self.game.game_over)

if __name__ == '__main__':
    unittest.main()