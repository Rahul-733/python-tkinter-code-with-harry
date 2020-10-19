from tkinter import *

root = Tk()
root.geometry("1000x500")
photo = PhotoImage(file="1.png")

label = Label(image=photo)
label.pack()

root.mainloop()


