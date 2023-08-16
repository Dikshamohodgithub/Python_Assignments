def Number_Pattern(n):

    for i in range(n):
        for j in range(n):
            print(j+1,end=" ")
        print("\n")
   

n=int(input("Enter number: "))
Number_Pattern(n)