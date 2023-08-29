'''
Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all prime numbers. Map function will multiply each number by 2. Reduce will return Maximum number from that numbers. (You can also use normal functions instead of lambda functions).

Input List = [2, 70, 11, 10, 17, 23, 31, 771 List after filter [2, 11, 17, 23, 31]

List after map = [4, 22, 34, 46, 62]

Output of reduce = 62
'''
from functools import reduce

def Prime(No):
    for i in range(2,No):
        if(No % i==0 ):
            return False
        else:
            return True
    
def Multiply(No):
    return No*2

def Maximum(No1,No2):
    if(No1>No2):
        return No1
    else:
        return No2

def main():
    Data =[]

    print("Enter number of elements : ")
    Size = int(input())

    print("input number: ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    print("Input data: ",Data)

    Output=list(filter(Prime,Data))
    print("list after filter: ",Output)

    moutput = list(map(Multiply,Output))
    print("list after map :",moutput)

    result= reduce(Maximum,moutput)
    print("output of reduce: ",result)

if __name__=="__main__":
    main()
