from tkinter import *
import tkinter as tk
from tkinter import messagebox


root = tk.Tk()

root.geometry('925x500+700+200')
    
frame = Frame(root,width=3200,height=3500,bg='gray')
frame.place(x=0,y=0)



def display_options():

    label = tk.Label(root, text="Options:",bg = "yellow")
    label.pack()
    for option in cities:
        option_label = tk.Label(root, text=option,bg="blue")
        option_label.pack()


def city_1():
  messagebox.showinfo("Information","You have choosed Ariyalur!!!")
  root.destroy()
  import city1_ariyalur

def city_2():
  messagebox.showinfo("Information","You have choosed Chennai!!!")
  root.destroy()
  import city2_chennai


def city_3():
  messagebox.showinfo("Information","You have choosed Coimbatore!!!")
  root.destroy()
  import city3_coimbatore


def city_4():
  messagebox.showinfo("Information","You have choosed Cuddalore!!!")
  root.destroy()
  import city4_cuddalore


def city_5():
  messagebox.showinfo("Information","You have choosed Dharmapuri!!!")
  root.destroy()
  import city5_dharmapuri


def city_6():
  messagebox.showinfo("Information","You have choosed Dindugal!!!")
  root.destroy()
  import city6_dindugal


def city_7():
  messagebox.showinfo("Information","You have choosed Erode!!!")
  root.destroy()
  import city7_erode


def city_8():
  messagebox.showinfo("Information","You have choosed Kallakurichi!!!")
  root.destroy()
  import city8_kallakurichi


def city_9():
  messagebox.showinfo("Information","You have choosed Kanchipuram!!!")
  root.destroy()
  import city9_kanchipuram


def city_10():
  messagebox.showinfo("Information","You have choosed Kanyakumari!!!")
  root.destroy()
  import city10_kanyakumari


def city_11():
  messagebox.showinfo("Information","You have choosed Karur!!!")
  root.destroy()
  import city11_karur


def city_12():
  messagebox.showinfo("Information","You have choosed Krishnagiri!!!")
  root.destroy()
  import city12_krishnagiri


def city_13():
  messagebox.showinfo("Information","You have choosed Madurai!!!")
  root.destroy()
  import city13_madurai


def city_14():
  messagebox.showinfo("Information","You have choosed Nagapattinam!!!")
  root.destroy()
  import city14_nagapattinam


def city_15():
  messagebox.showinfo("Information","You have choosed Namakkal!!!")
  root.destroy()
  import city15_namakkal


def city_16():
  messagebox.showinfo("Information","You have choosed Nilgiris!!!")
  root.destroy()
  import city16_nilgiris


def city_17():
  messagebox.showinfo("Information","You have choosed Perambalur!!!")
  root.destroy()
  import city17_perambalur


def city_18():
  messagebox.showinfo("Information","You have choosed Chengalpattu!!!")
  root.destroy()
  import city18_chengalpattu


def city_19():
  messagebox.showinfo("Information","You have choosed Pudukottai!!!")
  root.destroy()
  import city19_pudukottai


def city_20():
  messagebox.showinfo("Information","You have choosed Ramanathapuram!!!")
  root.destroy()
  import city20_ramanathapuram


def city_21():
  messagebox.showinfo("Information","You have choosed Salem!!!")
  root.destroy()
  import city21_salem


def city_22():
  messagebox.showinfo("Information","You have choosed Sivagangai!!!")
  root.destroy()
  import city22_sivagangai


def city_23():
  messagebox.showinfo("Information","You have choosed Thanjavur!!!")
  root.destroy()
  import city23_thanjavur


def city_24():
  messagebox.showinfo("Information","You have choosed Theni!!!")
  root.destroy()
  import city24_theni


def city_25():
  messagebox.showinfo("Information","You have choosed Thoothukudi!!!")
  root.destroy()
  import city25_thoothukudi


def city_26():
  messagebox.showinfo("Information","You have choosed Thiruchirapalli!!!")
  root.destroy()
  import city26_thiruchirapalli


def city_27():
  messagebox.showinfo("Information","You have choosed Tirunelveli!!!")
  root.destroy()
  import city27_tirunelveli


def city_28():
  messagebox.showinfo("Information","You have choosed Tiruppur!!!")
  root.destroy()
  import city28_tiruppur


def city_29():
  messagebox.showinfo("Information","You have choosed Tiruvarur!!!")
  root.destroy()
  import city29_tiruvarur


