import random
def hangman():
    words = ['python', 'java', 'kotlin', 'javascript']
    word = random.choice(words)
    guessed_letters = []

    lives = 6

    print("Welcome to Hangman!")
    print("_" * len(word))

    while lives > 0:
        guess = input("\nGuess a Letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
        else:
            lives -=1
            print("\nWrong guess. You lost a Life.")

        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
        print(display_word)

        if display_word == word:
            print("congratulations! You've guessed the word!. the word was", word)
            break
        else:
            print(f"You have {lives} lives left.")
        
        if lives == 0:
            print(f"Sorry you lost. the word was {word}.")
        
if __name__ == "__main__":
    hangman()
