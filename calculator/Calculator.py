from tkinter import * #Tkinter lib take all * = all
import math #package (lib)불러올땐 맨위에 작성

ui = Tk() # class  = book, we use ui variable to clarify 
ui.title("Calculator") # our ui's title = calculator
ui.resizable(False, False) # parameter = 2
ui.geometry("280x300")
ui.configure(background = 'green')
display = Entry(ui, width=28, justify='right')
display.grid(row = 0, column = 0 , columnspan = 4, pady=10, padx=4)


def myFunction():
    value = Entry.get(display) #get display's entry
    myFun = eval(value) * 29 / 30 # tax calc
    display.delete(0, END)
    display.insert(0, myFun)
def cancel():
    display.delete(0, 1)
def cancel_all():
    display.delete(0, END)
def equal(): #Great Job
    value = Entry.get(display)
    func = eval(value)
    display.delete(0, END)
    display.insert(0, func)

def buttonPress(value):#parameter = 메개변수
    """value이라는 변수 (1, 2, 3, + , / ...)을 받고 display.inser("end", value)"""
    display.insert(END, value)

#lambda 함수라고 쓰임.
#익명의 함수 -> 한줄로 몇백~몇천개의 함수를 요약

#Search - bar 
#command = myFunction 되게 좋아근데, 
#button = btn
btn_my = Button(ui, text='M', width = 5, command = myFunction)
btn_c = Button(ui, text='C', width = 5, command = cancel)
btn_CE = Button(ui, text='CE', width = 5, command = cancel_all)
btn_e = Button(ui, text='=', width = 5, command = equal)
#Number
btn_zero = Button(ui, text='0', width = 5, command = lambda: buttonPress('0'))
btn_one = Button(ui, text='1', width = 5, command = lambda: buttonPress('1'))
btn_Two = Button(ui, text='2', width = 5, command =  lambda: buttonPress('2'))
btn_Three = Button(ui, text='3', width = 5, command =  lambda: buttonPress('3'))
btn_four = Button(ui, text='4', width = 5, command =  lambda: buttonPress('4'))
btn_five = Button(ui, text='5', width = 5, command =  lambda: buttonPress('5'))
btn_six = Button(ui, text='6', width = 5, command =  lambda: buttonPress('6'))
btn_seven = Button(ui, text='7', width = 5, command =  lambda: buttonPress('7'))
btn_eight = Button(ui, text='8', width = 5, command =  lambda: buttonPress('8'))
btn_nine = Button(ui, text='9', width = 5, command =  lambda: buttonPress('9'))
#+, -, /, *
btn_plus = Button(ui, text='+', width = 5, command =  lambda: buttonPress('+'))
btn_minus = Button(ui, text='-', width = 5, command =  lambda: buttonPress('-'))
btn_mult = Button(ui, text='*', width = 5, command =  lambda: buttonPress('*'))
btn_div = Button(ui, text='/', width = 5, command =  lambda: buttonPress('/'))
btn_negative = Button(ui, text = '+/-', width = 5, command =  lambda: buttonPress('.'))
#.
btn_dot = Button(ui, text='.', width = 5, command =  lambda: buttonPress)

#button grid
btn_my.grid(row = 1, column=0, pady = 3)#computer always think that 0 = one 1 = scond
btn_c.grid(row = 1, column= 1)
btn_CE.grid(row = 1, column= 2)
btn_e.grid(row = 1, column = 3)
btn_zero.grid(row = 5, column = 0)
btn_one.grid(row = 2, column = 0)
btn_Two.grid(row = 2, column = 1)
btn_Three.grid(row = 2, column = 2)
btn_four.grid(row = 3, column = 0)
btn_five.grid(row = 3, column = 1)
btn_six.grid(row = 3, column = 2)
btn_seven.grid(row = 4, column = 0)
btn_eight.grid(row = 4, column = 1)
btn_nine.grid(row = 4, column = 2)
btn_plus.grid(row = 2, column = 3)
btn_minus.grid(row = 3, column = 3)
btn_mult.grid(row = 4, column = 3)
btn_div.grid(row = 5, column = 3)
btn_negative.grid(row = 5, column = 1)
btn_dot.grid(row = 5,column = 2)
ui.mainloop() # continuously loop