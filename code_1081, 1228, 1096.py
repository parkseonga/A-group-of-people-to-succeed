# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 11:40:11 2020

@author: a0105
"""

# 1081
x, y = map(int, input().split())

for a in range(0,x):
    
    a += 1

    for b in range(0,y):
        
        b += 1
        
        print(a,b)
        
        
# 1228
# 파이썬은 double형이 없음.
x, y = map(float, input().split()) 

normal = (x-100)*0.9
biman_test = (y-normal)*100/normal
    
if biman_test<=10:
    print('정상')
elif biman_test>10 and biman_test<=20:
    print('과체중')
elif biman_test>20:
    print('비만')
      
# 1096    
array = [[0]*19]*19
array[[2]][2] = 1
array.index(2,2)

array = [[0]*3]*3
array[0][1] = 1
