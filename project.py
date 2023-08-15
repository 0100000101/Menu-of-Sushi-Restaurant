import tkinter
from tkinter import *
from time import strftime
import secrets
import string

root=Tk()
root.title('chio-chio-san')
root.geometry('1600x900')
root.config(bg='#BCBCBC')
a=Frame(root)
photo_1=PhotoImage(file='fon2.gif')
image_1=Label(image=photo_1).place(x=0,y=0)
button1=Button(text='Menu',font='verdana 8 bold',command=lambda :menu())
button1.config(height=2,background='#FFFFFF')
button1.place(x=783,y=300)
text=Label(text='WELCOME',font=("Goudy Stout", 10),bg='#F6F6F6')
text.place(x=730)
b=Frame(root)
photo_3=PhotoImage(file='f1.gif')
image_3=Label(b,image=photo_3).place(x=0,y=0)
c=Frame(root)
c.config(bg='#81BBEF')
photo_2=PhotoImage(file='d2.gif')
image_2=Label(c,image=photo_2).place(x=480,y=0)
d=Frame(root)
photo_4=PhotoImage(file='check1.gif')
image_4=Label(d,image=photo_4).place(x=0,y=0)
e=Frame(root)
photo_6=PhotoImage(file='restaurant1.1.gif')
image_6=Label(e,image=photo_6).place(x=0,y=0)
button8=Button(e,text='food menu',font=('Harlow Solid Italic',15),command=lambda :food_menu())
button8.config(height=2,background='#FFFFFF')
button8.place(x=700,y=300)
button9=Button(e,text='drink menu',font=('Harlow Solid Italic',15),command=lambda :drink_menu())
button9.config(height=2,background='#FFFFFF')
button9.place(x=800,y=300)

photo_5=PhotoImage(file='qr1.2.png')
image_5=Label(d,image=photo_5).place(x=310,y=530)

button2=Button(b,text='Next',font=('Segoe Script',10),command=lambda :next())
button2.place(x=1300,y=700)
button3=Button(c,text='Completion',font=('Segoe Script',10),command=lambda :Total())
button3.place(x=1300,y=700)
button4=Button(b,text='Back',font=('Kristen ITC',10),command=lambda :Back1())
button4.place(x=20,y=20)
button5=Button(c,text='Back',font=('Kristen ITC',10),command=lambda :Back2())
button5.place(x=20,y=20)
button6=Button(d,text='Back',font=('Kristen ITC',10),command=lambda :Back3())
button6.place(x=20,y=20)

letters = string.ascii_letters
digits = string.digits
alphabet = letters + digits
pwd_length = 16
pwd = ''
for i in range(pwd_length):
  pwd += ''.join(secrets.choice(alphabet))
while True:
  pwd = ''
  for i in range(pwd_length):
    pwd += ''.join(secrets.choice(alphabet))

  if (any(char for char in pwd) and
      sum(char in digits for char in pwd)>=2):
          break

def my_time():
    time_string=strftime('%H:%M:%S %p  %A\n%x')
    l1.config(text=time_string)
def menu():
    a.forget()
    e.pack(expand=True,fill=BOTH)
    e.config(bg='#E4E3E3')
def food_menu():
    e.forget()
    b.pack(expand=True,fill=BOTH)

def drink_menu():
    e.forget()
    c.pack(expand=True,fill=BOTH)

def next():
    b.forget()
    c.pack(expand=True,fill=BOTH)

def Back1():
    b.forget()
    e.pack(expand=True,fill=BOTH)

def Back2():
    c.forget()
    e.pack(expand=True,fill=BOTH)
def Back3():
    d.forget()
    c.pack(expand=True,fill=BOTH)
