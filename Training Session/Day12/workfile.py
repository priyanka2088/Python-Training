import pandas as pd

data1=[{"Name":"RRR","Age":23,"City":"Kolkata"},
   {"Name":"PPP","Age":24,"City":"Palakkad"}]
df1=pd.DataFrame(data1)
print(df1)

data2=[{"Name":"SSS","Age":21,"City":"Chennai"},
   {"Name":"QQQ","Age":32,"City":"Pune"},
   {"Name":"AAA","Age":18,"City":"Bangalore"}]
df2=pd.DataFrame(data2)
print(df2)

df3=pd.concat([df1,df2])
print(df3)
print(df3.loc[0])
df3=pd.concat([df1,df2],ignore_index=True)
print(df3.loc[0])

#change 2nd Positin person city
df3.loc[2,'City']='Mumbai'
print(df3)

print(df3.loc[df3["Name"]=="SSS",'City'])
df3.loc[df3["Name"]=="SSS",'City']="Trivandrum"
print(df3)