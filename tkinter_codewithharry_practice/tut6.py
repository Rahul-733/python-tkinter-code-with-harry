from tkinter import *

root = Tk()
root.geometry("700x500")
root.title("Welcome")

# important label operations
# text=add the text
# bg=background
# fg=foreground
# font=sets the font
# padx=x padding
# pady=y padding
# relief=border styling__SUNKEn,RAISED,GROOVE,RIDGE

label = Label(text='''Hello friends this tkinter tutroial.Anthem’s vast, ever-changing world features unpredictable.welcome
                conditions, hazards, and enemies. Over time, Anthem will develop and expand – introducing unique
                stories, challenges, and world-shaking events.Hello friends this tkinter tutroial.so enjoy this tutorial'''
              , bg="red", fg="white", padx=13, pady=50, font="comicsansma 9 bold", borderwidth=3, relief=SUNKEN)
# important pack function
#   N
# W   E
#   S
# anchor-sw,se
# side-top,left,bootom,right
# fill
# padx
# pady


label.pack(side="top", anchor="sw", fill=X, padx=15, pady=20)
# label.pack(side=left,fill=Y)

root.mainloop()

