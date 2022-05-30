
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
import time
import sys
import tkinter.font as tkFont



s = socket(AF_INET,SOCK_STREAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1) #`reuse addr ป้องกันerror address already in use

BUFFER_SIZE = 1024

s.bind(('127.0.0.1', 7017)) #การกำหนดค่าต่างๆที่จำเป้นให้กับ socket object
s.settimeout(30)
s.listen(1)

                       

end_game = False
player=2

count_high = False
count_low = False

stb = True
rounds = 1
sum_ans = 0

         
correct = False

def win(player):
    player = str(player)
    messagebox.showinfo(title="Congratulation server", message='Congratulation, the winner is player ' + player)
    hideme() 
    restart()


def draw():
    messagebox.showinfo(title="Draw server", message='Draw' )
    hideme() 
    restart()


def lost(player):
    player = str(player)
    messagebox.showinfo(title="Nice Try! server", message='You lost, see you again next time!')
    hideme() 
    restart()

def check():    
    global rounds
    global end_game
    global correct
    ans = str(sum_ans)
    global count_high
    global count_low
    #c.send(ans.encode())
    if(count_high == False and count_low == False):
        pass
    else:
        if(rounds <4):
            #check p1 is correct answer -> win(player)
            if sum_ans > 9:
                if(count_high == True):
                    
                    messagebox.showinfo(title="Congratulation server", message='correct! answer is '+ ans)
                    startgame()
                    correct = True
                    
                    count_high = False
                else:
                    count_low = False
                    send_ans("lost")
                    lost(player)
                    
            else:
                if(count_low == True):
                    messagebox.showinfo(title="Congratulation server", message='correct! answer is '+ ans)
                    startgame()
                    correct = True
                    count_low = False
                else:
                    count_high = False
                    send_ans("lost")
                    lost(player)
                    
                    
                    
        else:
            if sum_ans > 9:
                if(count_high == True):
                    send_ans("draw")
                    draw()
                    count_high = False
                else:
                    count_low = False
                    send_ans("lost")
                    lost(player)
                    
            else:
                if(count_low == True):
                    send_ans("draw")
                    draw()
                    count_low = False
                else:
                    count_high = False
                    send_ans("lost")
                    lost(player)
            
        
        
def startgame():
    global rounds
    if (rounds <= 3):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        dice3= random.randint(1,6)
        
        ans=[dice1, dice2 ,dice3]
        
        global sum_ans
        sum_ans=sum(ans)
        
        
        
        
        #mylabel.config(text = sum_ans)
        rnd = str(rounds)
        label_round.config(text = "ROUND : " + rnd)
    rounds+=1
    start_button.configure(state=DISABLED)
    hideme()    
    send_round("ROUND : " + rnd)
    time.sleep(0.5) ##### delay เพื่อไม่ให้ clientได้รับroundกับrandomพร้อมกัน 
    send_random(sum_ans)

    
def restart():
    global rounds
    global count_low
    global count_high
    rounds = 1
    rnd = str(rounds)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    label_round.config(text = "ROUND : " + rnd)
    count_high =False
    count_low =False
    count_low = False
    send_ans('restart')
    #startgame()
    start_button.configure(state=NORMAL)
    hideme()
    #s.close()
    #handle_client()
    
    
     
    
            
            
        #check p1 is uncorrect answer -> lost(player)
        #if rounds = 3 -> draw()
def handle(type): #####
    if(type == "lost"):
        win(player)
    #elif(type == 'draw'):
    #    draw() ##################################################""" 
    elif(type == 'correct'):
        showme()
    else:
        pass

def send_round(rou):
    rou = str(rou)
    print("send round :",rou)
    rou = rou.encode()
    conn.send(rou)
    
def send_random(guess):
    guess = str(guess)
    print("send guess number:",guess)
    guess = guess.encode()
    conn.send(guess)
    
def send_ans(output):
    output = str(output)
    output = output.encode()
    conn.send(output)
    
     
""" def receive_message(c):
    while True:
        p = c.recv(10) #ขนาดข้อมูล 10
        receive_ans(p) """
        
        
def receive_ans(output):
    output = output.decode()
    print("recieve : ",output)
    output = str(output)
    handle(output)

    
conn = None
def handle_client():
    global player
    global conn
    conn, ad = s.accept()
    while True:
        try:        
            print("player connected")
            p = conn.recv(10)
            receive_ans(p)
            #receive = Thread(target = receive_message, args = [conn,])
            #receive.start()
        except: 
            print("close socket & thread")
            conn.close
            break
    sys.exit()
    


handle_thread = Thread(target=handle_client)
handle_thread.start()



    

    


#def quit():
 #   s.close()
  #  wind.destroy()

# root window
root = tk.Tk()
#root.geometry('420x390')
root.geometry('600x600')
root.resizable(False, False)
root.title('HIGH-LOW server side')
root.configure(bg = "LightPink")

global my_label
global label_round

fontExample1 = tkFont.Font(family="Impact", size=15)

label_round = tk.Label(root, text = "ROUND:    ", bg = "Lightpink", font=(fontExample1))
label_round.pack(padx = 20, pady = 20)
label_round.place(relx = 1.0, rely = 0.0, anchor ='ne')


fontExample = tkFont.Font(family="Impact", size=23, weight="bold")


""" label = tkinter.Label(root, text = "\n  HIGH-LOW GAME! \n", font=(fontExample), 
            bg = "LightPink", fg = "deep pink").pack()
 """
label = tkinter.Label(root, text =( "\nPLAYER 2\n\n" ), font=(fontExample), 
            bg = "LightPink", fg = "black").pack()

    

#label_round = tk.Label(root, text = "Hello World", bg = "red")
#label_round.pack(padx = 5, pady = 10)
""" mylabel = tk.Label(root, text = "Hello World", bg = "red")
mylabel.pack(padx = 5, pady = 10) """



#mybutton = tk.Button(root, text = "Click Me", command = startgame)
#mybutton.pack(padx = 5, pady = 10)
#IMG
dicesImg = Image.open(r"dices1.png").resize((500, 500))

#img = PhotoImage(file="dices.png")      

#label_img = Label(root, image=img,bg = "LightPink")
#label_img.pack(padx=10,pady=10)
resize_image = dicesImg.resize((173, 144), Image.ANTIALIAS)
 
img = ImageTk.PhotoImage(resize_image)

label1 = Label(image=img, bg='Lightpink')
label1.image = img
label1.pack()


dicesImg = Image.open(r"name1.png").resize((500, 500))
resize_image = dicesImg.resize((360, 80), Image.ANTIALIAS)
 
img = ImageTk.PhotoImage(resize_image)

label1 = Label(image=img, bg='Lightpink')
label1.image = img
label1.pack()




#def เพื่อให้ปุ่มหาย
def hide_me(event):
    #event.widget.pack_forget()
    #event.config
    start_button.configure(state=DISABLED)

def showme():
    high_button.configure(state=NORMAL)
    low_button.configure(state=NORMAL)
def hideme():
    high_button.configure(state=DISABLED)
    low_button.configure(state=DISABLED)
    
# high button
high_button = ttk.Button(
    root,
    text='HIGH',
    command=lambda: High(),
    state=DISABLED
    
)

# low button
low_button = ttk.Button(
    root,
    text='LOW',
    command=lambda: Low(),
    state=DISABLED
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
    expand=True,


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
restart_button.place(x=262, y=533)

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





root.mainloop()






    

