def printname(name,num):
    for i in range(num):
         print(str(i)+":"+name) 

print("Enter the User Name")
username=input()
print("How many times you want to print")
number=int(input())
printname(username,number)   