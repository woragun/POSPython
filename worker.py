from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class Employee:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1600x960+320+120')
        self.root.title('Worker')
        self.root.config(bg = 'white')
        self.root.focus_force()

        self.var_searchtype = StringVar()
        self.var_searchtext = StringVar()

        self.var_wrk_id = StringVar()
        self.var_wrk_name = StringVar()
        self.var_wrk_gender = StringVar()
        self.var_wrk_contact = StringVar()
        self.var_wrk_nationality = StringVar()
        self.var_wrk_wage = StringVar()

        searchFrame = LabelFrame(self.root,text='Search Worker',font=('futura',12,'bold'),bd = 1,bg = 'white')
        searchFrame.place(x= 400,y=20,width=800, height=80)

        cmb_search = ttk.Combobox(searchFrame,textvariable=self.var_searchtype,values=('Select','ID','Name','Number'),state='readonly',justify=CENTER,font=('futura',14))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search = Entry(searchFrame,textvariable=self.var_searchtext,font=('futura',14)).place(x=200,y = 10,width=200)
        btn_serch = Button(searchFrame,command=self.search,font=('futura',14,'bold'),bg = '#4caf50',fg = 'white',cursor='hand2').place(x = 440,y = 10,width = 150,height=30)

        title = Label(self.root,text='Worker Details',font = ('Futura',16,'bold'),bg = '#0f4d7d',fg='white',justify=CENTER).place(x =300,y=120,width = 1000)

        lbl_wrk_id = Label(self.root,text = 'ID', font =('Futura',14), bg = 'white').place(x=200,y=180)
        lbl_gender = Label(self.root,text = 'Gender', font =('Futura',14), bg = 'white').place(x=650,y=180)
        lbl_contact = Label(self.root,text = 'Contact', font =('Futura',14), bg = 'white').place(x=1050,y=180)

        txt_wrk_id = Entry(self.root,textvariable= self.var_wrk_id, font =('Futura',14), bg = 'white').place(x=350,y=180,width=180)
        cmb_gender = ttk.Combobox(self.root,textvariable=self.var_wrk_gender,values=('Select','Male','Female'),state='readonly',justify=CENTER,font=('futura',14))
        cmb_gender.place(x=800,y=180,width=180)
        cmb_gender.current(0)
        txt_contact = Entry(self.root,textvariable = self.var_wrk_contact, font =('Futura',14), bg = 'white').place(x=1200,y=180,width=180)

        lbl_wrk_name = Label(self.root,text = 'Name', font =('Futura',14), bg = 'white').place(x=200,y=280)
        lbl_nationality = Label(self.root,text = 'Nationality', font =('Futura',14), bg = 'white').place(x=650,y=280)
        lbl_wage = Label(self.root,text = 'Wage', font =('Futura',14), bg = 'white').place(x=1050,y=280)
        
        txt_wrk_name = Entry(self.root,textvariable=self.var_wrk_name, font =('Futura',14), bg = 'white').place(x=350,y=280)
        txt_nationality = Entry(self.root,textvariable = self.var_wrk_nationality, font =('Futura',14), bg = 'white').place(x=800,y=280)
        txt_wage = Entry(self.root,textvariable=self.var_wrk_wage, font =('Futura',14), bg = 'white').place(x=1200,y=280)

        btn_save = Button(self.root,text='Save',command=self.add,font=('futura',14,'bold'),bg = '#4caf50',fg = 'white',cursor='hand2').place(x = 400, y= 400,width = 120,height=30)
        btn_update = Button(self.root,text='Update',command=self.update,font=('futura',14,'bold'),bg = '#4caf50',fg = 'white',cursor='hand2').place(x = 540, y= 400,width = 120,height=30)
        btn_delete = Button(self.root,text='Delete',command=self.delete,font=('futura',14,'bold'),bg = '#4caf50',fg = 'white',cursor='hand2').place(x = 680, y= 400,width = 120,height=30)
        btn_clear = Button(self.root,text='Clear',command= self.clear,font=('futura',14,'bold'),bg = '#4caf50',fg = 'white',cursor='hand2').place(x = 820, y= 400,width = 120,height=30)
        
        emp_frame = Frame(self.root,bd = 3,relief=RIDGE)
        emp_frame.place(x=0,y = 600,relwidth=1,height=360)

        sc_v = Scrollbar(emp_frame,orient=VERTICAL)

        self.table = ttk.Treeview(emp_frame,columns=('id','name','gender','contact','nationality','wage'),yscrollcommand=sc_v.set)
        sc_v.pack(side=RIGHT,fill=Y)
        sc_v.config(command=self.table.yview())
        self.table.heading('id',text = 'Id')
        self.table.heading('name',text = 'Name')
        self.table.heading('gender',text = 'Gender')
        self.table.heading('contact',text = 'Contact')
        self.table.heading('nationality',text = 'Nationality')
        self.table.heading('wage',text = 'Wage')
        self.table['show'] = 'headings'

        self.table.column('id',width = 200)
        self.table.column('name',width = 400)
        self.table.column('gender',width = 100)
        self.table.column('contact',width = 300)
        self.table.column('nationality',width = 300)
        self.table.column('wage',width = 300)

        self.table.pack(fill = BOTH,expand=1)

        self.table.bind('<ButtonRelease-1>',self.get_data)

        self.show()

    def add(self):
        con = sqlite3.connect(database = r'FMS.db')
        cur = con.cursor()
        try:
            if self.var_wrk_id.get() == '' :
                messagebox.showerror('Error',"Id is required",parent = self.root)
            else:
                cur.execute('Select * from worker where id=?',(self.var_wrk_id.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror('Error',"Already Exits",parent = self.root)
                else:
                    cur.execute('Insert into worker (id,name,gender,contact,nationality,wage) values(?,?,?,?,?,?)',(
                                    self.var_wrk_id.get(),
                                    self.var_wrk_name.get(), 
                                    self.var_wrk_gender.get(),
                                    self.var_wrk_contact.get(),
                                    self.var_wrk_nationality.get(),
                                    self.var_wrk_wage.get()
                    ))
                    con.commit()
                    messagebox.showinfo('Success','Worker is added into the databease',parent = self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror('Error',f"Error due to : {str(ex)}",parent = self.root)

    def show(self):
        con = sqlite3.connect(database = r'FMS.db')
        cur = con.cursor()
        try:
            cur.execute('select * from worker')
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
        self.var_wrk_id.set(row[0]),
        self.var_wrk_name.set(row[1]), 
        self.var_wrk_gender.set(row[2]),
        self.var_wrk_contact.set(row[3]),
        self.var_wrk_nationality.set(row[4]),
        self.var_wrk_wage.set(row[5])
    def update(self):
        con = sqlite3.connect(database = r'FMS.db')
        cur = con.cursor()
        try:
            if self.var_wrk_id.get() == '' :
                messagebox.showerror('Error',"Id is required",parent = self.root)
            else:
                cur.execute('Select * from worker where id=?',(self.var_wrk_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror('Error',"Doesn't exist",parent = self.root)
                else:
                    cur.execute('Update worker set name=?,gender=?,contact=?,nationality=?,wage=? where id=?',(
                                    
                                    self.var_wrk_name.get(), 
                                    self.var_wrk_gender.get(),
                                    self.var_wrk_contact.get(),
                                    self.var_wrk_nationality.get(),
                                    self.var_wrk_wage.get(),
                                    self.var_wrk_id.get()
                    ))
                    con.commit()
                    messagebox.showinfo('Success','Worker is updated',parent = self.root)
                    self.show()
                    con.close()
        except Exception as ex:
            messagebox.showerror('Error',f"Error due to : {str(ex)}",parent = self.root)

    def delete(self):
        con = sqlite3.connect(database = r'FMS.db')
        cur = con.cursor()
        try:
            if self.var_wrk_id.get() == '' :
                messagebox.showerror('Error',"Id is required",parent = self.root)
            else:
                op = messagebox.askyesno('Confirm','Do you really want to delete?',parent=self.root)
                if op == True:
                    cur.execute('delete from worker where id=?',(self.var_wrk_id.get(),))
                    con.commit()
                    messagebox.showinfo('Delete','Deleted',parent = self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror('Error',f"Error due to : {str(ex)}",parent = self.root)
    
    def clear(self):
        self.var_wrk_id.set(""),
        self.var_wrk_name.set(""), 
        self.var_wrk_gender.set("Select"),
        self.var_wrk_contact.set(""),
        self.var_wrk_nationality.set(""),
        self.var_wrk_wage.set("")
        self.var_searchtext.set('')
        self.show()
    
    def search(self):
        con = sqlite3.connect(database = r'FMS.db')
        cur = con.cursor()
        try:
            if self.var_searchtype.get() =='Select' :
                messagebox.showerror('Error','Invalid Type',parent = self.root)
                cur.execute('select * from worker')
            elif self.var_searchtext.get() =='':
                messagebox.showerror('Error','Empty Text',parent = self.root)
            else:
                cur.execute("select * from worker where "+self.var_searchtype.get()+" LIKE '%"+self.var_searchtext.get()+"%'")
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
    obj = Employee(root)
    root.mainloop()