from tkinter import *

def click_btn_function(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                value = "Error"

        scvalue.set(value)
        screen.update()

    elif text == "CE":
        scvalue.set("")
        screen.update()
    elif text=="<--":
        ex = scvalue.get()
        # print(ex)
        ex = ex[0:len(ex) - 1]
        print(f"ex is{ex}")
        scvalue.set(ex)
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()
# root.geometry("840x600")
root.resizable(width=False, height=False)
root.title("Calculator")
root.configure(background="#223A4A")
font = ('Verdana', 20, 'bold')
scvalue = StringVar()
scvalue.set("")

screen = Entry(root, textvar=scvalue, font="lucida 30 bold", bg="#223A4A", fg="white")
screen.pack(fill=X, ipadx=8, ipady=20)
# buttonlist = ['7', '8', '9', 'X','6','5']
ArithmeticOp = ['X', '+', '-', '/', '=']
buttonFrame = Frame(root)
buttonFrame.pack(side=TOP)

perbtn = Button(buttonFrame, text="%", font=font, width=5, relief='ridge', activebackground='orange',
                activeforeground='white', bg="#070B0F", fg="white")
perbtn.grid(row=0, column=0)

allclearbtn = Button(buttonFrame, text="CE", font=font, width=5, relief='ridge', activebackground='orange',
                     activeforeground='white', bg="#070B0F", fg="white")
allclearbtn.grid(row=0, column=1)

clearbtn = Button(buttonFrame, text="<--", font=font, width=5, relief='ridge', activebackground='orange',
                  activeforeground='white', bg="#070B0F", fg="white")
clearbtn.grid(row=0, column=2)

# adding button
temp = 1
for i in range(1, 4):
    for j in range(0, 3):
        btn = Button(buttonFrame, text=str(temp), font=font, width=5, relief='ridge', activebackground='orange',
                     activeforeground='white', bg="#070B0F", fg="white")
        btn.grid(row=i, column=j)
        btn.bind('<Button-1>', click_btn_function)
        temp = temp + 1


DoublezeroBtn = Button(buttonFrame, text='00', font=font, width=5, relief='ridge', activebackground='orange',
                       activeforeground='white', bg="#070B0F", fg="white")
DoublezeroBtn.grid(row=4, column=0)

zeroBtn = Button(buttonFrame, text='0', font=font, width=5, relief='ridge', activebackground='orange',
                 activeforeground='white', bg="#070B0F", fg="white")
zeroBtn.grid(row=4, column=1)

DotBtn = Button(buttonFrame, text='.', font=font, width=5, relief='ridge', activebackground='orange',
                activeforeground='white', bg="#070B0F", fg="white")
DotBtn.grid(row=4, column=2)

# Arithmetic operator buttons
i = 0
j = 3
while i < 3:
    for op in ArithmeticOp:
        btn = Button(buttonFrame, text=str(op), font=font, width=5, relief='ridge', activebackground='orange',
                     activeforeground='white', bg="#070B0F", fg="white")
        btn.grid(row=i, column=j)
        btn.bind('<Button-1>', click_btn_function)
        i = i + 1


# binding all btns
DoublezeroBtn.bind('<Button-1>', click_btn_function)
zeroBtn.bind('<Button-1>', click_btn_function)
DotBtn.bind('<Button-1>', click_btn_function)
perbtn.bind('<Button-1>', click_btn_function)
allclearbtn.bind('<Button-1>', click_btn_function)
clearbtn.bind('<Button-1>', click_btn_function)

root.mainloop()
