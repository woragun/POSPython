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

        





if __name__ == '__main__':
    root = Tk()
    obj = Employee(root)
    root.mainloop()