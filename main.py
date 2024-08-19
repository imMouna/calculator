from tkinter import *
from tkinter import ttk
import ast


i = 0
def get_number(num):
    global i
    display.insert(i, num)
    i += 1

def get_operations(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length

def clear_all():
    display.delete(0, END)

def calculate():
    entire_string = display.get()
    try:
        node = ast.parse(entire_string,mode='eval')
        result = eval(compile(node, '<string>', 'eval'))
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, 'Error')

def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, "")


root = Tk()
root.configure(background='black')
root.title("Calculator App")
style = ttk.Style()
style.theme_use('clam')

style.configure('TEntry', foreground='black',
                background='white',
                fieldbackground='white',
                padding=4,
                height=15,
                relief='solid')

border_frame = Frame(root, background="#E4003A", padx=3)  # Adjust padding for border width
border_frame.grid(row=1, columnspan=6, pady=5)

display = ttk.Entry(border_frame, style='TEntry', width=25, font=('roboto', 13, 'bold'))
display.grid(row=1, columnspan=6, pady=5)

style.configure('TButton',
                font=('Helvetica', 12, 'bold'),
                padding=10,
                background='#F9E400',
                height=2,
                width=4,
                padx=8)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
counter = 0
for x in range(3):
    for y in range(3):
        button_text = numbers[counter]
        button = ttk.Button(text=button_text, style='TButton', command=lambda text=button_text: get_number(text))
        button.grid(row=x+2, column=y, padx=6, pady=3)
        counter += 1

last_button = ttk.Button(text='0', style='TButton', command=lambda: get_number(0))
last_button.grid(row=5, column=1, padx=6, pady=3)

ac_button = ttk.Button(text="AC", style='TButton', width=12, command=clear_all)
ac_button.grid(row=5, column=4, columnspan=2)

equal_to_button = ttk.Button(text="=", style='TButton', command=calculate)
equal_to_button.grid(row=5, column=0)

undo_button = ttk.Button(text="⬅", style='TButton', command=undo)
undo_button.grid(row=5, column=2)



operations = ['+', '-', '*', '/', '*3.14', '%', '(', '**', ')', '**2']
count = 0
for x in range(4):
    for y in range(3):
        if count < len(operations):
            button = ttk.Button(text=operations[count], style='TButton',
                                command=lambda text=operations[count]: get_operations(text))
            count += 1
            button.grid(row=x+2, column=y+3, padx=6, pady=3)
root.mainloop()
