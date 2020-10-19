from tkinter import *

root = Tk()
root.geometry("600x300")
root.title("Menu And submenu")


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

root.mainloop()
