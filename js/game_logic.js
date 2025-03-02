class NumberGame {
    constructor() {
        this.targetNumber = Math.floor(Math.random() * 100) + 1;
    }

    guess(number) {
        if (number < this.targetNumber) {
            return "Too low!";
        } else if (number > this.targetNumber) {
            return "Too high!";
        } else {
            return "Correct!";
        }
    }
}

module.exports = NumberGame;