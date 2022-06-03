import tkinter as tk

win = tk.Tk()
win.geometry('500x600+1100+200')
win.title('Размещаем виджеты')

btn1 = tk.Button(win, text='Hello 1')
btn2 = tk.Button(win, text='Hello 2')
btn3 = tk.Button(win, text='Hello 3')
btn4 = tk.Button(win, text='Hello 4')
btn5 = tk.Button(win, text='Hello 5')
btn6 = tk.Button(win, text='Hello 6')
btn7 = tk.Button(win, text='Hello 7')
btn8 = tk.Button(win, text='Hello 8')

btn1.grid(row=0,column=0) # первое - ряд, а второе - колонка
btn2.grid(row=0,column=1)
btn3.grid(row=1,column=0,stick='we') # если есть голое пространство 
btn4.grid(row=1,column=1)
btn5.grid(row=2,column=0)
btn6.grid(row=2,column=1)
btn7.grid(row=3,column=0, columnspan=2, stick='we')# columnspan=2 объединяет 2 колонки, stick - растягивет
btn8.grid(row=0,column=2, rowspan=4,stick='ns' ) #объединяет ряды

win.grid_columnconfigure(0,minsize=200)
win.mainloop()