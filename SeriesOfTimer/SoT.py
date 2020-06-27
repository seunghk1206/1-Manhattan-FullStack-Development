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
    for each in timers:
        a = list(each.split(':'))
        tempL.append(a[0]*3600)
        tempL.append(a[1]*60)
        tempL.append(a[2])
        timer(sum(tempL), 'TIME OVER')

def setTimer():
    screen1 = Toplevel(ui)
    screen1.title("set_timer")
    screen1.geometry("300x250")
    AoT = StringVar()
    global LoT
    LoT = Entry(screen1, textvariable = AoT)
    Button(screen1, text = "add", width = 10, height = 1, command = add_timer).pack()
    ui.mainloop()

def add_timer():
    Ts = LoT.get()
    file = open('username_info', "w") #[username_info].txt - > youngho.txt, file의 권한 = w -> Write
    file.write("\n")
    file.write(Ts) #new line
    file.close()
    Ts.delete(0, END)
btn_strtTimer = Button(ui, text='start timer', width = 10, command = SATtimer)
btn_strtTimer.grid(row = 2, column=0, pady = 3)
ui.mainloop()