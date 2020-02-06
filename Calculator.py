from tkinter import * #Tkinter lib take all * = all

ui = Tk() # class  = book, we use ui variable to clarify 
ui.title("Calculator") # our ui's title = calculator
ui.resizable(False, False) # parameter = 2
ui.geometry("280x300")
ui.configure(background = 'green')
display = Entry(ui, width=28, justify='right')
display.grid(row = 0, column = 0 , columnspan = 4, pady=10, padx=4)

def myFunction():
    value = Entry.get(display) #get display's entry
    myFun = float(value) * 0.967 # tax calc
    display.delete(0, END)
    display.insert(0, myFun)
def cancel():
    display.delete(0, 1)
def cancel_all():
    display.delete(0, END)

#Search - bar 

#button = btn
btn_my = Button(ui, text='M', width = 5, command = myFunction)
btn_c = Button(ui, text='C', width = 5, command = cancel)
btn_CE = Button(ui, text='CE', width = 5, command = cancel_all)
btn_e = Button(ui, text='=', width = 5)

#button grid
btn_my.grid(row = 1, column=0, pady = 3)#computer always think that 0 = one 1 = scond
btn_c.grid(row = 1, column=1)
btn_CE.grid(row = 1, column=2)
btn_e.grid(row = 1, column = 3)

ui.mainloop() # continuously loop