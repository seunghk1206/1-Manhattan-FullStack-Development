import os
import mouse
import time
import keyboard
from os import listdir
import pyautogui
run = True
count = 0
pyautogui.FAILSAFE = False
while run:
    FI = str(input('record = 0(note: press esc to stop the recording) run = 1 exit = 2 '))
    if FI == '0':
        runCoordinates = True
        try:
            if not(os.path.isdir("macro folder")):
                os.makedirs(os.path.join('macroFolder'))
        except:
            pass
        path = './macroFolder'
        file = open('./macroFolder/macrofile_' + str(len(listdir(path))) + '.txt', "w")
        while runCoordinates:
            
            if mouse.is_pressed('right') == True:
                file.write(str(mouse.get_position()))
                file.write('PR' + '\n')
            elif mouse.is_pressed('left') == True:
                file.write(str(mouse.get_position()))
                file.write('PL' + '\n')
            else:
                file.write(str(mouse.get_position())+'\n')
            time.sleep(0.1)
            if keyboard.is_pressed('Esc'):
                file.close()
                runCoordinates = False
    elif FI == '1':
        print(listdir('./macroFolder'))
        inp = int(input('for which macrofile would you like to play? '))
        File = open('./macroFolder/'+ listdir('./macroFolder')[inp], 'r')
        LoCoor = File.read().split('\n')
        tempL = []
        clicksIndices = []
        recursion = int(input('how many times would you like to play? '))
        for each in range(len(LoCoor)):
            try:
                if 'PR' in LoCoor[each]:
                    tempL.append([int(LoCoor[each].split(',')[0][1::]), int(LoCoor[each].split(',')[1][0:-3:])])
                    clicksIndices.append([each,1])
                elif 'PL' in LoCoor[each]:
                    tempL.append([int(LoCoor[each].split(',')[0][1::]), int(LoCoor[each].split(',')[1][0:-3:])])
                    clicksIndices.append([each,0])#0 = L 1 = R
                else:
                    tempL.append([int(LoCoor[each].split(',')[0][1::]), int(LoCoor[each].split(',')[1][0:-1:])])
            except:
                #if LoCoor[each] == '':
                    #tempL.append()
                #else:
                pass
        for _ in range(recursion):
            n = 0
            for each in range(len(tempL)):
                if n != len(clicksIndices)-1:
                    if clicksIndices[n][0] == each:
                        pyautogui.move(tempL[each][0], tempL[each][1], 0.05)
                        if clicksIndices[n][1] == 1:
                            pyautogui.click(tempL[each][0], tempL[each][1], button = 'right', clicks = 1)
                        elif clicksIndices[n][1] == 0:
                            pyautogui.click(tempL[each][0], tempL[each][1], button = 'left', clicks = 1)
                        n += 1
                    else:
                        pyautogui.move(tempL[each][0], tempL[each][1], 0.05)
                else:
                    pyautogui.move(tempL[each][0], tempL[each][1], 0.05)
    elif FI == '2':
        run = False
#DataPaper = open("", "r", encoding = "utf8")