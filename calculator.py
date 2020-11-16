# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 09:26:50 2020

@author: hp
"""

def add(a,b):
  return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def modulus(a,b):
    return a%b
print("Hello")
print("Welcome to Kachi's world")
print("Let's Calculate")

print("enter 1: add")
print("enter 2: sub")
print("enter 3: multiply")
print("enter 4: divide")
print("enter 5: modulus")

choice = int(input("enter 1/2/3/4/5"))
num1 = int(input("Enter the value of firstnum: "))
num2 = int(input("Enter the value of secondnum: "))
if choice == 1:
    print(num1, "+", num2, "is", add(num1,num2))
elif choice == 2:
    print(num1, "-", num2, "is", sub(num1,num2))
elif choice == 3:
    print(num1, "*", num2, "is", multiply(num1,num2))
elif choice == 4:
    print(num1, "/", num2, "is", divide(num1,num2))
elif choice == 5:
    print(num1, "%", num2, "is", modulus(num1,num2))    
else:
    print("invalid syntax")
