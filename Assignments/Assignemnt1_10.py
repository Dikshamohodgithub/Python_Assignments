#Write a program which accept name from user and display length of its name.

#---------------------------------------------------------------

"""def Count():

    str=input("Enter name:")
    string=len(str)
     print(string)

Count()
"""

def String_Length(x):
          j=0
          for i in x:
                    j=j+1
          print("Length of stirng=",+j)

x=input("Enter  string ")
String_Length(x)
