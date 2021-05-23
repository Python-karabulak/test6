# -*- coding: utf-8 -*-
"""
Created on Sat May  8 18:02:25 2021

@author: Умида
"""

# # #1
# def summa(*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return yigindi
# print(summa(1,2))

# #2
# print(summa(1,2,3,4,5))


# #3
# def summa(*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     return sum(sonlar)

# print(summa(4,5,6,7))


# #4
# def summa(x,y,*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     return x+y+sum(sonlar)
# print(summa(2,8))



#5 
def avto_info(kompaniya,model,rang,**malumotlar):
    """Avto haqidagi ma'lumotlarni lug'at ko'rinishdia qaytaruvchi funksiya"""
    malumotlar['kompaniya']=kompaniya
    malumotlar['model']=model
    malumotlar['rang']=rang
    return malumotlar
avto1 = avto_info("GM", "malibu", 'qora', yil=2018)
# avto2 = avto_info("Kia", "K5", rang='qizil', narh=35000)
print(avto1)
