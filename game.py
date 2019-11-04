#!/usr/bin/env python
# coding: utf-8

# In[1]:


class person:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amt):
        self.balance+=amt
    def withdraw(self,amt):
        if amt>self.balance:
            return -1
        else:
            self.balance-=amt
            return amt
    def __str__(self):
        return f"hello {self.name}, you have an amount of {self.balance} to bet from"


# In[2]:


import random
class deck:
    face=['spade','club','heart','diamond']
    rank=['two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace']
    values={'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'jack':10,'queen':10,'king':10,'ace':11}
    cards=[]
    for i in range(0,4):
        f1=face[i]
        for j in range(0,13):
            r1=rank[j]
            cards.append(r1+'-of-'+f1)
    def shf(self):  # shuffles the deck of cards
        cards=[random.shuffle(self.cards)]
    def asg(self):  # returns a random card
        return self.cards.pop()


# In[3]:


name=input('hello player, please enter your name: ')
bal=0
while bal<=0:
    bal=float(input('please enter the balance (must be >0): '))
p1=person(name,bal)
status='y'
win=lose=bust=0
total=21
while status =='y':
    d1=deck()
    print(p1)
    stop=False
    bet=int(input('how much amount do you wanna bet ??'))
    bet=p1.withdraw(bet)
    while bet==-1:
        bet=int(input('insufficient balance !!! enter again: '))
        bet=p1.withdraw(bet)
    #two lists to store the cards of dealer and player
    dealer=[]
    player=[]
    d=p=0 # indices for dealer and player list
    d1.shf()  # shuffling the deck of cards
    # now assigning 2 cards to dealer and player each
    dealer.append(d1.asg())
    dealer.append(d1.asg())
    player.append(d1.asg())
    player.append(d1.asg())
    dsum=psum=0 #sum of cards of dealer and player
    print("player's turn: ")
    temp=player[p]
    p+=1
    temp=temp.split('-')
    temp=temp[0]
    temp=d1.values[temp]
    psum+=temp
    temp=player[p]
    p+=1
    temp=temp.split('-')
    temp=temp[0]
    if temp=='ace' and sum>=11:
        temp=1
    else:
        temp=d1.values[temp]
    psum+=temp
    print('player has: '+player[0]+' and '+player[1])
    print(f"the value of player's card is {psum}")
    if psum ==21:
        stop=True # stop is stopping the execution of dealer's play
        win+=1
        print(f"{name} wins !!!")
        p1.deposit(2*bet)  # if player wins, then his money is doubled
    else:
        print ('dealer has: '+dealer[0]+' and one hidden card')
        action=input('hey player, press h to hit or s to stand: ')  #it defines the action of the player, either hit or stand
        while action =='h':
            d1.shf()
            player.append(d1.asg())
            print('player has: '+player[p])
            temp=player[p]
            p+=1
            temp=temp.split('-')
            temp=temp[0]
            if temp=='ace' and psum>=11:
                temp=1
            else:
                temp=d1.values[temp]
            psum+=temp
            if psum>21:
                bust+=1
                stop=True
                print(f"the value of player's card is {psum}")
                print(f"{name} is busted !!!")
                break
            elif psum == 21:
                win+=1
                stop=True
                print(f"the value of player's card is {psum}")
                print(f"{name} is wins !!!")
                p1.deposit(2*bet)  # if player wins, then his money is doubled
                break
            else:
                print(f"the value of player's card is {psum}")
                print ('dealer has: '+dealer[0]+' and one hidden card')
                action=input('hey player, press h to hit or s to stand: ')
        if not stop:
            print("dealer's turn: ")
            temp=dealer[d]
            d+=1
            temp=temp.split('-')
            temp=temp[0]
            temp=d1.values[temp]
            dsum+=temp
            temp=dealer[d]
            d+=1
            temp=temp.split('-')
            temp=temp[0]
            if temp=='ace' and dsum>=11:
                temp=1
            else:
                temp=d1.values[temp]
            dsum+=temp
            print ('dealer had: '+dealer[0]+' and '+dealer[1])
            print(f"the value of dealer's card is {dsum}")
            if dsum ==21:
                lose+=1
                print(f"dealer wins !!!")
            elif dsum>psum and dsum>=17:
                lose+=1
                print(f"dealer wins !!!")
            elif dsum<=psum and dsum>=17:
                win+=1
                print(f"{name} wins")
                p1.deposit(2*bet)  # if player wins, then his money is doubled
            else:
                while dsum < 17:
                    d1.shf()
                    dealer.append(d1.asg())
                    print('dealer has: '+dealer[d])
                    temp=dealer[d]
                    d+=1
                    temp=temp.split('-')
                    temp=temp[0]
                    if temp=='ace' and dsum>=11:
                        temp=1
                    else:
                        temp=d1.values[temp]
                    dsum+=temp
                    if dsum>21:
                        win+=1
                        print(f"the value of dealer's card is {dsum}")
                        print(f"dealer is busted !!!")
                        p1.deposit(2*bet)  # if player wins, then his money is doubled
                        break
                    elif dsum == 21:
                        lose+=1
                        print(f"the value of dealer's card is {dsum}")
                        print(f"dealer wins !!!")
                        break
                    elif dsum<21 and dsum>psum:
                        lose+=1
                        print(f"the value of dealer's card is {dsum} which is more than player's {psum}")
                        print(f"dealer wins !!!")
                        break
                    elif dsum<21 and dsum>17 and dsum<=psum:
                        win+=1
                        print(f"the value of dealer's card is {dsum} which is less than or equal to player's {psum}")
                        print(f"player wins !!!")
                        p1.deposit(2*bet)  # if player wins, then his money is doubled
                        break
                    else:
                        print(f"the value of dealer's card is {dsum}")
    print('summary: ')
    print(f"wins: {win}, loss: {lose}, bust: {bust}")
    status=input('do you wanna play again ?? prss y to continue or n to stop :')


# In[ ]:





# In[ ]:




