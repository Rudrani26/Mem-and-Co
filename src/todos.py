from tkinter import *
from tkinter import messagebox


def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")


def deleteTask():
    lb.delete(ANCHOR)


ws = Tk()
ws.geometry('1536x864')
ws.title('To do List ')
ws.config(bg='#40BB7B')

title_label = Label(ws,
                    text="Finish off the tasks!",
                    font=('Bungee Color', 40), bg='#40BB7B').place(x=520, y=50)


frame = Frame(ws)
frame.pack(pady=(150, 10))

lb = Listbox(
    frame,
    width=50,
    height=15,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
)
lb.pack(side=LEFT, fill=BOTH)

task_list = [

]

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    ws,
    font=('times', 24)
)

my_entry.pack(pady=20)

button_frame = Frame(ws, bg='#40BB7B')
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT, padx=25,)


delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT, padx=25)

back_btn = Button(
    button_frame,
    text='Go Back',
    font=('times 14'),
    bg='#3F5896',
    padx=20,
    pady=10,
    command=deleteTask
)
back_btn.pack(fill=BOTH, expand=True, side=BOTTOM, padx=25)


ws.mainloop()
