from re import X
import tkinter as tk
'''
обычно side = Tope
'''
win = tk.Tk()
win.title('What')
win.geometry('300x500+1000+200')
# l1 = tk.Label(win, text='Hello 1', bg='pink', width=5, height=3).pack(side=tk.BOTTOM)
# l2 = tk.Label(win, text='Hello 2', bg='orange', width=5, height=3).pack(side=tk.LEFT)
# l3 = tk.Label(win, text='Hello 3', bg='green', width=5, height=3).pack(side=tk.RIGHT)
# l4 = tk.Label(win, text='Hello 4', bg='yellow', width=5, height=3).pack(side=tk.TOP)
#l1 = tk.Label(win, text='Hello 1', bg='pink', width=5, height=3).pack(expand=1, fill=tk.X) # fill=tk.x - растягивает по x, а tk.y по y
win.mainloop()