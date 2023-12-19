# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 03:48:22 2023
Subject : Examples
@author: Mohammed Mostafa
"""
#number of days per Month
month_day=[0,31,28,31,30,31,30,31,31,30,31,30,31]  #first we make list of days in months 

"""
    Check if a given year is a leap year.

    Parameters:
    - year (int): The year to be checked.

    Returns:
    - True if the year is a leap year, False otherwise.
 """
 
    # Leap year condition:
    # 1. If the year is evenly divisible by 4
    # 2. If the year is not divisible by 100, except if it is divisible by 400
    
def is_leap(year):
    
    return year%4==0 and(year%100!=0 or year%400==0) 
def days_in_Month (year,month):
    
    if not 1<=month <=12:
        print("invalid month")
    elif month==2 and is_leap(year):
        return 29
        
    return month_day[month]

is_leap(2024)
print(is_leap(2024))
print(days_in_Month(2024, 2))