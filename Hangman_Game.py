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

def handle_guess(label, letter):
    display_string = ""
    for i in range(0, len(secret_word) - 1):
        if letter == secret_word[i]:
            display[i] = letter
    if display_string == secret_word:
        print("You won :)")
    label.configure(text=display)


# def timer(wrong_counter):
#     time_count = 0
#     time = 6
#     if time_count < 6:
#         print("bruh")
#         start_time = threading.Timer(time, show_hangman(wrong_counter))
#         wrong_counter += 1
#         start_time.start()


def hangman_draw():
    print("bruh")

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
    global secret_word
    global display_blanks
    global display
    global blanks
    global wrong_counter

    wrong_counter = 0
    time_count = 0
    clear_window()
    
    title = Label(root, text="HANGMAN", font=("HELVETICA", 50))
    title.grid(row = 0, columnspan=3, pady=20, padx=20)

    secret_word = choose_word()
    game_over = False
    display = StringVar()

    display_blanks = display_word(secret_word)
    display = display_blanks.split(" ")
    display.remove(display[-1])

    blanks = Label(root, text=display_blanks, font=("HELVETICA", 40))
    blanks.grid(row=4, column=1, pady = 200)
    
    press_a_key = Label(root, text="Press a key to make your guess.", font=("HELVETICA", 30))
    press_a_key.grid(row=5, column=1, pady=30)

    # game_over = game_status(secret_word, chosen_letters)

    def input(event):
        # global lives
        # lives = 30
        letter = event.char
        handle_guess(blanks, letter)

        # if incorrect == True:
        #     lives -= 1
        #     lives_string = "Lives: " + str(lives)
        #     lives_label.configure(text=lives_string)
        #
        # lives_string = "Lives: " + str(lives)
        # lives_label = Label(root, text = lives_string)
        # lives_label.grid(row=4, column=3)

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
