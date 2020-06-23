from tkinter import * #Tkinter lib take all * = all
import time
from pydub import AudioSegment
from pydub.playback import play
#package (lib)불러올땐 맨위에 작성
count = 0
ui = Tk() # class  = book, we use ui variable to clarify 
ui.title("SAT_timer") # our ui's title = calculator
ui.resizable(False, False) # parameter = 2
ui.geometry("500x300")
ui.configure(background = 'blue')
display = Entry(ui, width=28, justify='right')
display.grid(row = 5, column = 0, columnspan = 4, pady=10, padx=4)
label = Label(ui, text = 'time left:')
label.grid(row = 4, column = 0)
label2 = Label(ui, text = 'instructions')
label2.grid(row = 0, column = 0)
label3 = Label(ui, text = '1. please enter the directory where the file is located.')
label3.grid(row = 1, column = 0)
label4 = Label(ui, text = '(if using it for the first time)')
label4.grid(row = 2, column = 0)
label5 = Label(ui, text = '2. then press start timer!')
label5.grid(row = 3, column = 0)
def done():
    try:
        file = open('directory', "r")
        verify = file.read()
        global direc
        direc = AudioSegment.from_wav(verify + "/alarm.mp3", 15)
    except:
        directory = Entry.get(display)
        file = open('directory', "w") #[username_info].txt - > youngho.txt, file의 권한 = w -> Write
        file.write(directory)
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
    play(direc)
    print(description)
    time.sleep(5)
def SATtimer():
    global count
    count += 1
    if count%2 == 0:
        timer(5, 'test')
        timer(3900, 'TIMER OVER, RESTING TIME START')
        timer(595, 'TIMER OVER, Writing test start')
        timer(2095, 'TIMER OVER, Math without calc. start')
        timer(1495, 'TIMER OVER, RESTING TIME START')
        timer(295, 'TIMER OVER, Math with calc. start')
        timer(3295, 'TEST OVER')
    else:
        label6 = Label(ui, text = 'please click once more time to start/reset!')
        label6.grid(row = 7, column = 0)

btn_strtTimer = Button(ui, text='start timer', width = 10, command = SATtimer)
btn_strtTimer.grid(row = 6, column=0, pady = 3)
btn_strtTimer = Button(ui, text='Done', width = 10, command = done)
btn_strtTimer.grid(row = 6, column=1, pady = 3)
ui.mainloop()