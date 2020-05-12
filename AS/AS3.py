#random lib, while loop, for loop을 이용해서 유저와 input을 주고 받으며 자유로운 interaction 하나 만들기


import random
from random import sample

prompt = input("Do you want to start? [YES/NO]")
lotto = random.sample(range(1,47), 6)
#lotto = 1, 2,3,4,5,6
while prompt  == 'YES':
    for each in lotto:
        if each == 40:
            print("you win!")
        elif each == 46:
            print("you are second place!")
        elif each == 1:
            print("you lost")
        else:
            print("Bye")
        prompt = 'NO'