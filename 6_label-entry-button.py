import tkinter as tk
window = tk.Tk()

def sendMessage():
    text1 = iName.get()
    text2 = iLName.get()
    text3 = iTel.get()
    text = text1 + " " + text2 + " " + text3
    oName.configure(text=text)

window.title("Hello World")
window.minsize(width=160, height=90)

oName = tk.Label(master=window, text="Name")
oName.pack()
iName = tk.Entry(master=window)
iName.pack()

oLName = tk.Label(master=window, text="Last Name")
oLName.pack()
iLName = tk.Entry(master=window)
iLName.pack()

oTel = tk.Label(master=window, text="Tel")
oTel.pack()
iTel = tk.Entry(master=window)
iTel.pack()
bConfirm = tk.Button(master=window, text="Confirm", command=sendMessage)
bConfirm.pack()

window.mainloop()