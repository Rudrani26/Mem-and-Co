from tkinter import *
from tkinter import messagebox
import subprocess
from PIL import Image, ImageTk
import pymysql

window = Tk()
window.title("Sign Up")
window.geometry('1536x864')
window.configure(bg='#fff')

# -----------LOGO-----------------
image1 = Image.open("logo1.png")
img = ImageTk.PhotoImage(image1)

logo = Label(window, image=img, border=0, bg='white',
             width=765, height=944).place(x=35, y=35)

# --------SUBPROCESSES and FUNCTIONS-------------------


def clear():
    user.delete(0, END)
    psw.delete(0, END)
    c_psw.delete(0, END)


def signup():
    if user.get() == '' or psw.get() == '' or c_psw.get() == '':
        messagebox.showerror('Error', 'All Fields Are Required')
    elif psw.get() != c_psw.get():
        messagebox.showerror('Error', 'Passwords Should Match')
    else:
        try:
            con = pymysql.connect(
                host='localhost', user='root', password='Root@143314')
            mycursor = con.cursor()
        except:
            messagebox.showerror(
                'Error', 'Database Connectivity Issue, Please Try Again')
            return
        try:
            query = 'create database userdata'
            mycursor.execute(query)
            query = 'use userdata'
            mycursor.execute(query)
            query = ' create table users(id int auto_increment primary key not null, username varchar(255),password varchar(255) NOT NULL)'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')

        query = 'select * from users where username=%s'
        mycursor.execute(query, (user.get()))

        row = mycursor.fetchone()
        if row != None:
            messagebox.showerror('Error', 'Username Already Exists')
        else:
            query = 'insert into users(username,password) values (%s,%s)'
            mycursor.execute(query, (user.get(), psw.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Registration is successful')
            clear()
            window.destroy()
            import login


def sign():
    subprocess.call(["python", "login.py"])


# ---------MAINFRAME-----------------------
mainframe = Frame(window, width=400, height=400, bg='#fff')
mainframe.place(x=1000, y=200)
# heading
heading = Label(mainframe, text='Sign up', fg='green', bg='white',
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

# confirm password


def on_enter(e):
    c_psw.delete(0, 'end')


def on_leave(e):
    if c_psw.get() == '':
        c_psw.insert(0, 'Confirm Password')


c_psw = Entry(mainframe, width=25, fg='green', border=0,
              bg='white', font=('Microsoft YaHei UI Light', 15))
c_psw.place(x=30, y=220)
c_psw.insert(0, 'Confirm Password')
c_psw.bind('<FocusIn>', on_enter)
c_psw.bind('<FocusOut>', on_leave)

# other frames
frame2 = Frame(mainframe, width=295, height=2,
               bg='black').place(x=25, y=107)  # username
frame3 = Frame(mainframe, width=295, height=2,
               bg='black').place(x=25, y=177)  # password
frame4 = Frame(mainframe, width=295, height=2, bg='black').place(
    x=25, y=255)  # confirm password
label = Label(mainframe, text="Already have an account ?", fg='black',
              bg='white', font=('Microsoft YaHei UI Light', 13))
label.place(x=90, y=340)

# --------------ALL BUTTONS---------------

sign_up = Button(mainframe, width=39, pady=7, text='Sign Up', bg='green',
                 fg='white', border=0, command=signup).place(x=35, y=280)

sign_in = Button(mainframe, width=6, text='Sign in', border=0, bg='white',
                 cursor='hand2', fg='green', font=('Microsoft YaHei UI Light', 15), command=sign).place(x=150, y=365)

window.mainloop()
