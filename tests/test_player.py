import unittest
from unittest.mock import patch
from game.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player()

    @patch('builtins.input', side_effect=['50'])
    def test_make_guess_valid(self, mock_input):
        guess = self.player.make_guess()
        self.assertEqual(guess, 50)

    @patch('builtins.input', side_effect=['invalid', '50'])
    def test_make_guess_invalid_then_valid(self, mock_input):
        guess = self.player.make_guess()
        self.assertEqual(guess, 50)

    @patch('builtins.input', side_effect=['y'])
    def test_play_again_yes(self, mock_input):
        self.assertTrue(self.player.play_again())

    @patch('builtins.input', side_effect=['n'])
    def test_play_again_no(self, mock_input):
        self.assertFalse(self.player.play_again())

    @patch('builtins.input', side_effect=['invalid', 'y'])
    def test_play_again_invalid_then_yes(self, mock_input):
        self.assertTrue(self.player.play_again())

if __name__ == '__main__':
    unittest.main()