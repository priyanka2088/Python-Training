dict1={1:"RR",8:"MM",5:"SS",2:"PP"}
print(dict1)
max=-1
for key in dict1:
    if(key>max):
        max=key
print(max)    

print(dict1.keys())
print(type(dict1.keys()))
print(max(dict1.keys()))