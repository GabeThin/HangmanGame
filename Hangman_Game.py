from tkinter import *
import random


correct = False
incorrect = False

def choose_word():
    words = open("words.txt").readlines()
    myword = random.choice(words)
    return "the"

def display_word(word, chosen):
    #blanks.destroy()
    # show the word in its current state including blanks for letters not chosen.
    display_string = ""

    for i in range(0, len(word)):
        if (word[i] in chosen):
            display_string += word[i] + " "
        else:
            display_string += "_ "

    return display_string


def handle_guess(chosen, display_string):
    # get the guess, update chosen, give feedback to user such as -- you are correct

    word = secret_word
    letter = guess.get()

    if len(letter) == 1:
        if letter in word:
            print("correct")
            chosen += letter[0]

        else:
            print("incorrect")

        for i in range(0, len(word)):
            if (word[i] in chosen):
                display_string += word[i] + " "
            else:
                display_string += "_ "

    else:
        print("You can only guess one letter at a time")
    blanks = Label(root, text=display_string)
    blanks.pack(padx=(100, 0), side=LEFT)



    print(display_string)

    return letter[0]

def game_status(word, chosen):
    # show graphics & chosen letters
    wrongCounter = 0
    for letter in chosen:
        if letter not in word:
            wrongCounter += 1
    won = True
    for letter in word:
        if letter not in chosen:
            won = False
    if wrongCounter >= 7:
        print("You lost :(")
        show_hangman(wrongCounter)
        return True
    elif won:
        print("You Won!")
        show_hangman(wrongCounter)
        return True
    else:
        show_hangman(wrongCounter)
        print("Already guessed:", chosen)
        return False
    # announce the outcome if the game is over
    # return boolean of whether the game is over.


def show_hangman(wrongCounter):
    print("   --- ")
    if wrongCounter >= 1:
        print("   O  |")
    else:
        print("      |")
    if wrongCounter >= 2:
        if wrongCounter >= 3:
            if wrongCounter >= 4:
                print("  /|\ |")
            else:
                print("  /|  |")
        else:
            print("  /   |")
    else:
        print("      |")
    if wrongCounter >= 5:
        print("   |  |")
    else:
        print("      |")
    if wrongCounter >= 6:
        if wrongCounter >= 7:
            print("  / \ |")
        else:
            print("  /   |")
    else:
        print("      |")

def main_timed():
    next_round = True
    print(next_round)
    game_over = False
    global chosen_letters
    global secret_word
    secret_word = choose_word()
    for i in root.winfo_children():
            i.destroy()
    chosen_letters = ""
    while game_over == False:
       guess_text = Label(root, text="enter letter guess:")
       display_string = ""
       guess_text.pack(padx=(100, 0), side=LEFT)
       global guess
       guess = Entry(root)
       guess.pack(side=LEFT)
       submit = Button(root, text="Submit Guess", font=("Arial", 24))
       submit['command'] = lambda arg1 = chosen_letters, arg2 = display_string: handle_guess(arg1, arg2)
       submit.pack(side=LEFT)
       chosen_letters += handle_guess(chosen_letters, display_string)
       game_over = game_status(secret_word, chosen_letters)
       



root = Tk()
root.geometry("1440x900")
frame = Frame(root)
frame.pack()




def init_GUI():
    title = Label(frame, text="HANGMAN", font=("Arial", 40))
    title.grid(row = 0, columnspan=3)
    ready = Label(frame, text="Ready to play?", font=("Arial", 20))
    ready.grid(row = 5, column = 0)
    timed = Button(frame, text="PLAY", font=("Arial", 24), command=main_timed)
    timed.grid(row = 6, column = 0)



#HEAD
# main_timed()
#=========
init_GUI()
root.mainloop()
#c23a96fb9dba2587fe350abfede0c6e86132768c