def Total():
    c.forget()
    d.pack(expand=True,fill=BOTH)
    total1 = int(s1.get()) * 11
    total2 = int(s2.get()) * 13
    total3 = int(s3.get()) * 15
    total4 = int(s4.get()) * 15
    total5 = int(s5.get()) * 16
    total6 = int(s6.get()) * 13
    total7 = int(s7.get()) * 10
    total8 = int(s8.get()) * 10
    total9 = int(s9.get()) * 12
    total10 = int(s10.get()) * 14
    total11 = int(z1.get()) * 5
    total12 = int(z2.get()) * 5
    total13 = int(z3.get()) * 5
    total14 = int(z4.get()) * 2
    total15 = int(z5.get()) * 6
    total16 = int(z6.get()) * 3
    total17 = int(z7.get()) * 4
    total18 = int(z8.get()) * 4
    total19 = int(z9.get()) * 5
    total20 = int(z10.get()) * 4
    total21 = int(z11.get()) * 3
    total22 = int(z12.get()) * 6
    total23 = int(z13.get()) * 5
    total24 = int(z14.get()) * 15
    total25 = int(z15.get()) * 13
    total26 = int(z16.get()) * 18
    total27 = int(z17.get()) * 15
    total28 = int(z18.get()) * 17
    total29 = int(z19.get()) * 4.5
    total30 = int(z20.get()) * 4.5
    total31 = int(z21.get()) * 4.5
    total32 = int(z22.get()) * 4.5
    total33 = int(z23.get()) * 4.5
    total34 = int(z24.get()) * 3
    total35 = int(z25.get()) * 3.5
    total36 = int(z26.get()) * 4
    total37 = int(z27.get()) * 4
    total38 = int(z28.get()) * 5
    total39 = int(z29.get()) * 5
    total40 = int(z30.get()) * 3.5
    total41 = int(z31.get()) * 3.5
    total42 = int(z32.get()) * 3.7
    total43 = int(z33.get()) * 3
    total44 = int(z34.get()) * 5
    total45 = int(z35.get()) * 3.5
    total46 = int(z36.get()) * 3.5
    total47 = int(z37.get()) * 3
    total48 = int(z38.get()) * 3
    total49 = int(z39.get()) * 3.5
    total50 = int(z40.get()) * 4
    che = []
    if total1>0:
        che.append('Philadelphia Maki-----------------------------------------------------11 ₼')
    if total2>0:
        che.append('California Maki-------------------------------------------------------13 ₼')
    if total3>0:
        che.append('Shrimp salad----------------------------------------------------------15 ₼')
    if total4>0:
        che.append('Tempura Maki---------------------------------------------------------15 ₼')
    if total5>0:
        che.append('Black Dragon Maki---------------------------------------------------16 ₼')
    if total6>0:
        che.append('Red Dragon Maki-----------------------------------------------------13 ₼')
    if total7>0:
        che.append('Philadelphia Sesame Maki-------------------------------------------10 ₼')
    if total8>0:
        che.append('Tavuklu erişte---------------------------------------------------------10 ₼')
    if total9>0:
        che.append('Ebi Tempura Maki----------------------------------------------------12 ₼')
    if total10>0:
        che.append('Hawaiian Maki--------------------------------------------------------14 ₼')
    if total11>0:
        che.append('Cola----------------------------------------------------------------------5 ₼')
    if total12>0:
        che.append('Fanta--------------------------------------------------------------------5 ₼')
    if total13>0:
        che.append('Sprite--------------------------------------------------------------------5 ₼')
    if total14>0:
        che.append('Water--------------------------------------------------------------------2 ₼')
    if total15>0:
        che.append('Fruit Juice--------------------------------------------------------------6 ₼')
    if total16>0:
        che.append('Ayran--------------------------------------------------------------------3 ₼')
    if total17>0:
        che.append('Ice Tea------------------------------------------------------------------4 ₼')
    if total18>0:
        che.append('Banana-------------------------------------------------------------------4 ₼')
    if total19>0:
        che.append('Strawberry-------------------------------------------------------------5 ₼')
    if total20>0:
        che.append('Cherry-------------------------------------------------------------------4 ₼')
    if total21>0:
        che.append('Vanilla-------------------------------------------------------------------3 ₼')
    if total22>0:
        che.append('Chocolate----------------------------------------------------------------6 ₼')
    if total23>0:
        che.append('Mixed--------------------------------------------------------------------5 ₼')
    if total24>0:
        che.append('Red----------------------------------------------------------------------15 ₼')
    if total25>0:
        che.append('White-------------------------------------------------------------------13 ₼')
    if total26>0:
        che.append('Rose---------------------------------------------------------------------18 ₼')
    if total27>0:
        che.append('Medium White---------------------------------------------------------15 ₼')
    if total28>0:
        che.append('Sweet White-----------------------------------------------------------17 ₼')
    if total29>0:
        che.append('Cappuccino------------------------------------------------------------4.5 ₼')
    if total30>0:
        che.append('Espresso---------------------------------------------------------------4.5 ₼')
    if total31>0:
        che.append('Americano-------------------------------------------------------------4.5 ₼')
    if total32>0:
        che.append('Latte-------------------------------------------------------------------4.5 ₼')
    if total33>0:
        che.append('Macaccino-------------------------------------------------------------4.5 ₼')
    if total34>0:
        che.append('Tea-----------------------------------------------------------------------3 ₼')
    if total35>0:
        che.append('Apple Tea-------------------------------------------------------------3.5 ₼')
    if total36>0:
        che.append('Green Tea---------------------------------------------------------------4 ₼')
    if total37>0:
        che.append('Nescafe-----------------------------------------------------------------4 ₼')
    if total38>0:
        che.append('Hot Chocolate----------------------------------------------------------5 ₼')
    if total39>0:
        che.append('Jager Bomb-------------------------------------------------------------5 ₼')
    if total40>0:
        che.append('Jagermeister---------------------------------------------------------3.5 ₼')
    if total41>0:
        che.append('Tequila----------------------------------------------------------------3.5 ₼')
    if total42>0:
        che.append('Tequila Gold---------------------------------------------------------3.7 ₼')
    if total43>0:
        che.append('Tequila Rose------------------------------------------------------------3 ₼')
    if total44>0:
        che.append('Tequila Bomb-----------------------------------------------------------5 ₼')
    if total45>0:
        che.append('Sambuca--------------------------------------------------------------3.5 ₼')
    if total46>0:
        che.append('Black Sambuca-------------------------------------------------------3.5 ₼')
    if total47>0:
        che.append('Aplle Sourz-------------------------------------------------------------3 ₼')
    if total48>0:
        che.append('Blow Job---------------------------------------------------------------3 ₼')
    if total49>0:
        che.append('Jelly Bean-------------------------------------------------------------3.5 ₼')
    if total50>0:
        che.append('Anaconda---------------------------------------------------------------4 ₼')

    che = Variable(value=che)
    che_listbx = Listbox(d, listvariable=che, selectmode=MULTIPLE, width=50, height=17, bd=0,
                         font=('Comic Sans MS', 10))
    che_listbx.place(x=928, y=260)
    T_total=total1+total2+total3+total4+total5+total6+total7+total8+total9+total10+total11+total12+total13+total14\
            +total15+total16+total17+total18+total19+total20+total21+total22+total23+total24+total25+total26+total27\
            +total28+total29+total30+total31+total32+total33+total34+total35+total36+total37+total38+total39+total40\
            +total41+total42+total43+total44+total45+total46+total47+total48+total49+total50
    cem=Label(d,text=f'cem\t\t\t\t\t\t\t\t{T_total}')
    cem.place(x=935,y=590)
    EDV=T_total*18/100
    EDV1=Label(d,text=f'ƏDV 18% = {EDV}\t\t\t\t\t\t\t{T_total}')
    EDV1.place(x=935,y=615)
    T_EDV=Label(d,text=f'Toplam ədv = {EDV}')
    T_EDV.place(x=935,y=640)
    service_charge=T_total*5/100
    service_charge1=Label(d,text=f'Xidmət haqqı 5% = {service_charge}')
    service_charge1.place(x=935,y=690)
    bill=Label(d,text=f'Total: {T_total+service_charge} $',font=("Goudy Stout", 11))
    bill.place(x=1160, y=720)

