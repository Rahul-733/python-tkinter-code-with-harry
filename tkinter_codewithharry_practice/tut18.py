from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("600x300")
root.title("Message box")


def filefunc():
    print("File menu is work...")


def newprojectfunc():
    print("projet work...")


def savefunc():
    print("save work....")


def saveasfunc():
    print("save as work........")


def printfunc():
    print("print work.....")


def help1():
    print("help work...")
    tmsg.showinfo("Help","visit www.rocoderes.com")

def rate():
    value=tmsg.askquestion("was your Experience good?","You used thi gui ...was your Experience good?")
    if value=="yes":
        msg="gerat please visit our website www.rocoderes.com"
    else:
        msg="Tell us what want wrong."
    tmsg.showinfo("Experience",msg)


# only  main menu means single menu
# mymenu = Menu(root)
# mymenu.add_command(label="File", command=filefunc)
# mymenu.add_command(label="Exit", command=quit)
# root.config(menu=mymenu)


# main menu with submenu
mainmenu = Menu(root)

m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="New project", command=newprojectfunc)
m1.add_command(label="Save", command=savefunc)
m1.add_separator()
m1.add_command(label="Save As", command=saveasfunc)
m1.add_command(label="Print", command=printfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=m1)

m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Cut", command=newprojectfunc)
m2.add_command(label="Copy", command=savefunc)
m2.add_separator()
m2.add_command(label="Paste", command=saveasfunc)
m2.add_command(label="Find", command=printfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit", menu=m2)

m3 = Menu(mainmenu, tearoff=0)
m3.add_command(label="help", command=help1)
m3.add_command(label="rate us", command=rate)

root.config(menu=mainmenu)
mainmenu.add_cascade(label="Help", menu=m3)

root.mainloop()
