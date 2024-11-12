import pandas as pd

data1=[{"Name":"SSS","Age":19,"Birth City":"Chennai"},
   {"Name":"QQQ","Age":22,"Birth City":"Pune"},
   {"Name":"AAA","Age":18,"Birth City":"Bangalore"},
   {"Name":"RRR","Age":32,"Birth City":"Trivandrum"}]

data2=[{"Name":"SSS","Work Experience":1,"Work City":"New York"},
   {"Name":"QQQ","Work Experience":2,"Work City":"London"},
   {"Name":"AAA","Work Experience":3,"Work City":"USA"}]

df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)
print(df1)
print(df2)

df3=pd.merge(df1,df2,on="Name")
print(df3)

df3=pd.merge(df1,df2,on="Name",how="outer")
print(df3)
df3.to_csv('test_output.csv',index=False)

df3['Work Experience']=df3[df3["Name"]=="RRR"]['Work Experience'].fillna(value=df3["Work Experience"].mean)
print(df3)