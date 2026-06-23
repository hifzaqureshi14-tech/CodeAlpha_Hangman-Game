import random

def hangman():
    secret_word = random.choice(["python", "mirror", "computer", "books", "movies"])
    guessed = set()
    lives = 6

    print(f"Welcome to Hangman! You have {lives} lives.")

    while lives > 0:
        display = [char if char in guessed else "_" for char in secret_word]
        print(f"\nWord: {' '.join(display)}")
        if "_" not in display:
            return print("You win!")

        guess = input("Guess a letter: ").strip().lower()
        if not guess.isalpha() or len(guess) != 1 or guess in guessed:
            print("Invalid")
            continue
        guessed.add(guess)
        if guess not in secret_word:
            lives -= 1
            print(f"Wrong guess! Lives: {lives}")
    print(f"\nGame Over! The word was: {secret_word.upper()}")
if __name__ == "__main__":
        hangman()