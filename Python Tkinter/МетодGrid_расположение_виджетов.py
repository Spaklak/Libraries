import tkinter as tk

win = tk.Tk()
win.geometry('500x600+1100+200')
win.title('Размещаем виджеты')

btn1 = tk.Button(win, text='Hello 1')
btn2 = tk.Button(win, text='Hello 2')

btn1.grid()
btn2.grid()
win.mainloop()