from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
class Results:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        #===Bg Image===
        self.bg=ImageTk.PhotoImage(file="/Users/nithyasanthoshini/Desktop/rms/rms/images/BG3.png")
        #self.bg=ImageTk.PhotoImage(file="images/BG.png")
        bg=Label(self.root,image=self.bg).place(anchor="center",relx=0.5,rely=0.5)

        #===left Image===
        self.left=ImageTk.PhotoImage(file="/Users/nithyasanthoshini/Desktop/rms/rms/images/Left.png")
        left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)

        #====Register Frame=====
        frame1=Frame(self.root, bg= "white")
        frame1.place(x=480, y=100, width=700, height=500)

        title=Label(frame1, text= "VIEW RESULTS HERE" ,font=("times new roman" ,20, "bold"),bg="white",fg='green').place(x=50,y=30)

        #-------------------ROW1---------------------
        f_name=Label(frame1, text= "First Name" ,font=("times new roman" ,15, "bold"),bg="white",fg='purple').place(x=10,y=100)
        txt_fname=Entry(frame1, font= ("times new roman" ,15),bg= "lightgray",fg='black') .place(x=10, y=130, width=180)

        HallTicket=Label(frame1, text= "HallTicket No" ,font=("times new roman" ,15, "bold"),bg="white",fg='purple').place(x=200,y=100)
        txt_HallTicket=Entry(frame1, font= ("times new roman" ,15),bg= "lightgray",fg='black') .place(x=200, y=130, width=180)

        Answer=Label(frame1, text= "Department" ,font=("times new roman" ,15, "bold"),bg="white",fg='purple').place(x=400,y=100)
        txt_Answer=Entry(frame1, font= ("times new roman" ,15),bg= "lightgray",fg='black') .place(x=400, y=130, width=180)

        #--------------------Row2
        First_Y=Label(frame1, text= "First Year" ,font=("times new roman" ,15, "bold"),bg="white",fg='purple').place(x=80,y=170)
        btn=Button(frame1, text="1-1",font=("times new roman" ,15, "bold"),bg="green",fg='green').place(x=200,y=170)

        btn=Button(frame1, text="1-2",font=("times new roman" ,15, "bold"),bg="green",fg='green').place(x=370,y=170)


        #--------------------Row3
        Second_Y=Label(frame1, text= "Second Year" ,font=("times new roman" ,15, "bold"),bg="white",fg='purple').place(x=80,y=240)
        btn=Button(frame1, text="2-1",font=("times new roman" ,15, "bold"),bg="green",fg='green').place(x=200,y=240)

        btn=Button(frame1, text="2-2",font=("times new roman" ,15, "bold"),bg="green",fg='green').place(x=370,y=240)

        #--------------------Row4
        Third_Y=Label(frame1, text= "Third Year" ,font=("times new roman" ,15, "bold"),bg="white",fg='purple').place(x=80,y=310)
        btn=Button(frame1, text="3-1",font=("times new roman" ,15, "bold"),bg="green",fg='green').place(x=200,y=310)

        btn=Button(frame1, text="3-2",font=("times new roman" ,15, "bold"),bg="green",fg='green').place(x=370,y=310)

        #--------------------Row5
        Fourth_Y=Label(frame1, text= "Fourth Year" ,font=("times new roman" ,15, "bold"),bg="white",fg='purple').place(x=80,y=380)
        btn=Button(frame1, text="4-1",font=("times new roman" ,15, "bold"),bg="green",fg='green').place(x=200,y=380)

        btn=Button(frame1, text="4-2",font=("times new roman" ,15, "bold"),bg="green",fg='green').place(x=370,y=380)


        #--------------------Row3
    
        #email=Label(frame1, text= "Email" ,font=("times new roman" ,15, "bold"),bg="white",fg='purple').place(x=370,y=170)
        #txt_email=Entry(frame1, font= ("times new roman" ,15),bg= "lightgray",fg='black') .place(x=370, y=200, width=250)

        #--------------------Row3
        #question=Label(frame1, text= "B.Tech Regulation" ,font=("times new roman" ,15, "bold"),bg="white",fg='purple').place(x=50,y=240)
        

        #cmb_question=ttk.Combobox(frame1, font= ("times new roman" ,13), state='read only' , justify=CENTER) 
        #cmb_question['values']=("Select" , "r18", "r19" , "r20", "r21", "r22")
        #cmb_question.place(x=50, y=270, width=250)
       # cmb_question.current(0)

       # Answer=Label(frame1, text= "Department" ,font=("times new roman" ,15, "bold"),bg="white",fg='purple').place(x=370,y=240)
       #txt_Answer=Entry(frame1, font= ("times new roman" ,15),bg= "lightgray",fg='black') .place(x=370, y=270, width=250)

        #--------------------Row4-----
       # Password=Label(frame1, text= "Password" ,font=("times new roman" ,15, "bold"),bg="white",fg='purple').place(x=50,y=310)
       # txt_Password=Entry(frame1, font= ("times new roman" ,15),bg= "lightgray",fg='black') .place(x=50, y=340, width=250)

        #Cpassword=Label(frame1, text= "Confirm Password" ,font=("times new roman" ,15, "bold"),bg="white",fg='purple').place(x=370,y=310)
        #txt_Cpassword=Entry(frame1, font= ("times new roman" ,15),bg= "lightgray",fg='black') .place(x=370, y=340, width=250)

        #----------terms------
        #chk=Checkbutton(frame1,text="I Agree The Terms & Conditions", onvalue=1 , offvalue=0 ,bg="white",fg='purple',font=("times new roman",12)).place(x=50,y=380)

       # btn=Button(frame1, text="REGISTER NOW",font=("times new roman" ,15, "bold"),bg="green",fg='green').place(x=50,y=420)
       # btn_signin=Button(frame1, text="OR SIGN IN",font=("times new roman" ,15, "bold"),bg="green",fg='green').place(x=50,y=460)


root=Tk()
obj=Results(root)
root .mainloop()