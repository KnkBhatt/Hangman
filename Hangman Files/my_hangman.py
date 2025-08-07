import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)

chosen_word = list(chosen_word)
display = ["_"] * len(chosen_word)

print("".join(display))
lives = 6
guessed_letters = []

while lives>0:
    guess = input("Guess a letter : ").lower()
    if guess in guessed_letters:
        print("You already chose this word.")
        continue
    else:
        if guess in chosen_word:
            indexes = [i for i, l in enumerate(chosen_word) if l == guess]
            for i in indexes:
                display[i] = chosen_word[i]
            print("".join(display))
            guessed_letters.append(guess)
            if "_" not in display:
                print("YAY! You guessed the word:", "".join(display))
                break
        else:
            guessed_letters.append(guess)
            print("Wrong guess. 💔")
            lives-=1
            print(f"lives : {lives}")
            print(hangman_art.stages[lives])
            print("".join(display))

else:
    print("YOU LOSE.")
    print(f"The correct word was {"".join(chosen_word)}")

