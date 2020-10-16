from tkinter import *
import random

chosen_letters = ""

correct = False
incorrect = False

def choose_word():
    words = open("words.txt").readlines()
    myword = random.choice(words)
    return "the"

# def display_word(word, chosen):
#     display_string = ""
#
#     for i in range(0, len(word)):
#         if (word[i] in chosen):
#             display_string += word[i] + " "
#         else:
#             display_string += "_ "
#
#     return display_string

def handle_guess(chosen, display_string):
    # get the guess, update chosen, give feedback to user such as -- you are correct

    word = secret_word
    letter = guess.get()

    if len(letter) == 1:

        if letter in word:
            print("correct")
            chosen += letter[0]

            guess.delete(0, END)

            blanks.pack_forget()
            blanks.pack(padx=(100, 0), side=LEFT)

        else:
            print("incorrect")
            guess.delete(0, END)

        for i in range(0, len(word)):
            if (word[i] in chosen):
                display_string += word[i] + " "
            else:
                display_string += "_ "

        display.set(display_string)

    else:
        print("You can only guess one letter at a time")

    return letter[0], chosen

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
    game_over = False

    global chosen_letters
    global secret_word

    secret_word = choose_word()

    for i in root.winfo_children():
            i.destroy()

    while game_over == False:
        guess_text = Label(root, text="enter letter guess:")
        display_string = ""
        guess_text.pack(padx=(100, 0), side=LEFT)

        global guess
        guess = Entry(root)
        guess.pack(side=LEFT)

        global blanks
        global display

        display = StringVar()
        blanks = Label(root, textvariable=display)

        submit = Button(root, text="Submit Guess", font=("Arial", 24))
        submit['command'] = lambda arg1 = chosen_letters, arg2 = display_string: handle_guess(arg1, arg2)
        submit.pack(side=LEFT)

        letter, chosen = handle_guess(chosen_letters, display_string)

        print(chosen)

        chosen_letters += handle_guess(chosen, display_string)
        game_over = game_status(secret_word, chosen_letters)


root = Tk()
root.geometry("1440x900")
frame = Frame(root)
frame.pack()

def all_widgets (window) :
    widget_list = window.winfo_children()
    for item in widget_list:
        if item.winfo_children():
            _list.extend(item.winfo_children())
    return _list

def delete_click():
    return "yes"

def init_GUI():
    title = Label(root, text="HANGMAN", font=("Arial", 40))
    title.pack(pady=100)

    play = Button(root, text="PLAY", font=("Arial", 24), command=main_timed)
    play.pack(pady = (350, 0))

init_GUI()
root.mainloop()
