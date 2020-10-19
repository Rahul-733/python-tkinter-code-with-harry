from tkinter import *
from PIL import  ImageTk, Image

def every_100(text):
    final_text = ""
    for i in range(0, len(text)):
        final_text +=text[i]
        if i%100==0 and i!=0:
            final_text += "\n"
    return final_text

root = Tk()
root.title("rocoderes News - Aapka Apna Akhabaar")
root.geometry("1000x1000")


textlist=[]
photolist=[]
for i in range(0,3):
    with open(f"{i + 1}.txt",encoding="utf8") as f:
        text = f.read()
        textlist.append(every_100(text))
    image = Image.open(f"{i + 1}.png")

    # Resize these images
    image = image.resize((225, 265), Image.ANTIALIAS)
    photolist.append(ImageTk.PhotoImage(image))

f0 = Frame(root, width=800, height=70)
Label(f0, text="Rocoderes News", font="lucida 33 bold").pack()
Label(f0, text="visit www.rocoderes.com", font="lucida 10 bold").pack()
Label(f0, text="January 19, 2050", font="lucida 13 bold").pack()
f0.pack()

f1 = Frame(root, width=900, height=200, pady=14)
Label(f1, text=textlist[0], padx=22, pady=22).pack(side="left")
Label(f1, image=photolist[0], anchor="e").pack()
f1.pack(anchor="w")


f2 = Frame(root, width=900, height=200, pady=14, padx=22)
Label(f2, text=textlist[1], padx=22, pady=22).pack(side="right")
Label(f2, image=photolist[1], anchor="e", padx=22).pack()
f2.pack(anchor="w")


f3 = Frame(root, width=900, height=200, pady=34)
Label(f3, text=textlist[2], padx=22, pady=22).pack(side="left")
Label(f3, image=photolist[2], anchor="e").pack()
f3.pack(anchor="w")


root.mainloop()