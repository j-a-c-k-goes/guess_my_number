"""
Game is "Guess my number"
"""
# .................................................................. imports
from random import *
# .................................................................. main_function
def main():
    global secret
    secret = secret_number(n_1,n_2)    
    think = thinking(n_1,n_2)
    your_guesses = []
    for guesses in range(1, max_guesses):
        print()

        try:
            guess = int(input("input your guess as a number: "))
            print()

            if guess < secret:
                your_guesses.append(guess)
                print("your guess\t{}".format(guess))
                guess_too_low()
                guesses += 1
                print("your guesses: " + "".join(str(your_guesses)))
                print("guesses left\t{}".format(max_guesses - guesses))
                
                
            elif guess > secret:
                your_guesses.append(guess)
                print("your guess\t{}".format(guess))
                guess_too_high()
                guesses += 1
                print("your guesses: " + "".join(str(your_guesses)))
                print("guesses left\t{}".format(max_guesses - guesses))

            else:
                break

        except ValueError:
            error_message()
            guess = int(input("input your guess as a number: "))

    if guess == secret:
        correct_guess(secret, guesses)
        print()
            
    else:
       fail_guess(secret)
       print()
# .................................................................. sub_functions
def secret_number(n_1, n_2):
    return randint(n_1, n_2)
def thinking(n_1,n_2):
    string = "i am thinking of a number between {} and {}".format(n_1,n_2)
    print(string.title())
def guess_too_high():
    string = "your guess is too high"
    print(string.title())
def guess_too_low():
    string = "your guess is too low"
    print(string.title())
def take_guess():
    string = "take a guess"
    print(string.title())
def error_message():
    string = "please enter a valid number!"
    print(string)
def fail_guess(value):
    string = "actually the number i was thinking of was {}".format(secret)
    print(string.title())
def correct_guess(value_1, value_2):
    string = "nice! you guessed my secret number '{}' in {} attempts".format(value_1, value_2)
    print(string.title())
def menu():
    print("(1) for easy\n(2) for medium\n(3) for hard")
# .................................................................. on_load_export
if __name__ == "__main__":
    modes = ["easy", "medium", "hard"]

    while True:
        print("new game!".upper())
        menu()
        mode = int(input("choose a difficulty, (1),(2),(3): "))

        #if mode != 1 or mode != 2 or mode != 3:
            #print("difficulty does not exist...please use 1, 2, 3 to select a difficulty.")
            #mode = int(input("select (1),(2),or (3): "))
    
        if mode == 1:
            print("you selected {} for {}".format(mode,modes[0]))
            guesses = 0
            max_guesses = 3
            n_1 = 1
            n_2 = randint(15,20)

        if mode == 2:
            print("you selected {} for {}".format(mode,modes[1]))
            guesses = 0
            max_guesses = 5
            n_1 = 1
            n_2 = randint(25,100)

        if mode == 3:
            print("you selected {} for {}".format(mode,modes[2]))
            guesses = 0
            max_guesses = 7
            n_1 = 1
            n_2 = randint(100,1000)
        print()   
        main()
# .................................................................. bugs
"""
line 85, fix conditional statement if mode inputted not a valid mode
"""
# .................................................................. updates
