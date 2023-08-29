import tkinter as tk
import tkinter.ttk as ttk
from tkinter.font import Font

root = tk.Tk()
root.geometry('700x900')
root.resizable(False, False)
root.title('Sign Up Form')

database = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3",
    "user4": "password4",
    "user5": "password5",
    "user6": "password6",
    "user7": "password7",
    "user8": "password8",
    "user9": "password9",
    "user10": "password10"
}

def open_window():
    global i
    global j
    global k
    global y_coordinates
    global x_coordinates
    new_window = tk.Toplevel(root)
    new_window.title('Sign Up')
    new_window.geometry('700x900')
    new_window.resizable(False, False)
    background_image = tk.PhotoImage(file=r"C:\Users\josep\Downloads\png-clipart-inn-pub-medieval-miscellaneous-building.png")
    background_label = tk.Label(new_window, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    label3 = tk.Label(new_window, text="Sign Up", font=('arial', 20, 'bold'))
    label3.place(x=320, y=40)

    label4 = tk.Label(new_window, width=10, height=5)
    #label4.place(x=320, y=y_coordinates)
    j = 0
    k = 0
    def square_move_y():
        global k
        global y_coordinates
        global x_coordinates
        y_coordinates = [800, 800, 800, 800, 800, 800, 800, 810, 820, 830,
                         840, 850, 860, 870, 870, 870, 870, 870, 870,
                         870, 870,
                         860, 850, 840, 830, 820, 810, 800]
        x_coordinates = [270, 280, 290, 300, 310, 320, 330, 330, 330, 330,
                         330, 330, 330, 330, 320, 310, 300, 290, 280,
                         270, 260, 260, 260, 260, 260, 260, 260, 260]
        k += 1
        if k == len(y_coordinates) and k == len(x_coordinates):
            k = 0
        x = x_coordinates[k]
        y = y_coordinates[k]
        label4.place(x=x, y=y)
        label4.after(50, square_move_y)
    def change_colour2():
        global j
        colours = ['blue', 'red', 'green', 'orange', 'yellow',
                   'grey', 'purple', 'white']
        current_colour = label4.cget('background')
        label4.config(bg=colours[j])
        j += 1
        if j == len(colours):
            j = 0
        label4.after(50, change_colour2)
    def change_colour():
        current_colour = label3.cget('foreground')
        new_colour = 'red' if current_colour == 'blue' else 'blue'
        label3.config(foreground=new_colour)
        label3.after(100, change_colour)
    i = 0
    def change_size():
        global i
        sizes = [8, 9, 10, 11, 12, 13, 14, 15, 16,
                 15, 14, 13, 12, 11, 10, 9]
        current_size = label3.cget('width')
        label3.config(width=sizes[i])
        i += 1
        if i == len(sizes):
            i = 0
        label3.after(50, change_size)
    def submit():
        username_ = entry3.get()
        password_ = entry4.get()
        special_chars = '$#~-_():;?@'
        capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        numbers = '1234567890'
        str_ = ""
        message_label2 = tk.Label(new_window, text=str_)
        message_label2.place(x=200, y=680)

        if username_ in database:
            message_label_ = tk.Label(new_window, text='Username Taken',
                                      fg='red', font=('arial', 18))
            message_label_.place(x=200, y=600)
        else:
            if any(char not in special_chars for char in password_):
                str_ += "Must contain at least one special character\n"
            if any(char not in capital_letters for char in password_):
                str_ += "Must contain at least one capital letter\n"
            if any(char not in numbers for char in password_):
                str_ += "Must contain at least one number\n"
            if len(username_) < 4 or len(password_) < 4:
                str_ += "Must contain at lest 4 characters\n"
            if len(username_) > 18 or len(password_) > 18:
                str_ += "Must not contain more than 18 characters"
            if str_:
                message_label2.config(text=str_, fg='red')
            else:
                new_username = entry3.get()
                new_password = entry4.get()
                database[new_username] = new_password
                message_label2.config(text='User added to database!', fg='green')

    label5 = tk.Label(new_window, text='Choose a sensible username:',
                      font=('arial', 18))
    label5.place(x=200, y=200)
    entry3 = tk.Entry(new_window, width=20, font=('arial', 25))
    entry3.place(x=200, y=250)
    label6 = tk.Label(new_window, text='Choose a sensible password:',
                      font=('arial', 18))
    label6.place(x=200, y=300)
    entry4 = tk.Entry(new_window, width=20, font=('arial', 25))
    entry4.place(x=200, y=350)

    button4 = tk.Button(new_window, text='Submit', width=10,
                        height=2, font=('arial', 16), command=submit)
    button4.place(x=200, y=400)

    change_colour()
    change_size()
    change_colour2()
    square_move_y()

    new_window.mainloop()

trials = 0
def validate_login():
    username = entry1.get()
    password = entry2.get()

    if username in database and database[username] == password:
        message_label = tk.Label(root, text="Login successful", font=('arial', 20, 'bold'),
                                 fg='red')
        message_label.place(x=280, y=600)

        new_window2 = tk.Toplevel(root)
        new_window2.title('Welcome')
        new_window2.geometry('700x900')
        new_window2.resizable(False, False)

        label6 = tk.Label(new_window2, text=f'Welcome {username}',
                          font=('arial', 20), fg='gold')
        label6.place(x=200, y=200)

        new_window2.mainloop()
    else:
        message_label = tk.Label(root, text="Login not successful", font=('arial', 20, 'bold'),
                                 fg='red')
        message_label.place(x=280, y=600)

img = tk.PhotoImage(file=r"C:\Users\josep\Downloads\png-clipart-inn-pub-medieval-miscellaneous-building.png")
limg = tk.Label(root, image=img)
limg.pack()
label1 = tk.Label(root, text='Login Below', font=('arial', 25, 'bold'),
                  fg='white',bg='black', bd=1, highlightbackground='gold',
                  highlightthickness=2)
label1.place(x=280, y=10)

label2 = tk.Label(root, text='Username', font=('arial', 20, 'bold'))
label2.place(x=280, y=320)
entry1 = tk.Entry(root, width=20, font=('arial', 20), bd=1)
entry1.place(x=280, y=370)
label2 = tk.Label(root, text='Password', font=('arial', 20, 'bold'))
label2.place(x=280, y=420)
entry2 = tk.Entry(root, width=20, font=('arial', 20, 'bold'))
entry2.place(x=280, y=470)

button = tk.Button(root, width=10, height=1, text='Login',
                   font=('arial', 20, 'bold'), cursor='hand2',
                   command=validate_login)
button.place(x=280, y=510)

message_label = tk.Label(root, text="", font=('arial', 20, 'bold'),
                         fg='red')
message_label.place(x=280, y=600)

button2 = tk.Button(root, text="Don't have an account? Sign up",
                    font=('arial', 16), cursor='hand2',
                    command=open_window)
button2.place(x=240, y=700)

button3 = tk.Button(root, text='Wacky', cursor='hand2', font=('arial', 16))
button3.place(x=280, y=800)

l = 0

def button_size():
    global l
    widths = [7, 8, 9, 10, 11, 12, 11, 10, 9, 8]
    heights = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2]
    l = l % len(widths)  # ensures l stays within bounds of the list
    button3.config(width=widths[l], height=heights[l])
    l += 1
    button3.after(50, button_size)

button_size()
root.mainloop()