my_font=('times',12,'bold')
l1=tkinter.Label(d,font=my_font)
l1.place(x=1160,y=200)
my_time()
text=Label(b,text='food menu',font=("Goudy Stout", 15),bg='#DEC48E')
text.place(x=660,y=5)
text=Label(c,text='drink menu',font=("Goudy Stout", 15),bg='#F5E8E8')
text.place(x=650,y=5)
text=Label(d,text='TOTAL',font=("Goudy Stout", 7),bg='#BCBCBC')
text.place(x=760)
R1=Radiobutton(d,text='CREDIT AND DEBIT CARDS',value='CREDIT AND DEBIT CARDS',font=('Lucida Handwriting',10),bg='#D3D3D3')
R1.place(x=1130,y=100)
R2=Radiobutton(d,text='IN CASH',value='IN CASH',font=('Lucida Handwriting',10),bg='#D3D3D3')
R2.place(x=930,y=100)
hidden1=Label(c,text='        ',font=('MV Boli',25),bg='#FAF2F2')
hidden1.place(x=638,y=452)
hidden2=Label(c,text='                     ',font=('MV Boli',25),bg='#FAF2F2')
hidden2.place(x=630,y=65)
hidden3=Label(c,text='            ',font=('MV Boli',25),bg='#FAF2F2')
hidden3.place(x=763,y=350)
hidden4=Label(c,text='           ',font=('MV Boli',25),bg='#FAF2F2')
hidden4.place(x=575,y=643)
hidden5=Label(c,text='            ',font=('MV Boli',25),bg='#FAF2F2')
hidden5.place(x=763,y=650)
hidden6=Label(d,text='            ',font=('MV Boli',55),height=25,bg='#F7F7F7')
hidden6.place(x=900,y=570)
fiscal=Label(d,text='Fiscal ID:  'f'{pwd}')
fiscal.place(x=935,y=665)
#-----------------------------------------------
photo1=PhotoImage(file='180.gif')
image1=Label(b,image=photo1).place(x=150,y=100)
name1=Label(b,text='Philadelphia Maki',font=('MV Boli',14),bg='#C19946')
name1.place(x=150,y=70)
Ingredients1= ['İçindekiler: Avokado, krem peynir,','somon füme, susam, salatalık']
Ingredients_var1= Variable(value=Ingredients1)
Ingredients_listbx1= Listbox(b,listvariable=Ingredients_var1,selectmode=MULTIPLE,width=30,height=2,bd=1,bg='#DEC48E')
Ingredients_listbx1.place(x=150,y=283)
weight1=Label(b,text='200 g.',font=('Calibri',10),bg='#DEC48E')
weight1.place(x=150,y=320)
Price1=Label(b,text='11 ₼',font=('Segoe UI Black',13),bg='#DEC48E',fg='#CF3F3F')
Price1.place(x=210,y=317)
s1=Spinbox(b,from_=0,to=10,width=5,bg='#DEC48E')
s1.place(x=290,y=320)
#----------------------------------------------
photo2=PhotoImage(file='foto2.gif')
image2=Label(b,image=photo2).place(x=410,y=100)
name2=Label(b,text='California Maki',font=('MV Boli',14),bg='#C19946')
name2.place(x=410,y=70)
Ingredients2= ['İçindekiler: Avokado, mayonez,','surimi, kırmızı tobiko, salatalık']
Ingredients_var2= Variable(value=Ingredients2)
Ingredients_listbx2= Listbox(b,listvariable=Ingredients_var2,selectmode=MULTIPLE,width=30,height=2,bd=1,bg='#DEC48E')
Ingredients_listbx2.place(x=410,y=283)
weight2=Label(b,text='200 g.',font=('Calibri',10),bg='#DEC48E')
weight2.place(x=410,y=320)
Price2=Label(b,text='13 ₼',font=('Segoe UI Black',13),bg='#DEC48E',fg='#CF3F3F')
Price2.place(x=470,y=317)
s2=Spinbox(b,from_=0,to=10,width=5,bg='#DEC48E')
s2.place(x=550,y=320)
#----------------------------------------------
photo3=PhotoImage(file='foto0.gif')
image3=Label(b,image=photo3).place(x=660,y=100)
name3=Label(b,text='Shrimp salad',font=('MV Boli',14),bg='#C19946')
name3.place(x=660,y=70)
Ingredients3= ['İçindekiler: Karides tempura','salatası']
Ingredients_var3= Variable(value=Ingredients3)
Ingredients_listbx3= Listbox(b,listvariable=Ingredients_var3,selectmode=MULTIPLE,width=30,height=2,bd=1,bg='#DEC48E')
Ingredients_listbx3.place(x=660,y=283)
weight3=Label(b,text='240 g.',font=('Calibri',10),bg='#DEC48E')
weight3.place(x=660,y=320)
Price3=Label(b,text='15 ₼',font=('Segoe UI Black',13),bg='#DEC48E',fg='#CF3F3F')
Price3.place(x=720,y=317)
s3=Spinbox(b,from_=0,to=10,width=5,bg='#DEC48E')
s3.place(x=800,y=320)
#----------------------------------------------
photo4=PhotoImage(file='foto3.gif')
image4=Label(b,image=photo4).place(x=910,y=100)
name4=Label(b,text='Tempura Maki',font=('MV Boli',14),bg='#C19946')
name4.place(x=910,y=70)
Ingredients4= ['İçindekiler: Karides, somon füme,','krem peynir, salatalık']
Ingredients_var4= Variable(value=Ingredients4)
Ingredients_listbx4= Listbox(b,listvariable=Ingredients_var4,selectmode=MULTIPLE,width=30,height=2,bd=1,bg='#DEC48E')
Ingredients_listbx4.place(x=910,y=283)
weight4=Label(b,text='210 g.',font=('Calibri',10),bg='#DEC48E')
weight4.place(x=910,y=320)
Price4=Label(b,text='15 ₼',font=('Segoe UI Black',13),bg='#DEC48E',fg='#CF3F3F')
Price4.place(x=970,y=317)
s4=Spinbox(b,from_=0,to=10,width=5,bg='#DEC48E')
s4.place(x=1050,y=320)
#----------------------------------------------
photo5=PhotoImage(file='foto4.gif')
image5=Label(b,image=photo5).place(x=1160,y=100)
name5=Label(b,text='Black Dragon Maki',font=('MV Boli',14),bg='#C19946')
name5.place(x=1160,y=70)
Ingredients5= ['İçindekiler: Avokado, krem peynir,','surimi, salatalık, susam, unagi sos']
Ingredients_var5= Variable(value=Ingredients5)
Ingredients_listbx5= Listbox(b,listvariable=Ingredients_var5,selectmode=MULTIPLE,width=30,height=2,bd=1,bg='#DEC48E')
Ingredients_listbx5.place(x=1160,y=283)
weight5=Label(b,text='120 g.',font=('Calibri',10),bg='#DEC48E')
weight5.place(x=1160,y=320)
Price5=Label(b,text='16 ₼',font=('Segoe UI Black',13),bg='#DEC48E',fg='#CF3F3F')
Price5.place(x=1220,y=317)
s5=Spinbox(b,from_=0,to=10,width=5,bg='#DEC48E')
s5.place(x=1300,y=320)
#----------------------------------------------
photo6=PhotoImage(file='foto5.gif')
image6=Label(b,image=photo6).place(x=150,y=390)
name6=Label(b,text='Red Dragon Maki',font=('MV Boli',14),bg='#C19946')
name6.place(x=150,y=360)
Ingredients6= ['İçindekiler: Somon, mayonez,','avokado, surimi, salatalık']
Ingredients_var6= Variable(value=Ingredients6)
Ingredients_listbx6= Listbox(b,listvariable=Ingredients_var6,selectmode=MULTIPLE,width=30,height=2,bd=1,bg='#DEC48E')
Ingredients_listbx6.place(x=150,y=573)
weight6=Label(b,text='210 g.',font=('Calibri',10),bg='#DEC48E')
weight6.place(x=150,y=610)
Price6=Label(b,text='13 ₼',font=('Segoe UI Black',13),bg='#DEC48E',fg='#CF3F3F')
Price6.place(x=210,y=607)
s6=Spinbox(b,from_=0,to=10,width=5,bg='#DEC48E')
s6.place(x=290,y=610)
#----------------------------------------------
photo7=PhotoImage(file='foto6.gif')
image7=Label(b,image=photo7).place(x=410,y=390)
name7=Label(b,text='Philadelphia Sesame Maki',font=('MV Boli',11),bg='#C19946')
name7.place(x=410,y=362)
Ingredients7= ['İçindekiler: somon füme, avokado,','salatalık, susamlı peynir kreması']
Ingredients_var7= Variable(value=Ingredients7)
Ingredients_listbx7= Listbox(b,listvariable=Ingredients_var7,selectmode=MULTIPLE,width=30,height=2,bd=1,bg='#DEC48E')
Ingredients_listbx7.place(x=410,y=573)
weight7=Label(b,text='200 g.',font=('Calibri',10),bg='#DEC48E')
weight7.place(x=410,y=610)
Price7=Label(b,text='10 ₼',font=('Segoe UI Black',13),bg='#DEC48E',fg='#CF3F3F')
Price7.place(x=470,y=607)
s7=Spinbox(b,from_=0,to=10,width=5,bg='#DEC48E')
s7.place(x=550,y=610)
#----------------------------------------------
photo8=PhotoImage(file='foto7.gif')
image8=Label(b,image=photo8).place(x=660,y=390)
name8=Label(b,text='Tavuklu erişte',font=('MV Boli',11),bg='#C19946')
name8.place(x=660,y=360)
Ingredients8= ['İçindekiler: tavuk erişte']
Ingredients_var8= Variable(value=Ingredients8)
Ingredients_listbx8= Listbox(b,listvariable=Ingredients_var8,selectmode=MULTIPLE,width=30,height=2,bd=1,bg='#DEC48E')
Ingredients_listbx8.place(x=660,y=573)
weight8=Label(b,text='300 g.',font=('Calibri',10),bg='#DEC48E')
weight8.place(x=660,y=610)
Price8=Label(b,text='10 ₼',font=('Segoe UI Black',13),bg='#DEC48E',fg='#CF3F3F')
Price8.place(x=720,y=607)
s8=Spinbox(b,from_=0,to=10,width=5,bg='#DEC48E')
s8.place(x=800,y=610)
#----------------------------------------------
photo9=PhotoImage(file='foto8.gif')
image9=Label(b,image=photo9).place(x=910,y=390)
name9=Label(b,text='Ebi Tempura Maki',font=('MV Boli',11),bg='#C19946')
name9.place(x=910,y=360)
Ingredients9= ['İçindekiler: Marul üzerinde karides,','susam tohumları']
Ingredients_var9= Variable(value=Ingredients9)
Ingredients_listbx9= Listbox(b,listvariable=Ingredients_var9,selectmode=MULTIPLE,width=30,height=2,bd=1,bg='#DEC48E')
Ingredients_listbx9.place(x=910,y=573)
weight9=Label(b,text='180 g.',font=('Calibri',10),bg='#DEC48E')
weight9.place(x=910,y=610)
Price9=Label(b,text='12 ₼',font=('Segoe UI Black',13),bg='#DEC48E',fg='#CF3F3F')
Price9.place(x=970,y=607)
s9=Spinbox(b,from_=0,to=10,width=5,bg='#DEC48E')
s9.place(x=1050,y=610)
#----------------------------------------------
photo10=PhotoImage(file='image.gif')
image10=Label(b,image=photo10).place(x=1160,y=390)
name10=Label(b,text='Hawaiian Maki',font=('MV Boli',11),bg='#C19946')
name10.place(x=1160,y=360)
Ingredients10= ['İçindekiler: Füme yılan balığı, karides,','salatalık, baharatlı sos, yeşil tobiko']
Ingredients_var10= Variable(value=Ingredients10)
Ingredients_listbx10= Listbox(b,listvariable=Ingredients_var10,selectmode=MULTIPLE,width=30,height=2,bd=1,bg='#DEC48E')
Ingredients_listbx10.place(x=1160,y=573)
weight10=Label(b,text='190 g.',font=('Calibri',10),bg='#DEC48E')
weight10.place(x=1160,y=610)
Price10=Label(b,text='14 ₼',font=('Segoe UI Black',13),bg='#DEC48E',fg='#CF3F3F')
Price10.place(x=1220,y=607)
s10=Spinbox(b,from_=0,to=10,width=5,bg='#DEC48E')
s10.place(x=1300,y=610)
#----------------------------------------------------------------
#----------------------------------------------------------------
name_drink1=Label(c,text='SOFT DRINKS',font=('MV Boli',11),fg='#F2940B',bg='#F5E8E8')
name_drink1.place(x=557,y=120)
drink1= ['Cola------------------' , 'Fanta------------------','Sprite------------------',
         'Water------------------','Fruit Juice------------------','Ayran------------------','Ice Tea------------------']
