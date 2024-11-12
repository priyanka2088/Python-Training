import re
pattern='\d+'
test_str="hello 24 iam 32 now going on 55"
result=re.findall(pattern,test_str)
print(result)