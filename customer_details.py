from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter.messagebox import *
def fun_customer_details():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Vishu@8848",
        database='hotel_management',
        auth_plugin='mysql_native_password'
    )


    r=Tk()
    r.title('Customer details')
    r.geometry('1300x590+230+220')
    r.resizable(False, False)


    def save():
        if(entry_name.get()=='' or entry_fthr.get()=='' or combx_gender.get()=='' or entry_mail.get()=='' or entry_cntry.get()=='' or combx_id.get()=='' or entry_address.get()==''):
            showerror('error','please fill all necessary details')
        elif(len(entry_phn.get())<10 or len(entry_phn.get())>10):
            showerror('error','please enter a valid phone number')
        elif (len(entry_idno.get()) < 12 or len(entry_phn.get()) >12):
            showerror('error','please fill a valid id number')
        else:
            try:
                mycursor = mydb.cursor()

                sql="select Ref_no from customer"
                mycursor.execute(sql)
                d = mycursor.fetchall()
                for i in d:
                    c=i

                ref=int(c[len(c) - 1])


                sql = "INSERT INTO customer (Ref_no,Name,Father_Name,Gender,Phone_no,E_mail,Nationality,ID_Proof,ID_no,Address) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val = (str(ref+1),entry_name.get(),entry_fthr.get(),combx_gender.get(),entry_phn.get(),entry_mail.get(),entry_cntry.get(),combx_id.get(),entry_idno.get(),entry_address.get())
                mycursor.execute(sql, val)

                mydb.commit()
                fetch_data()

                showinfo('information','Customer details added successfully')


            except:
                showerror('error','something went wrong, try again later !')


    def update():
        if (entry_name.get() == '' or entry_fthr.get() == '' or combx_gender.get() == '' or entry_mail.get() == '' or entry_cntry.get() == '' or combx_id.get() == '' or entry_address.get() == ''):
            showerror('error', 'please fill all necessary details')
        elif (len(entry_phn.get()) < 10 or len(entry_phn.get()) > 10):
            showerror('error', 'please enter a valid phone number')

        elif (len(entry_idno.get()) < 12 or len(entry_idno.get()) > 12):
             showerror('error','please fill a valid id number')
        else:
            try:

                mycursor = mydb.cursor()

                sql = "UPDATE customer SET Name =%s, Father_Name =%s,Gender=%s,E_mail=%s,Nationality=%s,ID_Proof=%s,ID_no=%s,Address=%s WHERE Phone_no =%s"
                val = (entry_name.get(),entry_fthr.get(),combx_gender.get(),entry_mail.get(),entry_cntry.get(),combx_id.get(),entry_idno.get(),entry_address.get(),entry_phn.get())

                mycursor.execute(sql, val)

                mydb.commit()
                fetch_data()

                showinfo('information','Details updated Successfully')


            except:
                showerror('error','Something went wrong, try again later !')

    def delete():

        if (len(entry_phn.get()) < 10 or len(entry_phn.get()) > 10):
            showerror('error', 'please enter a valid phone number')
        else:
            try:

                mycursor = mydb.cursor()

                sql = "DELETE FROM customer WHERE Phone_no = %s"
                val = (entry_phn.get(),)

                mycursor.execute(sql, val)

                mydb.commit()
                fetch_data()

                showinfo('information','Details deleted')



            except:
                showerror('error','Something went wrong, try again later !')





    def reset():
        entry_ref.delete(0,END)
        entry_name.delete(0,END)
        entry_fthr.delete(0,END)
        combx_gender.current(0)
        entry_phn.delete(0,END)
        entry_mail.delete(0,END)
        entry_cntry.delete(0,END)
        combx_id.current(0)
        entry_idno.delete(0,END)
        entry_address.delete(0,END)

    def fetch_data():

        mycursor=mydb.cursor()
        mycursor.execute("Select * from customer")
        rows=mycursor.fetchall()
        if len(rows)!=0:
            cust_details_table.delete(*cust_details_table.get_children())
            for i in rows:
                cust_details_table.insert('',END,values=i)
            mydb.commit()


    def search():

        mycursor = mydb.cursor()

        mycursor.execute("select * from customer where "+str(combbx_srch.get())+" LIKE '%"+str(entry_srch.get())+"%'")
        rows=mycursor.fetchall()
        if len(rows)!=0:
            cust_details_table.delete(*cust_details_table.get_children())
            for i in rows:
                cust_details_table.insert("",END,values=i)
            mydb.commit()
        else:
            showerror('error','Not found, try again !')


    def get_cursor(event):
        cursor_row=cust_details_table.focus()
        content=cust_details_table.item(cursor_row)
        row=content['values']

        if(entry_ref.get()!='' or entry_name.get()!='' or entry_fthr.get()!='' or combx_gender.get()!='' or entry_phn.get()!='' or entry_mail.get()!='' or entry_cntry.get()!='' or combx_id.get()!='' or entry_idno.get()!='' or entry_address.get()!=''):
            reset()

        entry_ref.insert(END,row[0])
        entry_name.insert(END,row[1])
        entry_fthr.insert(END,row[2])
        combx_gender.current(t1.index(row[3]))
        entry_phn.insert(END,row[4])
        entry_mail.insert(END,row[5])
        entry_cntry.insert(END,row[6])
        combx_id.current(t2.index(row[7]))
        entry_idno.insert(END,row[8])
        entry_address.insert(END,row[9])



    f1=Frame(r,border=1,relief=RIDGE)
    f1.place(x=0,y=0,width=1324,height=70)

    f2=LabelFrame(r,border=2,relief=RIDGE,text='Customer Details',font=('areal',10,'bold'))
    f2.place(x=0,y=70,width=510,height=490)

    f3=LabelFrame(r,border=2,relief=RIDGE,text='View and Search Details',font=('areal',10,'bold'))
    f3.place(x=510,y=70,width=780,height=490)

    f4=Frame(f3,border=2,relief=RIDGE)
    f4.place(x=10,y=50,width=760,height=390)

    main_lbl=Label(f1,text='ADD CUSTOMER DETAILS',anchor=CENTER,background='black',foreground='gold',font=('Britannic Bold',30))
    main_lbl.place(x=0,y=0,width=1324,height=70)


    lbl_ref=Label(f2,text='Customer Reference:',font=(8))
    lbl_ref.place(x=10,y=0)
    lbl_name=Label(f2,text='Name:',font=(8))
    lbl_name.place(x=10,y=40)
    lbl_fthr=Label(f2,text="Father's Name:",font=(8))
    lbl_fthr.place(x=10,y=80)
    lbl_gender=Label(f2,text='Gender:',font=(8))
    lbl_gender.place(x=10,y=120)
    lbl_phn=Label(f2,text='Phone no:',font=(8))
    lbl_phn.place(x=10,y=160)
    lbl_mail=Label(f2,text='E-mail:',font=(8))
    lbl_mail.place(x=10,y=200)
    lbl_cntry=Label(f2,text='Nationality:',font=(8))
    lbl_cntry.place(x=10,y=240)
    lbl_id=Label(f2,text='ID Proof:',font=(8))
    lbl_id.place(x=10,y=280)
    lbl_idno=Label(f2,text='ID Number:',font=(8))
    lbl_idno.place(x=10,y=320)
    lbl_adrss=Label(f2,text='Address:',font=(8))
    lbl_adrss.place(x=10,y=360)



    entry_ref=ttk.Entry(f2,width=25,font=(2),state='disable')
    entry_ref.place(x=220,y=0)
    entry_name=ttk.Entry(f2,width=25,font=(2))
    entry_name.place(x=220,y=40)
    entry_fthr=ttk.Entry(f2,width=25,font=(2))
    entry_fthr.place(x=220,y=80)
    entry_phn=ttk.Entry(f2,width=25,font=(2))
    entry_phn.place(x=220,y=160)
    entry_mail=ttk.Entry(f2,width=25,font=(2))
    entry_mail.place(x=220,y=200)
    entry_cntry=ttk.Entry(f2,width=25,font=(2))
    entry_cntry.place(x=220,y=240)
    entry_idno=ttk.Entry(f2,width=25,font=(2))
    entry_idno.place(x=220,y=320)
    entry_address=ttk.Entry(f2,width=25,font=(2))
    entry_address.place(x=220,y=360)





    t1=tuple(('Male','Female','Other'))
    combx_gender=ttk.Combobox(f2,values=t1, state="readonly",font=(2))
    combx_gender.place(x=220,y=120,width=280)

    t2=tuple(('Adhar Card','Driving Liscence'))
    combx_id=ttk.Combobox(f2,values=t2, state="readonly",font=(2))
    combx_id.place(x=220,y=280,width=280)

    lbl_srch=Label(f3,text='Search by:',font=('arial'),background='red',foreground='white')
    lbl_srch.grid(row=0,column=0)

    search_var=StringVar()
    t5=tuple(('Phone_no', 'Ref_no', 'Name', 'Father_Name'))
    combbx_srch=ttk.Combobox(f3,state='readonly',values=t5,width=15,font=('arial',17),textvariable=search_var)

    combbx_srch.grid(row=0,column=1)
    combbx_srch.current(0)

    txt_search=StringVar()
    entry_srch=ttk.Entry(f3,font=('areal',17),textvariable=txt_search,width=15)
    entry_srch.grid(row=0,column=2)
    btn_srch=Button(f3,text='Search',font=('arial',15,'bold'),cursor='hand2',background='black',foreground='gold',command=search)
    btn_srch.grid(row=0,column=3)
    btn_show=Button(f3,text='Show all',font=('arial',15,'bold'),cursor='hand2',background='black',foreground='gold',command=fetch_data)
    btn_show.grid(row=0,column=4)

    scroll_x = ttk.Scrollbar(f4, orient=HORIZONTAL)
    scroll_y = ttk.Scrollbar(f4, orient=VERTICAL)

    cust_details_table=ttk.Treeview(f4,columns=('Ref_no','Name','Father_Name','Gender','Phone_no','E-mail','Nationality','ID_Proof','ID_no','Address'),xscrollcommand=scroll_x,yscrollcommand=scroll_y)

    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)

    scroll_x.config(command=cust_details_table.xview)
    scroll_y.config(command=cust_details_table.yview)

    cust_details_table.heading('Ref_no',text='Ref_no')
    cust_details_table.heading('Name',text='Name')
    cust_details_table.heading('Father_Name',text='Father_Name')
    cust_details_table.heading('Gender',text='Gender')
    cust_details_table.heading('Phone_no',text='Phone_no')
    cust_details_table.heading('E-mail',text='E-mail')
    cust_details_table.heading('Nationality',text='Nationality')
    cust_details_table.heading('ID_Proof',text='ID_Proof')
    cust_details_table.heading('ID_no',text='ID_no')
    cust_details_table.heading('Address',text='Address')

    cust_details_table['show']='headings'

    cust_details_table.column('Ref_no',width=100)
    cust_details_table.column('Name',width=100)
    cust_details_table.column('Father_Name',width=100)
    cust_details_table.column('Gender',width=100)
    cust_details_table.column('Phone_no',width=100)
    cust_details_table.column('E-mail',width=100)
    cust_details_table.column('Nationality',width=100)
    cust_details_table.column('ID_Proof',width=100)
    cust_details_table.column('ID_no',width=100)
    cust_details_table.column('Address',width=100)

    cust_details_table.pack(fill=BOTH,expand=1)
    cust_details_table.bind("<ButtonRelease-1>",get_cursor)
    fetch_data()


    save_btn=Button(r,text='SAVE',width=7,cursor='hand1',anchor=CENTER,font=('Britannic Bold',18), foreground="gold", background="black",command=save)
    save_btn.place(x=30,y=500)
    update_btn=Button(r,text='UPDATE',width=7,cursor='hand1',anchor=CENTER,font=('Britannic Bold',18), foreground="gold", background="black",command=update)
    update_btn.place(x=140,y=500)
    dlt_btn=Button(r,text='DELETE',width=7,cursor='hand1',anchor=CENTER,font=('Britannic Bold',18), foreground="gold", background="black",command=delete)
    dlt_btn.place(x=250,y=500)
    rst_btn=Button(r,text='RESET',width=7,cursor='hand1',anchor=CENTER,font=('Britannic Bold',18), foreground="gold", background="black",command=reset)
    rst_btn.place(x=360,y=500)

    r.mainloop()

