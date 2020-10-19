from tkinter import *
import random
import threading

def choose_word(): # chooses a random word from a list
    words = open("words.txt").readlines()
    myword = random.choice(words)
    return myword

def display_word(word): # displays the blanks for the word
    string = ""
    for i in range(0, len(word) - 1):
        string += "_ " # adds a blank for each letter in the secret word
    return(string)

def handle_guess(word, label, letter, lives): # handles the user's letter guess
    for i in range(0, len(word) - 1):
        if letter == word[i]: # if the guess is correct, it will replace the blank with the correct letter
            display[i] = letter
    if letter not in word: # if the guess is incorrect, it will subtract a life and remove a heart from the GUI window
        lives -= 1
        heart_text = str(show_hearts(lives))
        heart_label.configure(text=heart_text)
    label.configure(text=display)
    return lives

def game_status(lives): # checks if the game is over
    global win_counter
    display_string = ""

    for i in range(0, len(display)):
        display_string += str(display[i]) # creates a string from the secret word and whatever blanks the user has guessed correctly

    if lives == 0: # if you run out of lives, the window displays "YOU LOST :(" and returns True
        clear_window()
        you_lost = Label(root, text="YOU LOST :(", font=("Helvetica",40))
        you_lost.grid(row=3, column=1, padx=600, pady=350)
        return True
    if "_" not in display_string: # if you guess the entire word, you win
        win_counter += 1
        return False
    return False

def show_hearts(lives): # shows the number of lives in the window
    global heart_label

    heart_text = ""

    for i in range(0, lives): # for each life, the for loop adds a heart
        heart_text += "♡"

    return heart_text

def main_timed():
    global secret_word
    global display
    global blanks
    global lives
    global win_counter
    global heart_label

    lives = 7
    clear_window()

    title = Label(root, text="HANGMAN", font=("HELVETICA", 120)) # hangman title
    title.grid(row = 0, columnspan=3, pady=50, padx=400)

    heart_text = show_hearts(lives)
    heart_label = Label(root, text=heart_text, fg="red", font=("Arial", 50)) # shows lives
    heart_label.grid(row=3, column=1)

    secret_word = choose_word() # runs choose_word() to get a random word
    game_over = False
    display = StringVar()

    display_blanks = display_word(secret_word)
    display = display_blanks.split(" ")
    display.remove(display[-1])

    blanks = Label(root, text=display_blanks, font=("HELVETICA", 40))
    blanks.grid(row=4, column=1)
    press_a_key = Label(root, text="Press a key to make your guess", font=("HELVETICA", 20)) # instructions that are displayed in the window
    press_a_key.grid(row=5, column=1)

    win_counter = 0

    def input(event): # function runs when a key is pressed
        global blanks
        global secret_word
        global lives
        global game_over
        global display_blanks
        global display

        letter = event.char

        if letter.isalpha() == True:
            if win_counter == 0:
                lives = handle_guess(secret_word, blanks, letter, lives) # handles the guess using the user's key input
                game_over = game_status(lives) # runs game_status() to see if the game is over

            if win_counter == 1:
                clear_window()
                you_win = Label(root, text="YOU WIN!!", font=("Helvetica",40)) # if the user won, it displays "YOU WIN!!" in the window
                you_win.grid(row=3, column=1, padx=600, pady=350)

    root.bind("<Key>", input) # calls input function if a key is pressed

def clear_window():
    for i in root.winfo_children():
            i.destroy()

def init_GUI(): # title screen
    title = Label(root, text="HANGMAN", font=("HELVETICA", 120)) # hangman title
    title.grid(row = 0, columnspan=3, pady=50, padx=400)
    timed = Button(root, text="START", font=("Helvetica", 20), command=main_timed) # play button
    timed.grid(row = 2, columnspan=3)

root = Tk() # creates GUI window
root.geometry("1440x900") # sets window size
init_GUI() # runs title screen
root.mainloop() # runs window
