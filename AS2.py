#loop = 무언가를 반복하는것. 

#list 리스트


#for loop -> 제한된 범위 안에서 반복 -> 처음부터 range를 정해야함
#while loop -> 무한한 범위 안에서 반복  -> 나중에 loop을 나가는데 쓰임

#list's index    


#1번째 바퀴에서는 eachName = 승현
#2번째 바퀴에서는 eachName = 영호
#3번째 바퀴에서는 eachName = 철수
#4번째 바퀴에서는 eachName = 짱구 


#[승현, 영호, 철수, 짱구]
#   0    1    2    3
listA = [1,2,3,4,5,6,7,8,9] #대괄호 안에 컴마로 이어주는 숫자들, 길이는 9
listB = ['승현', '영호', '철수', '짱구'] #길이는 4


for eachNumber in listA: #얘는 eachNumber에다가 listA가 가지고 있는 각각의 숫자를 넣는거야
   print(listA)

for each in range(1,10): # 1 ~ 10까지가 아니라 1~9까지야  1부터 10 미만
    print("FFF")
    

for each in range(len(listA)): # len =  > length
    print('is it 9?')

import random #random lib 가져와라
from random import sample #sample 이미 랜덤의 값을 정하는 알고리즘 (수학적 공식)

lotto = random.sample(range(1,47),6) #1~46까지의 범위중에서 6개를 뽑아라 랜덤으로.

print("로또 번호 입니다: ", lotto)
    
# inputX = input("Do you want to see the result? [Y/N] ")

# while inputX == 'Y':# 만약 ~ 일때 반복해!
#     #if, for, while , elif 등등 에서는 equal sign 항상 == 이렇게 두개로 쓴다.
#     print(listA)
#     inputX = 'x' #loop 을 나가려고 할 때
    