def Factorial(n):
          i=1
          while n>0:
                    i=i*n
                    n=n-1
          return i

x=(int(input("Enter the number")))
print("Factorial ",x,Factorial(x))