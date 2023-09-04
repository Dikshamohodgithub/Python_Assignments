'''
 Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which are even. Map function will calculate its square. Reduce will return addition of all that numbers.

Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]

List after filter = [2, 4, 4, 2, 8, 10] List after map = [4, 16, 16, 4, 64, 100]

Output of reduce =204
'''
from functools import reduce

def CheckEven(No):
    if(No %2 ==0 ):
        return True
    else:
        return False
    
def Square(No):
    return No**2

def Add(No1,No2):
    return No1+No2

def main():
    Data=[]
    print("Enter number of elements: ")
    Size=int(input())

    print("Enter the elements:")
    for i in range(Size):
        value=int(input())
        Data.append(value)

    output=list(filter( CheckEven,Data))
    print("List After filter: ",output)

    moutput=list(map(Square,output))
    print("List After map:",moutput)

    Result=reduce(Add,moutput)
    print("Output of reduce ",Result)

if __name__=="__main__":
    main()