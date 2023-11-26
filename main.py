import os
import customtkinter as ctk
from PIL import ImageTk, Image
from tkinter import PhotoImage, Button
import feed as fd
from tkinter import messagebox as mb
import pygame as py

os.system("pip install -r requirements.txt")
py.mixer.init()

#urgent commit
global i
i = 0

py.mixer.music.load("audios/bg_music.mp3")
py.mixer.music.play(loops=-1)

wrong = py.mixer.Sound('audios/wrong.wav')
wrong.set_volume(1)

passed = py.mixer.Sound('audios/pass.wav')
passed.set_volume(1)

victory = py.mixer.Sound('audios/victory.wav')
victory.set_volume(1)

failure = py.mixer.Sound('audios/failure-1-89170.wav')
failure.set_volume(1)

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("564x797+700+150")
app.title('HangMan Game -TEAM 2-')
app.after(201, lambda: app.iconbitmap('images/image.ico'))
check_butt = PhotoImage(file='images/check.png')

i1 = PhotoImage(file='Hangman images/1.png')
i2 = PhotoImage(file='Hangman images/2.png')
i3 = PhotoImage(file='Hangman images/3.png')
i4 = PhotoImage(file='Hangman images/4.png')
i5 = PhotoImage(file='Hangman images/5.png')
i6 = PhotoImage(file='Hangman images/6.png')

man = [i1, i2, i3, i4, i5, i6]


def error():
    wrong.play()


def victroy():
    victory.play()


def good():
    passed.play()


def stop():
    py.mixer.music.stop()


def gameover():
    failure.play()


def choose_word():
    x = fd.get_word()
    x = x.lower()
    print(x)
    return x


def new_game():
    global i
    l1.configure(image=img1)
    global word_to_guess, guesses_left, guessed_letters, game_over
    word_to_guess = choose_word()
    guesses_left = 6
    i = 0
    guessed_letters = []
    game_over = False
    update_display()


def update_display():
    display_word = ""
    for letter in word_to_guess:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
    show_up.configure(text=display_word)
    counter.configure(text=str(guesses_left))

    if display_word == word_to_guess:
        victroy()
        if mb.askyesno(title="YOU WON", message=f"You win! The word was:{word_to_guess}\nWant To Continue ? "):
            game_over = True
            new_game()
        else:
            exit()
    elif guesses_left == 0:
        gameover()
        if mb.askyesno(message=f"You lose! The word was: {word_to_guess}\n Want To Continue?"):
            game_over = True
            new_game()
        else:
            exit()


def guess_letter():
    global guesses_left, game_over, i  # Add this line to declare guesses_left as a global variable
    if not game_over:
        letter = entry1.get()
        letter = letter.lower()
        if letter.isalpha() and len(letter) == 1:
            if letter in guessed_letters:
                error()
                mb.showwarning(message="You already guessed that letter.")
            else:
                guessed_letters.append(letter)
                if letter not in word_to_guess:
                    error()
                    l1.configure(image=man[i])
                    i += 1
                    guesses_left -= 1
                else:
                    good()
                update_display()
                entry1.delete(0)
        else:
            error()
            mb.showwarning(message="Please enter a single letter.")
            entry1.delete(0)
            entry1.delete(0)
    else:
        error()
        if mb.askyesno(message="Game over. Start a new game."):
            new_game()
        else:
            exit()


if __name__ == '__main__':
    img1 = ImageTk.PhotoImage(Image.open("images/Play.png"))
    l1 = ctk.CTkLabel(master=app, image=img1)
    l1.pack()
    l2 = ctk.CTkLabel(
        master=app,
        text="Guess a Character from the word",
        font=('Century Gothic', 20),
        bg_color='#813f34')
    l2.place(x=120, y=618)

    check_button = Button(app,
                          image=check_butt,
                          width=30,
                          height=30,
                          borderwidth=0,
                          bg='#813f34',
                          background="#813f34",
                          command=new_game)
    check_button.place(x=420, y=656)

    '''hangman = ctk.CTkLabel(master=app,
                           image=head,
                           bg_color='#e1ae7c')
    hangman.place(x=258, y=248)'''

    counter = ctk.CTkLabel(
        master=app,
        text="6",
        height=50,
        width=50,
        text_color="Black",
        font=('Century Gothic', 30),
        bg_color='#8b4f45',
        corner_radius=8)
    counter.place(x=377, y=220)

    show_up = ctk.CTkLabel(
        master=app,
        text="_______",
        font=('Times New Roman', 40),
        bg_color='#813f34')
    show_up.place(x=230, y=700)

    entry1 = ctk.CTkEntry(
        master=app,
        height=38,
        width=220,
        bg_color='#813f34',
        border_color='black',
        placeholder_text_color='#e0ad7b',
        placeholder_text='\tEnter Character',
        corner_radius=10)
    entry1.bind("<Return>", lambda event=None: guess_letter())

    entry1.place(x=180, y=652)
    new_game()
    app.mainloop()

# checking the git functions
