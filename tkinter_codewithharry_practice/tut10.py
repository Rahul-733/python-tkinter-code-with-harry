from tkinter import *

root = Tk()
root.title("tut10-Entry&grid")
root.geometry("600x300")


def getvalue():
    print(f'username is: {uservalue.get()}')
    print(f'password is: {passvalue.get()}')


user = Label(root, text="Username: ")
password = Label(root, text="password: ")
# here grid(row=0,col=0)  by default but you can change the value of grid
user.grid()
password.grid(row=1)
# varibles are:
# Booleanvar Doublevar,Intvar,Stringvar

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable=uservalue)
passentry = Entry(root, textvariable=passvalue)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

Button(text="submit", command=getvalue).grid()
root.mainloop()

