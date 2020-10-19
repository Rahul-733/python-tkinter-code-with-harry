# 500x400
# ready
from tkinter import *

root = Tk()
root.geometry("500x400")
root.title("Welcome")

label = Label(text="ready......", bg="red", fg="white", padx=10, pady=10)
label.pack(side=BOTTOM, fill=X)

root.mainloop()
