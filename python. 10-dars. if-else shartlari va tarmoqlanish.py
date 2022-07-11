# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 16:42:06 2022

@author: Ogabek
"""

                                  #PYTHON DARSLARI.10-DARS
                                  #MAVZU: IF-ELSEshartlari
                                  #va tarmoqlanish
avtolar = ['audi','bmw','volvo','kia','hyundai']
for avto in avtolar:
    if avto == 'bmw':#..agar avto bmw ga teng bo'lsa...
        print(avto.upper())
    else:#aks holda...
        print(avto.title())




#(==) tengmi?
#(!=)teng emasmi?

ism = "Ali"      
ism.lower() == "ali"
ism = input("\n\tIsmingiz nima?")
if ism.lower() != 'ali':#Agar ism Aliga teng bo'lmasa..
   print(f"Uzr, {ism.title()} biz Alini kutyapmiz.")
else:
    print("Salom, Ali")
    
    
    
    
javob = float(input("1-misol\n12x6 nechaga teng?>>>"))
savol = float(input("2-misol\n43x8 nechaga teng?>>>"))
if javob!=72:
    print("1-misol\nJavob xato!")
else:
    print("1-misol\nJavob to'gri")
    
if savol!=344:
    print("2-misol\nJavob xato")
else:
    print("2-misol\nJavob to'g'ri")
    
    
    
    
    
yosh = int(input("Yoshingiz nechada?>>>"))
if yosh <= 18:
    print("Xush kelibsiz!")
else:
    print("Uzr kirish mumkin emas!")
    
    
    
    
login = input("Yangi login tanlng:")
if len(login)<=5:
    print("Login 5 ta  harfdan ko'proq bo'lishi shart!")
    
    
    
    
yil = int(input("Tug'ilgan yilingizni kiriting:"))
if 2022-yil<18:
    print(f"Yoshingiz {2022-yil} da ekan.")
    print("Kirish mumkin emas!")
else:
    print("Xush kelibsiz!")
    
    
    
    
yosh = int(input("Yoshingiz nechada?>>>"))
if yosh>65: print("Siz COVID-19 risk guruhida ekansiz")
else:
    print("Siz sog'lom ekansiz!")

x, y = 50, 40
print("x>y") if x>y else print("x<y") 