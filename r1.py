from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
class R1:
    def __init__(self,root):
        self.root=root
        self.root.title("1-1")
        self.root.geometry("1350x700+0+0")

        #===Bg Image===
        self.bg=ImageTk.PhotoImage(file="/Users/nithyasanthoshini/Desktop/rms/rms/images/BG3.png")
        #self.bg=ImageTk.PhotoImage(file="images/BG.png")
        bg=Label(self.root,image=self.bg).place(anchor="center",relx=0.5,rely=0.5)

        #===left Image===
        self.left=ImageTk.PhotoImage(file="/Users/nithyasanthoshini/Desktop/rms/rms/images/Left.png")
        left=Label(self.root,image=self.left).place(x=50,y=100,width=400,height=500)

        frame1=Frame(self.root, bg= "White")
        frame1.place(x=380, y=100, width=900, height=550)

        title=Label(frame1, text= "1-1" ,font=("times new roman" ,30, "bold"),bg="white",fg='green').place(x=250,y=50)


        f_name=Label(frame1, text= "First Name" ,font=("times new roman" ,15, "bold"),bg="white",fg='purple').place(x=10,y=100)
        txt_fname=Entry(frame1, font= ("times new roman" ,15),bg= "lightgray",fg='black') .place(x=10, y=130, width=180)

        HallTicket=Label(frame1, text= "HallTicket No" ,font=("times new roman" ,15, "bold"),bg="white",fg='purple').place(x=200,y=100)
        txt_HallTicket=Entry(frame1, font= ("times new roman" ,15),bg= "lightgray",fg='black') .place(x=200, y=130, width=180)

        Answer=Label(frame1, text= "Department" ,font=("times new roman" ,15, "bold"),bg="white",fg='purple').place(x=400,y=100)
        txt_Answer=Entry(frame1, font= ("times new roman" ,15),bg= "lightgray",fg='black') .place(x=400, y=130, width=180)








root=Tk()
obj=R1(root)
root.mainloop()        