from itertools import count
import tkinter as tk
from tkinter import BOTTOM, CENTER, LEFT, RIGHT, Place, ttk
from turtle import left, right
from xml.etree.ElementTree import tostring
from PIL import Image, ImageTk

# root window
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('HIGH-LOW')


# high button
count_low = False
count_high = False

def High():
    global count_high
    count_high = True
    global count_low
    count_low = False


def Low():
    global count_low
    count_low = True
    global count_high
    count_high = False


high_button = ttk.Button(
    root,
    text='HIGH',
    command=lambda: High() 
)
high_button.pack(
    ipadx=5,
    ipady=5,
    side=LEFT,
    expand=True,
)

# low button
low_button = ttk.Button(
    root,
    text='LOW',
    command=lambda: Low()
)

# ขนาดของการแสดงปุ่ม
low_button.pack(
    ipadx=5,
    ipady=5,
    side=RIGHT,
    expand=True
)

reset_button = ttk.Button(
    root,
    text='RESET',
    command=lambda: Reset()
)

# ขนาดของการแสดงปุ่ม
reset_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

reset_button.place(x=110, y=130)

print(count_high)
root.mainloop()
print('2' , count_high)
'''
pImg = Image.open(r"S_48775216.jpg").resize((100, 100))
lImg = Image.open(r"year3-2.jpg").resize((100, 100))

buttonframe = tkinter.Frame(window, bg = "lemon chiffon") 
buttonframe.pack()

def High(high):
    global message
    message = high

    # client_socket.send(message.encode())  
    data = client_socket.recv(BUFFER_SIZE).decode()
    if(data > 9):
        print("YOU WIN")
        client_socket.close()
    else :
        print("YOU LOSE")  
        client_socket.close()

    tkinter.Label(window, text = data, bg = "lemon chiffon", font=("Arial", 10), fg = "firebrick1").pack()

def Low(low):
    global message
    message = low

    data = client_socket.recv(BUFFER_SIZE).decode()
    if(data <= 9):
        print("YOU WIN")
        client_socket.close()
    else :
        print("YOU LOSE")  
        client_socket.close()

    tkinter.Label(window, text = data, bg = "lemon chiffon", font=("Arial", 10), fg = "firebrick1").pack()
'''