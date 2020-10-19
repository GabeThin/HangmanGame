from tkinter import *
import random
import threading

def choose_word():
    words = open("words.txt").readlines()
    myword = random.choice(words)
    return myword

def display_word(word):
    string = ""
    for i in range(0, len(word) - 1):
        string += "_ "
    return(string)

def handle_guess(word, label, letter, lives):
    for i in range(0, len(word) - 1):
        if letter == word[i]:
            display[i] = letter
    if letter not in word:
        lives -= 1
        print(lives)
    label.configure(text=display)
    return lives

def game_status(lives):
    global old_win_counter
    global win_counter
    display_string = ""

    old_win_counter = win_counter

    for i in range(0, len(display)):
        display_string += str(display[i])

    if lives == 0:
        print("You lost :(")
        return True
    if "_" not in display_string:
        win_counter += 1
        return False
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
    global secret_word
    global display_blanks
    global display
    global blanks
    global lives
    global win_counter

    clear_window()
    
    title = Label(root, text="HANGMAN", font=("HELVETICA", 120))
    title.grid(row = 0, columnspan=3, pady=50, padx=400)

    secret_word = choose_word()
    game_over = False
    display = StringVar()

    display_blanks = display_word(secret_word)
    display = display_blanks.split(" ")
    display.remove(display[-1])

    space = Frame(root)
    space.grid(row=2, pady=200)

    blanks = Label(root, text=display_blanks, font=("HELVETICA", 40))
    blanks.grid(row=4, column=1, pady = 10, padx=400)
    
    press_a_key = Label(root, text="Press a key to make your guess.", font=("HELVETICA", 20))
    press_a_key.grid(row=5, column=1, pady=1, padx=400)

    lives = 10
    win_counter = 0

    def input(event):
        global secret_word
        global lives
        global game_over
        global display_blanks
        global display
        if win_counter == 0:
            letter = event.char
            print(secret_word)
            lives = handle_guess(secret_word, blanks, letter, lives)
            game_over = game_status(lives)

        elif win_counter - old_win_counter == 1:
            secret_word = choose_word()
            print(secret_word)
            letter = event.char
            display_blanks = display_word(secret_word)
            display = display_blanks.split(" ")
            display.remove(display[-1])
            blanks.configure(text = display_blanks)

            lives = handle_guess(secret_word, blanks, letter, lives)
            game_over = game_status(lives)



    if game_over == True:
        print("game_over")

    root.bind("<Key>", input)

root = Tk()
root.geometry("1440x900")

def clear_window():
    for i in root.winfo_children():
            i.destroy()

def all_widgets (window) :
    widget_list = window.winfo_children()
    for item in widget_list:
        if item.winfo_children():
            _list.extend(item.winfo_children())
    return _list


def init_GUI():
    title = Label(root, text="HANGMAN", font=("HELVETICA", 120))
    title.grid(row = 0, columnspan=3, pady=50, padx=400)
    timed = Button(root, bd = 5, text="START", font=("Helvetica", 20), bg="red",command=main_timed)
    timed.grid(row = 2, columnspan=3)

init_GUI()
root.mainloop()
