# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 23:03:03 2023
Subject : Lists, Tuples, and Sets
@author: mohammed mostafa
"""

courses=['python','Machine-learning','Deep-learning','neural-network'] #this is list from 4 element 
print(courses)
print(len(courses)) #len == lenght and this is a function to count all element in the list 
print(courses[3]) # to print the 3rd element in the list 

#know that the count start from zero not 1

print(courses[-1]) #negative index that mean last elemnt 

#try to write this code print(courses[4])  ===> out of the range 

print(courses[0:2])
courses.append('Art') #now you add anew element in list 
print(courses)

courses.insert(0, 'Anatomy') #now i insert anew value but in any location i want the fisrt parameter refer to the location of index 
print(courses)

courses_2=['Math','pythics']
courses.insert(0,courses_2) # in this line i insert this list in first index only not 0  and 1 just 0
print(courses[0])

courses_3=['ALgebra','Integration']

courses.extend(courses_3)
print(courses) # extend mean add an element in list not list [['Math', 'pythics'], 'Anatomy', 'python', 'Machine-learning', 'Deep-learning', 'neural-network', 'Art', 'ALgebra', 'Integration']

courses.remove(courses_2)
print(courses)

courses.pop() #used to remove last value in list or hold it 
print(courses)
poped =courses.pop() #save the last element in anew var and clear it from the list
print(poped)

courses.reverse() # this function reverse the list 
print(courses)

courses.sort() # this function sort letter with alphabet letters 
print(courses)
num=[1,3,5,7,9,0]
num.sort()
print(num) #but unforteionatly this way of sorted cahnge the arrange of list in variable holder or ram if we want to use sort but not make change in orignal data 

num_sort=sorted(num)
print(num_sort)

print(min(num)) # min and max number 
print(sum(num)) #printsum of all numbers 

print(courses.index('python')) #to get the number of element in the list 

print('Math' in courses) #Then the out put tell me are Math in list or no 

for item in courses: #this mean print all items in this list the item name is not standard 
    print(item)
    
for index,items in enumerate(courses): #to print item with the number of elemnt start with zero 
    print(index,items)
    
for index,items in enumerate(courses,start=1): #to print item with the number of elemnt start with one
    print(index,items)


course_str=' - '.join(courses) #this mean put all items in new list but the character between them is -
print(course_str)

New_str=course_str.split(' - ') #return the list in the original value comma
print(New_str)
#------------------------------------------start with tuple ------------------------------------------------------------

Tuple_1=('Math','Art','Anatomy','Python')
Tuple_2=Tuple_1
print(Tuple_1)
print(Tuple_2)
# Tuple_1[0]=('Art') #then code make eror why ? 'tuple' object does not support item assignment ==> imutable 

#the diffrence between list and tuple that list is mutable but Tupple is imutable 

#sets not ordered value and not duplicate  sets not care about order of element lets try this 

Courses={'Math','History','Anatomy','Mechanical'}
print(Courses) #the out is {'Mechanical', 'History', 'Anatomy', 'Math'} not care about order

Courses={'Math','History','Anatomy','Mechanical','Math'} # i write  math twice but the out have one math only not support duplicate 
print(Courses)

#you can compare about 2 sets to know number of items common in 2 sets 

Courses={'Math','History','Anatomy','Mechanical'}
Ar_Courses={'Math','Art','Geography','Mechanical'}

print(Courses.intersection(Ar_Courses)) # the common items in two sets 
print(Courses.difference(Ar_Courses))  # the diffrent  items in two sets 
print(Courses.union(Ar_Courses))      #union 2 sets 

#empty list 
List=[]
List=list()
#empty Tuple
Tuple=()
Tuple=tuple()
#empty sets
Set={}
Set=set()
 