drink1= Variable(value=drink1)
drink1_listbx= Listbox(c,listvariable=drink1,selectmode=MULTIPLE,width=15,height=7,bd=1,bg='#E2C9C9',
                       font=('Comic Sans MS',10))
drink1_listbx.place(x=557,y=140)
v1=Label(c,text='5.00$',bg='#F5E8E8')
v1.place(x=680,y=141)
z1=Spinbox(c,from_=0,to=10,width=5,bg='#E2C9C9')
z1.place(x=713,y=141)
v2=Label(c,text='5.00$',bg='#F5E8E8')
v2.place(x=680,y=160)
z2=Spinbox(c,from_=0,to=10,width=5,bg='#E2C9C9')
z2.place(x=713,y=160)
v3=Label(c,text='5.00$',bg='#F5E8E8')
v3.place(x=680,y=181)
z3=Spinbox(c,from_=0,to=10,width=5,bg='#E2C9C9')
z3.place(x=713,y=181)
v4=Label(c,text='2.00$',bg='#F5E8E8')
v4.place(x=680,y=200)
z4=Spinbox(c,from_=0,to=10,width=5,bg='#E2C9C9')
z4.place(x=713,y=200)
v5=Label(c,text='6.00$',bg='#F5E8E8')
v5.place(x=680,y=220)
z5=Spinbox(c,from_=0,to=10,width=5,bg='#E2C9C9')
z5.place(x=713,y=220)
v6=Label(c,text='3.00$',bg='#F5E8E8')
v6.place(x=680,y=240)
z6=Spinbox(c,from_=0,to=10,width=5,bg='#E2C9C9')
z6.place(x=713,y=240)
v7=Label(c,text='4.00$',bg='#F5E8E8')
v7.place(x=680,y=260)
z7=Spinbox(c,from_=0,to=10,width=5,bg='#E2C9C9')
z7.place(x=713,y=260)
#----------------------------------------------
name_drink2=Label(c,text='MILK SHAKES',font=('MV Boli',11),fg='#F2940B',bg='#F5E8E8')
name_drink2.place(x=557,y=300)
drink2= ['Banana------------------' , 'Strawberry------------------','Cherry------------------',
         'Vanilla------------------','Chocolate------------------','Mixed------------------']
