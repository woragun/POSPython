import tkinter as tk

class FMS:
    def __init__(self,root):
        self.root = root
        self.root.geometry = ('1920x1080+0+0')
        self.root.title = ('Farm Management System')


root = tk.Tk()
obj = FMS(root)
root.mainloop()
