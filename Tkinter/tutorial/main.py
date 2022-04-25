# Python tkinter To Do List from python guides(https://pythonguides.com/python-tkinter-todo-list)

from tkinter import *
from tkinter import messagebox

BACKGROUND_COLOR = "#223441"

window = Tk()
window.geometry("500x450+500+200")
window.config(bg=BACKGROUND_COLOR)
window.title("To Do List✏️")

frame = Frame(window)
frame.pack(pady=10)

listbox = Listbox(frame, width=25, height=8, font=("Arial", 18), bd=0, fg="white", bg=BACKGROUND_COLOR,
                  activestyle="none")
listbox.pack(side=LEFT, fill=BOTH)

task_list = [
    'Eat apple',
    'drink water',
    'go gym',
    'write software',
    'write documentation',
    'take a nap',
    'Learn something',
    'paint canvas',
    'something to drink',
    'play with pingping'
]

for item in task_list:
    listbox.insert(END, item)

scrollbar = Scrollbar(frame, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

my_entry = Entry(window, font=("Arial", 24), background="white", foreground="black")

my_entry.pack(pady=20)

button_frame = Frame(window)
button_frame.pack(pady=20)


def new_task():
    task = my_entry.get()
    if task != "":
        listbox.insert(END, task)
        my_entry.delete(0, END)
    else:
        messagebox.showwarning("warning", "Please write some task.")


add_button = Button(button_frame, text="ADD", font=("Arial", 20), padx=20, pady=10, command=new_task)
add_button.pack(fill=BOTH, expand=True, side=LEFT)


def delete_task():
    listbox.delete(ANCHOR)


delete_button = Button(button_frame, text="DELETE", font=("Arial", 20), padx=20, pady=10, command=delete_task)
delete_button.pack(fill=BOTH, expand=True, side=RIGHT)

window.mainloop()
