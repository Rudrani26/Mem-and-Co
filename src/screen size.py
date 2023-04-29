from tkinter import *
from PIL import Image, ImageTk
import webbrowser
import subprocess


# Create the main window
root = Tk()
root.title('Welcome to Mem. and Co.')
root.geometry("1536x864")
root.configure(bg="#40BB7B")

# LOGO Image
img = PhotoImage(file='welcomepic_withoutbg.png')
#img=PhotoImage.resize((450, 350))
label1 = Label(root, image=img, bg='#40BB7B').place(x=850, y=200)
img.zoom(10, 10)

# Add some buttons to navigate to other pages
frame = Frame(root, width=750, height=700, bg='#40BB7B')
frame.place(x=70, y=50)

# Add a welcome message label
heading = Label(frame, text='Welcome to Mem. and Co!',
                fg='white', bg='#40BB7B', font=('Arial', 20, 'bold'))
heading.place(x=200, y=80)

# aboutus text
heading1 = Label(frame, text='Thankyou for choosing us as a resource for your dementia care journey.',
                 fg='white', bg='#40BB7B', font=('Arial', 15, 'bold'), width='57')
heading1.place(x=15, y=150)
heading2 = Label(frame, text='We are here to support you every step of the way.',
                 fg='white', bg='#40BB7B', font=('Arial', 15, 'bold'), width='42')
heading2.place(x=100, y=180)

#text = Text(root)
#text.insert(INSERT, "Hello.....")
# text.place(x=110,y=150)

# Move to Games page


def gamespage():
    subprocess.call(["python", "Games.py"])


games_button = Button(frame, text='Play Games', border=0, font=(
    'Arial', 18), fg='white', bg='#3F5896', width='30', command=gamespage)
games_button.place(x=130, y=230)

# Move to blogs page


def paintpage():
    subprocess.call(["python", "paint.py"])


blogs_button = Button(frame, text='Lets Paint', border=0, font=(
    'Arial', 18), fg='white', bg='#3F5896', width='30', command=paintpage)
blogs_button.place(x=130, y=310)

# Move to to dos page


def todopage():
    subprocess.call(["python", "todos.py"])


todo_button = Button(frame, text='Create a To Do List', border=0, font=(
    'Arial', 18), fg='white', bg='#3F5896', width='30', command=todopage)
todo_button.place(x=130, y=390)


def userpage():
    subprocess.call(["python", "userprofile.py"])


userp_button = Button(frame, text='Your User Profile', border=0, font=(
    'Arial', 18), fg='white', bg='#3F5896', width='30', command=userpage)
userp_button.place(x=130, y=470)
# def sign():
#     subprocess.call(["python", "login.py"])


def whatsappweb():
    webbrowser.open(
        "www.alz.org/help-support/community/support-groups")


whatsapp_button = Button(frame, text='Join Support Group', border=0, font=(
    'Arial', 18), fg='white', bg='#3F5896', width='30', command='whatsappweb')
whatsapp_button.place(x=130, y=550)
# def sign():
#     subprocess.call(["python", "login.py"])


# Run the main event loop
root.mainloop()
