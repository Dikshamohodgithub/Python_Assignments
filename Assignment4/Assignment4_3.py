'''
Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90. Map function will increase each number by 10. Reduce will return product of all that numbers.

Input List -[4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

List after filter = 176, 89, 86, 90, 70]

List after map = [86, 99, 96, 100, 80] Output of reduce=6538752000
'''
from functools import reduce

def Greater(No):
    if(No >=70 and No<=90):
        return True 
    else:
        return False
    
def Increase(No):
    return No+10

def Product(No1,No2):
    return No1*No2

def main():
    Data=[]
    print("Enter number of elements: ")
    Size=int(input())

    print("Enter the elements:")
    for i in range(Size):
        value=int(input())
        Data.append(value)

    output=list(filter(Greater,Data))
    print("List after filter:",output)

    moutput=list(map(Increase,output))
    print("List after map:",moutput)

    Result=reduce(Product,moutput)
    print("Output of reduce:",Result)

if __name__=="__main__":
    main()