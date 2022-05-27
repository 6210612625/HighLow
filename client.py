
import socket
from tkinter import *
import tkinter
import random
from tkinter import messagebox
from socket import *
from threading import Thread
import tkinter as tk
from tkinter import LEFT, RIGHT, ttk
from turtle import left, right




s = socket(AF_INET,SOCK_STREAM)
BUFFER_SIZE = 1024

s.connect(('127.0.0.1', 7077))

rounds = 1
end_game = False
player=2

count_high = False
count_low = False
sum_ans = 0



def win(player):
    messagebox.showinfo(title="Congratulation", message='Congratulation winner is ' + player)
    restart()


def draw():
    messagebox.showinfo(title="Draw", message='Draw' )
    restart()


def lost(player):
    messagebox.showinfo(title="Nice Try!", message='player '+player+' is lost, see you again next time!')
    restart()

def check():    
    global rounds
    global end_game
    if(rounds <=3):
        #check p1 is correct answer -> win(player)
        if sum_ans > 9:
            if(count_high == True):
                rounds+=1
            else:
                send_ans("lost")
                lost(player)
                
        else:
            if(count_low == True):
                rounds+=1
            else:
                send_ans("lost")
                lost(player)
                
    else:
        send_ans("draw")
        draw()
        
    
            
            
        #check p1 is uncorrect answer -> lost(player)
        #if rounds = 3 -> draw()
def handle(type):

    if(type == "lost"):
        win(player)
    else:
        draw()
def handle_ran(ans):
    global sum_ans
    sum_ans = ans
    check()
    
    
def restart():
    global rounds
    rounds = 1


#def quit():
 #   s.close()
  #  wind.destroy()

# root window
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('HIGH-LOW')


# high button

high_button = ttk.Button(
    root,
    text='HIGH',
    command=lambda: High()
    
)

# low button
low_button = ttk.Button(
    root,
    text='LOW',
    command=lambda: Low()
)

# setting botton
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

root.mainloop()

    
def send_ans(output):
    output = str(output)
    output = output.encode()
    s.send(output)

def receive_ans(output):
    output = output.decode()
    output = str(output)
    handle(output)
    
def receive_ran(output):
    output = output.decode()
    output = str(output)
    handle_ran(output)
    


    

receive = Thread(target=receive_ans)
receive.start()


    


    
    

