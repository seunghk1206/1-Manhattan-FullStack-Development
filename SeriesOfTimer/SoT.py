from tkinter import * #Tkinter lib take all * = all
import time
import pygame
#package (lib)불러올땐 맨위에 작성
count = 0
pygame.mixer.init()
alarm = pygame.mixer.Sound('./SAT_timer/alarm(wav).wav')
ui = Tk() # class  = book, we use ui variable to clarify 
ui.title("SAT_timer") # our ui's title = calculator
ui.resizable(False, False) # parameter = 2
ui.geometry("500x300")
ui.configure(background = 'blue')
display = Entry(ui, width=28, justify='right')
display.grid(row = 1, column = 0, columnspan = 4, pady=10, padx=4)
label = Label(ui, text = 'time left:')
label.grid(row = 0, column = 0)
def timer(NoS, description):
    for remaining in range(NoS, 0, -1):
        a = remaining-(3600*(remaining//3600))
        b = a//60
        c = remaining-(remaining//3600*3600)-(b*60)
        display.delete(0, END)
        display.insert(END, remaining//3600)
        display.insert(END, ":")
        display.insert(END, b)
        display.insert(END, ":")
        display.insert(END, c)
        print(remaining//3600, ':', b, ':', c)
        ui.update()
        time.sleep(1)
    display.delete(0, END)
    display.insert(0, description)
    ui.update()
    print(description)
    alarm.play()
    time.sleep(5)
def SATtimer():
    tempL = []
    file = open('timerList', 'r')
    timers = file.read().splitlines()
    print(timers)
    timers.remove(timers[0])
    for each in timers:
        a = list(each.split(':'))
        print(a)
        tempL.append(int(a[0])*3600)
        tempL.append(int(a[1])*60)
        tempL.append(int(a[2]))
        timer(sum(tempL), 'TIME OVER')
        tempL = []

def setTimer():
    global screen1
    screen1 = Toplevel(ui)
    screen1.title("set_timer")
    screen1.geometry("500x300")
    AoT = StringVar()
    AoT2 = StringVar()
    AoT3 = StringVar()
    AoT4 = StringVar()
    AoT5 = StringVar()
    global LoT
    LoT = Entry(screen1, textvariable = AoT)
    LoT.grid(row = 1, column = 0, pady = 3)
    global LoT2
    LoT2 = Entry(screen1, textvariable = AoT2)
    LoT2.grid(row = 2, column = 0, pady = 3)
    global LoT3
    LoT3 = Entry(screen1, textvariable = AoT3)
    LoT3.grid(row = 3, column = 0, pady = 3)
    global LoT4
    LoT4 = Entry(screen1, textvariable = AoT4)
    LoT4.grid(row = 4, column = 0, pady = 3)
    global LoT5
    LoT5 = Entry(screen1, textvariable = AoT5)
    LoT5.grid(row = 5, column = 0, pady = 3)
    btn_add = Button(screen1, text = "add", width = 10, height = 1, command = add_timer)
    btn_add.grid(row = 6, column = 0, pady = 3)
    instructions = Label(screen1, text = 'add the wanted amount of time by order from up to down')
    instructions.grid(row = 7, column = 0)
    instructions2 = Label(screen1, text = 'Format: H:M:S')
    instructions2.grid(row = 8, column = 0)
    ui.mainloop()

def add_timer():
    Ts = LoT.get()
    Ts2 = LoT2.get()
    Ts3 = LoT3.get()
    Ts4 = LoT4.get()
    Ts5 = LoT5.get()
    file = open('timerList', "w") #[username_info].txt - > youngho.txt, file의 권한 = w -> Write
    file.write(Ts+'\n') #new line
    file.write(Ts2+'\n')
    file.write(Ts3+'\n')
    file.write(Ts4+'\n')
    file.write(Ts5+'\n')
    file.close()
btn_strtTimer = Button(ui, text = 'start timer', width = 10, command = SATtimer)
btn_strtTimer.grid(row = 2, column=0, pady = 3)
btn_addATime = Button(ui, text = 'add a timer', width = 10, command = setTimer)
btn_addATime.grid(row = 3, column = 0, pady = 3)
ui.mainloop()