from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


def analyze_mood():
    mood = mood_slider.get()
    if mood >= 8:
        message = "You're doing great! We are glad to see you happy."
    elif mood >= 5:
        message = "You're feeling okay. Play a few games and cheer up!"
    elif mood >= 3:
        message = "You might be feeling a bit down. Relax and take rest."
    else:
        message = "You should talk to someone. Please contact your loved one."
    result_label.config(text=message)


# Create the main window
root = Tk()
root.title('About Me')
root.geometry("1536x864")
root.configure(bg="#3F5896")

# FRAME: USER DETAILS
frame = Frame(root, width=750, height=900, bg='#40BB7B')
frame.place(x=00, y=00)
heading = Label(frame, text='Personal Information', fg='white',
                bg='#40BB7B', font=('Arial', 20, 'bold'))
heading.place(x=200, y=70)

# IMAGE
img = PhotoImage(
    file='personalinfo_pic-removebg.png')
label1 = Label(frame, image=img, bg='#40BB7B', width='225',
               height='250').place(x=230, y=120)
# img.zoom(10,10)

name = Label(frame, text='My Name:', fg='white',
             bg='#40BB7B', font=('Arial', 15, 'bold'))
name.place(x=50, y=400)
name = Label(frame, text='Rudrani Chavarkar', fg='black',
             bg='#40BB7B', font=('Arial', 15, 'bold'))
name.place(x=200, y=400)

age = Label(frame, text='My Age:', fg='white',
            bg='#40BB7B', font=('Arial', 15, 'bold'))
age.place(x=50, y=470)
age = Label(frame, text='70 years', fg='black',
            bg='#40BB7B', font=('Arial', 15, 'bold'))
age.place(x=200, y=470)

address = Label(frame, text='My Address:', fg='white',
                bg='#40BB7B', font=('Arial', 15, 'bold'))
address.place(x=50, y=540)
address = Label(frame, text='A-702, Sunflower Apartments, Bandra (West), Mumbai',
                fg='black', bg='#40BB7B', font=('Arial', 15, 'bold'))
address.place(x=200, y=540)

hobby = Label(frame, text='I like to:', fg='white',
              bg='#40BB7B', font=('Arial', 15, 'bold'))
hobby.place(x=50, y=610)
hobby = Label(frame, text='Draw and Sing', fg='black',
              bg='#40BB7B', font=('Arial', 15, 'bold'))
hobby.place(x=200, y=610)

care = Label(frame, text='My Caretaker:', fg='white',
             bg='#40BB7B', font=('Arial', 15, 'bold'))
care.place(x=50, y=680)
care = Label(frame, text='Vaishnavi Hindalekar', fg='black',
             bg='#40BB7B', font=('Arial', 15, 'bold'))
care.place(x=200, y=680)

# ROOT: MOOD ANALYSE
heading = Label(root, text='Mood Analyser', fg='white',
                bg='#3F5896', font=('Arial', 20, 'bold'))
heading.place(x=1050, y=70)

feel = Label(root, text='How are you feeling today?', fg='white',
             bg='#3F5896', font=('Arial', 15, 'bold'))
feel.place(x=1020, y=200)

mood_slider = Scale(root, from_=0, to=10,
                    orient=HORIZONTAL, width='20', length='350')
mood_slider.set(50)
mood_slider.place(x=970, y=300)

analyze_button = Button(root, text="Analyze", font=(
    'Arial', 15, 'bold'), command=analyze_mood, width='17')
analyze_button.place(x=1050, y=400)

result_label = Label(root, text="", font=('Arial', 15, 'bold'), fg='dark blue')
result_label.place(x=870, y=500)

quit_button = Button(root, text="Quit", width='17', font=(
    'Arial', 15, 'bold'), command=root.quit)
quit_button.place(x=1050, y=600)

root.mainloop()
# 40BB7B