drink2= Variable(value=drink2)
drink2_listbx= Listbox(c,listvariable=drink2,selectmode=MULTIPLE,width=15,height=7,bd=1,bg='#E2C9C9',
                       font=('Comic Sans MS',10))
drink2_listbx.place(x=557,y=320)
v8=Label(c,text='4.00$',bg='#F5E8E8')
v8.place(x=680,y=320)
z8=Spinbox(c,from_=0,to=10,width=5,bg='#E2C9C9')
z8.place(x=713,y=320)
v9=Label(c,text='5.00$',bg='#F5E8E8')
v9.place(x=680,y=340)
z9=Spinbox(c,from_=0,to=10,width=5,bg='#E2C9C9')
z9.place(x=713,y=340)
v10=Label(c,text='4.00$',bg='#F5E8E8')
v10.place(x=680,y=360)
z10=Spinbox(c,from_=0,to=10,width=5,bg='#E2C9C9')
z10.place(x=713,y=360)
v11=Label(c,text='3.00$',bg='#F5E8E8')
v11.place(x=680,y=380)
z11=Spinbox(c,from_=0,to=10,width=5,bg='#E2C9C9')
z11.place(x=713,y=380)
v12=Label(c,text='6.00$',bg='#F5E8E8')
v12.place(x=680,y=400)
z12=Spinbox(c,from_=0,to=10,width=5,bg='#E2C9C9')
z12.place(x=713,y=400)
v13=Label(c,text='5.00$',bg='#F5E8E8')
v13.place(x=680,y=420)
z13=Spinbox(c,from_=0,to=10,width=5,bg='#E2C9C9')
z13.place(x=713,y=420)
#----------------------------------------------
name_drink3=Label(c,text='WINE',font=('MV Boli',11),fg='#F2940B',bg='#F5E8E8')
name_drink3.place(x=557,y=480)
drink3= ['Red------------------' , 'White------------------','Rose------------------','Medium White------------------',
         'Sweet White------------------']
