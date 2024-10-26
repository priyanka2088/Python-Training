def remove_vowles(s):
    result=[]
    # vowles=['a','e','i','o','u','A','E','I','O','U']
    # for i in range(len(s)):
    #     if s[i] not in vowles:
    #         result+=s[i]
    return result

print("Please Enter the String :")
userInput=input()
print("String After Removing Vowles ="+remove_vowles(userInput))
