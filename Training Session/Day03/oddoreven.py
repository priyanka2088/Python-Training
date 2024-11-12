def odd_even(num):
    if(num%2==0):
        return "Even"
    else:
        return "Odd"

print("Hi User, please Enter Your Number")
number=input()   
result=odd_even(int(number))
print("The given number "+number+" is "+result)
