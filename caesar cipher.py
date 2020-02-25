import tkinter as tk
from tkinter import messagebox
key = 'abcdefghijklmnopqrstuvwxyz'
offset = 4

def decrypt():
    result = ''
    for l in TE.get():
        try:
            i = (key.index(l) - offset) % 26
            result += key[i]
        except ValueError:
            result += l
    messagebox.showinfo('ถอดรหัสแล้ว',result)

def encrypt():
    result = ''
    for l in TE.get():
        try:
            i = (key.index(l) + offset) % 26
            result += key[i]
        except ValueError:
            result += l
    messagebox.showinfo('เข้ารหัสแล้ว',result)

root = tk.Tk()
root.geometry('800x600')
root.option_add("*Font","consolas 20")
w = tk.Label(root, text="การถอดรหัสแบบ Caesar Cipher")
w.pack()

alltank = tk.StringVar()
TE = tk.Entry(root,textvariable= alltank)
TE.pack()

BCal = tk.Button (root, text="ถอดรหัสข้อมูล" , command=decrypt)
BCal.pack()

BCal2 = tk.Button (root, text="ล้าง")
BCal2.pack()


root.mainloop()