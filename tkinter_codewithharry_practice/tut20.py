from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.title("radio button")
root.geometry("600x400")

def getorder():
    tmsg.showinfo("order received",f"we have received your order for {var.get()}. Thanks for ordering")


var = StringVar()
var.set("Radio")


Label(root, text="what would you like to have sir?", font="lucida 19 bold", justify=LEFT, pady=14).pack()

# here we can also use list
# list1 = ["Dosa", "Idly", "paratha", "samosa"]
# for i in range(len(list1)):
#     radio = Radiobutton(root, text=list1[i], padx=14, variable=var, value=i + 1).pack(anchor="w")

radio=Radiobutton(root,text="Dosa",padx=14,variable=var,value="Dosa").pack(anchor="w")
radio=Radiobutton(root,text="Idly",padx=14,variable=var,value="Idly").pack(anchor="w")
radio=Radiobutton(root,text="paratha",padx=14,variable=var,value="paratha").pack(anchor="w")
radio=Radiobutton(root,text="samosa",padx=14,variable=var,value="samosa").pack(anchor="w")

Button(root,text="get order",command=getorder).pack()
root.mainloop()
