import random

# List of predefined words
words = ["python", "computer", "science", "hangman", "program"]

# Randomly choose a word
word = random.choice(words)

# Variables
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

# Display hidden word
display_word = ["_"] * len(word)

print("🎮 Welcome to Hangman Game!")

# Game loop
while wrong_guesses < max_wrong_guesses and "_" in display_word:
    print("\nWord:", " ".join(display_word))
    print("Wrong guesses left:", max_wrong_guesses - wrong_guesses)

    # User input
    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("⚠ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Correct guess
    if guess in word:
        print("✅ Correct Guess!")

        # Update display word
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
    else:
        print("❌ Wrong Guess!")
        wrong_guesses += 1

# Final result
if "_" not in display_word:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n💀 Game Over! The word was:", word)