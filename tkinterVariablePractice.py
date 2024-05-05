import tkinter as tk
from tkinter import ttk

# get the content of the entry
def button_func():
    entry_text = entry.get()

    # update the label
    #label.config(text = 'some other text')
    label['text'] = entry_text
    entry['state'] = 'disabled'
    # print(label.configure())

def change_func():
    label['text'] = 'some text'
    entry['state'] = 'enabled'

# window
window = tk.Tk()
window.title('Getting and setting widgets')

# widgets
label = ttk.Label(master = window, text = 'Some text')
label.pack()
entry = ttk.Entry(master = window)
entry.pack()
button = ttk.Button(master = window, text = 'The button', command = button_func)
button.pack()

# exercise
button2 = ttk.Button(master = window, text = 'Second Button', command = change_func)
button2.pack()

# run
window.mainloop()