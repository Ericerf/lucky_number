import sys
import os
#print(os.getcwd())
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
import random
import datetime
from unittest.mock import patch
from lucky_number_oop import NumberGuessingGame


class TestNumberGuessingGame(unittest.TestCase):

    # Test for the welcome_message function
    def test_welcome_message(self):
        game = NumberGuessingGame(input_function=lambda: "")
        with patch('builtins.print') as mocked_print:
            game.welcome_message()
        mocked_print.assert_called_once_with("Welcome to the Number Guessing Game!")

    # Test for getting a valid player name
    def test_get_player_name_valid(self):
        with patch('builtins.input', return_value="Ali Daei"):
            game = NumberGuessingGame()
            game.get_player_name()
            self.assertEqual(game.player_name, "Ali Daei")

    # Test for getting an invalid player name followed by a valid one
    def test_get_player_name_invalid_followed_by_valid(self):
        with patch('builtins.input', side_effect=["1234", "Ali Daei"]):
            game = NumberGuessingGame()
            game.get_player_name()
            self.assertEqual(game.player_name, "Ali Daei")

    # Test for getting a valid player birthdate
    def test_get_player_birthdate_valid(self):
        with patch('builtins.input', return_value="20000101"):
            game = NumberGuessingGame()
            game.get_player_birthdate()
            self.assertEqual(game.player_birthdate, datetime.date(2000, 1, 1))

    # Test for getting an invalid birthdate format followed by a valid one
    def test_get_player_birthdate_invalid_format(self):
        with patch('builtins.input', side_effect=["200001321", "20000101"]):
            game = NumberGuessingGame()
            game.get_player_birthdate()
            self.assertEqual(game.player_birthdate, datetime.date(2000, 1, 1))

    # Test for getting an invalid birthdate followed by a valid one
    def test_get_player_birthdate_invalid_date(self):
        with patch('builtins.input', side_effect=["20001301", "20000101"]):
            game = NumberGuessingGame()
            game.get_player_birthdate()
            self.assertEqual(game.player_birthdate, datetime.date(2000, 1, 1))

    # Test for calculating player age when underage
    def test_calculate_player_age_underage(self):
        game = NumberGuessingGame()
        game.player_birthdate = datetime.date(datetime.datetime.now().year - 10, 1, 1)  # setting age to 10 years
        with patch('builtins.print') as mocked_print:
            game.calculate_player_age()
        mocked_print.assert_called_with("Sorry, you are not allowed to play because you are underage.")
        self.assertTrue(game.done)
        self.assertEqual(game.player_age, 10)

    # Test for calculating player age when not underage
    def test_calculate_player_age_not_underage(self):
        game = NumberGuessingGame()
        game.player_birthdate = datetime.date(datetime.datetime.now().year - 20, 1, 1)  # setting age to 20 years
        game.calculate_player_age()
        self.assertFalse(game.done)
        self.assertEqual(game.player_age, 20)

    # Test for playing the game again with a "yes" response
    def test_play_again_yes(self):
        with patch('builtins.input', return_value="y"):
            game = NumberGuessingGame()
            game.play_again()
            self.assertFalse(game.done)

    # Test for playing the game again with a "no" response
    def test_play_again_no(self):
        with patch('builtins.input', return_value="n"):
            game = NumberGuessingGame()
            with patch('builtins.print') as mocked_print:
                game.play_again()
            mocked_print.assert_called_with("Thanks for playing. Goodbye!")
            self.assertTrue(game.done)

    # Test for starting the game with a correct guess
    def test_start_correct_guess(self):
        # Create an instance of the game with mocked input function
        game_inputs = iter(["Ali Daei", "20000101", "50", "n"])  # Added "n" for the play again query
        with patch('builtins.input', side_effect=lambda _: next(game_inputs)):
            with patch('builtins.print') as mocked_print:
                with patch('random.choice', return_value=50):
                    with patch.object(random, 'randint', return_value=50):  # this will force all random numbers to be 50
                        game = NumberGuessingGame()
                        game.start()

        # Ensure that the expected print calls were made, including the correct guess.
        print_calls = [call_args[0][0] for call_args in mocked_print.call_args_list]
        self.assertIn('Congratulations, your lucky number is 50. You got it from try #1', print_calls)

if __name__ == "__main__":
    unittest.main()
