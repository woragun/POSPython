from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
class Employee:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1600x960+320+120')
        self.root.title('Worker')
        self.root.config(bg = 'white')
        self.root.focus_force()

        self.var_searchtype = StringVar()
        self.var_searchtext = StringVar()
        self.var_searchgender = StringVar()

        self.var_wrk_id = StringVar()
        self.var_wrk_name = StringVar()
        self.var_wrk_gender = StringVar()
        self.var_wrk_contact = StringVar()
        self.var_wrk_nationality = StringVar()
        self.var_wrk_wage = StringVar()

        searchFrame = LabelFrame(self.root,text='Search Worker',font=('futura',12,'bold'),bd = 1,bg = 'white')
        searchFrame.place(x= 400,y=20,width=800, height=80)

        cmb_search = ttk.Combobox(searchFrame,textvariable=self.var_searchtype,values=('Select','Name','Number'),state='readonly',justify=CENTER,font=('futura',14))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search = Entry(searchFrame,textvariable=self.var_searchtext,font=('futura',14)).place(x=200,y = 10,width=200)
        btn_serch = Button(searchFrame,font=('futura',14,'bold'),bg = '#4caf50',fg = 'white',cursor='hand2').place(x = 440,y = 10,width = 150,height=30)

        title = Label(self.root,text='Worker Details',font = ('Futura',16,'bold'),bg = '#0f4d7d',fg='white',justify=CENTER).place(x =300,y=120,width = 1000)

        lbl_wrk_id = Label(self.root,text = 'ID', font =('Futura',14), bg = 'white').place(x=200,y=180)
        lbl_gender = Label(self.root,text = 'Gender', font =('Futura',14), bg = 'white').place(x=650,y=180)
        lbl_contact = Label(self.root,text = 'Contact', font =('Futura',14), bg = 'white').place(x=1050,y=180)

        txt_wrk_id = Entry(self.root,textvariable= self.var_wrk_id, font =('Futura',14), bg = 'white').place(x=350,y=180,width=180)
        cmb_gender = ttk.Combobox(self.root,textvariable=self.var_searchgender,values=('Select','Male','Female'),state='readonly',justify=CENTER,font=('futura',14))
        cmb_gender.place(x=800,y=180,width=180)
        cmb_gender.current(0)
        txt_contact = Entry(self.root,textvariable = self.var_wrk_contact, font =('Futura',14), bg = 'white').place(x=1200,y=180,width=180)

        lbl_wrk_name = Label(self.root,text = 'Name', font =('Futura',14), bg = 'white').place(x=200,y=280)
        lbl_nationality = Label(self.root,text = 'Nationality', font =('Futura',14), bg = 'white').place(x=650,y=280)
        lbl_wage = Label(self.root,text = 'Wage', font =('Futura',14), bg = 'white').place(x=1050,y=280)
        
        txt_wrk_name = Entry(self.root,textvariable=self.var_wrk_name, font =('Futura',14), bg = 'white').place(x=350,y=280)
        txt_nationality = Entry(self.root,textvariable = self.var_wrk_nationality, font =('Futura',14), bg = 'white').place(x=800,y=280)
        txt_wage = Entry(self.root,textvariable=self.var_wrk_wage, font =('Futura',14), bg = 'white').place(x=1200,y=280)

        btn_save = Button(self.root,text='Save',font=('futura',14,'bold'),bg = '#4caf50',fg = 'white',cursor='hand2').place(x = 400, y= 400,width = 120,height=30)
        btn_update = Button(self.root,text='Update',font=('futura',14,'bold'),bg = '#4caf50',fg = 'white',cursor='hand2').place(x = 540, y= 400,width = 120,height=30)
        btn_delete = Button(self.root,text='Delete',font=('futura',14,'bold'),bg = '#4caf50',fg = 'white',cursor='hand2').place(x = 680, y= 400,width = 120,height=30)
        btn_clear = Button(self.root,text='Clear',font=('futura',14,'bold'),bg = '#4caf50',fg = 'white',cursor='hand2').place(x = 820, y= 400,width = 120,height=30)
        
        emp_frame = Frame(self.root,bd = 3,relief=RIDGE)
        emp_frame.place(x=0,y = 600,relwidth=1,height=360)

        sc_v = Scrollbar(emp_frame,orient=VERTICAL)

        self.table = ttk.Treeview(emp_frame,columns=('Id','Name','Gender','Contact','Nationality','Wage'),yscrollcommand=sc_v.set)
        sc_v.pack(side=RIGHT,fill=Y)
        sc_v.config(command=self.table.yview())
        self.table.heading('Id',text = 'Id')
        self.table.heading('Name',text = 'Name')
        self.table.heading('Gender',text = 'Gender')
        self.table.heading('Contact',text = 'Contact')
        self.table.heading('Nationality',text = 'Nationality')
        self.table.heading('Wage',text = 'Wage')
        self.table['show'] = 'headings'

        self.table.column('Id',width = 200)
        self.table.column('Name',width = 400)
        self.table.column('Gender',width = 100)
        self.table.column('Contact',width = 300)
        self.table.column('Nationality',width = 300)
        self.table.column('Wage',width = 300)

        self.table.pack(fill = BOTH,expand=1)



if __name__ == '__main__':
    root = Tk()
    obj = Employee(root)
    root.mainloop()