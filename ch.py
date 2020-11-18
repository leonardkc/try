# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 07:52:21 2020

@author: hp
"""
#odd number
def is_odd(n):
    if n % 2 == 1:
        return True
    else:
        return False
number = int(input("Please Enter a Number: "))
print(is_odd(number))

#odd number in range
def odd():
   
   for i in range(lower, maximum+1):
        if(i%2 != 0):
            print(i)
lower = int(input("Enter lower limit range: "))
maximum = int(input("Enter maximum limit range: " ))
print(odd())
 
#reverse a given number
def reverse(n):
    d = 0
    rev = 0
    while(n>0):
        d=n%10
        n=int(n // 10)
        rev=rev*10+d
        return rev
x = int(input("Enter a number: "))
r = reverse(x)
print("Number : ",x)
print("Reverse : ",r)
     
#inverted star
def star(n):
    for i in range(n,0,-1):
        print((n-1) * ' ' + i * '*')
n = int(input("Enter number of Rows: "))
print(star(n))

#swap numbers
def swapNumbers(number1, number2):
    temporary = number1
    number1 = number2
    number2 = temporary
    print("After swap: ")
    print("number1: ", number1)
    print("number2: ", number2)
number1 = int(input("Enter first Number: "))
number2 = int(input("Enter second Number: "))
print("Before swap: ")
print("number1: ", number1)
print("number2: ", number2)
swapNumbers(number1,number2)

#average number in a given list
A=list()
n=int(input("Enter the size of the List ::"))
print("Enter the number ::")
for i in range(int(n)):
   k=int(input(""))
   A.append(int(k))
sm=sum(A)
avg=sm/n
print("SUM = ",sm)
print("AVERAGE = ",avg)

