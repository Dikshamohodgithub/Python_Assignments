'''
Write a program which contains one lambda function which accepts two parameters and return

its multiplication.

Input: 4 3 Input: 6 3

Output:12 Output:18
'''
def Multiplication(No1,No2):
    return No1 * No2

MultiplicationX =lambda No1,No2: No1 * No2
def main():
    # value=int(input("Enter number: ")) user input
    #Result=Power(value)
    Result=Multiplication(4,3)
    print("Output:",Result)

    Result=Multiplication(6,3)
    print("Output:",Result)

if __name__=="__main__":
    main()

'''
Output: 12
Output: 18
'''