import random

rolls = 1
for i in range(0, rolls):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice3= random.randint(1,6)
    a=[dice1, dice2 ,dice3]
    b=sum(a)
    
    print(a)
    print(b)
    
    if b <= 6:
        print("low")
    else:
        print("high")
