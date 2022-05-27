
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

s.bind(('127.0.0.1', 7077)) #การกำหนดค่าต่างๆที่จำเป้นให้กับ socket object
s.listen(5)

rounds = 1
end_game = False
player=1

count_high = False
count_low = False




def win(player):
    messagebox.showinfo(title="Congratulation", message='Congratulation winner is ' + player)
    restart()


def draw():
    messagebox.showinfo(title="Draw", message='Draw' )
    restart()


def lost(player):
    messagebox.showinfo(title="Nice Try!", message='You lost, see you again next time!')
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
    
def restart():
    global rounds
    rounds = 1
    s.close()
    handle_client()

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


def send_random(guess):
    guess = int(guess)
    guess = guess.encode()
    conn.send(guess)
    
def send_ans(output):
    output = str(output)
    output = output.encode()
    conn.send(output)

def receive_ans(output):
    output = output.decode()
    output = str(output)
    handle(output)
    
conn = None
def handle_client():
    global player
    global conn
    player = 1
    conn, ad = s.accept()
    receive = Thread(target = receive_ans, args = [conn,])
    receive.start()
    


acc = Thread(target=handle_client)
acc.start()


    

while True:
    if (rounds < 3):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        dice3= random.randint(1,6)
        
        ans=[dice1, dice2 ,dice3]
        
        global sum_ans
        sum_ans=sum(ans)
        send_random(sum_ans)
        
        rounds+=1
        
    check()
    

