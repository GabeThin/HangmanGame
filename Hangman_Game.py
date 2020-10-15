from tkinter import *
import random

def choose_word():
  words = open("words.txt").readlines()
  myword = random.choice(words)
  return (myword)

def display_word(word,chosen):
  #show the word in its current state including blanks for letters not chosen.
  display_string = ""

  for i in range(0,len(word)):
    if(word[i] in chosen):
      display_string += word[i] + " "
    else:
      display_string += "_ "

  return display_string

def handle_guess(word, letter):
  #get the guess, update chosen, give feedback to user such as -- you are correct
  print(letter)

  if len(letter) == 1:
    if letter in word:
      print("correct")
      print("")

    else:
      print("incorrect")
      print("")

  else:
    print("You can only guess one letter at a time")

  return letter[0]

def game_status(word,chosen):
  #show graphics & chosen letters
  wrongCounter = 0
  for letter in chosen:
    if letter not in word:
      wrongCounter+= 1
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
    print("Already guessed:",chosen)
    return False
  #announce the outcome if the game is over
  #return boolean of whether the game is over.

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

def timed_GUI():
  guess_text = Label(root, text="enter letter guess:")
  guess_text.pack(padx=(100, 0), side=LEFT)
  guess = Entry(root)
  guess.pack(side=LEFT)
  secret_word = "the"
  submit = Button(frame, text = "Submit Guess", font = ("Arial", 24), command=check_guess())
  submit.pack(pady = (350, 0), padx = 100, side = LEFT)
  
  
def check_guess():
  letter = guess.get()

def main_timed():
  for i in root.winfo_children():
    i.destroy()
  game_over = False
  secret_word = "the"

  timed_GUI()

  chosen_letters = ""
  while game_over == False:
    word_display = Label(root, text="the")

    word_display.pack(pady = (350, 0), padx = 100, side = LEFT)
    chosen_letters += handle_guess(secret_word, chosen_letters)
    game_over = game_status(secret_word, chosen_letters)

root = Tk()
root.geometry("1440x900")
frame = Frame(root)
frame.pack()

def init_GUI():
  title = Label(frame, text = "HANGMAN", font = ("Arial", 40))
  title.pack(pady = 100)

  # default = Button(frame, text = "DEFAULT", font = ("Arial", 24), command=main_default)
  # default.pack(pady = (350, 0), padx = 100, side = LEFT)

  timed = Button(frame, text = "TIMED", font = ("Arial", 24), command=main_timed)
  timed.pack(pady = (350, 0), padx = 100, side = LEFT)

init_GUI()
root.bind("<Return>", handle_guess("the", "b"))
root.mainloop()
