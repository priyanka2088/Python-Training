try:
     num1=int(input("enter numerator"))
     num2=int(input("enter denominator"))
     result=num1/num2
     print(result)

except ZeroDivisionError as e:
     print("you cannot divide by zero")

except Exception as e:
     print("Something happened, we are looking into it")
     print(e)

print("Completed successfully")
