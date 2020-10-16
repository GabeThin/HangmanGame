from tkinter import *
import random
import tkinter as tk


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
    blanks = "_ _ _ "
    for i in range(0, len(word)):
        if (word[i] in chosen):
            blanks.replace
        else:
            display_string += "_ "

    return display_string


def handle_guess(chosen, display_string):
    # get the guess, update chosen, give feedback to user such as -- you are correct

    word = secret_word
    letter = guess.get()
    blanks_content = ""

    if len(letter) == 1:
        if letter in word:
            print("correct")
            chosen += letter[0]

        else:
            print("incorrect")

        for i in range(0, len(word)):
            if (word[i] in chosen):
                blanks_content += word[i] + " "
            else:
                blanks_content += "_ "

    else:
        print("You can only guess one letter at a time")
    display_string.set(blanks_content)
    blanks = Label(display_string.root, textvariable=display_string)
    blanks.pack(padx=(100, 0), side=LEFT)



    print(blanks_content)

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
        display_string = tk.StringVar()
        display_string.root = tk.Tk()
        guess_text.pack(padx=(100, 0), side=LEFT)
        global guess
        guess = Entry(root)
        guess.pack(side=LEFT)
        submit = Button(root, text="Submit Guess", font=("Arial", 24))
        submit['command'] = lambda arg1 = chosen_letters, arg2 = display_string: handle_guess(arg1, arg2)
        submit.pack(side=LEFT)
        chosen_letters += handle_guess(chosen_letters, display_string)
        game_over = game_status(secret_word, chosen_letters)
       
        
#         if next_round==True:
#             guess_text = Label(root, text="enter letter guess:")
#             display_string = ""
#             guess_text.pack(padx=(100, 0), side=LEFT)
#             global guess
#             guess = Entry(root)
#             guess.pack(side=LEFT)
#             submit = Button(root, text="Submit Guess", font=("Arial", 24))
#             submit['command'] = lambda arg1 = chosen_letters, arg2 = display_string: handle_guess(arg1, arg2)
#             submit.pack(side=LEFT)
#             chosen_letters += handle_guess(chosen_letters, display_string)
#             game_over = game_status(secret_word, chosen_letters)
#             next_round = False
#         else:
#             widget_list = all_children(root)
#             for item in widget_list:
#                 item.pack_forget()
#             next_round= True


root = Tk()
root.geometry("1440x900")
frame = Frame(root)
frame.pack()

# def all_widgets (window) :
#     widget_list = window.winfo_children()
#     for item in widget_list :
#         if item.winfo_children():
#             _list.extend(item.winfo_children())
#     return _list

# def delete_click():
#     return "yes"

def init_GUI():
    title = Label(frame, text="HANGMAN", font=("Arial", 40))
    title.pack(pady=100)

#     deletebutton = Button(root, text="Submit Guess", font=("Arial", 24), command=delete_click)
#     deletebutton.pack(side=LEFT)
#     if delete_click() == "yes":
#         for i in root.winfo_children():
#             i.destroy()

    timed = Button(frame, text="PLAY", font=("Arial", 24), command=main_timed)
    timed.pack(pady=(350, 0), padx=100, side=LEFT)



#HEAD
# main_timed()
#=========
init_GUI()
root.mainloop()
#c23a96fb9dba2587fe350abfede0c6e86132768c
