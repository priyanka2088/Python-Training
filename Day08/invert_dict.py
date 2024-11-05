data={1:'a',2:'b',3:'c'}
#i need key as value and value as key

print("-----way1-----")
new_data={}
for key in data:
    value=data[key]
    new_data[value]=key
print(new_data)  

new_data={}
print("-----way2-----")
for key,value in data.items():
    new_data[value]=key
print(new_data)
