from socket import *
from tkinter import *
import tkinter
from tkinter import messagebox
from threading import Thread
import tkinter as tk
from tkinter import LEFT, RIGHT, ttk
from PIL import Image, ImageTk
import sys
import tkinter.font as tkFont

player = 1

count_high = False
count_low = False

rounds = 1
sum_ans = 3


def win(player):
    player = str(player)
    messagebox.showinfo(title="Congratulation client", message='Congratulation, the winner is player ' + player)
    restart()


def draw():
    messagebox.showinfo(title="Draw client", message='Draw' )
    restart()


def lost(player):
    player = str(player)
    messagebox.showinfo(title="Nice Try! client", message='You lost, see you again next time!' )
    restart()

#check p1 is uncorrect answer -> lost(player)
#if rounds = 3 -> draw()
def check(sum_ans):    
    global rounds
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
                    hideme()
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
                    hideme()
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
        

def handle(type):
    global rounds
    if(type == "lost"):
        win(player)
    elif(type == 'draw'):
        draw()
    elif(type == 'restart'):
        restart()
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
    showme()
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
    hideme()


s = socket(AF_INET,SOCK_STREAM)
BUFFER_SIZE = 1024

s.connect(('127.0.0.1', 7017))
#cมี server คนเดียวเลยไม่ต้องระบุ 
def receive_message():
    while True:
        p = s.recv(10)
        if p.decode() != "":
            apply(p)
        else:
            print("connection close")
            s.close()
            break
    print("close socket")
    sys.exit()


def send_ans(output):
    output = str(output)
    print("send :",output)
    output = output.encode()
    
    s.send(output)
        
def apply(input):
    input = input.decode()
    input = str(input)
    print("recieve :",input)
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


# root window
root = tk.Tk()
root.geometry('600x600')
root.resizable(False, False)
root.title('HIGH-LOW client side')
root.configure(bg = "LightPink")

global my_label
global label_round

fontExample1 = tkFont.Font(family="Impact", size=15)

label_round = tk.Label(root, text = "ROUND:    ", bg = "Lightpink", font=(fontExample1))
label_round.pack(padx = 20, pady = 20)
label_round.place(relx = 1.0, rely = 0.0, anchor ='ne')

fontExample = tkFont.Font(family="Impact", size=23, weight="bold")

label = tkinter.Label(root, text =( "\nPLAYER 1\n\n" ), font=(fontExample), 
            bg = "LightPink", fg = "black").pack()


#IMG dice
dicesImg = Image.open(r"dices1.png").resize((500, 500))
resize_image = dicesImg.resize((173, 144), Image.ANTIALIAS)
 
img = ImageTk.PhotoImage(resize_image)

label1 = Label(image=img, bg='Lightpink')
label1.image = img
label1.pack()

#IMG high low
dicesImg = Image.open(r"name1.png").resize((500, 500))

resize_image = dicesImg.resize((360, 80), Image.ANTIALIAS)
 
img = ImageTk.PhotoImage(resize_image)

label1 = Label(image=img, bg='Lightpink')
label1.image = img
label1.pack()

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


root.mainloop()
    