drink3= Variable(value=drink3)
drink3_listbx= Listbox(c,listvariable=drink3,selectmode=MULTIPLE,width=15,height=7,bd=1,bg='#E2C9C9',
                       font=('Comic Sans MS',10))
drink3_listbx.place(x=557,y=500)
v14=Label(c,text='15.00$',bg='#F5E8E8')
v14.place(x=679,y=500)
z14=Spinbox(c,from_=0,to=10,width=5,bg='#E2C9C9')
z14.place(x=715,y=500)
v15=Label(c,text='13.00$',bg='#F5E8E8')
v15.place(x=679,y=520)
z15=Spinbox(c,from_=0,to=10,width=5,bg='#E2C9C9')
z15.place(x=715,y=520)
v16=Label(c,text='18.00$',bg='#F5E8E8')
v16.place(x=679,y=540)
z16=Spinbox(c,from_=0,to=10,width=5,bg='#E2C9C9')
z16.place(x=715,y=540)
v17=Label(c,text='15.00$',bg='#F5E8E8')
v17.place(x=679,y=560)
z17=Spinbox(c,from_=0,to=10,width=5,bg='#E2C9C9')
z17.place(x=715,y=560)
v18=Label(c,text='17.00$',bg='#F5E8E8')
v18.place(x=679,y=580)
z18=Spinbox(c,from_=0,to=10,width=5,bg='#E2C9C9')
z18.place(x=715,y=580)
#----------------------------------------------
name_drink4=Label(c,text='HOT DRINKS',font=('MV Boli',11),fg='#F2940B',bg='#F5E8E8')
name_drink4.place(x=763,y=120)
drink4= ['Cappuccino------------------' , 'Espresso---------------------------','Americano---------------------------',
         'Latte---------------------------','Mocaccino---------------------------','Tea---------------------------',
         'Apple Tea---------------------------','Green Tea---------------------------',
         'Nescafe---------------------------','Hot Chocolate------------------']
