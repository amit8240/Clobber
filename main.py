MAX_TRIES = 6


def opening():
    """
        prints the starting of the game.
    """
    HANGMAN_ASCII_ART = "Welcome to the game Hangman\n" + """  
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/
                    """

    print(HANGMAN_ASCII_ART, "\nYou have", MAX_TRIES, "tries")
    print("LET'S START :)")


def check_valid_input(letter_guessed, old_letters_guessed):
    """checks the validation of the input.
            :param letter_guessed: letter_guessed value
            :param old_letters_guessed: old_letters_guessed value
            :type letter_guessed: str
            :type old_letters_guessed: list
            :return: False the input is more than 1 length long or is not a letter or if the letter is in the old_letters_guessed list and True otherwise
            :rtype: bool
    """
    if len(letter_guessed) > 1 or not letter_guessed.isalpha():
        return False
    for letter in old_letters_guessed:
        if letter == letter_guessed:
            return False
    return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """adds the letter_guessed into the old_letters_guessed list if the letter us valid.
        :param letter_guessed: letter_guessed value
        :param old_letters_guessed: old_letters_guessed value
        :type letter_guessed: str
        :type old_letters_guessed: list
        :return: True if the letter is valid, and it was not guessed before and False if not
        :rtype: bool
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print('X')
        print(*sorted(old_letters_guessed), sep=" -> ")  # separates the letters by '->'
        return False


def show_hidden_word(secret_word, old_letters_guessed):
    """returns the secret word with the right guesses.
        :param secret_word: secret_word value
        :param old_letters_guessed: old_letters_guessed value
        :type secret_word: str
        :type old_letters_guessed: list
        :return: The secret word with the letters from the list in the right location
        :rtype: str
    """
    word = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            word += letter + " "
        else:
            word += "_ "
    return word


def check_win(secret_word, old_letters_guessed):
    """check the user won.
        :param secret_word: secret_word value
        :param old_letters_guessed: old_letters_guessed value
        :type secret_word: str
        :type old_letters_guessed: list
        :return: True if all the letters that contains the secret word were guessed and False if not
        :rtype: bool
    """
    return not ('_' in show_hidden_word(secret_word, old_letters_guessed))


def print_hangman(num_of_tries):
    """prints the hangman in num_of_tries index in HANGMAN_PHOTOS.
        :param num_of_tries: num_of_tries value
        :type num_of_tries: int
    """
    HANGMAN_PHOTOS = {
        1: """
            x-------x
            """,
        2: """
            x-------x
            |
            |
            |
            |
            |""",
        3: """
            x-------x
            |       |
            |       0
            |
            |
            |""",
        4: """
            x-------x
            |       |
            |       0
            |       |
            |
            |""",
        5: """
            x-------x
            |       |
            |       0
            |      /|\ 
            |
            |""",
        6: """
            x-------x
            |       |
            |       0
            |      /|\ 
            |      /
            |""",
        7: """
            x-------x
            |       |
            |       0
            |      /|\ 
            |      / \ 
            |"""
    }
    print(HANGMAN_PHOTOS.get(num_of_tries))


def choose_word(file_path, index):
    """find the word in the index in the file located in file_path.
        :param file_path: file_path value
        :param index: index value
        :type file_path: str
        :type index: int
        :return: The word in index in the file
        :rtype: str
    """
    diff_words = []
    input_file = open(file_path, "r")
    words = input_file.read().split(" ")
    words[0] = words[0].replace("ן»¿", "")
    while index - 1 >= len(words):
        index -= len(words)
    for word in words:
        if not (word in diff_words):
            diff_words.append(word)
    input_file.close()
    return words[index - 1]


def hangman_game(secret_word):
    """prints the status of the hangman game.
        :param secret_word: secret_word value
        :type secret_word: str
    """
    old_letters_guesses = []
    num_of_tries = 0
    print("You have", MAX_TRIES, "tries good luck!")
    print(show_hidden_word(secret_word, old_letters_guesses))
    while num_of_tries <= MAX_TRIES and not check_win(secret_word, old_letters_guesses):
        letter_guessed = input("Enter a letter: ").lower()
        while not try_update_letter_guessed(letter_guessed, old_letters_guesses):  # until the input is valid
            print("try again")
            letter_guessed = input("Enter a letter: ").lower()
        if letter_guessed not in secret_word:  # if the letter is not in the secret word
            num_of_tries += 1
            print_hangman(num_of_tries)
            remaining_tries = MAX_TRIES - num_of_tries + 1
            if remaining_tries != 1:
                print("\033[31mYou have\033[0m\033[31m", remaining_tries,
                      "\033[0m\033[31mmore tries\033[0m")  # prints in red
            else:
                print("\033[31mYou have one last try!!!\033[0m")  # prints in red
        else:
            print("\033[32myay!\033[0m")  # prints in green
        print(show_hidden_word(secret_word, old_letters_guesses))
    if num_of_tries > MAX_TRIES:
        print("You lost :(")
        print("The secret word was\033[33m", secret_word, "\033[33m")  # prints the secret word in yellow
    else:
        print("\033[33mYou got it!!!")  # prints in yellow


if __name__ == '__main__':
    print(len(str(3)))
    opening()
    file_path = input("Enter the path to the file: ")
    index = int(input("Enter index: "))
    secret_word = choose_word(file_path, index)
    hangman_game(secret_word)
