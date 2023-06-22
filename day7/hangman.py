import random
import hangman_stage as art
import hangman_words as words
print(art.logo)

life = 5
chosen_word = random.choice(words.word_list)

hint = ["-"] * len(chosen_word)
while ("-" in hint):
    is_letter = False
    guess = input("Guess a letter: ").lower()

    for index, letter in enumerate(chosen_word):
        if letter == guess:
            hint[index] = letter
            is_letter = True
            break

    if guess in hint:
        print(f"You've already guessed {guess}")
        continue
    elif not is_letter:
        print(f"You've guessed wrong letter {guess}. You loose a life")
        print(art.stages[life])
        life -= 1
        if life < 0:
            break

    print(hint)

if life > 0:
    print("You win")
else:
    print("You lose")
