from tkinter import * #Tkinter lib take all * = all
import time
import pygame
import os
#package (lib)불러올땐 맨위에 작성
direc = './SoT_timers/'
NoTs = []
LoTs = []
count = 0
pygame.mixer.init()
alarm = pygame.mixer.Sound('./SAT_timer/alarm(wav).wav')
ui = Tk() # class  = book, we use ui variable to clarify 
ui.title("SAT_timer") # our ui's title = calculator
ui.resizable(True, True) # parameter = 2
ui.geometry("500x300")
ui.configure(background = 'gray')
#display = Entry(ui, width=28, justify='right')
#display.grid(row = 1, column = 0, columnspan = 4, pady=10, padx=4)
label = Label(ui, text = 'time left:')
label.grid(row = 0, column = 0)
def timer(NoS, description):
    for remaining in range(NoS, 0, -1):
        a = remaining-(3600*(remaining//3600))
        b = a//60
        c = remaining-(remaining//3600*3600)-(b*60)
        #display.delete(0, END)
        #display.insert(END, remaining//3600)
        #display.insert(END, ":")
        #display.insert(END, b)
        #display.insert(END, ":")
        #display.insert(END, c)
        timerLabelH = Label(ui, width = 20, height = 10, text = remaining//3600, font = ('comicsans', 20))
        timerLabelH.grid(row = 1, column = 0)
        timerLabelM = Label(ui, width = 20, height = 10, text = b, font = ('comicsans', 20))
        timerLabelM.grid(row = 1, column = 1)
        timerLabelS = Label(ui, width = 20, height = 10, text = c, font = ('comicsans', 20))
        timerLabelS.grid(row = 1, column = 2)
        print(remaining//3600, ':', b, ':', c)
        ui.update()
        time.sleep(1)
    Lodesc = description.split(' ')
    try:
        descLabel = Label(ui, width = 20, height = 10, text = Lodesc[0], font = ('comicsans', 20))
        descLabel.grid(row = 1, column = 0)
        descLabel = Label(ui, width = 20, height = 10, text = Lodesc[1], font = ('comicsans', 20))
        descLabel.grid(row = 1, column = 1)
        descLabel = Label(ui, width = 20, height = 10, text = Lodesc[2], font = ('comicsans', 20))
        descLabel.grid(row = 1, column = 2)
    except: 
        pass
    ui.update()
    print(description)
    alarm.play()
    time.sleep(5)

def SATtimer():
    tempL = []
    for each in NoTs:
        file = open(direc + each, 'r')
        timers = file.read().splitlines()
        print(timers)
        Timers = Label(ui, text = 'current timer:' + each)
        Timers.grid(row = 4, column = 0)
        for i in timers:
            a = list(i.split(':'))
            print(a)
            tempL.append(int(a[0])*3600)
            tempL.append(int(a[1])*60)
            tempL.append(int(a[2]))
            timer(sum(tempL), each + ' OVER')
            tempL = []
        os.remove(direc + each)

def setTimer():
    global screen1
    screen1 = Toplevel(ui)
    screen1.title("set_timer")
    screen1.geometry("500x300")
    AoT = StringVar()
    AoT2 = StringVar()
    global LoT
    LoT = Entry(screen1, textvariable = AoT)
    LoT.grid(row = 1, column = 0, pady = 3)
    global NoT
    NoT = Entry(screen1, textvariable = AoT2)
    NoT.grid(row = 1, column = 1, pady = 3)
    btn_add = Button(screen1, text = "add", width = 10, height = 1, command = add_timer)
    btn_add.grid(row = 6, column = 0, pady = 3)
    btn_delATime = Button(screen1, text = 'delete', width = 10, command = delT)
    btn_delATime.grid(row = 7, column = 0, pady = 3)
    instructions = Label(screen1, text = 'add the wanted amount of time on the left and the name right')
    instructions.grid(row = 8, column = 0)
    instructions2 = Label(screen1, text = 'Format: H:M:S')
    instructions2.grid(row = 9, column = 0)
    ui.mainloop()

def add_timer():
    Ts = LoT.get()
    Ts2 = NoT.get()
    file = open(direc + Ts2, "w") #[username_info].txt - > youngho.txt, file의 권한 = w -> Write
    file.write(Ts) #new line
    file.close()
    global NoTs
    NoTs.append(Ts2)
    global LoTs
    LoTs.append(Ts)
    print(NoTs, LoTs)
    N = Label(screen1, text = NoTs)
    T = Label(screen1, text = LoTs)
    N.grid(row = 10, column = 0)
    T.grid(row = 11, column = 0)

def delT():
    os.remove(direc + str(NoTs[-1]))
    NoTs.remove(NoTs[-1])
    LoTs.remove(LoTs[-1])
    deleted = Label(screen1, text = 'file successfully deleted!')
    deleted.grid(row = 12, column = 0)
    N = Label(screen1, text = NoTs)
    T = Label(screen1, text = LoTs)
    N.grid(row = 10, column = 0)
    T.grid(row = 11, column = 0)
btn_strtTimer = Button(ui, text = 'start timer', width = 10, command = SATtimer)
btn_strtTimer.grid(row = 2, column=0, pady = 3)
btn_addATime = Button(ui, text = 'add a timer', width = 10, command = setTimer)
btn_addATime.grid(row = 3, column = 0, pady = 3)
ui.mainloop()