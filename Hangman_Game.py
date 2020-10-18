from tkinter import *
from tkinter.ttk import *
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

def handle_guess(label, letter, lives):
    for i in range(0, len(secret_word) - 1):
        if letter == secret_word[i]:
            display[i] = letter
    if letter not in secret_word:
        lives -= 1
        print(lives)
    label.configure(text=display)
    return lives

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

def show_hearts():
    
    photo = PhotoImage(file = "heart.jpeg")
    
    
    
#     heart_path = "heart.jpeg"
#     heart_img = ImageTk.PhotoImage(Image.open(heart_path))
#     heart_label = tk.Label(image = heart_img)
#     heart_label.grid()
    
#     heart_load = Image.open("heart.png")
#     heart = ImageTk.PhotoImage(heart_load)
    
#     heart_display = Label(self, image=heart)
#     heart_display.image = heart_load
#     heartdisplay.grid(row=2, column =2)
    
#     hearts_canvas = Canvas(root, width = 300, height = 300)      
#     hearts_canvas.grid(row = 3) 
#     heart = PhotoImage(file="heart.png")      
#     hearts_canvas.create_image(20,20, anchor=NW, image=img)      

    

def main_timed():
    global secret_word
    global display_blanks
    global display
    global blanks
    global lives

    clear_window()
    
    title = Label(root, text="HANGMAN", font=("HELVETICA", 120))
    title.grid(row = 0, columnspan=3, pady=50, padx=400)

    secret_word = choose_word()
    game_over = False
    display = StringVar()

    show_hearts()
    
    display_blanks = display_word(secret_word)
    display = display_blanks.split(" ")
    display.remove(display[-1])

    space = Frame(root)
    space.grid(row=2, pady=200)
    
    
    blanks = Label(root, text=display_blanks, font=("HELVETICA", 40))
    blanks.grid(row=4, column=1, pady = 10, padx=400)
    
    press_a_key = Label(root, text="Press a key to make your guess.", font=("HELVETICA", 20))
    press_a_key.grid(row=5, column=1, pady=1, padx=400)

    # game_over = game_status(secret_word, chosen_letters)
    lives = 10

    def input(event):
        global lives
        letter = event.char
        lives = handle_guess(blanks, letter, lives)

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
