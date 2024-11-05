def arithemeticfun(num1,num2,choice):
    print("Start of the Function")
    if(choice=="add"):
        return num1+num2
    elif(choice=="sub"):
        return num1-num2
    elif(choice=="multi"):
        return num1*num2


input_code=0
while(input_code != 4):
    print("1.Addition of Two Numbers\n2.Subtraction of Two Numbers\n3.Multiplication of Two Numbers\n4.Exit\n")
    input_code=int(input("Enteryour Choice : "))
    if(input_code== 1):
        a=int(input("Enter the First Number : "))
        b=int(input("Enter the Second Number : "))
        print("a + b = ",arithemeticfun(a,b,"add"))
    elif(input_code== 2):
        a=int(input("Enter the First Number : "))
        b=int(input("Enter the Second Number : "))
        print("a - b = ",arithemeticfun(a,b,"sub")) 
    elif(input_code==3):
        a=int(input("Enter the First Number : "))
        b=int(input("Enter the Second Number : "))
        print("a * b = ",arithemeticfun(a,b,"multi"))
print("end ")        
        

