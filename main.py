from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk


r=Tk()
r.title('Hotel Management system')
r.geometry('1550x850')

img2=ImageTk.PhotoImage(file='img2.jpg')
lbl_img2=Label(r,image=img2,border=2,text='SHREE GANGA RAM HOTEL',font=('Broadway',40,'bold'),compound=CENTER,foreground="yellow")
lbl_img2.place(x=0,y=0,width=1550,height=190)


def cust():
    import customer_details
    customer_details.fun_customer_details()



def book():
    import room_booking
    room_booking.fun_room_booking()

def details():
    import room_details
    room_details.fun_details()



def destroy():
    r.destroy()





f1=Frame(r,border=1,relief=RIDGE)
f1.place(x=226,y=190,width=1324,height=620)

lbl_menu=Label(r,text='MENU',anchor=CENTER,font=('Britannic Bold',20,'bold'),border=0,background='black',foreground='gold',relief=RIDGE)
lbl_menu.place(x=0,y=190,width=226,height=50)

btn_frame=Frame(r,border=2,relief=RIDGE)
btn_frame.place(x=0,y=237,width=226,height=180)
r.wm_attributes('-transparentcolor', '#ab23ff')
style = Style()
style.configure("BW.TLabel",anchor=CENTER,font=('Britannic Bold',16), foreground="gold", background="black")

cust_btn=Button(btn_frame,text='CUSTOMER',cursor='hand2',style="BW.TLabel",command=cust)
cust_btn.place(x=0,y=0,width=226,height=44)

book_btn=Button(btn_frame,text='ROOM BOOKING',cursor='hand2',style='BW.TLabel',command=book)
book_btn.place(x=0,y=45,width=226,height=44)

det_btn=Button(btn_frame,text='DETAILS',cursor='hand2',style='BW.TLabel',command=details)
det_btn.place(x=0,y=90,width=226,height=44)

lgout_btn=Button(btn_frame,text='EXIT',cursor='hand2',style='BW.TLabel',command=destroy)
lgout_btn.place(x=0,y=135,width=226,height=44)

img6=ImageTk.PhotoImage(file='img6.jpg')
lbl_img6=Label(f1,image=img6,border=2)
lbl_img6.place(x=0,y=0,width=1324,height=620)

img5=ImageTk.PhotoImage(file='img5.jpg')
lbl_img5=Label(r,image=img5,border=2)
lbl_img5.place(x=0,y=417,width=226,height=210)

img4=ImageTk.PhotoImage(file='img4.jpg')
lbl_img4=Label(r,image=img4,border=2)
lbl_img4.place(x=0,y=627,width=226,height=210)
r.mainloop()
