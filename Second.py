
"""
Created on Fri Dec 15 14:17:25 2023

subject : all tips in strings in python 

@author: mohamammed Mostafa
"""

My_message='hello world'
print(My_message)
print(My_message[0:5])
print(My_message.capitalize()) ## to captilized the out put of the message 
Message=My_message.replace('world', 'universe') ## to raplace words and store it in new variable
print(Message)
print(My_message.find('universe'))  ## the oput of this line is -1 because they donot found this word in this variable 
print(My_message.find('world'))  ## The out put is the number of col that you can find this word

## how to adding multiple strings and concatinate them in one sentence------------------------------------------------------------------##

greeting ='hello'
name ='Mohammed'

user_greeting=greeting+ name
print(user_greeting) ## with out any spaces 
user_greeting=greeting+' - '+ name ##to make spaces you can put adding symbol and adding empty string or single qoutes
print(user_greeting)

user_greeting='{} {} .welcome!'.format(greeting, name.capitalize())
print(user_greeting)
user_greeting=f'{greeting} {name.capitalize()} .welcome!'## same formating function and the advantages of this function that you can use palce holder 
print(user_greeting)

print(dir(user_greeting)) ## this line learn me how all fuctions i can use with this data type 
print(help(str()))  ##  this give me all inforamtion about my data type
print(help(str.lower)) ## this line give me all information about lower function in python like the change can occur 