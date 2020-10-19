from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("400x300")
root.title("slider in tkinte")


def getdollars():
    print(f"we have credited {myslider1.get()} dollars to your bank account")
    tmsg.showinfo("Account credited!", f"we have credited {myslider1.get()} dollars to your bank account")


# myslider=Scale(root,from_=0,to=100)
# myslider.pack()
Label(root, text="How many dollars do you want?").pack()

myslider1 = Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=50)
# myslider1.set(10)
myslider1.pack()
Button(root, text="Get dollars", command=getdollars).pack(pady=20)

root.mainloop()
