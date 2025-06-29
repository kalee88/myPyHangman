import random

def hangman():
    words = ["python", "banana", "keyboard", "program", "giraffe", "hangman"]
    word = random.choice(words).lower()
    guessed_letters = []
    tries = 6

    print("🎉 Welcome to Hangman!")
    print("_ " * len(word))

    while tries > 0:
        guess = input("\nGuess a letter: ").lower()

        #Write code in the following lines that checks to see if the guess was a single letter. Check if guess was in the alphabet and has a length of 1 character. Continue if the if statement is true.
        #if ()
        #    print()
        #    continue

        #Write code in the following lines that checks if the letter guess was already guessed previously. Continue if the if statement is true.
        #if ()
        #    print()
        #    continue

        #Write code in the following lines that adds the guess to the list guess_letters above.
        #guessed_letters.

        if guess in word:
            print("✅ Good guess!")
        else:
            print("❌ Nope, that letter's not in the word.")
            tries -= 1

        # Display current progress
        display = [letter if letter in guessed_letters else "_" for letter in word]
        print(" ".join(display))
        print(f"❤️ Tries left: {tries}")

        if "_" not in display:
            print("\nYou won! The word was:", word)
            break
    else:
        print("\nYou lost! The word was:", word)

# Run the game
hangman()
