#!/usr/bin/env python
# coding: utf-8

# In[19]:


# Import required libraries :
from tkinter import *
##import simpleaudio as sa
import random
import tkinter.font as font
import time


running = True

while running == True:
    # Calculate starting time :
    start_time = time.time()

    root = Tk()
    root.geometry('+100+100')
    root.configure(bg="#40BB7B")
    root.iconphoto(True, PhotoImage(file="SUP.png"))
    root.title("JUMBLE WORDS")
    root.resizable(width=False, height=False)

    # Load sound files :
    #start = sa.WaveObject.from_wave_file("Start.wav")
    # one = sa.WaveObject.from_wave_file("Win.wav")
    # two = sa.WaveObject.from_wave_file("Lose.wav")
    #three = sa.WaveObject.from_wave_file("6.wav")

    # start.play()

    # Select a word from list :
    def random_word():
        words = ["APPLE", "MANGO", "PINEAPPLE", "CHERRY", "PLUM", "GRAPES"]
        pick = random.choice(words)
        return pick

    # Jumble the selected word :
    def jumbled_word(word):
        word = random.sample(word, len(word))
        word_jumbled = "".join(word)
        return word_jumbled

    # Randomly selected word :
    pick = random_word()

    # Jumbled word :
    jumbled = jumbled_word(pick)

    # Get the letters from jumbled word :
    list1 = list(jumbled)
    len_list1 = len(list1)

    # Get the PhotoImages for our letters :
    for i in range(len_list1):
        list1[i] = PhotoImage(file=str(list1[i])+str("_P.png"))

    row_0 = 0
    col_0 = 0

    # Arrange the letters on the main window :
    for i in range(len_list1):
        B = Label(root, image=list1[i])
        B.grid(row=row_0, column=col_0)
        col_0 = col_0 + 1

    # Blank space for row_1 :
    root.grid_rowconfigure(1, minsize=10)

    # Modify font :
    myFont = font.Font(family='Calibri',  weight='bold')

    # For label image :
    your_choice = PhotoImage(file="YOUR_GUESS.png")
    surprise = PhotoImage(file="SUP.png")
    win = PhotoImage(file="WINNN.png")
    lose = PhotoImage(file="LOSEEE.png")
    check = PhotoImage(file="CHECKK.png")
    close = PhotoImage(file="CLOSEE.png")

    # To arrange the labels in center :
    #x = math.floor(len_list1/2)

    # Entry label :
    label = Label(root, image=your_choice)
    label.grid(row=2, column=0, columnspan=len_list1)
    label["font"] = myFont

    # Add blank space :
    root.grid_rowconfigure(3, minsize=10)

    # Add entry widget :
    e1 = Entry(root, bd=5, bg="#9ca1db", justify=CENTER,
               font=myFont, fg="#000000")
    e1.grid(row=4, column=0, columnspan=len_list1)

    # Add blank space :
    root.grid_rowconfigure(5, minsize=10)

    # Get the entry value in upper case :
    answer = (e1.get()).upper()

    # Make list of correct word :
    list2 = list(pick)

    # Load images for correct word :
    for j in range(len(list2)):
        list2[j] = PhotoImage(file=str(list2[j])+str("_P.png"))

    # Check button :
    button = Button(root, image=check, command=lambda: result())
    button.grid(row=6, column=0)

    # Close button :
    Btn = Button(root, image=close, command=lambda: reset())
    Btn.grid(row=6, column=len_list1-1)

    # Add blank space :
    root.grid_rowconfigure(7, minsize=10)

    # Label that will display result :
    label2 = Label(root, image=surprise)
    label2.grid(row=8, column=0, columnspan=len_list1)

    root.grid_rowconfigure(9, minsize=10)

    # Modify the fonts :
    myFont = font.Font(family='Comic Sans MS', weight='bold')

    # Label to show time taken :
    label3 = Label(root, text=" TIME : ", width=12, bg="#3F5896",
                   justify=CENTER, font=myFont, fg="#000000", relief=RAISED)
    label3.grid(row=12, column=0, columnspan=len_list1)

    # Function to check whether the user's guess is correct or not :
    def result():
        # Get the entry value in upper case :
        answer = (e1.get()).upper()

        if answer == pick:
            # Caculate the time consumed :
            time_taken = time.time() - start_time
            time_taken = int(time_taken)

            # Change the label :
            label3.configure(text="TIME : "+str(time_taken)+" Sec")

            # Play win sound :
            # one.play()

            # Change label image to win :
            label2.configure(image=win)

            # Showing original word :
            col_2 = 0
            row_2 = 10

            # Display the origianl word :
            for i in range(len_list1):
                B = Label(root, image=list2[i])
                B.grid(row=row_2, column=col_2)
                col_2 = col_2+1

            # Add blank space :
            root.grid_rowconfigure(11, minsize=10)

            # To play again after 3 sec :
            root.update_idletasks()
            root.after(3000)
            root.destroy()

        else:
            # Play a sound file :
            # two.play()

            # Change the label :
            label2.configure(image=lose)

            # Change back to original label image :
            root.update_idletasks()
            root.after(500)
            label2.configure(image=surprise)

            # Clear the entry :
            e1.delete(0, "end")

    # Function that triggers by pressing CLOSE button :

    def reset():
        # Play a sound file :
        # three.play()

        # Change the running value to false :
        global running
        running = False

        # CLose the main window :
        root.destroy()

    # Enter the main loop :
    root.mainloop()


# In[ ]:


# In[ ]:
