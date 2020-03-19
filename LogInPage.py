from tkinter import *

def register_user(): # regiser 버튼 

    username_info = username.get() # username 의 값을 가져옴
    password_info = password.get()

    if len(password_info) >= 8:
        file = open(username_info+".txt", "w") #[username_info].txt - > youngho.txt, file의 권한 = w -> Write
        file.write("username: " + username_info)
        file.write("\n") #new line
        file.write("password: " + password_info)
        file.close()

        username_entry.delete(0,END)
        password_entry.delete(0,END)

        Label(screen1, text = "Registration Successful", fg = "green", font = ("Calibri", 13)).pack()
    else:
        password_entry.delete(0,END)
        Label(screen1, text = "The password has to be more than 8 digits!", fg = "red", font = ("Calibri", 13)).pack()

def login_user():
    
    username_info = username.get() # username 의 값을 가져옴
    password_info = password.get()
    file = open(username_info.txt, 'r')
    userID_check = file.read()
    password_check = file.read()
    if password_info == password_check and username_info == userID_check:
        pass

def register():
    global screen1
    screen1 = Toplevel(screen) #screen으로 인한 새로운 페이지
    screen1.title("Register")
    screen1.geometry("300x250")
    screen1.title("Mahattan Project Login Page")
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text = "Please ebter your info below").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Username").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text = "Password").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()

def login():
    screen2 = Toplevel(screen) #screen으로 인한 새로운 페이지
    screen2.title("login")
    screen2.geometry("300x350")
    screen2.title("Mahattan Project Login Page")


def login_page():
    global screen
    screen = Tk()
    screen.geometry("300x350")
    screen.title("Mahattan Project Login Page")
    Label(text = "Manhattan Project Login Page", bg = "grey", width = 300, height = 2, font = ("calibri", 13)).pack()
    Label(text = "").pack()
    Button(text = "Login", width = 30, height = 2, command = login).pack()
    Label(text = "").pack()
    Button(text = "Register", width = 30, height = 2, command = register).pack()

    screen.mainloop()

login_page()