import pandas as pd

# empdata={"eId":[11,12,13,14,15,16],
#          "ename":["Anu","Manu","Sanu","Vinu","Tharun","kiran"],
#          "age":[23,34,35,21,42,51]}
# df=pd.DataFrame(empdata)
# print(df)
# print(df['ename'])#datatype series
# print(df[['eId','ename']])#datatype datframe

s=pd.Series([10,15,20,34,28])
df=pd.DataFrame(s)
df.columns=["List1"]
df["List2"]=2
df["List3"]=df["List1"]+df["List2"]
print(df)

df.pop("List3")
df1=df.drop("List2",axis=1)#delete data column wise(axis=1)
print(df1)
df2=df.drop(index=[2,3],axis=0)#delete data row wise with given index
print(df2)

