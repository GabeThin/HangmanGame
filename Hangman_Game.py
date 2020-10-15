from tkinter import *
import random


correct = False

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


def handle_guess():
    # get the guess, update chosen, give feedback to user such as -- you are correct
    letter = guess.get()
    word = secret_word

    if len(letter) == 1:
        if letter in word:
            print("correct")
            display = StringVar()
            blanks = Label(root, textvariable=display)
            blanks.pack(padx=(100, 0), side=LEFT)
            display.set(display_word(secret_word, chosen_letters))
            
            
        else:
            print("incorrect")
        next_round= False
        

    else:
        print("You can only guess one letter at a time")
    return letter[0]


# def clear_display():
#     blanks.destroy()


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
  
        if next_round==True:
            guess_text = Label(root, text="enter letter guess:")
            guess_text.pack(padx=(100, 0), side=LEFT)
            global guess
            guess = Entry(root)
            guess.pack(side=LEFT)
            submit = Button(root, text="Submit Guess", font=("Arial", 24), command=handle_guess)
            submit.pack(side=LEFT)
            chosen_letters += handle_guess()
            game_over = game_status(secret_word, chosen_letters)
            next_round = False
        else:
            for i in root.winfo_children():
                i.destroy()
            next_round= True
           
        
root = Tk()
root.geometry("1440x900")
frame = Frame(root)
frame.pack()


def init_GUI():
    title = Label(frame, text="HANGMAN", font=("Arial", 40))
    title.pack(pady=100)

    timed = Button(frame, text="PLAY", font=("Arial", 24), command=main_timed)
    timed.pack(pady=(350, 0), padx=100, side=LEFT)


#HEAD
# main_timed()
#=========
init_GUI()
root.mainloop()
#c23a96fb9dba2587fe350abfede0c6e86132768c
