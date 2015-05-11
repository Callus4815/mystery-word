import random
import re

def get_file():
    with open('/usr/share/dict/words') as list_of_words:
        words = list_of_words.read()
        words = words.split()
        return words

def easy_words(words):
    easy_words = []

    for chosen_word in words:
        if len(chosen_word) <= 6 and len(chosen_word) >= 4:
            easy_words.append(chosen_word)
    return easy_words

def medium_words(word_list):
    medium_words = []
    for chosen_word in word_list:
        if len(chosen_word) <= 8 and len(chosen_word) >=6:
            medium_words.append(chosen_word)
    return medium_words

def hard_words(word_list):
    hard_words = []
    for chosen_word in word_list:
        if len(chosen_word) >= 8:
            hard_words.append(chosen_word)
    return hard_words

def random_word(words):
    random_word = []
    random_word = random.choice(words)
    return random_word

def display_word(random_word,guess):

    letter_in_word = []
    for letter in random_word:
        if letter in guess:
            letter_in_word.append(letter)
        else:
            letter_in_word.append("_")
    letter_in_word = " ".join(letter_in_word)
    return letter_in_word.upper()


def is_word_complete(word,guess):
    for letter in word:
        if letter not in guess:
            return False
    return True

def user_Input():
    print("Welcome to MYSTERY WORD!!!!!!!!!")
    mode = input("What difficulty level would you like this to be([E]asy,[M]edium, [H]ard): ")

    mode = re.sub(r'[^A-Za-z0-9]','',mode).upper()

    return mode



def get_word(modage, words):

    if modage == 'E'.upper():
        easy_list = easy_words(words)
        word1 = random_word(easy_list).upper()
        print("Your word has {} letters in it".format(len(word1)))

        return word1
    elif modage == 'M'.upper():
        medium_list = medium_words(words)
        word2 = random_word(medium_list).upper()
        print("Your word has {} letters in it".format(len(word2)))
        return word2
    elif modage == 'H'.upper():
        hard_list = hard_words(words)
        word3 = random_word(hard_list).upper()
        print("Your word has {} letters in it".format(len(word3)))
        return word3

        #need to put a catch all here
def guess_letters(any_word):
    count = 8
    guessed_letter=[]
    missed_letter = []
    while count != 0:
        guess1 = input("Please guess a letter: ").upper()
        guess1 = re.sub(r'[^A-Za-z0-9]','',guess1)
        if guess1 in guessed_letter:
            print('You guessed that already but,')
        guessed_letter.append(guess1)
        if len(guess1) > 1:
            print("That is invalid, please try again.")
        elif is_word_complete(any_word,guessed_letter)==True:
                print("Congratulations, you have solved the mystery word, it was {}.".format(any_word))
                break;

        elif guess1 in any_word:
            guessed_letter.append(guess1)
            print("Good guess!!")
            print(display_word(any_word, guessed_letter))
            print("You have {} guesses left".format(count))
        elif guess1 not in any_word:
            missed_letter.append(guess1)
            print('Sorry that letter is not in the word')
            count-=1
            print("You have {} guesses left".format(count))
            if count == 0:
                print("Sorry, you lose. The word was {}".format(any_word))
    return

while True:
    if __name__ == '__main__':
        words = get_file()
        modage = user_Input()
        word = get_word(modage, words)
        guess_letters(word)

    while True:
        answer =input('Would you like to play again? (y/n): ')
        if answer in ('y', 'n'):
            break
        print( 'Invalid input.')
    if answer == 'y':
        continue
    else:
        print ('Thanks for playing!, Goodbye')
        break
