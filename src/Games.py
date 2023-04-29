import customtkinter as ctk
from tkinter import *
from PIL import Image, ImageTk
import subprocess

root = ctk.CTk()
root.geometry("1536x864")
root.config(background='#40BB7B')
root.title("mem & co.")

image1 = Image.open("game1.png")
resize_image = image1.resize((765, 944))
img = ImageTk.PhotoImage(resize_image)

Label(root, image=img, border=0, bg='#40BB7B',
      width=765, height=944).place(x=35, y=35)

title_label = ctk.CTkLabel(root,
                           text="Lets Play Games",
                           font=ctk.CTkFont(
                               size=60, weight="bold", family="Bungee Color"),
                           fg_color="#40BB7B")
title_label.pack(padx=20, pady=(40, 20))
title_label.place(x=856, y=80)

# Move to Mem Flip


def memflip():
    subprocess.call(["python", "memorypuzzlegame.py"])


memflip_button = ctk.CTkButton(root, text="Memory Flip",
                               width=500,
                               height=100,
                               font=("Arial", 30),
                               fg_color="#3F5896",
                               hover_color="#576381",
                               command=memflip
                               )

memflip_button.pack(pady=20)
memflip_button.place(x=850, y=200)


def sudoku():
    subprocess.call(["python", "Sudoku.py"])


sudoku_button = ctk.CTkButton(root, text="Sudoku",
                              width=500,
                              height=100,
                              font=("Arial", 30),
                              fg_color="#3F5896",
                              hover_color="#576381",
                              command=sudoku
                              )

sudoku_button.pack(pady=20)
sudoku_button.place(x=850, y=400)


def wordgame():
    subprocess.call(["python", "Jumbled_Words.py"])


Wordgame_button = ctk.CTkButton(root, text="Word Game",
                                width=500,
                                height=100,
                                font=("Arial", 30),
                                fg_color="#3F5896",
                                hover_color="#576381",
                                command=wordgame
                                )

Wordgame_button.pack(pady=20)
Wordgame_button.place(x=850, y=600)

root.mainloop()
