from cProfile import label
from itertools import count
from struct import pack
import tkinter as tk
import webbrowser
def say_hello():
    win2 = tk.Tk()
    win2.geometry=('500x600+1100+500')
    win2.title('salam')
    win2.minsize(300, 400)
    label = tk.Label(win2, text='Salam,brat',
    bg = 'blue',
    fg='white'
    )
    label.pack()
    win2.mainloop()

count = 0

def counter():
    global count
    count += 1
    button2['text'] = f'Счётчик: {count}' # тут мы у нашей кнопки меняем словарь

def Main_avin():
    command=webbrowser.open('https://www.youtube.com/watch?v=WmCKo6AofnU&ab_channel=%D0%9D%D0%B8%D0%BA%D0%BE%D0%BB%D0%B0%D0%B9%D0%9C%D0%BE%D0%BB%D0%BE%D0%B4%D0%B5%D1%86')

def first_avin():
    win3 = tk.Tk()
    win3.geometry=('500x600+1100+500')
    win3.title('Смерть')
    win3.minsize(300, 400)
    button = tk.Button(win3, text='Удачи',
    command=Main_avin,
    background='cyan',
    fg='green',
    width=50,
    height=50
    )
    button.pack()
    win3.mainloop()

win = tk.Tk()
win.geometry('2560x1440')
win.config(background='darkgoldenrod')
win.title('My first button')
win.title('My second desktop')

button1 = tk.Button(win,text='Press me', # нажать ctrl на кнопке
background='blue',
fg='black',
font=('Times New Roman', 12, 'italic'),
relief=tk.RAISED,
command=say_hello, # сюда передаётся то, что сделает кнопочка
width=1000,
height=30
)
button2 = tk.Button(win, text=f'Счётчик: {count}',
command=counter,
bg = 'red',
fg = 'white',
activebackground='Purple',
relief=tk.RAISED,
bd = 3,
width=1000,
height=30
)

button3 = tk.Button(win, text='Авинь мова',
command=first_avin,
width=1000,
height=30
)

button3.pack()
button1.pack()
button2.pack()
win.mainloop()