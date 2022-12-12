from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Window")
        self.root.geometry("1350x700+0+0")
        #===Bg Image===
        self.bg=ImageTk.PhotoImage(file="/Users/nithyasanthoshini/Desktop/rms/rms/images/BG3.png")
        bg=Label(self.root,image=self.bg).place(anchor="center",relx=0.5,rely=0.5)
        #====LOGO IMAGE=======
       # self.bg=ImageTk.PhotoImage(file="/Users/nithyasanthoshini/Desktop/rms/rms/images/Left.png")
        #bg=Label(self.root,image=self.bg).place(anchor="se",x=50,y=80)



        #===left Image===
        self.left=ImageTk.PhotoImage(file="/Users/nithyasanthoshini/Desktop/rms/rms/images/Left3.jpg")
        left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)
        #====Register Frame=====
        frame1=Frame(self.root, bg= "White")
        frame1.place(x=480, y=100, width=700, height=500)

        title=Label(frame1, text= "LOGIN HERE" ,font=("times new roman" ,30, "bold"),bg="white",fg='green').place(x=250,y=50)

        email=Label(frame1, text= "Email Address" ,font=("times new roman" ,18, "bold"),bg="white",fg='purple').place(x=250,y=150)
        txt_email=Entry(frame1, font= ("times new roman" ,15),bg= "lightgray",fg='black').place(x=250, y=180, width=350, height=35)
     
        Password=Label(frame1, text= "Password" ,font=("times new roman" ,18, "bold"),bg="white",fg='purple').place(x=250,y=250)
        txt_Password=Entry(frame1, font= ("times new roman" ,15),bg= "lightgray",fg='black') .place(x=250, y=280, width=350,height=35)

        btn=Button(frame1, text="LOGIN",font=("times new roman" ,20, "bold"),bg="green",fg='green').place(x=250,y=340)

        btn=Button(frame1, text="OR REGISTER NEW ACCOUNT",font=("times new roman" ,15, "bold"),bg="green",fg='green').place(x=250,y=400)








root=Tk()
obj=Login(root)
root .mainloop()
