import tkinter as tk

def show_o():
    num = int(num_i.get())

    if num == 0:
        display.configure(text='Cannot 0')
        return

    output = ''
    for i in range(1,13):
        output += str(num) + ' x ' + str(i)
        output += ' = ' + str(num * i) + '\n'
    display.configure(text=output)

window = tk.Tk()
window.title('Multiplication Table')
window.minsize(width=400, height=500)

title_label = tk.Label(master=window, text='Multiple')
title_label.pack(pady=20)

num_i = tk.Entry(master=window)
num_i.pack(pady=10)

confirm_b = tk.Button(master=window, text='Enter', width=15, height=2, command=show_o)
confirm_b.pack()

display = tk.Label(master=window)
display.pack()

window.mainloop()