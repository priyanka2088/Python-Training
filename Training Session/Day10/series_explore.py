"""
Implement 5 methods and any 5 attributes in series
"""
import pandas as pd

s=pd.Series([14,10,23,34,5],index=['a','b','c','d','e'])
#attributes
print("-------loc-------")
print(s.loc['d'])
print("-------iloc------")
print(s.iloc[3])
print("-------iat--------")
print(s.iat[2])#access a single value
print("-------empty--------")
print("is 's' series empty ?",s.empty)
s=s[s<5]
print(s)
print("is 's' series empty ?",s.empty)

print("-------is_unique------")
s1=pd.Series([1,2,3])
s2=pd.Series([1,2,2,3])
print("is s1 series is unique? ",s1.is_unique)
print("is s2 series is unique ? ",s2.is_unique)


#Methods
s=pd.Series([1,2,3,3,5,6,2,4])
print("-------where-------")
print(s.where(s>=3))
print("-------Unique-------")
print(s.unique())
print("-------sort_values-------")
print(s.sort_values(ascending=True))
print("-------replace-------")
print(s.replace(2,8))
print("-------drop_duplicates-------")
print(s.drop_duplicates())

