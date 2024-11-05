import pandas as pd

serie1=pd.Series([1,2,3,4,5])
print("Multiply Series Value by 2")
print(serie1*2)
print("Find Square f all series value ")
print(serie1*serie1)
print("Find All Series Value greater than 2")
print(serie1[serie1>2])

s1=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
s2=pd.Series([10,20,30,40,50],index=['a','b','c','d','e'])
s3=pd.Series([11,21,31,41],index=['a','b','c','d'])
print("Add series 1 and 2")
print(s1+s2)
print("Addseries2 and 3")
print(s2+s3)
print("Add series 2 and 3 , fill unmatched index with zero")
print(s2.add(s3,fill_value=0))