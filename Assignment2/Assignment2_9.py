#Write a program which accept number from user and return addition of digits in that number.
#-------------------------------------------------------------------------------------------

Number = int(input("Please Enter any Number: "))
Count = 0
while(Number > 0):
    Number = Number // 10
    Count = Count + 1

print("\n Number of Digits in a Given Number = %d" %Count)