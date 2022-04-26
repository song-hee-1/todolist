# Python tkinter To Do List from python guides(https://pythonguides.com/python-tkinter-todo-list)

from tkinter import *
from tkinter import messagebox
import pandas

BACKGROUND_COLOR = "#223441"

# ---------------------------- READ FILE ----------------------------- #

data = pandas.read_csv("todo_list.csv", index_col=0)
todolist = data["list"].to_list()


# ---------------------------- TASK FUNCTION ----------------------------- #

def new_task():
    task = my_entry.get()
    if task != "":
        listbox.insert(END, task)
        todolist.append(task)
        my_entry.delete(0, END)

    else:
        messagebox.showwarning("warning", "Please write some task.")


def delete_task():
    try:
        for i in listbox.curselection():
            list_item = str(listbox.get(i))
            listbox.delete(ANCHOR)
            todolist.remove(list_item)
            my_entry.delete(0, END)
    except UnboundLocalError:
        messagebox.showwarning("warning", "Please select some task.")


def edit_task():
    new_data = my_entry.get()
    todolist[index] = new_data
    listbox.delete(index)
    listbox.insert(index, new_data)
    my_entry.delete(0, END)


def select_for_listbox(event):
    global index, list_item
    listbox = event.widget
    for i in listbox.curselection():
        index = i
        list_item = str(listbox.get(i))
    my_entry.delete(0, END)
    my_entry.insert(0, string=list_item)


def on_save():
    new_data = pandas.DataFrame(todolist, columns=["list"])
    new_data.to_csv("todo_list.csv")


def on_exit():
    if messagebox.askokcancel(title="Warning", message="Do you want to quit? \n Unsaved files will be deleted."):
        window.destroy()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.geometry("500x450+500+200")
window.config(bg=BACKGROUND_COLOR)
window.title("To Do List✏️")

frame = Frame(window)
frame.pack(pady=10)

menubar = Menu(window)
file_menu = Menu(menubar, tearoff=0)

file_menu.add_command(label="저장", command=on_save)
file_menu.add_command(label="끝내기", command=on_exit)

menubar.add_cascade(label="파일", menu=file_menu)

listbox = Listbox(frame, width=25, height=8, font=("Arial", 18), bd=0, fg="white", bg=BACKGROUND_COLOR,
                  activestyle="none")
listbox.pack(side=LEFT, fill=BOTH)

for item in todolist:
    listbox.insert(END, item)

scrollbar = Scrollbar(frame, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

listbox.bind('<<ListboxSelect>>', select_for_listbox)

my_entry = Entry(window, font=("Arial", 24), background="white", foreground="black")

my_entry.pack(pady=20)

button_frame = Frame(window)
button_frame.pack(pady=20)

add_button = Button(button_frame, text="ADD", font=("Arial", 20), padx=10, pady=10, command=new_task)
add_button.grid(row=0, column=0)

edit_button = Button(button_frame, text="EDIT", font=("Arial", 20), padx=10, pady=10, command=edit_task)
edit_button.grid(row=0, column=1)

delete_button = Button(button_frame, text="DELETE", font=("Arial", 20), padx=10, pady=10, command=delete_task)
delete_button.grid(row=0, column=3)

window.config(menu=menubar)
window.mainloop()
