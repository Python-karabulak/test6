# -*- coding: utf-8 -*-
"""
Created on Sat May  8 17:58:59 2021

@author: Умида
"""

# #1 Ro'yxat uzatish
# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism]=baho
#     return baholar

# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar)
# print(baholar)


# #2 ro'yxatga o'zgarish kiritish 
# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar)
# print(talabalar)



# #3
# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar[:])
# print(talabalar)


#4
def katta_harf(ismlar):
    s=[]
    for i in ismlar:
        s.append(i.title())
    return s   
ismlar = ['ali', 'vali', 'hasan', 'husan']
# print(ismlar)
# ismlar=katta_harf(ismlar)
# print(ismlar)

# #5
ismlar = ['ali', 'vali', 'hasan', 'husan']
yangi_ismlar = katta_harf(ismlar)
print(ismlar)
print(yangi_ismlar)

