import random

def choose_random_word():
    word_list = ["python", "hangman", "programming", "computer", "keyboard", "developer"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def hangman():
    word = choose_random_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    
    while True:
        print(f"Word: {display_word(word, guessed_letters)}")
        print(f"Remaining attempts: {attempts}")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print("Incorrect guess.")
            if attempts == 0:
                print("You've run out of attempts. The word was:", word)
                break

        if display_word(word, guessed_letters) == word:
            print("Congratulations! You've guessed the word:", word)
            break

if __name__ == "__main__":
    hangman()
