from tkinter import *

root = Tk()
root.geometry("600x300")
root.title("Tut9-Button")
f1 = Frame(root, bg="grey", borderwidth=3, relief=SUNKEN)
f1.pack(side=LEFT, anchor="ne")


def Button1():
    print("Button1 click........")


def Button2():
    print("Button2 click.........")


def Button3():
    print("Button3 click.........")


def Button4():
    print("Button4 click.........")


b1 = Button(f1, text="Button1", fg="red", command=Button1)
b1.pack(side=LEFT, padx=20)

b2 = Button(f1, text="Button2", fg="red", command=Button2)
b2.pack(side=LEFT, padx=20)

b3 = Button(f1, text="Button3", fg="red", command=Button3)
b3.pack(side=LEFT, padx=20)

b4 = Button(f1, text="Button4", fg="red", command=Button4)
b4.pack(side=LEFT, padx=20)

root.mainloop()

