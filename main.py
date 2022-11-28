from tkinter import *
from PIL import Image,ImageTk
class FMS:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1920x1080+0+0')
        self.root.title('Farm Management System')
        self.root.configure(bg='#ffdeab')

        title = Label(self.root,text='Farm Management System',font=('futura','40','bold'),bg = '#517d30',fg='#fffde0').place(x = 0,y = 0,relwidth=1,height = 80)
        self.lbl_clock = Label(self.root,text='Welcome to Sriwan Farm\t\t Date: DD-MM-YYYY\t\t Time:HH:MM',font=('futura','20','bold'),bg = '#517d30',fg='#fffde0')
        self.lbl_clock.place(y=80,relwidth=1,height = 40)

        Menu = Frame(self.root,relief = RIDGE,bg = '#517d30')
        Menu.place(x=0, y=120,width = 384,height = 960)

        self.home_img = Image.open('img\home.png')
        self.home_img = self.home_img.resize((200,200))
        self.home_img = ImageTk.PhotoImage((self.home_img))
        
        btn_home = Button(Menu,image =self.home_img,bg = '#517d30',highlightthickness = 0, bd = 0).pack(side=TOP)
        btn_storage = Button()


root = Tk()
obj = FMS(root)
root.mainloop()
