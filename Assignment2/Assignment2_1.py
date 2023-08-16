import Arithmetic

def main():
    value1=int(input("Enter first value"))
    value2=int(input("Enter second value"))

    Result=0

    Result=Arithmetic.Add(value1,value2)
    print("Addition is: ",Result)

    Result=Arithmetic.Sub(value1,value2)
    print("Substraction is: ",Result)

    Result=Arithmetic.Mul(value1,value2)
    print("Multiplication is: ",Result)

    Result=Arithmetic.Div(value1,value2)
    print("Division is: ",Result)


if __name__=="__main__":
    main()