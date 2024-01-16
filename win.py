from tkinter import Tk, Label, Entry, Button
from ttkbootstrap import *
from ttkbootstrap.constants import *

class Window(Tk):
    def __init__(self):
        super().__init__()
        self.title("Mile to Km Converter")
        self.minsize(width=100, height=100)
        self.config(padx=5, pady=5)
        self.input = Entry(bootstyle='success' ,width=10)
        self.input.grid(padx=70, pady=10,column=1, row=0)
        self.m_l = Label(bootstyle='warning' ,text='Miles', font=('Comic', 20, 'italic'))
        self.m_l.grid(column=2, row=0, padx=70, pady=10)
        self.eq_l = Label(bootstyle='danger',text='is equal to', font=('Comic', 20, 'italic'))
        self.eq_l.grid(column=0, row=1)
        self.num = Label(bootstyle='info' ,text=f'{0}', font=('Comic', 20, 'italic'))
        self.num.grid(column=1, row=1)
        self.km_l = Label(bootstyle='primary' ,text='Km', font=('Comic', 20, 'italic'))
        self.km_l.grid(column=2, row=1)
        self.calc = Button(bootstyle='success-outline' ,text='Calculate', command=self.calculate)
        self.calc.grid(column=1, row=2)
        self.mainloop()
    
    def calculate(self):
        self.km = 1.609
        self.num.config(text=f'{round(float(self.input.get()) * self.km, 2)}')
        
        
 