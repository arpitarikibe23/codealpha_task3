
import random

# List of words for the game
words = ["python", "hangman", "developer", "coding", "challenge", "computer", "science"]

# Function to choose a random word
def get_random_word():
    return random.choice(words)

# Function to display the word with guessed letters
def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

# Main game function
def play_hangman():
    word = get_random_word()
    guessed_letters = set()
    attempts = 6  # Maximum incorrect guesses allowed

    print("🎮 Welcome to Hangman!")
    print("Try to guess the word, one letter at a time.")
    
    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("✅ Good job! The letter is in the word.")
        else:
            attempts -= 1
            print(f"❌ Wrong guess! You have {attempts} attempts left.")

        if all(letter in guessed_letters for letter in word):
            print(f"\n🎉 Congratulations! You guessed the word: {word}")
            break
    else:
        print(f"\n💀 Game Over! The word was: {word}")

# Run the game
if __name__ == "__main__":
    play_hangman()
