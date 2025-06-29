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

        if not guess.isalpha() or len(guess) != 1:
            print("❌ Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

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
            print("\n🎉 You won! The word was:", word)
            break
    else:
        print("\n💀 You lost! The word was:", word)

# Run the game
hangman()
