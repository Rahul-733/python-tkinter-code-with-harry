from tkinter import *

root = Tk()

canvas_width = 800
canvas_height = 400
root.geometry(f"{canvas_width}x{canvas_height}")
canvas_widght = Canvas(root, width=canvas_width, height=canvas_height)
canvas_widght.pack()

# the line goes from the point x1,y1 to x2,y2
canvas_widght.create_line(0, 0, 800, 400,fill="red")
canvas_widght.create_line(800, 0, 0, 400,fill="red")

# to create a rectangle specify parameters in this order-coors of top left and coors of bottom right
canvas_widght.create_rectangle(3,5,700,300,fill="green")

canvas_widght.create_text(200,200,text="python GUI",fill="white")

canvas_widght.create_oval(344,233,244,355,fill="blue")
root.mainloop()
