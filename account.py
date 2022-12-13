from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
from stock import Stock
class Account:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1600x960+320+120')
        self.root.title('Account')
        self.root.config(bg = 'white')
        self.root.focus_force()

        self.var_item_id = StringVar()
        self.var_item_name = StringVar()
        self.var_item_quantity = StringVar()
        self.var_item_price = StringVar()

        
        btn_save = Button(self.root,text='Add',command=self.add,font=('futura',14,'bold'),bg = '#4caf50',fg = 'white',cursor='hand2').place(x = 400, y= 500,width = 120,height=30)
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
        self.table['show'] = 'headings'

        self.table.column('id',width = 200)
        self.table.column('name',width = 400)
        self.table.column('quantity',width = 300)
        self.table.column('price',width = 300)
        self.table.pack(fill = BOTH,expand=1)
        self.table.bind('<ButtonRelease-1>',self.get_data)
        self.show()

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
                                    self.var_item_id.get()
                    ))
                    con.commit()
                    messagebox.showinfo('Success','Stock is updated',parent = self.root)
                    self.show()
                    con.close()
        except Exception as ex:
            messagebox.showerror('Error',f"Error due to : {str(ex)}",parent = self.root)

    
    def clear(self):
        self.var_item_id.set(""),
        self.var_item_name.set(""), 
        self.var_item_quantity.set(""),
        self.var_item.price.set(""),
        self.var_searchtext.set('')
        self.show()
    
   

        


if __name__ == '__main__':
    root = Tk()
    obj = Stock(root)
    root.mainloop()