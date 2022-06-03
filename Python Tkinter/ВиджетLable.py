import tkinter as tk
#label для отображения текстовой команды 
win = tk.Tk()
win.geometry('500x600+1100+500')
win.title('My second desktop')
win.iconphoto(False, tk.PhotoImage(file='kek.png'))

label_1 = tk.Label(win, text='''Hello 
world''', # 3 кавычки, что переносить строки
                    background='red', # цвет фона для надписи
                    fg='white', #цвет самой надписи
                    font=('Arial,',15,'bold'), # стиль текста, его размер, а после жирный либо курсив либо подчеркнутый
                    padx=10,  #отступ по x типо красной строки
                    # pady=40,  отступы по y 
                    width=20, # ширина текстового поля
                    height=10, # высота текстового поля
                    anchor='nw', # меняет положение текста по типу must be n, ne, e, se, s, sw, w, nw, or center
                    relief=tk.RAISED, #границы
                    bd=5, # ширина границы
                    justify=tk.LEFT # выравнивает текст, если в нём несколько строк
) # создаём текстовое поле
label_1.pack() # распологает кнопку на экране
win.mainloop()