import pandas as pd

data={
    'Store':['Store1','Store1','Store2','Store2','Store3','Store3','Store4','Strore5'],
    'Region':['North','North','South','South','East','East','North','South'],
    'Sale':[200,150,300,250,400,350,100,200]
}
df=pd.DataFrame(data)
print(df)

df2=df.groupby(['Store']).agg({'Sale':sum}).reset_index()
print(df2)

df3=df.groupby(['Region']).agg({'Sale':sum}).reset_index()
print(df3)

df4=pd.merge(df,df3,on='Region',how='left',suffixes=('_Store','_Region'))
print(df4)

df4['SalesByRegion%']=df4['Sale_Store']/df4['Sale_Region']*100
print(df4)

