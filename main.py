import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('PySequencer')
content = ttk.Frame(root)
loopbuttons = ttk.Frame(content)

button1 = ttk.Button(loopbuttons)
button2 = ttk.Button(loopbuttons)
button3 = ttk.Button(loopbuttons)
button4 = ttk.Button(loopbuttons)
button5 = ttk.Button(loopbuttons)
button6 = ttk.Button(loopbuttons)
button7 = ttk.Button(loopbuttons)
button8 = ttk.Button(loopbuttons)


def render():
    content.grid()
    loopbuttons.grid()
    button1.grid(column=0, row=0)
    button2.grid(column=1, row=0)
    button3.grid(column=2, row=0)
    button4.grid(column=3, row=0)
    button5.grid(column=4, row=0)
    button6.grid(column=5, row=0)
    button7.grid(column=6, row=0)
    button8.grid(column=8, row=0)

render()
root.mainloop()