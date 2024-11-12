import re
#pattern='[1-9]'#only numbers
pattern='[^1-9]'#not numbers
test_string=input("Enter the string to Test : ")
result=re.match(pattern,test_string)
if(result):
    print("Search Successfull")
else:
    print("Search UnSuccessfull")    