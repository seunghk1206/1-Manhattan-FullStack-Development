from tkinter import * #Tkinter lib take all * = all
import time
import sys
#package (lib)불러올땐 맨위에 작성
ui = Tk() # class  = book, we use ui variable to clarify 
ui.title("Calculator") # our ui's title = calculator
ui.resizable(False, False) # parameter = 2
ui.geometry("280x100")
ui.configure(background = 'green')
display = Entry(ui, width=28, justify='right')
display.grid(row = 0, column = 0 , columnspan = 4, pady=10, padx=4)

def timer(NoS, description):
    for remaining in range(NoS, 0, -1):
        a = remaining-(3600*(remaining//3600))
        b = a//60
        c = remaining-(remaining//3600*3600)-(b*60)
        print(remaining//3600, ':', b, ':', c)
        time.sleep(1)
    display.delete(0, END)
    display.insert(0, description)
    time.sleep(5)
def SATtimer():
    timer(5, 'done')

btn_strtTimer = Button(ui, text='start timer', width = 15, command = SATtimer)
btn_strtTimer.grid(row = 1, column=0, pady = 3)
ui.mainloop()