drink4= Variable(value=drink4)
drink4_listbx= Listbox(c,listvariable=drink4,selectmode=MULTIPLE,width=20,height=11,bd=1,bg='#E2C9C9',
                       font=('Comic Sans MS',10))
drink4_listbx.place(x=763,y=140)
v19=Label(c,text='4.50 $',bg='#F5E8E8')
v19.place(x=927,y=141)
z19=Spinbox(c,from_=0,to=10,width=5,bg='#E2C9C9')
z19.place(x=962,y=141)
v20=Label(c,text='4.50 $',bg='#F5E8E8')
v20.place(x=927,y=160)
z20=Spinbox(c,from_=0,to=10,width=5,bg='#E2C9C9')
z20.place(x=962,y=160)
v21=Label(c,text='4.50 $',bg='#F5E8E8')
v21.place(x=927,y=180)
z21=Spinbox(c,from_=0,to=10,width=5,bg='#E2C9C9')
z21.place(x=962,y=180)
v22=Label(c,text='4.50 $',bg='#F5E8E8')
v22.place(x=927,y=200)
z22=Spinbox(c,from_=0,to=10,width=5,bg='#E2C9C9')
z22.place(x=962,y=200)
v23=Label(c,text='4.50 $',bg='#F5E8E8')
v23.place(x=927,y=220)
z23=Spinbox(c,from_=0,to=10,width=5,bg='#E2C9C9')
z23.place(x=962,y=220)
v24=Label(c,text='3.00 $',bg='#F5E8E8')
v24.place(x=927,y=240)
z24=Spinbox(c,from_=0,to=10,width=5,bg='#E2C9C9')
z24.place(x=962,y=240)
v25=Label(c,text='3.50 $',bg='#F5E8E8')
v25.place(x=927,y=260)
z25=Spinbox(c,from_=0,to=10,width=5,bg='#E2C9C9')
z25.place(x=962,y=260)
v26=Label(c,text='4.00 $',bg='#F5E8E8')
v26.place(x=927,y=280)
z26=Spinbox(c,from_=0,to=10,width=5,bg='#E2C9C9')
z26.place(x=962,y=280)
v27=Label(c,text='4.00 $',bg='#F5E8E8')
v27.place(x=927,y=300)
z27=Spinbox(c,from_=0,to=10,width=5,bg='#E2C9C9')
z27.place(x=962,y=300)
v28=Label(c,text='5.00 $',bg='#F5E8E8')
v28.place(x=927,y=320)
z28=Spinbox(c,from_=0,to=10,width=5,bg='#E2C9C9')
z28.place(x=962,y=320)
#----------------------------------------------
name_drink5=Label(c,text='SHOTS',font=('MV Boli',11),fg='#F2940B',bg='#F5E8E8')
name_drink5.place(x=763,y=390)
drink5= ['Jager Bomb------------------' , 'Jagermeister---------------------------','Tequila---------------------------',
         'Tequila Gold---------------------------','Tequila Rose---------------------------',
         'Tequila Bomb---------------------------','Sambuca---------------------------',
         'Black Sambuca---------------------------','Aplle Sourz---------------------------',
         'Blow Job-----------------------','Jelly Bean-----------------------','Anaconda-----------------------']
