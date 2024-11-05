import re
pattern="^a...s$"
test_string=input("Enter the string to Test : ")
result=re.match(pattern,test_string)
if(result):
    print("Search Successfull")
else:
    print("Search UnSuccessfull")    