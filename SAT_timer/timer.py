from tkinter import * #Tkinter lib take all * = all
import time
#package (lib)불러올땐 맨위에 작성

ui = Tk() # class  = book, we use ui variable to clarify 
ui.title("Calculator") # our ui's title = calculator
ui.resizable(False, False) # parameter = 2
ui.geometry("280x100")
ui.configure(background = 'green')
display = Entry(ui, width=28, justify='right')
display.grid(row = 0, column = 0 , columnspan = 4, pady=10, padx=4)


def SATtimer():
    for remaining in range(3900, 0, -1):
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
        time.sleep(1)
    display.delete(0, END)
    display.insert(0, 'TIMER OVER, RESTING TIME START')
    time.sleep(5)
    for remaining in range(595, 0, -1):
        a = remaining-(3600*(remaining//3600))
        b = a//60
        display.delete(0, END)
        display.insert(END, remaining//3600)
        display.insert(END, ":")
        display.insert(END, a//60)
        display.insert(END, ":")
        display.insert(END, b//60)
        time.sleep(1)
    display.delete(0, END)
    display.insert(0, 'TIMER OVER, Writing test start')
    time.sleep(5)
    for remaining in range(2095, 0, -1):
        a = remaining-(3600*(remaining//3600))
        b = a//60
        display.delete(0, END)
        display.insert(END, remaining//3600)
        display.insert(END, ":")
        display.insert(END, a//60)
        display.insert(END, ":")
        display.insert(END, b//60)
        time.sleep(1)
    display.delete(0, END)
    display.insert(0, 'TIMER OVER, Math without calc. start')
    time.sleep(5)
    for remaining in range(1495, 0, -1):
        a = remaining-(3600*(remaining//3600))
        b = a//60
        display.delete(0, END)
        display.insert(END, remaining//3600)
        display.insert(END, ":")
        display.insert(END, a//60)
        display.insert(END, ":")
        display.insert(END, b//60)
        time.sleep(1)
    display.delete(0, END)
    display.insert(0, 'TIMER OVER, RESTING TIME START')
    time.sleep(5)
    for remaining in range(295, 0, -1):
        a = remaining-(3600*(remaining//3600))
        b = a//60
        display.delete(0, END)
        display.insert(END, remaining//3600)
        display.insert(END, ":")
        display.insert(END, a//60)
        display.insert(END, ":")
        display.insert(END, b//60)
        time.sleep(1)
    display.delete(0, END)
    display.insert(0, 'TIMER OVER, Math with calc. start')
    time.sleep(5)
    for remaining in range(3295, 0, -1):
        a = remaining-(3600*(remaining//3600))
        b = a//60
        display.delete(0, END)
        display.insert(END, remaining//3600)
        display.insert(END, ":")
        display.insert(END, a//60)
        display.insert(END, ":")
        display.insert(END, b//60)
        time.sleep(1)
    display.delete(0, END)
    display.insert(0, 'TEST OVER')

#lambda 함수라고 쓰임.
#익명의 함수 -> 한줄로 몇백~몇천개의 함수를 요약

#Search - bar 
#command = myFunction 되게 좋아근데, 
#button = btn
btn_strtTimer = Button(ui, text='start timer', width = 15, command = SATtimer)
#button grid
btn_strtTimer.grid(row = 1, column=0, pady = 3)
ui.mainloop() # continuously loop