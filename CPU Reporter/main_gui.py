import main
from tkinter import *
import tkinter.font as font
# from tkinter.ttk import *
import time


def send_email_():
    generation_seconds = int((txt.get()))

    if selected.get() == 1:
        main.send_pdj_email(generation_seconds)
    elif selected.get() == 2:
        main.send_plaint_text_email(generation_seconds)
    lbl5.grid(column=1, row=8)


grid_height = 600
grid_width = 700


window = Tk()
window.geometry(f'{grid_width}x{grid_height}')
window.title("CPU Reporter")
sent = False

#button font
myFont = font.Font(size=20)

#labels
lbl = Label(window, text="        ", font=("Arial Bold", 50))
lbl2 = Label(window, text="         ", font=("Arial Bold", 50))
lbl3 = Label(window, text="Send CPU report via email.", font=("Arial Bold", 20))
lbl4 = Label(window, text="Enter duration of the report:", font=("Arial Bold", 15))
lbl5 = Label(window, text="Email Sent!", font=("Arial Bold", 15))

lbl.grid(column=0, row=0)
lbl2.grid(column=3, row=0)
lbl3.grid(column=1, row=0)
lbl4.grid(column=1, row=5)
if sent:
    lbl5.grid(column=1, row=6)

#entry for generation_seconds
txt = Entry(window,width=10)
txt.grid(column=1, row=6)
txt.focus()

#send button
send_button = Button(window, text='Send Email', command=send_email_)
send_button.grid(column=1, row=7)
#radio buttons
selected = IntVar()

rad1 = Radiobutton(window,text='Send Graph Report', value=1, variable=selected)
rad2 = Radiobutton(window,text='Send Text Report', value=2, variable=selected)
rad1['font'] = myFont
rad2['font'] = myFont
rad1.grid(column=1, row=1)
rad2.grid(column=1, row=2)

window.mainloop()
