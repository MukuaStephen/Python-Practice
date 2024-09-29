secret_number = 7
guess_number = 0
guess = 0
while guess != secret_number:
    guess_number += 1
    guess = input("Guess a number between 1 and 10:")
    guess = int(guess)
print(f"Your guessed it in {guess_number} tries!")