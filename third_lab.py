
"""
Created on Fri Dec 15 15:46:51 2023

subject : third project in python  (int ,float )

@author: Mohammed Mostafa
"""
#Arithematic operators:
#Addition :        2+3
#subtraction:      3-2
#Multiplication:   3*2
#Divsion:          3/2
#Floor division    3//2
#Exponent          3**2
#Modelus           3%2

#-------------Comparisons-------------
#Equal:                    3==2
#Not Equal:                3!=2
#Greater than:             3>2
#Less than :               3<2
#Greater or equal:         3>=2
#Less or Equal:            3<=2
#------------------------------------

num =3
num_2=3.15
num_1='100'
Num_2='200'
# we can make casting to convert var from string to int or any data type
num_1=int(num_1)
Num_2=int(Num_2) # if i adding these variable then the compiler will deal with them as an integer 

print(type(num))

print(type(num_2))
print(3/2) # if you try to run this line on python 2 the out put will be 1 and ignoring the decimal value 
print(3//2)
print(3**2)
print(3%2) 
print(3*(2+1)) #in python the oportunity for ()


print(abs(-3)) #absolute value of this number 
print(round(3.7)) #the 3.7 rounded up to 4
print(round(3.75,1))

print(num>num_2)

print(num_1+Num_2)
