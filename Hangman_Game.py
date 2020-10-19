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
        heart_text = str(show_hearts())
        print(heart_text)
        heart_label.configure(text=heart_text)
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

def show_hearts():
    global lives
    global heart_label

    heart_text = ""

    for i in range(0, lives - 1):
        heart_text += "♡"

    return heart_text

def main_timed():
    global secret_word
    global display_blanks
    global display
    global blanks
    global lives
    global win_counter
    global heart_label

    lives = 15
    clear_window()
    
    title = Label(root, text="HANGMAN", font=("HELVETICA", 120))
    title.grid(row = 0, columnspan=3, pady=50, padx=400)

    heart_text = show_hearts()
    heart_label = Label(root, text=heart_text, fg="red", font=("Arial", 50))
    heart_label.grid(row=3, column=1)

    secret_word = choose_word()
    game_over = False
    display = StringVar()
    
    display_blanks = display_word(secret_word)
    display = display_blanks.split(" ")
    display.remove(display[-1])

    blanks = Label(root, text=display_blanks, font=("HELVETICA", 40))
    blanks.grid(row=4, column=1)
    press_a_key = Label(root, text="Press a key to make your guess", font=("HELVETICA", 20))
    press_a_key.grid(row=5, column=1)

    win_counter = 0

    def input(event):
        global blanks
        global secret_word
        global lives
        global game_over
        global display_blanks
        global display

        letter = event.char

        if letter.isalpha() == True:
            if win_counter == 0:
                print(secret_word)
                lives = handle_guess(secret_word, blanks, letter, lives)
                game_over = game_status(lives)

            if win_counter == 1:
                clear_window()
                you_win = Label(root, text="YOU WIN!!", font=("Helvetica",40))
                you_win.grid(row=3, column=1, padx=400, pady=300)

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
    timed = Button(root, text="START", font=("Helvetica", 20), command=main_timed)
    timed.grid(row = 2, columnspan=3)

init_GUI()
root.mainloop()