drink5= Variable(value=drink5)
drink5_listbx= Listbox(c,listvariable=drink5,selectmode=MULTIPLE,width=20,height=13,bd=1,bg='#E2C9C9',
                       font=('Comic Sans MS',10))
drink5_listbx.place(x=763,y=410)
v29=Label(c,text='5.00 $',bg='#F5E8E8')
v29.place(x=927,y=410)
z29=Spinbox(c,from_=0,to=10,width=5,bg='#E2C9C9')
z29.place(x=962,y=410)
v30=Label(c,text='3.50 $',bg='#F5E8E8')
v30.place(x=927,y=430)
z30=Spinbox(c,from_=0,to=10,width=5,bg='#E2C9C9')
z30.place(x=962,y=430)
v31=Label(c,text='3.50 $',bg='#F5E8E8')
v31.place(x=927,y=450)
z31=Spinbox(c,from_=0,to=10,width=5,bg='#E2C9C9')
z31.place(x=962,y=450)
v32=Label(c,text='3.70 $',bg='#F5E8E8')
v32.place(x=927,y=470)
z32=Spinbox(c,from_=0,to=10,width=5,bg='#E2C9C9')
z32.place(x=962,y=470)
v33=Label(c,text='3.00 $',bg='#F5E8E8')
v33.place(x=927,y=490)
z33=Spinbox(c,from_=0,to=10,width=5,bg='#E2C9C9')
z33.place(x=962,y=490)
v34=Label(c,text='5.00 $',bg='#F5E8E8')
v34.place(x=927,y=508)
z34=Spinbox(c,from_=0,to=10,width=5,bg='#E2C9C9')
z34.place(x=962,y=510)
v35=Label(c,text='3.50 $',bg='#F5E8E8')
v35.place(x=927,y=527)
z35=Spinbox(c,from_=0,to=10,width=5,bg='#E2C9C9')
z35.place(x=962,y=530)
v36=Label(c,text='3.50 $',bg='#F5E8E8')
v36.place(x=927,y=546)
z36=Spinbox(c,from_=0,to=10,width=5,bg='#E2C9C9')
z36.place(x=962,y=550)
v37=Label(c,text='3.00 $',bg='#F5E8E8')
v37.place(x=927,y=565)
z37=Spinbox(c,from_=0,to=10,width=5,bg='#E2C9C9')
z37.place(x=962,y=570)
v38=Label(c,text='3.00 $',bg='#F5E8E8')
v38.place(x=927,y=585)
z38=Spinbox(c,from_=0,to=10,width=5,bg='#E2C9C9')
z38.place(x=962,y=590)
v39=Label(c,text='3.50 $',bg='#F5E8E8')
v39.place(x=927,y=605)
z39=Spinbox(c,from_=0,to=10,width=5,bg='#E2C9C9')
z39.place(x=962,y=610)
v40=Label(c,text='4.00 $',bg='#F5E8E8')
v40.place(x=927,y=625)
z40=Spinbox(c,from_=0,to=10,width=5,bg='#E2C9C9')
z40.place(x=962,y=630)

root.mainloop()
