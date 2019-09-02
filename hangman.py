import os
import random
import tkinter as tk
import tkinter.messagebox
from tkinter import *

import pygame
from PIL import Image
from PIL import ImageTk

game_level = 1
word = None
letters = []
remain_letters = 1


def easygame():
    game("easy")


def normalgame():
    game("normal")


def hardgame():
    game("hard")


def paint_hangman(game_level, main):
    global photoImg
    global word
    global hangman_word
    # global main1

    width = 200
    height = 400
    address = r"HangmanPhotos\\" + str(game_level) + ".png"
    img = Image.open(address)
    img = img.resize((width, height), Image.ANTIALIAS)
    photoImg = ImageTk.PhotoImage(img)
    hangman_label = Label(main, image=photoImg, bg="white")

    var = StringVar()
    hangman_message = Label(main, textvariable=var, bg="burlywood2", borderwidth=5, relief="raised")
    hangman_label.place(x=10, y=250, relwidth=0.3, relheight=0.5)
    hangman_message.place(x=500, y=10, relwidth=0.3, relheight=0.1)
    hangman_word = Frame(main, bg='white')
    print(word, '********')
    global letters

    i = 0
    for letter in word:
        letters.append(Label(hangman_word, borderwidth=5, bg="khaki3", relief="raised"))

        letters[i].pack(side=LEFT, fill=BOTH, expand=1, anchor=W, padx=2)

        letters[i].config(width=5, height=5)

        i += 1

    hangman_word.place(x=500, y=300)
    if (game_level == 1):
        var.set("Welcome!\nLets play the game!\nYou have 6 chances")
    elif (game_level == 2):
        var.set("First mistake!\nYou have 5 chances ")
    elif (game_level == 3):
        var.set("Second mistake!\nYou have 4 chances ")
    elif (game_level == 4):
        var.set("Third mistake!\nYou have 3 chances ")
    elif (game_level == 5):
        var.set("Forth mistake!\nYou have 2 chances\nBe careful! ")
    elif (game_level == 6):
        var.set("Only one chance! :( ")
    else:
        var.set("Game over!")
        lose(main)


def game(range):
    # game_level = 1
    easywords = ["red", "blue", "orange", "white", "black", "yellow", "green", "purple", "book", "pencil", "hello",
                 "tree"]
    normalwords = ["watermelon", "chair", "computer", "flower", "birthday", "television", "airplane", "tiger",
                   "pineapple"]
    hardwords = ["expensive", "oxygen", "equivalence", "awkward", "galaxy", "gatecrasher", "irregardless",
                 "Flabbergasted"]

    global word
    # global main1

    if range == "easy":
        word = random.choice(easywords)

    elif range == "normal":
        word = random.choice(normalwords)

    else:
        word = random.choice(hardwords)

    print(word, range)

    rangepage.destroy()
    print("hellllo")

    main = Tk()

    C = Canvas(main, bg="blue", height=800, width=1360)
    gamephoto = PhotoImage(file=r"HangmanPhotos/main.png")
    background_label = Label(main, image=gamephoto)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    global buttons
    keybored = Label(main)
    i = 0
    buttons = []
    # l1 = Label(main,text="test")
    # l1.pack()
    for item in alphabet:
        buttons.append(Button(keybored, text=item, font='helv36', bg='khaki1', relief="raised",
                              command=lambda x=item: isInWord(x, main)))

        buttons[i].pack(side=LEFT, fill=BOTH, expand=1, anchor=W, padx=2)
        buttons[i].config(justify=LEFT)
        buttons[i].config(height=2, width=2)

        i += 1

    paint_hangman(game_level, main)
    keybored.place(x=500, y=580)
    C.pack()
    main.mainloop()


