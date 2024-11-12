import pandas as pd

runs={'Tcs':{'Qtr1':2500,'Qtr2':3000,'Qtr3':3500,'Qtr4':2800},
      'Wipro':{'Qtr1':3500,'Qtr2':2000,'Qtr3':2400,'Qtr4':1000},
      'UST':{'Qtr1':2600,'Qtr2':4000,'Qtr3':1500,'Qtr4':4200}}

df=pd.DataFrame(runs)
print("---------loc-----------")
print(df)
print(df.loc['Qtr3',:])
print(df.loc['Qtr1':'Qtr3',:])
print(df.loc[:,'Wipro'])
sum=df.loc[:,'Wipro'].sum()
print(sum)
print(df.loc['Qtr1'])
print(df.loc['Qtr1':'Qtr3'])

print("---------iloc-----------")

#iloc
print(df.iloc[2,:])
print(df.iloc[0:2,:])
print(df.iloc[:,1])
sum=df.iloc[:,1].sum()
print(sum)
print(df.iloc[0])
print(df.iloc[0:1])

print("Top 3 rows",df.head(3))
print("Last 2 Rows",df.tail(2))

s={'Name':["Anu","Manu","Sanu","Varun"]}
df1=pd.DataFrame(s,index=[True,False,True,False])
print(df1)
df1.columns=["Name"]
print(df1)
print(df1.loc[True])
print(df1.iloc[1])