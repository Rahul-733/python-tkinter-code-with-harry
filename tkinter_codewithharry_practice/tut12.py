from tkinter import *

root = Tk()


def getvalue():
    with open("txt_tut12.txt", 'a',encoding="utf8") as f:
        f.write(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emengercyvalue.get(), paymntvalue.get(), foodservicevalue.get()}\n ")
    # print(f'username is: {namevalue.get()}')
    # print(f'phone is: {phonevalue.get()}')
    # print(f'gender is: {gendervalue.get()}')
    # print(f'emengercy is: {emengercyvalue.get()}')
    # print(f'paymnt is: {paymntvalue.get()}')
    # print("----------------------------------------")


    print("done")


root.title("tut11")
root.geometry("644x344")
# root.minsize(644, 344)
# root.maxsize(644, 344)
#

Label(root, text="Welcome to rocoderes", font="comicsansms 13 bold", pady=15).grid(row=0, column=3)

name = Label(root, text="name")
phone = Label(root, text="phone")
gender = Label(root, text="gender")
emengercy = Label(root, text="Emergency Contact")
paymnt = Label(root, text="payment mode")

name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emengercy.grid(row=4, column=2)
paymnt.grid(row=5, column=2)

namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emengercyvalue = StringVar()
paymntvalue = StringVar()
foodservicevalue = IntVar()

nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emengercyentry = Entry(root, textvariable=emengercyvalue)
paymntentry = Entry(root, textvariable=paymntvalue)

nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emengercyentry.grid(row=4, column=3)
paymntentry.grid(row=5, column=3)

foodservice = Checkbutton(text="Want to prebook your meals?", variable=foodservicevalue, pady=10)
foodservice.grid(row=6, column=3)
Button(text="Submit to rocoderes", command=getvalue).grid(row=7, column=3)

label1 = Label(text="visit www.rocoderes.com", padx=10, pady=10)
label1.grid(row=10, column=3)
root.mainloop()
