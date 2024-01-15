from tkinter import Tk

class Window(Tk):
    def __init__(self):
        super().__init__()
        self.title("Mile to Km Converter")
        self.minsize(width=400, height=400)
        self.mainloop()