# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 11:24:42 2023
Subject : Dictionareis lab 5
@author: Mohammed Mostafa ELsayed
"""

# in dictitionary we use key the key is a unique identifier  and the value is that data

student={'name':'Mohammed','age':'25','courses':['english','Math'],1:'191290'}
print(student)
print(student['name'])
print(student['courses']) #all of two lines is key then i ask computer to print the value of this key 
print(student[1])

#try this line print(student[phone]) 
print(student.get('phone','Not Found')) #thsi is get function itis just wanna to find this key if the key donot exist then the out is None 

student['Phone_number']=900909092 #to add anew key and value in the dic
print(student.get('Phone_number'))


student.update({'name':'Mahmoud','age':'27','Phone_number':'020231345998'} ) #to update the keys and the value in the keys 
print(student)

del(student['courses']) #to delete key from dictionary 
print(student)

age = student.pop('age') #i remove this key and his value from the original dic and hold it in new var 
print(age)

print(len(student))
print(student.values())#to print values in the dict
print(student.keys())#to print keys 
print(student.items())#to print keys and value 

for key in student:
    print(key)
    
for value in student.values(): #to print the value of keys 
    print(value)

for items in student.items(): #toprint all items in dic like value and keys
    print(items)