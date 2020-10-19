# 733*434
from tkinter import *

root = Tk()

# width x height
root.geometry("733x434")

# width,height
# root.minsize(300, 100)
root.minsize(733, 434)

# width,height
# root.maxsize(1200, 900)
root.maxsize(733, 434)

label = Label(text="welcome to pycharm")
label.pack()

root.mainloop()


