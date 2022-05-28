
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
from PIL import Image, ImageTk




s = socket(AF_INET,SOCK_STREAM)
BUFFER_SIZE = 1024

s.bind(('127.0.0.1', 7077)) #การกำหนดค่าต่างๆที่จำเป้นให้กับ socket object
s.listen(5)



end_game = False
player=1

count_high = False
count_low = False

stb = True
rounds = 0
sum_ans = 0

         
correct = False

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
    global correct
    ans = str(sum_ans)
    #c.send(ans.encode())
    if(count_high == False and count_low == False):
        pass
    else:
        if(rounds <=3):
            #check p1 is correct answer -> win(player)
            if sum_ans > 9:
                if(count_high == True):
                    
                    messagebox.showinfo(title="Congratulation", message='correct! answer is '+ ans)
                    startgame()
                    correct = True
                else:
                    #send_ans("lost")
                    lost(player)
                    
                    
                    
            else:
                if(count_low == True):
                    messagebox.showinfo(title="Congratulation", message='correct! answer is '+ ans)
                    startgame()
                    correct = True
                else:
                    #send_ans("lost")
                    lost(player)
                    
                    
        else:
            #send_ans("draw")
            draw()
        
        
            
    
            
            
        #check p1 is uncorrect answer -> lost(player)
        #if rounds = 3 -> draw()
def handle(type):
    if(type == "lost"):
        win(player)
    elif(type == 'draw'):
        draw()
    else:
        pass
    
""" def send_random(guess):
    guess = str(guess)
    guess = guess.encode()
    conn.send(guess)
    
def send_ans(output):
    output = str(output)
    output = output.encode()
    conn.send(output)
    
     
def receive_message(c):
    while True:
        p = c.recv(10) #ขนาดข้อมูล 10
        receive_ans(p)
        
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
    receive = Thread(target = receive_message, args = [conn,])
    receive.start()
    


acc = Thread(target=handle_client)
acc.start() """


def startgame():
    global rounds
    if (rounds <= 3):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        dice3= random.randint(1,6)
        
        ans=[dice1, dice2 ,dice3]
        
        global sum_ans
        sum_ans=sum(ans)
        
        
        
        rounds+=1
        mylabel.config(text = sum_ans)
        rnd = str(rounds)
        label_round.config(text = "ROUND : " + rnd)
    start_button.configure(state=DISABLED)
    

    


#def quit():
 #   s.close()
  #  wind.destroy()

# root window
root = tk.Tk()
#root.geometry('420x390')
root.geometry('1000x1000')
root.resizable(False, False)
root.title('HIGH-LOW')
root.configure(bg = "LightPink")

global my_label
global label_round
label = tkinter.Label(root, text = "\n\n  HIGH-LOW GAME! \n\n", font=("Arial", 20), 
            bg = "LightPink", fg = "deep pink").pack()

label = tkinter.Label(root, text =( "hi" ), font=("Arial", 20), 
            bg = "LightPink", fg = "deep pink").pack()

    

label_round = tk.Label(root, text = "Hello World", bg = "red")
label_round.pack(padx = 5, pady = 10)
mylabel = tk.Label(root, text = "Hello World", bg = "red")
mylabel.pack(padx = 5, pady = 10)


mybutton = tk.Button(root, text = "Click Me", command = startgame)
mybutton.pack(padx = 5, pady = 10)
#IMG
dicesImg = Image.open(r"dices.png").resize((100, 100))

img = PhotoImage(file="dices.png")      

label_img = Label(root, image=img,bg = "LightPink")
label_img.pack(padx=10,pady=10)

#def เพื่อให้ปุ่มหาย
def hide_me(event):
    #event.widget.pack_forget()
    #event.config
    start_button.configure(state=DISABLED)
    
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
start_button = ttk.Button(
    root,
    text='START',
    command=lambda: startgame()
    
)

start_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
    
)

restart_button = ttk.Button(
    root,
    text='RESTART',
    command=lambda: restart()
)
# ขนาดของการแสดงปุ่ม
restart_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)
restart_button.place(x=110, y=130)

def High():
    global count_high
    count_high = True
    global count_low
    count_low = False
    check()


def Low():
    global count_low
    count_low = True
    global count_high
    count_high = False
    check()

def restart():
    global rounds
    global count_low
    global count_high
    rounds = 0
    count_high =False
    count_low =False
    startgame()
    #s.close()
    #handle_client()



root.mainloop()






    

