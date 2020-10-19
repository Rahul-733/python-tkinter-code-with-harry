from tkinter import *

root = Tk()
root.title("tut14-Events")
root.geometry("600x400")


def clickme(event):
    print(f"you clicked on button {event.x} and {event.y}")


widght = Button(root, text="click")
widght.pack()

widght.bind('<Button-1>', clickme)
widght.bind('<Double-1>',quit)

root.mainloop()
