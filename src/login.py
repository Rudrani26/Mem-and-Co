from tkinter import *
from tkinter import messagebox
import subprocess
from PIL import Image, ImageTk
import pymysql

root = Tk()
root.title("Login")
root.geometry("1536x864")
root.configure(bg="#fff")

# ------------LOGO---------------------
image1 = Image.open("logo1.png")
img = ImageTk.PhotoImage(image1)

logo = Label(root, image=img, border=0, bg='white',
             width=600, height=600).place(x=150, y=100)

# ------Subprocesses and functions----------


def clear():
    user.delete(0, END)
    psw.delete(0, END)


def signin():
    if user.get() == '' or psw.get() == '':
        messagebox.showerror('Error', 'All Fields Are Required')
    else:
        try:
            con = pymysql.connect(
                host='localhost', user='root', password='Root@143314')
            mycursor = con.cursor()
        except:
            messagebox.showerror(
                'Error', 'Database Connectivity Issue, Please Try Again')
            return

        query = 'use userdata'
        mycursor.execute(query)
        query = 'select * from users where username=%s and password=%s'
        mycursor.execute(query, (user.get(), psw.get()))

        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror('Error', 'Invalid Username or Password')
        else:
            messagebox.showinfo('Welcome', 'Login Successful!')
            clear()
            root.destroy()
            import home

# move to register page


def signup_command():
    subprocess.call(["python", "register.py"])

# ----------Mainframe--------------


mainframe = Frame(root, width=500, height=600, bg="white",)
mainframe.place(x=1000, y=250)

heading = Label(mainframe, text='Sign in', fg='green', bg='white',
                font=('Microsoft YaHei UI Light', 30, 'bold'))
heading.place(x=100, y=3)

# username


def on_enter(e):
    user.delete(0, 'end')


def on_leave(e):
    if user.get() == '':
        user.insert(0, 'Username')


user = Entry(mainframe, width=25, fg='green', border=0,
             bg='white', font=('Microsoft YaHei UI Light', 15))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

# password


def on_enter(e):
    psw.delete(0, 'end')


def on_leave(e):
    if psw.get() == '':
        psw.insert(0, 'Password')


psw = Entry(mainframe, width=25, fg='green', border=0,
            bg='white', font=('Microsoft YaHei UI Light', 15))
psw.place(x=30, y=150)
psw.insert(0, 'Password')
psw.bind('<FocusIn>', on_enter)
psw.bind('<FocusOut>', on_leave)

# -------------other frames---------------------------

frame2 = Frame(mainframe, width=295, height=2, bg='black').place(x=25, y=107)
frame3 = Frame(mainframe, width=295, height=2, bg='black').place(x=25, y=177)

# --------Buttons--------------------------

signin_button = Button(mainframe, width=39, pady=7, text='Sign In', bg='green',
                       fg='white', border=0, command=signin).place(x=35, y=204)

label = Label(mainframe, text="Don't have an account?", fg='black',
              bg='white', font=('Microsoft YaHei UI Light', 11))
label.place(x=70, y=270)

# signup button
sign_up = Button(mainframe, width=6, text='Sign up', border=0, bg='white', cursor='hand2',
                 fg='green', font=('Microsoft YaHei UI Light', 11), command=signup_command)
sign_up.place(x=240, y=267)


root.mainloop()
