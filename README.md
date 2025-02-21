# Number Guessing Game

A simple number guessing game implemented in Python.

## How to Play

- The game will randomly select a number between 1 and 100.
- You have to guess the number within a limited number of attempts.
- After each guess, you will receive feedback indicating if your guess was too low, too high, or correct.
- If you guess the correct number, you win! If you run out of attempts, the game is over.

## Setup

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/number_guessing_game.git
   cd number_guessing_game
   ```

2. (Optional) Create a virtual environment and activate it:

   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

## Running the Game

To start the game, run:

```sh
python main.py
```

## Running Tests

To run the tests, use:

```sh
python -m unittest discover -s tests
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
