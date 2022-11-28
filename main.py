from tkinter import *
class FMS:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1920x1080+0+0')
        self.root.title('Farm Management System')

        title = Label(self.root,text='Farm Management System',font=('futura','40','bold'),bg = '#517d30',fg='#fffde0').place(x = 720,y = 0)
        

root = Tk()
obj = FMS(root)
root.mainloop()
