#Write a program which contains one function named as Add() which accepts two numbers from user and return addition of that two numbers.
#----------------------------------------------------------------------------------------------------------------------------------------

def Add(No1,No2):
    Addition = No1+No2
    return Addition

value1=int(input("Enter value1 : "))
value2=int(input("Enter value2 : "))
Answer=Add(value1,value2)

print("Addition is: ",Answer)