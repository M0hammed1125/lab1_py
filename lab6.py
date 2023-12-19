# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 13:09:08 2023
subject : conditional and booleans 
@author: Mohammed Mostafa 
"""

language ='java'

if language == 'python': #not python 
    print('conditional is true ')
elif language=='java':
    print('languge is java ')
elif language=='java script':
    print('languge is java script ')
else  :
    print('conditional is false')
    
#python doesnot have switch case ever because else and elif are plenty clean enough to do this 

#lets use And  oR  not 
user ='Admin'
logged_in=True
if (user=='Admin' and logged_in):
    print('Admin page')
else:
    print('user page')
    

user_2 ='Admin'
logged_in_2=False

if user == 'Admin' and not logged_in_2:
    print('great work')
else :
      print('Try again')
        
      
# what is the diffrence between is and ==
#lets try to do 2 lists 

a=[1,2,3]
b=[1,2,3]
print(a==b) #The out is true this check if a same b in value not in same location in ram 
print(a is b) #the out is true they have same values but not same location in ram 
#lets try to display the location of var in ram 
print(id(a))
print(id(b))
#to make two lists have same location and same value 

b=a
print(id(a))
print(id(b))
print(a is b) #then the out put is true 
print(id(a) is id(b))

#False == None == zero == any empty sequencing ''  ()  []== any empty mapping {}
#you can check if string is empty or dictionary you can use this 





 