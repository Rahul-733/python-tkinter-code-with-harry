from tkinter import *

root = Tk()
root.geometry("600x300")
root.title("tut8-Frame")

f1 = Frame(root, bg="grey", borderwidth=3, relief=SUNKEN)
f1.pack(side=LEFT, fill=Y)

f2 = Frame(root, bg="grey", borderwidth=9, relief=SUNKEN)
f2.pack(side=TOP, fill=X)

l = Label(f1, text="This is Frame tut", font="comicsansma 9 bold")
l.pack(pady=122, padx=10)

l = Label(f2, text="Welcome to the python GUI using TKinter", font="comicsansma 19 bold", fg="red")
l.pack(pady=20, padx=20)

root.mainloop()
