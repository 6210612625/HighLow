from socket import *
from tkinter import *
import tkinter
import random
from tkinter import messagebox
from threading import Thread
import tkinter as tk
from tkinter import LEFT, RIGHT, ttk
from turtle import left, right
from PIL import Image, ImageTk

end_game = False
player = 1

count_high = False
count_low = False

stb = True
rounds = 1
sum_ans = 0


def win(player):
    player = str(player)
    messagebox.showinfo(title="Congratulation client", message='Congratulation winner is ' + player)
    restart()


def draw():
    messagebox.showinfo(title="Draw", message='Draw' )
    restart()


def lost(player):
    player = str(player)
    global sum_ans
    ans = str(sum_ans)
    messagebox.showinfo(title="Nice Try! client", message='player '+player+' is lost, see you again next time!' + ans)
    restart()

def send_ans(output):
    output = str(output)
    print("send :",output)
    output = output.encode()
    
    s.send(output)
    
def check(sum_ans):    
    global rounds
    global end_game
    global correct
    global count_high
    global count_low
    sum_ans = int(sum_ans)
    ans = str(sum_ans)

    if(count_high == False and count_low == False):
        pass
    else:
        if(rounds <=3):
            #check p1 is correct answer -> win(player)
            if sum_ans > 9:
                if(count_high == True):
                    send_ans("correct")
                    messagebox.showinfo(title="Congratulation client", message='correct! answer is '+ ans)
                    
                    correct = True
                    count_high = False
                    
                else:
                    send_ans("lost")
                    lost(player)
                    count_low = False
            else:
                if(count_low == True):
                    send_ans("correct")
                    messagebox.showinfo(title="Congratulation client", message='correct! answer is '+ ans)
                    correct = True
                    count_low = False
                else:
                    send_ans("lost")
                    lost(player)  
                    count_high = False
        else:
            send_ans("draw")
            draw()
        #hideme()
        send_ans("correct")
        
        #check p1 is uncorrect answer -> lost(player)
        #if rounds = 3 -> draw()
def handle(type):
    global rounds
    if(type == "lost"):
        win(player)
    elif(type == 'draw'):
        draw()
    elif(type == 'ROUND : 1'):
        rounds = 1
        rnd = str(rounds)
        label_round.config(text = "ROUND : " + rnd)
    elif(type == 'ROUND : 2'):
        rounds = 2
        rnd = str(rounds)
        label_round.config(text = "ROUND : " + rnd)
    elif(type == 'ROUND : 3'):
        rounds = 3
        rnd = str(rounds)
        label_round.config(text = "ROUND : " + rnd)
    else:
        pass
    
def handle_ran(ans):
    global sum_ans
    ans = int(ans)
    sum_ans = ans
    #showme()
    check(sum_ans)
    
    
def restart():
    global rounds
    global count_low
    global count_high
    rounds = 1
    rnd = str(rounds)
    label_round.config(text = "ROUND : " + rnd)
    count_high =False
    count_low =False


s = socket(AF_INET,SOCK_STREAM)
BUFFER_SIZE = 1024

s.connect(('127.0.0.1', 7077))
#cมี server คนเดียวเลยไม่ต้องระบุ 
def receive_message():
    while True:
        p = s.recv(10)
        apply(p)
        
def apply(input):
    input = input.decode()
    input = str(input)
    incheck(input)
    
def incheck(inn):
    inn = str(inn)
    digi = inn.isdigit()
    
    if(digi ==  True):
        handle_ran(inn)
        
    else:
        handle(inn)


    

receive = Thread(target=receive_message)
receive.start()


#def quit():
 #   s.close()
  #  wind.destroy()

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

    

label_round = tk.Label(root, text = "ROUND : 0", bg = "red")
label_round.pack(padx = 5, pady = 10)
mylabel = tk.Label(root, text = "Hello World", bg = "red")
mylabel.pack(padx = 5, pady = 10)



#IMG
dicesImg = Image.open(r"dices.png").resize((100, 100))

img = PhotoImage(file="dices.png")      

label_img = Label(root, image=img,bg = "LightPink")
label_img.pack(padx=10,pady=10)

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
    #state=DISABLED
    
)

# low button
low_button = ttk.Button(
    root,
    text='LOW',
    command=lambda: Low(),
    #state=DISABLED
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
    global sum_ans
    global rounds
    check(sum_ans)


def Low():
    global count_low
    count_low = True
    global count_high
    count_high = False
    global sum_ans
    check(sum_ans)


""" def receive_ans(output):
    output = output.decode()
    output = int(output)
    handle(output)
    
def receive_ran(output):
    output = output.decode()
    output = str(output)
    handle_ran(output) """



root.mainloop()
    


    
    

