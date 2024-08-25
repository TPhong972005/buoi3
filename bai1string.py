# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 09:52:13 2024

@author: ADMIN
"""

var='Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM'
print(var[0:16])
print(var[18:27])
print(var[29:42])
print(var[44:54])
print(var[56:63])

print()

s= var.split(", ")
print("bang 1")
for b in s:
    print(b)
print()
print("bang 2")
s2=  var.replace("P. ","").replace("Q. ","").replace("Tp. ","")
s3= s2.split(", ")
for c in s3:
    print(c)
    
    

    
    
    




