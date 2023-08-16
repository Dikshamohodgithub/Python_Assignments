def Pattern(x):
    for i in range(x):
        for j in range(i,x):
            print("*",end="  ")

        print("\n")
          

x=int(input("Enter number: "))
Pattern(x)