def lose(main):
    print("loooooooooooooooooooooooose")
    global word
    global game_level
    # global main1
    statment = "The word was: " + word + "\n"
    answer = tk.messagebox.askquestion("Game over!\n",
                                       statment +
                                       "Do you want to play again?")
    if answer == 'yes':
        try:
            main.destroy()
            os.system('rm *.pyc')
            os.system('python hangman.py')


        except:
            pass
        # main.destroy()
        game_level = 1
        startFunc()
    else:
        main.destroy()


def win(main):
    print("Wiiiiiiiiiiiiiiiiiiiiiiiiiiiin")
    global game_level
    answer = tk.messagebox.askquestion("Congratulations",
                                       "You won this game. " +
                                       "Do you want to play again?")
    # global main1
    if answer == 'yes':

        try:
            main.destroy()
            os.system('rm *.pyc')
            os.system('python hangman.py')


        except:
            pass
    else:
        main.destroy()


def isInWord(x, main):
    global game_level
    global letters
    global remain_letters
    global word
    main.update()

    # global main1
    j = 0

    print(game_level, "game_level")

    if game_level < 7:

        if x in word:

            while j < len(word):
                if x == word[j]:
                    letters[j].config(text=x, font='2')
                j += 1
            for i in buttons:
                if i['text'] == x:
                    i.config(bg='light green', state=DISABLED, fg='black')

        else:

            game_level += 1
            print(game_level)
            paint_hangman(game_level, main)
            for i in buttons:

                if i['text'] == x:
                    i.config(bg='tomato', state=DISABLED, fg='black')

    remain_letters = len(word)
    print(remain_letters, 'len')
    for i in letters:

        if i["text"] != "":
            remain_letters -= 1
            print(i["text"], '-')

    if remain_letters == 0:
        print("You won")
        win(main)

    print(remain_letters, 'remain')


def startFunc():
    try:
        top.destroy()

    except:
        pass

    global rangepage
    rangepage = Tk()
    C1 = Canvas(rangepage, bg="blue", height=800, width=1360)
    filename = PhotoImage(file=r"HangmanPhotos\welcome.png")
    background_label = Label(rangepage, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    easyphoto = PhotoImage(file=r"HangmanPhotos\easy.png")
    easy = easyphoto.subsample(1, 1)
    but3 = tk.Button(rangepage, text="Easy", image=easy, borderwidth=10, command=easygame)
    but3.config(width=200, height=50)

    normalphoto = PhotoImage(file=r"HangmanPhotos\normal.png")
    normal = normalphoto.subsample(1, 1)
    but4 = tk.Button(rangepage, text="Normal", image=normal, borderwidth=10, command=normalgame)
    but4.config(width=200, height=50)

    hardphoto = PhotoImage(file=r"HangmanPhotos\hard.png")
    hard = hardphoto.subsample(1, 1)
    but5 = tk.Button(rangepage, text="Hard", image=hard, borderwidth=10, command=hardgame)
    but5.config(width=200, height=50)

    but3.place(relx=0.4, rely=0.55)
    but4.place(relx=0.4, rely=0.68)
    but5.place(relx=0.4, rely=0.81)
    C1.pack()
    rangepage.mainloop()


def exitFunc():
    top.destroy()


top = Tk()
C = Canvas(top, bg="blue", height=800, width=1360)
filename = PhotoImage(file=r"HangmanPhotos\welcome.png")
background_label = Label(top, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

playphoto = PhotoImage(file=r"HangmanPhotos\P1.png")
play = playphoto.subsample(1, 1)
but1 = tk.Button(top, text="Play", image=play, borderwidth=10, command=startFunc)
but1.config(width=200, height=50)

exitphoto = PhotoImage(file=r"HangmanPhotos\E1.png")
exit = exitphoto.subsample(1, 1)
but2 = tk.Button(top, text="Exit", image=exit, borderwidth=10, command=exitFunc)
but2.config(width=200, height=50)

pygame.init()

pygame.mixer.music.load(r"music.mp3")

pygame.mixer.music.play()

but1.place(relx=0.25, rely=0.7)
but2.place(relx=0.55, rely=0.7)
C.pack()
top.mainloop()
