from colorama import init, Fore, Back, Style
init()
import pandas as pd

df = pd.read_csv(r"C:\Users\lenovo\Downloads\wordle-bank.csv", header = None)
random_row = df.sample()
random_word = random_row.iloc[0, 0]

random_word_cap = random_word.upper()
print(random_word_cap)

def word_match(a, b):
    output = ""
    correct_positions = []
    incorrect_positions = []

    hidden_word_copy =  list(a)
    guess_copy = list(b)

    for i in range(len(a)):
        if b[i] == a[i]:
            correct_positions.append(i)
            hidden_word_copy[i] = '*'
            guess_copy[i] = '*'
    
    for i in range(len(b)):
        if guess_copy[i] != '*':
            if guess_copy[i] in hidden_word_copy:
                incorrect_positions.append(i)
                hidden_word_copy[hidden_word_copy.index(guess_copy[i])] = '*'
    
    for i in range(len(b)):
        if i in correct_positions:
            output += Fore.GREEN + a[i].upper() + Style.RESET_ALL
        elif i in incorrect_positions:
            output += Fore.YELLOW + b[i].lower() + Style.RESET_ALL
        else:
            output += Fore.LIGHTBLACK_EX + '.' + Style.RESET_ALL
    return output

def wordle():
    hidden_word = random_word_cap

    print(Fore.BLUE + 'Welcome to Wordle!')
    print(Fore.BLUE + 'You have 6 guesses to the secret word. Goodluck!')

    no_of_guesses = 1
    while no_of_guesses <= 6:
        guess = input(Style.RESET_ALL + "\n Guess no. ({}), make it count: ".format(no_of_guesses))
        guess_word = guess.upper()

        if len(guess_word) == 5:
            guess_feedback = word_match(hidden_word, guess_word)
            print(guess_feedback)
            no_of_guesses += 1
        else:
            print('Please enter 5-letter word only for the guess!')
            no_of_guesses = no_of_guesses
        
        if guess_word == hidden_word:
            print(Fore.CYAN + Style.BRIGHT + f"Congratulations! The secret word is '{hidden_word}' and you guessed it correctly! \n You win, Hooray!!" + Style.RESET_ALL)
            break

    else:
        print(Fore.RED + f"\nSo sorry! You're unfortunately out of guesses. The secret word is '{hidden_word}'." + Style.RESET_ALL)

wordle()
