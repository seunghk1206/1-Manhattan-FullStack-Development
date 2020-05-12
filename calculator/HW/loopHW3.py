#random lib, while loop, for loop을 이용해서 유저와 input을 주고 받으며 자유로운 interaction 하나 만들기
from tkinter import *
import random
from random import sample

ui = Tk() # class  = book, we use ui variable to clarify 
ui.title("lotto generator") # our ui's title = calculator
ui.resizable(False, False) # parameter = 2
ui.geometry("280x300")
ui.configure(background = 'green')
display = Entry(ui, width=28, justify='right')
display.grid(row = 0, column = 0 , columnspan = 4, pady=10, padx=4)

def cancel_all():
    display.delete(0, END)
def lotto():
    Val = eval(Entry.get(display))
    lotte = random.sample(range(1,1001), Val)
    for each in range(1,1001):
        if lotte == 40:
            display.delete(0,END)
            display.insert(END, "You are the first!")
        elif lotte == 46:
            display.delete(0,END)
            display.insert(END, "You are second!")
        elif lotte == 682:
            display.delete(0,END)
            display.insert(END, "You are third")
        else:
            display.delete(0,END)
            display.insert(END, "You fail! Try again!")
    print(lotte)
def buttonPress(value):#parameter = 메개변수
    """value이라는 변수 (1, 2, 3, + , / ...)을 받고 display.inser("end", value)"""
    display.insert(END, value)
btn_CE = Button(ui, text='CE', width = 5, command = cancel_all)
btn_e = Button(ui, text='=', width = 5, command = lotto)
#Number
btn_zero = Button(ui, text='0', width = 5, command = lambda: buttonPress('0')) #얘내들을 바꿔줘야해
btn_one = Button(ui, text='1', width = 5, command = lambda: buttonPress('1'))#근데 여기서는 규칙상 '1' string 문자형태로 써야함
btn_Two = Button(ui, text='2', width = 5, command =  lambda: buttonPress('2'))
btn_Three = Button(ui, text='3', width = 5, command =  lambda: buttonPress('3'))
btn_four = Button(ui, text='4', width = 5, command =  lambda: buttonPress('4'))
btn_five = Button(ui, text='5', width = 5, command =  lambda: buttonPress('5'))
btn_six = Button(ui, text='6', width = 5, command =  lambda: buttonPress('6'))
btn_seven = Button(ui, text='7', width = 5, command =  lambda: buttonPress('7'))
btn_eight = Button(ui, text='8', width = 5, command =  lambda: buttonPress('8'))
btn_nine = Button(ui, text='9', width = 5, command =  lambda: buttonPress('9'))
#+, -, /, *


#button grid
#computer always think that 0 = one 1 = scond
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
ui.mainloop() # continuously loop