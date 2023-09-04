'''

Write a program which contains one lambda function which accepts one parameter and return power of two.

Input: 4 Input: 6

Output: 16 Output:64

'''

def Power(No):
    return 2**No

PowerX =lambda No: 2**No
def main():
    # value=int(input("Enter number: ")) user input
    #Result=Power(value)
    Result=Power(4)
 
    print("Output:",Result)

    Result=Power(6)
    print("Output:",Result)

if __name__=="__main__":
    main()

'''

Output: 16
Output: 64
'''
