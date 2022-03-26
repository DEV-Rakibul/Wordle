import random

grid = [["x", "x", "x", "x", "x"],["x", "x", "x", "x", "x"],["x", "x", "x", "x", "x"],["x", "x", "x", "x", "x"],["x", "x", "x", "x", "x"],["x", "x", "x", "x", "x"]]

word_list = ['which', 'their', 'would', 'there', 'could', 'other', 'about', 'great', 'these', 'after', 'first', 'never',
             'where', 'those', 'shall', 'being', 'might', 'every', 'think', 'under', 'found', 'still', 'while', 'again',
             'place', 'young', 'years', 'three', 'right', 'house', 'whole', 'world', 'thing', 'night', 'going', 'heard',
             'heart', 'among', 'asked', 'small', 'woman', 'whose', 'quite', 'words', 'given', 'taken', 'hands', 'until',
             'since', 'light']



def print_grid():
    for row in grid:
        print(row)


def word_generator():
    word = random.choice(word_list)

    return word

def game(word, grid):

    def wrong_letters(letter):
        letters = []
        letters.append(letter)

        return letters

    letters = ""
    out_of_guesses = False
    try_num = 0
    guessed = False

    while not guessed:
        guess = input("Guess the word: ")

        while len(guess) != 5:
            guess = input("Invalid input. Try again: ")

        letters_guessed = 0
        for i, letter in enumerate(guess):
            if letter == word[i]:
                letters_guessed += 1
                if letters_guessed == 5:
                    print("You guessed!")
                    try_num += 1
                    guessed = True
                    break

        if guessed is True:
            break

        for i in range(len(guess)):
            current_letter = guess[i]
            if current_letter == word[i]:
                grid[try_num][i] = current_letter
            else:
                if current_letter not in letters or current_letter not in guess:
                    letters += str(wrong_letters(current_letter))

        print("The letters which aren't in the word are: ",letters)
        try_num += 1
        print_grid()

        if try_num > 5:
            out_of_guesses = True
            print("                                   ")
            print("Out of guesses! The word was: ",word)
            break

def main():
    # word = word_generator()
    word = "svery"
    print_grid()
    game(word, grid)


if input("Do you want play wordle [Y/N]: ").upper() == "Y":
    main()
else:
    quit()
