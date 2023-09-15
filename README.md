# NumQuest - The Number Guessing Game

Welcome to the 'NumQuest' Experience! In this game, you'll try to guess a secret number chosen by the computer. You'll receive hints about how close your guess is to the correct number.

## Rules

- The computer selects a random number between 1 and 100.
- If your guess is within 10 units of the secret number, you'll be told you're "WARM."
- If your guess is further than 10 units away, you'll be told you're "COLD."
- If your current guess is closer to the secret number than your previous guess, you'll be told you're "WARMER."
- If your current guess is farther from the secret number than your previous guess, you'll be told you're "COLDER."

## Getting Started

1. Clone the repository to your local machine.
2. Run the Python script: `python numquest.py`

## How to Play

1. Input your guess for the secret number when prompted.
2. Receive feedback on your guess.
3. Keep guessing until you correctly guess the secret number.

## Example

```bash
$ python numquest.py
Welcome to the 'NumQuest' Experience!

...

I am in the process of conceiving a numerical value concealed within the realm of 1 to 100.
What's your guess then?
50
COLD!

...

I am in the process of conceiving a numerical value concealed within the realm of 1 to 100.
What's your guess then?
42
WARMER!

...

Congratulations! You guessed it correctly in X number of guesses.
