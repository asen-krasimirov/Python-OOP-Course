from tkinter import *
from main import main


information = main()


def get_specs():
    button.grid_remove()
    info_label.grid(sticky='nw', column=0, row=8)


window = Tk()
window.title("PC Specs")
window.geometry('430x600')

# Creating a scrollbar
frame = Frame(window)
frame.pack(fill=BOTH, expand=1)

canvas = Canvas(frame)
canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Scrollbar
scrollbar = Scrollbar(frame, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

second_frame = Frame(canvas)

canvas.create_window((0, 0), window=second_frame, anchor='nw')


hardware_information_text = f""" Your PC specifications: 

Operating System: \n{information['OS']}

CPU(s): \n{information['CPU(s)']}

RAM: \n{information['RAM']}

Motherboard Model: \n{information['Motherboard Model']}

GPU(s): {information['GPU(s)']}

Storage Model(s): \n{information['Storage Model(s)']}

Total Storage Size: \n{information['Total Storage Size']}
"""

info_label = Label(second_frame, text=hardware_information_text, font=10)

label_hidden_3 = Label(second_frame, text='                                          ')

button = Button(second_frame, text="Show me my PC Specs", command=get_specs)
button.grid(column=2, row=2)

exit_button = Button(second_frame, text="Exit Application", command=exit)
exit_button.grid(column=10, row=10)


label_hidden_3.grid(column=0, row=2)

window.mainloop()
