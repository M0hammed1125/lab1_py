# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 13:38:19 2023
Subject : loop and iterations 
@author: Mohammed Mostafa
"""

nums=[1,2,3,4,5]
nums_2=[1,2,3,4,5,6,7,8,9,10]
for num in nums:
    if num ==3:
        print('Found it')
        break
    print(num)

for num in nums_2:
    if num == 3:
        print('Scape this number')
        continue
    print(num)
    
numbers =[1,2,3]

for number in numbers:
     
     for letter in 'abc':
         print(number , letter)
         
         
for i in range(1,10):
    print(i)
    
x=0;
while(x<10):
    if x==5:
        break
    print(x)
    x+=1