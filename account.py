from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
from stock import Stock
class Account:
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
        self.var_item_date = StringVar()

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

        lbl_date = Label(self.root,text = 'Date', font =('Futura',14), bg = 'white').place(x=400,y=380)
        txt_quantity = Entry(self.root,textvariable=self.var_item_date, font =('Futura',14), bg = 'white').place(x=500,y=380)

        tn_save = Button(self.root,text='Add',command=self.add,font=('futura',14,'bold'),bg = '#4caf50',fg = 'white',cursor='hand2').place(x = 400, y= 500,width = 120,height=30)
        btn_update = Button(self.root,text='Update',command=self.update,font=('futura',14,'bold'),bg = '#4caf50',fg = 'white',cursor='hand2').place(x = 540, y= 500,width = 120,height=30)
        btn_delete = Button(self.root,text='Delete',command=self.delete,font=('futura',14,'bold'),bg = '#4caf50',fg = 'white',cursor='hand2').place(x = 680, y= 500,width = 120,height=30)
        btn_clear = Button(self.root,text='Clear',command='Clear',font=('futura',14,'bold'),bg = '#4caf50',fg = 'white',cursor='hand2').place(x = 820, y= 500,width = 120,height=30)

        stc_frame = Frame(self.root,bd = 3,relief=RIDGE)
        stc_frame.place(x=0,y = 600,relwidth=1,height=360)

        sc_v = Scrollbar(stc_frame,orient=VERTICAL)

        self.table = ttk.Treeview(stc_frame,columns=('id','name','quantity','price','date'),yscrollcommand=sc_v.set)
        sc_v.pack(side=RIGHT,fill=Y)
        sc_v.config(command=self.table.yview())

        self.table.heading('id',text = 'Id')
        self.table.heading('name',text = 'Name')
        self.table.heading('quantity',text = 'Quantity')
        self.table.heading('price',text = 'Price')
        self.table.heading('date',text = 'Date')
        self.table['show'] = 'headings'

        self.table.column('id',width = 200)
        self.table.column('name',width = 400)
        self.table.column('quantity',width = 300)
        self.table.column('price',width = 300)
        self.table.column('date',width = 400)
        self.table.pack(fill = BOTH,expand=1)
        self.table.bind('<ButtonRelease-1>',self.get_data)
        self.show()

    def add(self):
        con = sqlite3.connect(database = r'FMS.db')
        cur = con.cursor()
        try:
            if self.var_item_id.get() == '' :
                messagebox.showerror('Error',"Id is required",parent = self.root)
            else:
                cur.execute('Select * from stock where id=?',(self.var_item_id.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror('Error',"Already Exits",parent = self.root)
                else:
                    cur.execute('Insert into stock (id,name,quantity,price,date) values(?,?,?,?,?)',(
                                    self.var_item_id.get(),
                                    self.var_item_name.get(),
                                    self.var_item_quantity.get(),
                                    self.var_item_price.get(),
                                    self.var_item_date.get()
                    ))
                    con.commit()
                    messagebox.showinfo('Success','Item is added into the databease',parent = self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror('Error',f"Error due to : {str(ex)}",parent = self.root)

    def show(self):
        con = sqlite3.connect(database = r'FMS.db')
        cur = con.cursor()
        try:
            cur.execute('select * from stock')
            rows = cur.fetchall()
            self.table.delete(*self.table.get_children())
            for r in rows:
                self.table.insert('', END,values = r)
        except Exception as ex:
            messagebox.showerror('Error',f"Error due to : {str(ex)}",parent = self.root)

    def get_data(self,ev):
        f = self.table.focus()
        content = (self.table.item(f))
        row = content['values']
        self.var_item_id.set(row[0]),
        self.var_item_name.set(row[1]), 
        self.var_item_quantity.set(row[2]),
        self.var_item_price.set(row[3]),
        self.var_item_date.set(row[4]),

    def update(self):
        con = sqlite3.connect(database = r'FMS.db')
        cur = con.cursor()
        try:
            if self.var_item_id.get() == '' :
                messagebox.showerror('Error',"Id is required",parent = self.root)
            else:
                cur.execute('Select * from stock where id=?',(self.var_item_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror('Error',"Doesn't exist",parent = self.root)
                else:
                    cur.execute('Update stock set name=?,quantity=?,price=?, date = ? where id=?',(
                                    
                                    self.var_item_name.get(), 
                                    self.var_item_quantity.get(),
                                    self.var_item_price.get(),
                                    self.var_item_date.get(),
                                    self.var_item_id.get()
                    ))
                    con.commit()
                    messagebox.showinfo('Success','Stock is updated',parent = self.root)
                    self.show()
                    con.close()
        except Exception as ex:
            messagebox.showerror('Error',f"Error due to : {str(ex)}",parent = self.root)

    def delete(self):
        con = sqlite3.connect(database = r'FMS.db')
        cur = con.cursor()
        try:
            if self.var_item_id.get() == '' :
                messagebox.showerror('Error',"Id is required",parent = self.root)
            else:
                op = messagebox.askyesno('Confirm','Do you really want to delete?',parent=self.root)
                if op == True:
                    cur.execute('delete from stock where id=?',(self.var_item_id.get(),))
                    con.commit()
                    messagebox.showinfo('Delete','Deleted',parent = self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror('Error',f"Error due to : {str(ex)}",parent = self.root)
    
    def clear(self):
        self.var_item_id.set(""),
        self.var_item_name.set(""), 
        self.var_item_quantity.set(""),
        self.var_item.price.set(""),
        self.var_item_date.set(''),
        self.var_searchtext.set('')
        self.show()
    
    def search(self):
        con = sqlite3.connect(database = r'FMS.db')
        cur = con.cursor()
        try:
            if self.var_searchtext.get() =='':
                messagebox.showerror('Error','Empty Text',parent = self.root)
            else:
                cur.execute("select * from stock where "+self.var_searchtext.get()+"%'")
                rows = cur.fetchall()
                if len(rows) !=0:
                    self.table.delete(*self.table.get_children())
                    for r in rows:
                        self.table.insert('', END,values = r)
                else:
                    messagebox.showerror('Error','Not Found',parent = self.root)
        except Exception as ex:
            messagebox.showerror('Error',f"Error due to : {str(ex)}",parent = self.root)

        


if __name__ == '__main__':
    root = Tk()
    obj = Stock(root)
    root.mainloop()