from tkinter import *
from PIL import Image,ImageTk
class Employee:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1600x960+320+120')
        self.root.title('Worker')
        self.root.config(bg = 'white')
if __name__ == '__main__':
    root = Tk()
    obj = Employee(root)
    root.mainloop()