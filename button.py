import tkinter as tk
from tkinter import LEFT, RIGHT, ttk
from turtle import left, right
from PIL import Image, ImageTk

# root window
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('HIGH-LOW')


# high button
high_button = ttk.Button(
    root,
    text='HIGH',
    command=lambda: root.High()
    
)

# low button
low_button = ttk.Button(
    root,
    text='LOW',
    command=lambda: root.High()
)

# ขนาดของการแสดงปุ่ม
high_button.pack(
    ipadx=5,
    ipady=5,
    side=LEFT,
    expand=True,
    
)

low_button.pack(
    ipadx=5,
    ipady=5,
    side=RIGHT,
    expand=True
)
root.mainloop()

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