def city_30():
  messagebox.showinfo("Information","You have choosed Tiruvannamalai!!!")
  root.destroy()
  import city30_tiruvannamalai


def city_31():
  messagebox.showinfo("Information","You have choosed Vellore!!!")
  root.destroy()
  import city31_vellore


def city_32():
  messagebox.showinfo("Information","You have choosed Vilupuram!!!")
  root.destroy()
  import city32_vilupuram


def city_33():
  messagebox.showinfo("Information","You have choosed Virudhunagar!!!")
  root.destroy()
  import city33_virudhunagar






def display_cities():

 cities = []
 city1=Button(frame,height=0,width = 15,pady=2,text='Ariyalur',bg='red',command = city_1,font=('Times New Roman',10,'bold'),fg='white',border=0).place(x=50,y=50)
 cities.append(city1)
 city2=Button(frame,height=0,width = 15,pady=2,text='Chennai',bg='red',command = city_2,font=('Times New Roman',10,'bold'),fg='white',border=0).place(x=50+130*1,y=50)
 cities.append(city2)
 city3=Button(frame,height=0,width = 15,pady=2,text='Coimbatore',bg='red',command = city_3,font=('Times New Roman',10,'bold'),fg='white',border=0).place(x=50+130*2,y=50)
 cities.append(city3)
 city4=Button(frame,height=0,width = 15,pady=2,text='Cuddalore',command = city_4,bg='red',font=('Times New Roman',10,'bold'),fg='white',border=0).place(x=50+130*3,y=50)
 cities.append(city4)
 city5=Button(frame,height=0,width = 15,pady=2,text='Dharmapuri',bg='red',command = city_5,font=('Times New Roman',10,'bold'),fg='white',border=0).place(x=50+130*4,y=50)
 cities.append(city5)
 city6=Button(frame,height=0,width = 15,pady=2,text='Dindugal',bg='red',command = city_6,font=('Times New Roman',10,'bold'),fg='white',border=0).place(x=50+130*5,y=50)
 cities.append(city6)
 city7=Button(frame,height=0,width = 15,pady=2,text='Erode',bg='red',command = city_7,font=('Times New Roman',10,'bold'),fg='white',border=0).place(x=50,y=50+50)
 cities.append(city7)
 city8=Button(frame,height=0,width = 15,pady=2,text='Kallakurichi',bg='red',command = city_8,font=('Times New Roman',10,'bold'),fg='white',border=0).place(x=50+130,y=50*2)
 cities.append(city8)
 city9=Button(frame,height=0,width = 15,pady=2,text='Kanchipuram',bg='red',command = city_9,font=('Times New Roman',10,'bold'),fg='white',border=0).place(x=50+130*2,y=50*2)
 cities.append(city9)
 city10=Button(frame,height=0,width = 15,pady=2,text='Kanyakumari',bg='red',command = city_10,font=('Times New Roman',10,'bold'),fg='white',border=0).place(x=50+130*3,y=50*2)
 cities.append(city10)
 city11=Button(frame,height=0,width = 15,pady=2,text='Karur',bg='red',command = city_11,font=('Times New Roman',10,'bold'),fg='white',border=0).place(x=50+130*4,y=50*2)
 cities.append(city11)
 city12=Button(frame,height=0,width = 15,pady=2,text='Krishnagiri',bg='red',command = city_12,font=('Times New Roman',10,'bold'),fg='white',border=0).place(x=50+130*5,y=50*2)
 cities.append(city12)
 city13=Button(frame,height=0,width = 15,pady=2,text='Madurai',bg='red',command = city_13,font=('Times New Roman',10,'bold'),fg='white',border=0).place(x=50,y=50*3)
 cities.append(city13)
 city14=Button(frame,height=0,width = 15,pady=2,text='Nagapattinam',bg='red',command = city_14,font=('Times New Roman',10,'bold'),fg='white',border=0).place(x=50+130,y=50*3)
 cities.append(city14)
 city15=Button(frame,height=0,width = 15,pady=2,text='Namakkal',bg='red',command = city_15,font=('Times New Roman',10,'bold'),fg='white',border=0).place(x=50+130*2,y=50*3)
 cities.append(city15)
 city16=Button(frame,height=0,width = 15,pady=2,text='Nilgiris',bg='red',command = city_16,font=('Times New Roman',10,'bold'),fg='white',border=0).place(x=50+130*3,y=50*3)
 cities.append(city16)
 city17=Button(frame,height=0,width = 15,pady=2,text='Perambalur',bg='red',command = city_17,font=('Times New Roman',10,'bold'),fg='white',border=0).place(x=50+130*4,y=50*3)
 cities.append(city17)
 city18=Button(frame,height=0,width = 15,pady=2,text='Chengalpattu',bg='red',command = city_18,font=('Times New Roman',10,'bold'),fg='white',border=0).place(x=50+130*5,y=50*3)
 cities.append(city18)
 city19=Button(frame,height=0,width = 15,pady=2,text='Pudukottai',bg='red',command = city_19,font=('Times New Roman',10,'bold'),fg='white',border=0).place(x=50,y=50*4)
 cities.append(city19)
 city20=Button(frame,height=0,width = 15,pady=2,text='Ramanathapuram',bg='red',command = city_20,font=('Times New Roman',10,'bold'),fg='white',border=0).place(x=50+130,y=50*4)
 cities.append(city20)
 city21=Button(frame,height=0,width = 15,pady=2,text='Salem',bg='red',command = city_21,font=('Times New Roman',10,'bold'),fg='white',border=0).place(x=50+130*2,y=50*4)
 cities.append(city21)
 city22=Button(frame,height=0,width = 15,pady=2,text='Sivagangai',bg='red',command = city_22,font=('Times New Roman',10,'bold'),fg='white',border=0).place(x=50+130*3,y=50*4)
 cities.append(city22)
 city23=Button(frame,height=0,width = 15,pady=2,text='Thanjavur',bg='red',command = city_23,font=('Times New Roman',10,'bold'),fg='white',border=0).place(x=50+130*4,y=50*4)
 cities.append(city23)
 city24=Button(frame,height=0,width = 15,pady=2,text='Theni',bg='red',command = city_24,font=('Times New Roman',10,'bold'),fg='white',border=0).place(x=50+130*5,y=50*4)
 cities.append(city24)
 city25=Button(frame,height=0,width = 15,pady=2,text='Thoothukudi',bg='red',command = city_25,font=('Times New Roman',10,'bold'),fg='white',border=0).place(x=50,y=50*5)
 cities.append(city25)
 city26=Button(frame,height=0,width = 15,pady=2,text='Thiruchirapalli',bg='red',command = city_26,font=('Times New Roman',10,'bold'),fg='white',border=0).place(x=50+130,y=50*5)
 cities.append(city26)
 city27=Button(frame,height=0,width = 15,pady=2,text='Tirunelveli',bg='red',command = city_27,font=('Times New Roman',10,'bold'),fg='white',border=0).place(x=50+130*2,y=50*5)
 cities.append(city27)
 city28=Button(frame,height=0,width = 15,pady=2,text='Tiruppur',bg='red',command = city_28,font=('Times New Roman',10,'bold'),fg='white',border=0).place(x=50+130*3,y=50*5)
 cities.append(city28)
 city29=Button(frame,height=0,width = 15,pady=2,text='Tiruvarur',bg='red',command = city_29,font=('Times New Roman',10,'bold'),fg='white',border=0).place(x=50+130*4,y=50*5)
 cities.append(city29)
 city30=Button(frame,height=0,width = 15,pady=2,text='Tiruvannamalai',bg='red',command = city_30,font=('Times New Roman',10,'bold'),fg='white',border=0).place(x=50+130*5,y=50*5)
 cities.append(city30)
 city31=Button(frame,height=0,width = 15,pady=2,text='Vellore',bg='red',command = city_31,font=('Times New Roman',10,'bold'),fg='white',border=0).place(x=50,y=50*6)
 cities.append(city31)
 city32=Button(frame,height=0,width = 15,pady=2,text='Vilupuram',bg='red',command = city_32,font=('Times New Roman',10,'bold'),fg='white',border=0).place(x=50+130,y=50*6)
 cities.append(city32)
 city33=Button(frame,height=0,width = 15,pady=2,text='Virudhunagar',bg='red',command = city_33,font=('Times New Roman',10,'bold'),fg='white',border=0).place(x=50+130*2,y=50*6)
 cities.append(city33)

 def display_cities():
    for city in cities:
       label = tk.Label(root,text=city,bg="gray")
       label.pack()

Button(frame,height=0,width = 15,pady=2,text='View cities ↓',bg='sky blue',font=('Times New Roman',10,'bold'),fg='black',border=2.0,command = display_cities).place(x=400,y=10)


img=PhotoImage(file=r"D:\python program\select city.png")
Label(root,image=img,bg="gray").place(x = 535, y = 290)



root.title("Cities")


#display_cities()

root.mainloop()


