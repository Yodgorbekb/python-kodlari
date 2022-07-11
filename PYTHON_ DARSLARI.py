# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 13:11:13 2022

@author: Ogabek
"""
ism = 'Ahad'
ism = input("Ismingiz nima ?")
print("Assalomu alaykum, " + ism.upper())
t_yil = int(input("Tug'ilgan yilingizni kiriting:"))
print("Siz", + 2022 - t_yil, "yoshda ekansiz")
savol = input("Siz qaysi bayramlarni yoqtirasiz ?")
print("Menga " + savol + " bayramlari yoqadi")
                 #11-DARS AMALIYOT.
son = float(input("Juft son kiriting:"))
if son%2:
    print('Bu son juft emas.')
else:
    print("To'g'i javob!!!")
print("Muzeyga marhamat!!!")
yosh = int(input("Yoshingiz nechada?"))
if yosh<10 or yosh>60:
    print('Muzeyga kirish bepul!')
elif yosh<18:
    print("Muzeyga kirish 10000 so'm")
elif yosh>18:
    print("Muzeyga kirish 20000 so'm")
else:
    print("Muzeyga kirish bepul!")

print("Sonlarni taqqoslash")    
x = float(input("Birinchi sonni kiriting:"))    
y = float(input("Ikkinchi sonni kiriting:"))
if x==y:
    print(f"{x}={y}")
elif x<y:
    print(f"{x}<{y}")
else:
    print(f"{x}>{y}")
print("Do'konimizga xush kelibsiz,\n iltimos 5ta mahsulot sotib oling")
mahsulotlar = ['un','yog\'','go\'sht','muzqaymoq','baliq','suv','makaro\'n','saryog\'','shashlik','kolbasa','pomidor','bodiring']
savat = []
mavjud_emas = []
bor_mahsulotlar = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing:"))
for mahsulot in savat:
  if mahsulot in savat:
      if mahsulot in mahsulotlar:
       print(f"Do'konimizda {mahsulot} bor\n")
  else:
      print(f"Do'konimizda {mahsulot} yo'q\n")
print(savat)      

      
foydalanuvchilar = ("anvar","umar","og'abek","yodgorbek","alisher")
parol = input("Yangi login tanlang: ")
if parol in foydalanuvchilar:
    print("Login band, yangi login kiriting!")
else:
    print("Xush kelibsiz!!")
    
kun = input("Bugun haftani qaysi kuni?\n>>>")
if kun.lower()=='shanba' or kun.lower()=='yakshanba':
     print("Bugun uyda dam olamiz!!")
else:
     print("Bugun ish kuni$$")
