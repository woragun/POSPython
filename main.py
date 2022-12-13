from tkinter import *
from PIL import Image,ImageTk
from worker import Employee
from tkinter import ttk
from stock import Stock
class FMS:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1920x1080+0+0')
        self.root.title('Farm Management System')
        self.root.configure(bg='#ffdeab')

        title = Label(self.root,text='Farm Management System',font=('futura','40','bold'),bg = '#517d30',fg='#fffde0').place(x = 0,y = 0,relwidth=1,height = 80)
        self.lbl_clock = Label(self.root,text='Welcome to Sriwan Farm',font=('futura','20','bold'),bg = '#517d30',fg='#fffde0')
        self.lbl_clock.place(y=80,relwidth=1,height = 40)

        Menu = Frame(self.root,relief = RIDGE,bg = '#517d30')
        Menu.place(x=0, y=120,width = 384,height = 960)

        self.home_img = Image.open('img\home.png')
        self.home_img = self.home_img.resize((150,150))
        self.home_img = ImageTk.PhotoImage((self.home_img))
        
        self.worker_img = Image.open('img\home.png')
        self.worker_img = self.worker_img.resize((150,150))
        self.worker_img = ImageTk.PhotoImage((self.worker_img))

        self.storage_img = Image.open('img\storage.png')
        self.storage_img = self.storage_img.resize((150,150))
        self.storage_img = ImageTk.PhotoImage((self.storage_img))

        self.account_img = Image.open('img\profit.png')
        self.account_img = self.account_img.resize((150,150))
        self.account_img = ImageTk.PhotoImage((self.account_img))
        
        self.history_img = Image.open('img\history.png')
        self.history_img = self.history_img.resize((150,150))
        self.history_img = ImageTk.PhotoImage((self.history_img))

        btn_home = Button(Menu,image =self.home_img,bg = '#517d30',highlightthickness = 0, bd = 0).pack(side=TOP)
        btn_worker = Button(Menu,image=self.worker_img,command=self.worker,bg = '#517d30',highlightthickness=0,bd=0).pack(side=TOP,pady=20)
        btn_storage = Button(Menu,image=self.storage_img,command=self.stock,bg = '#517d30',highlightthickness=0,bd=0).pack(side=TOP,pady=20)
        btn_account = Button(Menu,image =self.account_img,bg = '#517d30',highlightthickness = 0, bd = 0).pack(side=TOP,pady=20)
        btn_history = Button(Menu,image=self.history_img,bg = '#517d30',highlightthickness=0,bd=0).pack(side=TOP)

    def worker(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Employee(self.new_win)
    def stock(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Stock(self.new_win)

        
if __name__ == '__main__':
    root = Tk()
    obj = FMS(root)
    root.mainloop()
