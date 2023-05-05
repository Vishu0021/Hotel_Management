from tkinter import *
from tkcalendar import *
from tkinter import ttk
from datetime import datetime
import mysql.connector
from tkinter.messagebox import *
def fun_room_booking():
    r=Tk()
    r.title('Room booking')
    r.geometry('1300x590+230+220')
    r.resizable(False, False)

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Vishu@8848",
        database='hotel_management',
        auth_plugin='mysql_native_password'
    )
    def save():
        if(entry_chkin.get()=='' or combbx_room.get()=='' or entry_roomno.get()==''):
            showerror('error','please fill all necessary details')
        elif(len(entry_phn.get())>10 or len(entry_phn.get())<10):
            showerror('error','please fill a valid phone number')
        else:
            mycursor = mydb.cursor()
            sql = "INSERT INTO room_booking (Phone_no,chkin_date,chkout_date,Room_type,Room_no,No_of_days,Total_amount,Discount,Total_cost) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (entry_phn.get(),entry_chkin.get(),entry_chkout.get(),combbx_room.get(),entry_roomno.get(),entry_days.get(),entry_amount.get(),entry_discount.get(),entry_total.get())
            mycursor.execute(sql, val)
            mydb.commit()
            fetch_data()
            showinfo('information', 'Customer details added successfully')



    def update():
        if (entry_chkin.get() == ''or combbx_room.get() == '' or entry_roomno.get() == '' or entry_days.get()=='' or entry_amount.get()=='' or entry_discount.get()=='' or entry_total.get()=='' ):
            showerror('error', 'please fill all necessary details')
        elif (len(entry_phn.get()) > 10 or len(entry_phn.get()) < 10):
            showerror('error', 'please fill a valid phone number')
        else:
            try:
                mycursor = mydb.cursor()

                sql = "UPDATE room_booking SET chkin_date=%s,chkout_date=%s,Room_type=%s,Room_no=%s,No_of_days=%s,Total_amount=%s,Discount=%s,Total_cost=%s WHERE Phone_no =%s"
                val = (entry_chkin.get(), entry_chkout.get(), combbx_room.get(), entry_roomno.get(), entry_days.get(), entry_amount.get(),entry_discount.get(), entry_total.get(), entry_phn.get())

                mycursor.execute(sql, val)

                mydb.commit()
                fetch_data()
                showinfo('information', 'Details updated Successfully')

            except:
                showerror('error','Something went wrong, try again later !')
    def delete():
        if (len(entry_phn.get()) > 10 or len(entry_phn.get()) < 10):
            showerror('error', 'please enter a valid phone number')
        else:
            try:
                mycursor = mydb.cursor()

                sql = "DELETE FROM room_booking WHERE Phone_no = %s"
                val = (entry_phn.get(),)

                mycursor.execute(sql, val)

                mydb.commit()
                fetch_data()
                showinfo('information', 'Details deleted')

            except:
                showerror('error','Something went wrong, try again later !')
    def reset():
        entry_phn.delete(0,END)
        entry_chkin.delete(0,END)
        entry_chkout.delete(0,END)
        combbx_room.current(0)
        entry_roomno.delete(0,END)
        entry_days.delete(0,END)
        entry_amount.delete(0,END)
        entry_discount.delete(0,END)
        entry_total.delete(0,END)

    def fetch_data():

        mycursor=mydb.cursor()
        mycursor.execute("Select * from room_booking")
        rows=mycursor.fetchall()
        if len(rows)!=0:
            cust_room_table.delete(*cust_room_table.get_children())
            for i in rows:
                cust_room_table.insert('',END,values=i)
            mydb.commit()

    def get_cursor(event):
        cursor_row=cust_room_table.focus()
        content=cust_room_table.item(cursor_row)
        row=content['values']
        if(entry_phn.get()!='' or entry_chkin.get()!='' or entry_chkout.get()!='' or combbx_room.get()!='' or entry_roomno.get()!='' or entry_days.get()!='' or entry_amount.get()!='' or entry_discount.get()!='' or entry_total.get()!=''):
            reset()
        entry_phn.insert(END,row[0])
        entry_chkin.insert(END,row[1])
        entry_chkout.insert(END,row[2])
        combbx_room.current(t1.index(row[3]))
        entry_roomno.insert(END,row[4])
        entry_days.insert(END,row[5])
        entry_amount.insert(END,row[6])
        entry_discount.insert(END,row[7])
        entry_total.insert(END,row[8])

    def search():

        mycursor = mydb.cursor()

        mycursor.execute("select * from room_booking where "+str(combbx_srch.get())+" LIKE '%"+str(entry_srch.get())+"%'")
        rows=mycursor.fetchall()
        if len(rows)!=0:
            cust_room_table.delete(*cust_room_table.get_children())
            for i in rows:
                cust_room_table.insert("",END,values=i)
            mydb.commit()


    def fetch__data():
        if (entry_phn.get()==''):
            showerror('error','please enter a valid mobile number',parent=r)
        else:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Vishu@8848",
                database='hotel_management',
                auth_plugin='mysql_native_password'
            )

            mycursor = mydb.cursor()
            sql = "select Name from customer where Phone_no=%s"
            val = (entry_phn.get(),)
            mycursor.execute(sql, val)
            row = mycursor.fetchone()

            if (row==None):
                showerror('error', 'Contact number not found, check it again !')
            else:
                save_btn['state']='normal'
                mydb.commit()


    def calculate():
        indate=entry_chkin.get()
        outdate=entry_chkout.get()
        indate=datetime.strptime(indate,'%m/%d/%y')
        outdate=datetime.strptime(outdate,'%m/%d/%y')
        entry_days.insert(END,abs(outdate-indate).days)

        if(combbx_room.get()=='Ac'):
            days=entry_days.get()
            x=1200*int(days)
            entry_amount.insert(END,x)
        elif(combbx_room.get()=='Non-Ac'):
            days=entry_days.get()
            x=900 * int(days)
            entry_amount.insert(END,x)
        else:
            days=entry_days.get()
            x=700*int(days)
            entry_amount.insert(END,x)


        amount = int(entry_amount.get())



        if(int(days)>=10):
            dis=amount*10/100
            entry_discount.insert(END,str(dis))

            entry_total.insert(END,amount - dis)
        elif(int(days)>=5):
            dis=amount*5/100
            entry_discount.insert(END,str(dis))

            entry_total.insert(END,amount - dis)
        else:
            dis=0
            entry_discount.insert(END,str(dis))
            entry_total.insert(END,amount - dis)




    f1=Frame(r,border=1,relief=RIDGE)
    f1.place(x=0,y=0,width=1324,height=70)

    f2 = LabelFrame(r, border=2, relief=RIDGE, text='Room Booking Details', font=('areal', 10, 'bold'))
    f2.place(x=0, y=70, width=510, height=490)

    f3 = LabelFrame(r, border=2, relief=RIDGE, text='View and Search Details', font=('areal', 10, 'bold'))
    f3.place(x=510, y=70, width=780, height=490)

    f4 = Frame(f3, border=2, relief=RIDGE)
    f4.place(x=10, y=50, width=760, height=390)


    main_lbl=Label(f1,text='ROOM BOOKING',anchor=CENTER,background='black',foreground='gold',font=('Britannic Bold',30))
    main_lbl.place(x=0,y=0,width=1324,height=70)

    lbl_phn=Label(f2,text='Phone no:',font=(8))
    lbl_phn.place(x=10,y=0)
    lbl_chkin=Label(f2,text='Check-in Date:',font=(8))
    lbl_chkin.place(x=10,y=40)
    lbl_chkout=Label(f2,text='Check-out Date:',font=(8))
    lbl_chkout.place(x=10,y=80)
    lbl_room=Label(f2,text='Room Type:',font=(8))
    lbl_room.place(x=10,y=120)
    lbl_roomno=Label(f2,text='Room no:',font=(8))
    lbl_roomno.place(x=10,y=160)
    lbl_days=Label(f2,text='No. Of Days:',font=(8))
    lbl_days.place(x=10,y=200)
    lbl_amount=Label(f2,text='Total Amount:',font=(8))
    lbl_amount.place(x=10,y=240)
    lbl_discount=Label(f2,text='Discount:',font=(8))
    lbl_discount.place(x=10,y=280)
    lbl_total=Label(f2,text='Total Cost:',font=(8))
    lbl_total.place(x=10,y=320)

    entry_phn=Entry(f2,width=25,font=(2))
    entry_phn.place(x=220,y=0)
    entry_chkin=DateEntry(f2,selectmode='day',font=(8))
    entry_chkin.place(x=220,y=40,width=280)
    entry_chkout=DateEntry(f2,selectmode='year',font=(8))
    entry_chkout.place(x=220,y=80,width=280)
    entry_roomno=Entry(f2,width=25,font=(2))
    entry_roomno.place(x=220,y=160,width=280)
    entry_days=Entry(f2,width=25,font=(2))
    entry_days.place(x=220,y=200)
    entry_amount=Entry(f2,width=25,font=(2))
    entry_amount.place(x=220,y=240)
    entry_discount=Entry(f2,width=25,font=(2))
    entry_discount.place(x=220,y=280)
    entry_total=Entry(f2,width=25,font=(2))
    entry_total.place(x=220,y=320)

    t1=tuple(('Ac','Non-Ac','Non-Ac & Non-Attach Bathroom'))
    combbx_room=ttk.Combobox(f2,values=t1,state='readonly',font=(2))
    combbx_room.place(x=220,y=120,width=280)

    btn1=Button(r,text='Calculate',width=7,cursor='hand1',anchor=CENTER,font=('Brush Script MT',15),background='black',foreground='gold',command=calculate)
    btn1.place(x=37,y=440)
    save_btn = Button(r, text='SAVE', width=7, cursor='hand1',state='disabled' ,anchor=CENTER, font=('Britannic Bold', 18),foreground="gold", background="black",command=save)
    save_btn.place(x=30, y=480)
    update_btn = Button(r, text='UPDATE', width=7, cursor='hand1', anchor=CENTER, font=('Britannic Bold', 18),foreground="gold", background="black",command=update)
    update_btn.place(x=140, y=480)
    dlt_btn = Button(r, text='DELETE', width=7, cursor='hand1', anchor=CENTER, font=('Britannic Bold', 18),foreground="gold", background="black",command=delete)
    dlt_btn.place(x=250, y=480)
    rst_btn = Button(r, text='RESET', width=7, cursor='hand1', anchor=CENTER, font=('Britannic Bold', 18),foreground="gold", background="black",command=reset)
    rst_btn.place(x=360, y=480)


    ftch_btn=Button(f2, text='check',width=7,cursor='hand2',anchor=CENTER,font=('arial',10,'bold'),foreground='gold',background='black',command=fetch__data)
    ftch_btn.place(x=440,y=0)


    lbl_srch = Label(f3, text='Search by:', font=('arial'), background='red', foreground='white')
    lbl_srch.grid(row=0, column=0)

    search_var = StringVar()
    t5 = tuple(('Phone_no',))
    combbx_srch = ttk.Combobox(f3, state='readonly', values=t5, width=15, font=('arial', 17), textvariable=search_var)
    combbx_srch.grid(row=0, column=1)
    combbx_srch.current(0)

    txt_search = StringVar()
    entry_srch = ttk.Entry(f3, font=('areal', 17), textvariable=txt_search, width=15)
    entry_srch.grid(row=0, column=2)
    btn_srch = Button(f3, text='Search', font=('arial', 15, 'bold'), cursor='hand2', background='black',
                      foreground='gold',command=search)
    btn_srch.grid(row=0, column=3)
    btn_show = Button(f3, text='Show all', font=('arial', 15, 'bold'), cursor='hand2', background='black',
                      foreground='gold',command=fetch_data)
    btn_show.grid(row=0, column=4)

    scroll_x = ttk.Scrollbar(f4, orient=HORIZONTAL)
    scroll_y = ttk.Scrollbar(f4, orient=VERTICAL)

    cust_room_table = ttk.Treeview(f4, columns=('Phone_no', 'chkin_date', 'chkout_date', 'Room_type', 'Room_no', 'No_of_days', 'Total_amount', 'Discount', 'Total_cost'),xscrollcommand=scroll_x, yscrollcommand=scroll_y)

    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)

    scroll_x.config(command=cust_room_table.xview)
    scroll_y.config(command=cust_room_table.yview)

    cust_room_table.heading('Phone_no',text='Phone_no')
    cust_room_table.heading('chkin_date',text='chkin_date')
    cust_room_table.heading('chkout_date',text='chkout_date')
    cust_room_table.heading('Room_type',text='Room_type')
    cust_room_table.heading('Room_no',text='Room_no')
    cust_room_table.heading('No_of_days',text='No_of_days')
    cust_room_table.heading('Total_amount',text='Total_amount')
    cust_room_table.heading('Discount',text='Discount')
    cust_room_table.heading('Total_cost',text='Total_cost')

    cust_room_table['show']='headings'

    cust_room_table.column('Phone_no',width=100)
    cust_room_table.column('chkin_date',width=100)
    cust_room_table.column('chkout_date',width=100)
    cust_room_table.column('Room_type',width=100)
    cust_room_table.column('Room_no',width=100)
    cust_room_table.column('No_of_days',width=100)
    cust_room_table.column('Total_amount',width=100)
    cust_room_table.column('Discount',width=100)
    cust_room_table.column('Total_cost',width=100)

    cust_room_table.pack(fill=BOTH, expand=1)
    cust_room_table.bind("<ButtonRelease-1>", get_cursor)
    fetch_data()



    r.mainloop()
