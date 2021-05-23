# -*- coding: utf-8 -*-
"""
Created on Sun May  9 00:31:46 2021

@author: Умида
"""

# #1
# lambda argument:ifoda
# import math
# uzunlik = lambda pi, r : 2*pi*r
# print(uzunlik(math.pi,10))

# # #2
# product = lambda x, y : x ** y
# print(product(3, 2))



# #3
# def daraja(n):
#     return lambda x : x**n

# kvadrat = daraja(2)
# kub = daraja(3)
# print(f"3-ning kvadrati {kvadrat(3)} ga, kubi {kub(3)} ga teng")


# #
# from math import sqrt

# sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati
# ildizlar = list(map(sqrt,sonlar))
# print(sonlar)
# print(ildizlar)


# #6
# from math import sqrt

# sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati
# ildizlar = list(map(sqrt,sonlar))


# #7
# sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati

# def daraja2(x):
#     """Berilgan sonning kvadratini qaytaruvchi funksiya"""
#     return x*x
# print(sonlar)
# print(list(map(daraja2,sonlar))) # sonlar ning kvadratini hisoblaymiz


# #8
# kvadratlar = list(map(lambda x:x*x,sonlar))
# print(kvadratlar)

# #9
# kvadratlar = []
# for son in sonlar:
#     kvadratlar.append(son*son)
# print(kvadratlar)

#10
# a = [4, 5, 6,7]
# b = [7, 8, 9,1]
# c = [4, 6, 3,7]
# a_plus_b = list(map(lambda x,y,z:x+y+z,a,b,c))
# print(a_plus_b)


# #11
# ismlar = ['hasan','husan','olim','umid']
# print(list(map(lambda matn:matn.upper(),ismlar)))


# #12
# import random as r

# sonlar = r.sample(range(500),5) # 0-99 oralig'ida 10 ta tasodifiy sonlar

# def juftmi(x):
#     """x juft bo'lsa True, aks holda False qaytaruvchu funksiya"""
#     return x%2==1

# juft_sonlar = list(filter(juftmi,sonlar))
# print(sonlar)
# print(juft_sonlar)


# #13
# import random as r

# sonlar = r.sample(range(100),10) # 0-99 oralig'ida 10 ta tasodifiy sonlar
# juft_sonlar = list(filter(lambda son: son%2==0,sonlar))

# print(sonlar)
# print(juft_sonlar)


# #14
mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]

mevalar_b = list(filter(lambda meva:meva.startswith('o'),mevalar))
print(mevalar_b)


# #15
mevalar2 = list(filter(lambda meva:len(meva)<=5, mevalar))
print(mevalar2)


# #16
print(list(filter(lambda meva:(len(meva)<=5 and (meva.startswith('ol') or meva.endswith('n'))), mevalar)))



