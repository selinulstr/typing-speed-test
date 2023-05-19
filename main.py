from tkinter import *
import tkinter.messagebox
from words import words
import random


t = 60
timer = None
WORDS_TYPED = 0
RANDOM_WORD = random.choice(words)
BG = "#898AA6"
FG = "#C9BBCF"


def change_word():
    global RANDOM_WORD, text_label
    text_label.grid_forget()
    typing_entry.grid(row=3, column=0, columnspan=3)
    typing_entry.focus()
    RANDOM_WORD = random.choice(words)
    typing_entry.delete(0, END)
    text_label = Label(text=f"{RANDOM_WORD}", bg=BG, fg="white", font=("Courier", 37, "bold"))
    text_label.grid(row=2, column=0, columnspan=3, pady=20)


def s():
    start_button.grid_forget()
    change_word()
    countdown(t)


def start_game(sv):
    global RANDOM_WORD, WORDS_TYPED, text_label
    current_letter = (len(sv.get()) - 1)
    if sv.get() == RANDOM_WORD:
        WORDS_TYPED += len(RANDOM_WORD)
        change_word()
    elif sv.get():
        try:
            if sv.get()[current_letter] != RANDOM_WORD[current_letter]:
                text_label.config(text=f"{RANDOM_WORD}", bg="Red")
            else:
                text_label.config(text=f"{RANDOM_WORD}")
        except IndexError:
            text_label.config(text=f"{RANDOM_WORD}", bg="Red")


def callback():
    start_game(sv)


def countdown(t):
    global WORDS_TYPED, timer
    minutes, secs = divmod(t, 60)
    time = '{:02d}:{:02d}'.format(minutes, secs)
    p.config(text=f"Time Left: {time}")
    if t > 0:
        timer = root.after(1000, countdown, t - 1)
    else:
        p.config(text=f"Time Left: 00:00")
        tkinter.messagebox.showinfo("Results", f"The results are in, you type at {(WORDS_TYPED / 5) / 0.5} WPM.")
        text_label.grid_forget()
        typing_entry.grid_forget()
        start_button.configure(text="RESTART")
        start_button.grid(row=2, column=0, columnspan=3, pady=70)


root = Tk()
root.title("TYPING SPEED TEST")
root.geometry("610x400")
root.configure(pady=30, padx=30, background=BG)
text_label = Label(text=f"{RANDOM_WORD}")


title_label = Label(root, text="TYPING SPEED TEST", font=("Courier", 40, "bold"), background=BG, fg=FG)
title_label.grid(row=0, column=0, columnspan=3)

p = Label(root, text=f"Time Left: 01:00", font=("Courier", 30, "bold"), background=BG, fg=FG)
p.grid(row=1, column=0, columnspan=3)

start_button = Button(root, text="Start", command=s, fg=BG, bg="#B7D3DF", font=("Courier", 25, "bold"))
start_button.grid(row=2, column=0, columnspan=3, pady=70)

sv = tkinter.StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: callback())
typing_entry = Entry(root, textvariable=sv, width=20, font=("Courier", 30, "bold"))


root.mainloop()