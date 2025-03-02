# Number Game

This is a number guessing game implemented in Python. The game allows the player to guess a number between 1 and 100, and provides feedback on whether the guess is too low, too high, or correct.

## Project Structure

```
game/
    __init__.py
    __pycache__/
        __init__.cpython-313.pyc
        game_logic.cpython-313.pyc
        player.cpython-313.pyc
    game_logic.py
    player.py
js/
    game_logic.js
LICENSE
main.py
README.md
requirements.txt
tests/
    __init__.py
    __pycache__/
        test_game_logic.cpython-313.pyc
        test_player.cpython-313.pyc
    test_game_logic.py
    test_player.py
utils/
    __init__.py
    helpers.py
```

## Getting Started

### Python

1. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

2. Run the game:

    ```bash
    python main.py
    ```

### JavaScript

1. Navigate to the `js` directory:

    ```bash
    cd js
    ```

2. Install the required packages (if any):

    ```bash
    npm install
    ```

3. Run the game logic tests:

    ```bash
    node game_logic.js
    ```

### Integrating Python and JavaScript

You can integrate the JavaScript logic with the Python code using a tool like `PyExecJS` which allows you to execute JavaScript code from Python.

1. Install `PyExecJS`:

    ```bash
    pip install PyExecJS
    ```

2. Update your Python code to use the JavaScript logic:

    ```python
    import execjs

    with open('js/game_logic.js') as f:
        js_code = f.read()

    ctx = execjs.compile(js_code)
    number_game = ctx.call('NumberGame')

    guess_result = number_game.guess(50)
    print(guess_result)
    ```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
