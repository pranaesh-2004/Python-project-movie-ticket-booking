from tkinter import *
import tkinter as tk
from tkinter import messagebox


root = Tk()
root.title("City")
root.geometry('925x500+700+200')
    
frame = Frame(root,width=3200,height=3500,bg='gray')
frame.place(x=0,y=0)

img=PhotoImage(file=r"D:\python program\welcome page.png",height=1500,width=1000)
Label(root,image=img,bg="gray").place(x = 0, y = 45)



def display_options():
  root.destroy()
  import city_displaying
  

Button(frame,height=0,width = 15,pady=4,text='View cities ↓',bg='sky blue',font=('Times New Roman',10,'bold'),fg='black',border=2.0,command = display_options).place(x=550,y=10)


def signin_city():
    Search = code.get()
    if (Search =="Ariyalur" or Search == "ariyalur"):
        messagebox.showinfo("Information","You have choosed Ariyalur!!!")
        root.destroy()
        import city1_ariyalur
         
    elif (Search == 'Chennai' or Search == "chennai"):
          messagebox.showinfo("Information","You have choosed Chennai!!!")
          root.destroy()
          import city2_chennai

    elif (Search == 'Coimbatore' or Search == "coimbatore"):
          messagebox.showinfo("Information","You have choosed Coimbatore!!!")
          root.destroy()
          import city3_coimbatore

    elif (Search == 'Cuddalore' or Search == "cuddalore"):
          messagebox.showinfo("Information","You have choosed Cuddalore!!!")
          root.destroy()
          import city4_cuddalore
          
    elif (Search == 'Dharmapuri' or Search == "dharmapuri"):
          messagebox.showinfo("Information","You have choosed Dharmapuri!!!")
          root.destroy()
          import city5_dharmapuri
          
    elif (Search == 'Dindugal' or Search == "dindugal"):
          messagebox.showinfo("Information","You have choosed Dindugal!!!")
          root.destroy()
          import city6_dindugal
          
    elif (Search == 'Erode' or Search == "erode"):
          messagebox.showinfo("Information","You have choosed Erode!!!")
          root.destroy()
          import city7_erode
          
    elif (Search == 'Kallakurichi' or Search == "kallakurichi"):
          messagebox.showinfo("Information","You have choosed Kallakurichi!!!")
          root.destroy()
          import city8_kallakurichi
          
    elif (Search == 'Kanchipuram' or Search == "kanchipuram"):
          messagebox.showinfo("Information","You have choosed Kanchipuram!!!")
          root.destroy()
          import city9_kanchipuram
          
    elif (Search == 'Kanyakumari' or Search == "kanyakumari"):
          messagebox.showinfo("Information","You have choosed Kanyakumari!!!")
          root.destroy()
          import city10_kanyakumari
          
    elif (Search == 'Karur' or Search == "karur"):
          messagebox.showinfo("Information","You have choosed Karur!!!")
          root.destroy()
          import city11_karur
          
    elif (Search == 'Krishnagiri' or Search == "krishnagiri"):
          messagebox.showinfo("Information","You have choosed Krishnagiri!!!")
          root.destroy()
          import city12_krishnagiri
          
    elif (Search == 'Madurai' or Search == "madurai"):
          messagebox.showinfo("Information","You have choosed Madurai!!!")
          root.destroy()
          import city13_madurai
          
    elif (Search == 'Nagapattinam' or Search == "nagapattinam"):
          messagebox.showinfo("Information","You have choosed Nagapattinam!!!")
          root.destroy()
          import city14_nagapattinam
          
    elif (Search == 'Namakkal' or Search == "namakkal"):
          messagebox.showinfo("Information","You have choosed Namakkal!!!")
          root.destroy()
          import city15_namakkal
          
    elif (Search == 'Nilgiris' or Search == "nilgiris"):
          messagebox.showinfo("Information","You have choosed Nilgiris!!!")
          root.destroy()
          import city16_nilgiris
          
    elif (Search == 'Perambalur' or Search == "perambalur"):
          messagebox.showinfo("Information","You have choosed Perambalur!!!")
          root.destroy()
          import city17_perambalur
          
    elif (Search == 'Chengalpattu' or Search == "chengalpattu"):
          messagebox.showinfo("Information","You have choosed Chengalpattu!!!")
          root.destroy()
          import city18_chengalpattu
          
    elif (Search == 'Pudukottai' or Search == "pudukottai"):
          messagebox.showinfo("Information","You have choosed Pudukottai!!!")
          root.destroy()
          import city19_pudukottai
          
    elif (Search == 'Ramanathapuram' or Search == "ramanathapuram"):
          messagebox.showinfo("Information","You have choosed Ramanathapurum!!!")
          root.destroy()
          import city20_ramanathapuram
          
    elif (Search == 'Salem' or Search == "salem"):
          messagebox.showinfo("Information","You have choosed Salem!!!")
          root.destroy()
          import city21_salem
          
    elif (Search == 'Sivagangai' or Search == "sivagangai"):
          messagebox.showinfo("Information","You have choosed Sivagangai!!!")
          root.destroy()
          import city22_sivagangai
          
    elif (Search == 'Thanjavur' or Search == "thanjavur"):
          messagebox.showinfo("Information","You have choosed Thanjavur!!!")
          root.destroy()
          import city23_thanjavur
          
    elif (Search == 'Theni' or Search == "theni"):
          messagebox.showinfo("Information","You have choosed Theni!!!")
          root.destroy()
          import city24_theni
          
    elif (Search == 'Thoothukudi' or Search == "thoothukudi"):
          messagebox.showinfo("Information","You have choosed Thoothukudi!!!")
          root.destroy()
          import city25_thoothukudi
          
    elif (Search == 'Thiruchirapalli' or Search == "thiruchirapalli"):
          messagebox.showinfo("Information","You have choosed Thiruchirapalli!!!")
          root.destroy()
          import city26_thiruchirapalli
          
    elif (Search == 'Tirunelveli' or Search == "tirunelveli"):
          messagebox.showinfo("Information","You have choosed Tirunelveli!!!")
          root.destroy()
          import city27_tirunelveli
          
    elif (Search == 'Tiruppur' or Search == "tiruppur"):
          messagebox.showinfo("Information","You have choosed Tiruppur!!!")
          root.destroy()
          import city28_tiruppur
          
    elif (Search == 'Tiruvarur' or Search == "tiruvarur"):
          messagebox.showinfo("Information","You have choosed tiruvarur!!!")
          root.destroy()
          import city29_tiruvarur
          
    elif (Search == 'Tiruvannamalai' or Search == "tiruvannamalai"):
          messagebox.showinfo("Information","You have choosed Tiruvannamalai!!!")
          root.destroy()
          import city30_tiruvannamalai
          
    elif (Search == 'Vellore' or Search == "vellore"):
          messagebox.showinfo("Information","You have choosed Vellore!!!")
          root.destroy()
          import city31_vellore
          
    elif (Search == 'Vilupuram' or Search == "vilupuram"):
          messagebox.showinfo("Information","You have choosed Vilupuram!!!")
          root.destroy()
          import city32_vilupuram
          
    elif (Search == 'Virudhunagar' or Search == "virudhunagar"):
          messagebox.showinfo("Information","You have choosed Virudhunagar!!!")
          root.destroy()
          import city33_virudhunagar
          
          
    else:
        messagebox.showerror("Invalid","Enter a valid City!!")
        root.destroy()
        



'''def search():
    root = Tk()
    root.geometry('925x500+700+200')
    
    frame = Frame(root,width=3200,height=3500,bg='gray')
    frame.place(x=0,y=0)'''

  
   # code = Entry(frame,width=60,fg='black',border=2,bg='white',font=('Times New Roman',14,'bold'))
   # code.place(x=60,y=10)
   # code.insert(0,'Search for your city')
   # Button(frame,width=20,pady=5,text='Search',bg='red',font=('Times New Roman',10,'bold'),fg='white',border=0).place(x=650,y=10)
    #need to put command=signin in above line...


###############--------------------------------############################

    
def on_enter(e):
      code.delete(0,'end')
def on_leave(e):
      name = code.get()
      if name=='':
        code.insert(0,'Search for your city')

code = Entry(frame,width = 59, fg="black",bg = "white", border = 4,font = ("Times new roman",11,"bold"))
code.place(x = 60,y = 12)
Button(frame,height=0,width = 20,pady=4,text='Search',bg='red',font=('Times New Roman',10,'bold'),fg='white',border=2.0,command = signin_city).place(x=670,y=10)
code.insert(0,"Search for your city :")
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)




    
root.mainloop()


#search()





    
