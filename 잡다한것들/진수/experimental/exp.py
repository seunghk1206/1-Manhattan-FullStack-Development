import string
import itertools
import keyboard
import pyautogui
import mouse
a = [str(each) for each in range(10)]
for each in itertools.chain([string.ascii_lowercase]):
    for eachLetter in each:
        a.append(eachLetter)
a.append('#')
a.append('@')
print(len(a))
print(0.1*0.1)
print(format(10000, '#b'))
print('0'*10)
run = True
while run:
    print(mouse.get_position(), mouse.is_pressed('left'))