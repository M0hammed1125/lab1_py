# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 03:07:41 2023
Subject : Functions in python
@author: Mohammed Mostafa 
"""

def hello_function(): #def Mean definition itis posible to write emepty function with out any parameter 
   # pass # we put pass thatis mean we want to fill this function latter 
   # print('Hello_function!') # if we use print then the function still empty function because it doesnot return any thing 
    return 'Hello_function_1'
   
hello_function() #now we call this  function 
print(hello_function) #if we forget () then we will print the location of the function
print(hello_function()) #now the out is none because this is empty function 

#function is very great tool  you can decrease code size and exucting time 
print(hello_function().upper()) #in this line i use the out put of my function is input for another function 
#i donot want to learn or know all codes for any function i just want to know what type of inputs and out puts 

#def greating_func(greatting): #now you must type string in this input or any data type
 #   return '{} Function'.format(greatting)

#print(greating_func('Hi')) 

#lets make it more complixty 

def greating_func(greatting , name): #two in put in function 
    return '{} {}'.format(greatting ,name)
print(greating_func('hi', 'Mohammed'))

def Student_info(*arg ,**karg):
    print(arg) #the tupple of our input 
    print(karg) #the dict of our input 

Student_info('Math','Python',Name='Mohammed',Grade=3.7 )

courses=['Math','Art']
info={'Name':'Mahmoud','Grade':3.76}

Student_info(courses, info) # then the out put is not true 
Student_info(*courses, **info)