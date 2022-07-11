# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 13:58:29 2022

@author: Ogabek
"""

                              #python darslari 17-dars
                              #WHILE TSIKLI
#INPUT()
#ism = input("Ismingiz nima? ")
#savol = f"Salom, {ism.title()}. Yoshingiz nechada? "                              
#yosh = input(savol)
#yosh = int(yosh)
#height = input("Bo'yigiz necha metr?")
#height = float(height)

#While()
#son = 1
#while son<=5:#toki son 5dan kichik yoki teng ekan
#    print(son, end=' ')
#    son = son + 1
#    son += 1
#print("dastur tugadi")

#while and input
#print("Kiritilgan sonning kvadratini qytaruvchi dastur.")
#savol = "Istalgan son kiriting "
#savol += "(dasturni to'xtatish uchun 'exit' deb yozing):"
#qiymat = ''
#while qiymat != 'exit':
#    qiymat = input(savol)
#    if qiymat != 'exit':
#        print(float(qiymat)**2)
#print("Dastur tugadi")

# ishora 
#print("Kiritilgan sonni kvadratini qaytaruvchi dastur.")
#savol = "Istalgan son kiriting "
#savol += "(Dasturni to'xtatish uchun 'exit' deb yozing):"
#ishora = True 
#while ishora:
#    qiymat = input(savol)
#    if qiymat == 'exit':
#        ishora = False
#    else:
#        print(float(qiymat)**2)
#print("Dastur to'xtadi")    
 
#break while
#print("Kiritilgan sonni kvadratini qaytaruvchi dastur")
#savol = "Istalgan son kiriting "
#savol += "(Dasturni to'xatatish uchun ' exit' deb yozing):"

#while True: #abadiy tsikli
#    qiymat = input(savol)
#    if qiymat == 'exit':
#        break
#    else:
#        print(float(qiymat)**2)
#print('Dastur tugadi')

#break for

#sonlar = list(range(1,11))
#for son in sonlar:
#    if son == 5:
#        break
#    print(f"{son} ning kvadrati {son**2} ga teng")
    
    #continune
#sonlar = list(range(1,11))
#for son in sonlar:
#    if son == 5:
#        continue
#    print(f"{son} ning kvadrati {son**2} ga teng")  

        #Continue while
#son = 0
#while son<10:
#    son += 1
#    if son%2==0:#sonni juft yokin toqligini tekshiruvchi operator
#        continue
#    else:
#        print(son)        

#infinite loop - abadiy tsikli
#son = 0
#while son<10:
#    son += 1
#    if son%2!=0:
#        continue
#    else:
#        print(son)

#son = 0
#while son<10:
#    son += 1
#    if son%2!=0:
#        continue
#    else:
#        print(son)
        
#son = 1
#while son>0:
#    son += 1
#    if son%2!=0:
#        continue
#    else:
#            print(son)
                         #AMALIYOT
#savol = "Yoqtirgan kitoblaringizni kiriting"
#savol += "(Dasturni to'xtatish uchun 'stop' deb yozing):"                         
#while True:
#   kitob = input(savol)
#    if kitob == 'stop':
#print("Dastur tugadi")
#print("Katta raxmat")        

print("Muzeyga marhamat") 
savol = "Yoshingiz nechada"
savol += "\n(Dasturni tugatish uchun 'exit' yoki 'quit' deb yozing) "
ishora = True
while ishora:
    qiymat = input(savol)
    if qiymat == 'exit' or qiymat == 'quit':
        break
    yosh = int(qiymat)
    
    if yosh<7:
        narh = 2000
    elif 7<=yosh<18:
        narh = 3000
    elif 18<yosh<65:
        narh = 10000
    else: narh = 0
    
    if narh==0:
            print("Sizga kirish bepul")
    else:
            print(f"CHipta {narh} so'm")
               
         
             
              
print("Dastur tugadi")            