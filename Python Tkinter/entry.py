import tkinter as tk
'''
entry - ввод
чтобы сделать entry нужно:
m = tk.Entry(win) больше ничего нельзя. Размещать только отдельной строкой
m.grid(row=0,column=0)
get - что-то получить из m
insert - что-то вставить в поле
delete - удалить из поля
'''

def get_entry():
    value = name.get()
    if value:
        print(value)
    else:
        print('Empty Entry')
def deleted():
    name.delete(0,'end') # чтобы всё удалить 

def sub():
    print(name.get())
    print(password.get())
win = tk.Tk()
win.title('Entry что-то')
win.geometry('1000x500+400+400')
tk.Label(win, text='Имя').grid(row=0,column=0,sticky='w')
tk.Label(win, text='Пароль').grid(row=1, column=0)
name = tk.Entry(win)
password = tk.Entry(win, show='*') # show - отображает то, что передано в кавычках
name.grid(row=0,column=1)
password.grid(row=1,column=1)

tk.Button(win,text='get', command=get_entry).grid(row=2,column=0,sticky='we')
tk.Button(win,text='Delete', command=deleted).grid(row=2,column=1,sticky='we')
tk.Button(win,text='ins', command=lambda: name.insert(0, 'Hello')).grid(row=2,column=2,sticky='we')
tk.Button(win,text='Submit', command=sub).grid(row=3,column=0,sticky='we')
win.mainloop()