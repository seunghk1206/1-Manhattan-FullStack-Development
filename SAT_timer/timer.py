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
    global count
    count += 1
    if count%2 == 1:
        timer(5, 'testing')
        timer(3900, 'TIMER OVER, RESTING TIME START')
        timer(595, 'TIMER OVER, Writing test start')
        timer(2095, 'TIMER OVER, Math without calc. start')
        timer(1495, 'TIMER OVER, RESTING TIME START')
        timer(295, 'TIMER OVER, Math with calc. start')
        timer(3295, 'TEST OVER')
    else:
        label6 = Label(ui, text = 'please click once more time to restart!')
        label6.grid(row = 3, column = 0)

btn_strtTimer = Button(ui, text='start timer', width = 10, command = SATtimer)
btn_strtTimer.grid(row = 2, column=0, pady = 3)
ui.mainloop()