from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter.messagebox import *

def fun_details():
    r=Tk()
    r.title('Room details')
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
        if (entry_floor.get() == '' or entry_roomno.get() == '' or combbx_room.get() == ''):
            showerror('error', 'Please fill all necessary details')
        else:
            try:
                mycursor = mydb.cursor()
                sql = "INSERT INTO room_details (Floor,Room_no,Room_type) values(%s,%s,%s)"
                val = (entry_floor.get(),entry_roomno.get(),combbx_room.get())
                mycursor.execute(sql, val)
                mydb.commit()
                showinfo('information','Details saved successfully')
            except:
                showerror('error','Something went wrong, try again later !')
    def update():
        if(entry_floor.get()=='' or entry_roomno.get()=='' or combbx_room.get()==''):
            showerror('error','Please fill all necessary details')
        else:
            try:
                mycursor = mydb.cursor()

                sql = "UPDATE room_details SET Floor=%s,Room_type=%s WHERE Room_no =%s"
                val = (entry_floor.get(),combbx_room.get(),entry_roomno.get())

                mycursor.execute(sql, val)

                mydb.commit()
                showinfo('information','Details updated successfully')
            except:
                showerror('error','Something went wrong,try again !')
    def delete():
        if(entry_roomno.get()==''):
            showerror('error','fill room number')
        else:
            try:
                mycursor = mydb.cursor()

                sql = "DELETE FROM room_details WHERE Room_no = %s"
                val = (entry_roomno.get(),)

                mycursor.execute(sql, val)

                mydb.commit()
                showinfo('information', 'Details deleted successfully')
            except:
                showerror('error','something went wrong, try again later !')
    def reset():

        entry_floor.delete(0, END)
        entry_roomno.delete(0, END)
        combbx_room.current(0)

    def fetch_data():

        mycursor=mydb.cursor()
        mycursor.execute("Select * from room_details")
        rows=mycursor.fetchall()
        if len(rows)!=0:
            room_details.delete(*room_details.get_children())
            for i in rows:
                room_details.insert('',END,values=i)
            mydb.commit()


    def get_cursor(event):
        cursor_row = room_details.focus()
        content = room_details.item(cursor_row)
        row = content['values']

        if (entry_floor.get()!='' or entry_roomno.get()!='' or combbx_room.get()!=''):
            reset()

        entry_floor.insert(END, row[0])
        entry_roomno.insert(END, row[1])
        combbx_room.current(t1.index(row[2]))



    f1 = Frame(r, border=2, relief=RIDGE)
    f1.place(x=0, y=0, width=1324, height=70)

    f2 = LabelFrame(r, border=2, relief=RIDGE, text='Add Rooms', font=('areal', 10, 'bold'))
    f2.place(x=50, y=80, width=450, height=420)

    f3 = LabelFrame(r, border=2, relief=RIDGE, text='Room Details', font=('areal', 10, 'bold'))
    f3.place(x=510, y=80, width=780, height=420)


    main_lbl = Label(f1, text='ROOM DETAILS', anchor=CENTER, background='black', foreground='gold',font=('Britannic Bold', 30))
    main_lbl.place(x=0, y=0, width=1324, height=70)


    lbl_floor=Label(f2,text='Floor:',font=('arial',15,'bold'))
    lbl_floor.place(x=0,y=0)
    lbl_roomno=Label(f2,text='Room_no:',font=('arial',15,'bold'))
    lbl_roomno.place(x=0,y=40)
    lbl_room=Label(f2,text='Room_type:',font=('arial',15,'bold'))
    lbl_room.place(x=0,y=80)

    entry_floor=Entry(f2,width=15,font=('arial',15))
    entry_floor.place(x=160,y=0)
    entry_roomno=Entry(f2,width=15,font=('arial',15))
    entry_roomno.place(x=160,y=40)

    t1=tuple(('Ac','Non-Ac','Non-Ac & Non-Attach Bathroom'))
    combbx_room=ttk.Combobox(f2,values=t1,state='readonly',font=('arial',15))
    combbx_room.place(x=160,y=80,width=170)
    combbx_room.current(0)

    save_btn = Button(f2, text='SAVE', width=7, cursor='hand1', anchor=CENTER,font=('Britannic Bold', 18), foreground="gold", background="black", command=save)
    save_btn.place(x=10, y=180)
    update_btn = Button(f2, text='UPDATE', width=7, cursor='hand1', anchor=CENTER, font=('Britannic Bold', 18),foreground="gold", background="black", command=update)
    update_btn.place(x=120, y=180)
    dlt_btn = Button(f2, text='DELETE', width=7, cursor='hand1', anchor=CENTER, font=('Britannic Bold', 18),foreground="gold", background="black", command=delete)
    dlt_btn.place(x=230, y=180)
    rst_btn = Button(f2, text='RESET', width=7, cursor='hand1', anchor=CENTER, font=('Britannic Bold', 18),foreground="gold", background="black", command=reset)
    rst_btn.place(x=340, y=180)

    scroll_x = ttk.Scrollbar(f3, orient=HORIZONTAL)
    scroll_y = ttk.Scrollbar(f3, orient=VERTICAL)

    room_details = ttk.Treeview(f3, columns=('Floor','Room_no','Room_type'), xscrollcommand=scroll_x, yscrollcommand=scroll_y)

    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)

    scroll_x.config(command=room_details.xview)
    scroll_y.config(command=room_details.yview)

    room_details.heading('Floor', text='Floor')
    room_details.heading('Room_no', text='Room_no')
    room_details.heading('Room_type', text='Room_type')

    room_details['show'] = 'headings'

    room_details.column('Floor', width=100)
    room_details.column('Room_no', width=100)
    room_details.column('Room_type', width=100)

    room_details.pack(fill=BOTH, expand=1)
    room_details.bind("<ButtonRelease-1>", get_cursor)
    fetch_data()

    r.mainloop()
