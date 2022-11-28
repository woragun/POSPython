from tkinter import *
from PIL import Image,ImageTk
class FMS:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1920x1080+0+0')
        self.root.title('Farm Management System')

        title = Label(self.root,text='Farm Management System',font=('futura','40','bold'),bg = '#517d30',fg='#fffde0').place(x = 0,y = 0,relwidth=1)
        self.lbl_clock = Label(self.root,text='Welcome to Farm Management System\t\t Date: DD-MM-YYYY\t\t Time:HH:MM',font=('futura','20','bold'),bg = '#517d30',fg='#fffde0')
        self.lbl_clock.place(y=75,relwidth=1)

        

root = Tk()
obj = FMS(root)
root.mainloop()
