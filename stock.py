from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class Stock:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1600x960+320+120')
        self.root.title('Worker')
        self.root.config(bg = 'white')
        self.root.focus_force()

        self.var_searchtext = StringVar()

        self.var_item_id = StringVar()
        self.var_item_name = StringVar()
        self.var_item_quantity = StringVar()
        self.var_item_price = StringVar()

        searchFrame = LabelFrame(self.root,text='Search Item',font=('futura',12,'bold'),bd = 1,bg = 'white')
        searchFrame.place(x= 400,y=20,width=800, height=80)
        txt_search = Entry(searchFrame,textvariable=self.var_searchtext,font=('futura',14)).place(x=200,y = 10,width=200)
        btn_serch = Button(searchFrame,font=('futura',14,'bold'),bg = '#4caf50',fg = 'white',cursor='hand2').place(x = 440,y = 10,width = 150,height=30)

        title = Label(self.root,text='Stock Details',font = ('Futura',16,'bold'),bg = '#0f4d7d',fg='white',justify=CENTER).place(x =300,y=120,width = 1000)
        lbl_id = Label(self.root,text = 'Id', font =('Futura',14), bg = 'white').place(x=400,y=180)
        lbl_name = Label(self.root,text = 'Name', font =('Futura',14), bg = 'white').place(x=850,y=180)

        txt_id = Entry(self.root,textvariable=self.var_item_id, font =('Futura',14), bg = 'white').place(x=500,y=180)
        txt_name = Entry(self.root,textvariable = self.var_item_name, font =('Futura',14), bg = 'white').place(x=950,y=180)

        lbl_quantity = Label(self.root,text = 'Quantity', font =('Futura',14), bg = 'white').place(x=400,y=280)
        lbl_price = Label(self.root,text = 'Price', font =('Futura',14), bg = 'white').place(x=850,y=280)

        txt_quantity = Entry(self.root,textvariable=self.var_item_quantity, font =('Futura',14), bg = 'white').place(x=500,y=280)
        txt_price = Entry(self.root,textvariable = self.var_item_price, font =('Futura',14), bg = 'white').place(x=950,y=280)

        tn_save = Button(self.root,text='Add',command=self.add,font=('futura',14,'bold'),bg = '#4caf50',fg = 'white',cursor='hand2').place(x = 400, y= 400,width = 120,height=30)
        btn_update = Button(self.root,text='Update',command=self.update,font=('futura',14,'bold'),bg = '#4caf50',fg = 'white',cursor='hand2').place(x = 540, y= 400,width = 120,height=30)
        btn_delete = Button(self.root,text='Delete',command=self.delete,font=('futura',14,'bold'),bg = '#4caf50',fg = 'white',cursor='hand2').place(x = 680, y= 400,width = 120,height=30)
        btn_clear = Button(self.root,text='Clear',command='Clear',font=('futura',14,'bold'),bg = '#4caf50',fg = 'white',cursor='hand2').place(x = 820, y= 400,width = 120,height=30)

        stc_frame = Frame(self.root,bd = 3,relief=RIDGE)
        stc_frame.place(x=0,y = 600,relwidth=1,height=360)

        sc_v = Scrollbar(emp_frame,orient=VERTICAL)

        self.table = ttk.Treeview(emp_frame,columns=('id','name','quantity','price'),yscrollcommand=sc_v.set)
        sc_v.pack(side=RIGHT,fill=Y)
        sc_v.config(command=self.table.yview())

        


if __name__ == '__main__':
    root = Tk()
    obj = Stock(root)
    root.mainloop()