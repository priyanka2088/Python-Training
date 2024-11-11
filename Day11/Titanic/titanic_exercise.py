import pandas as pd

data=pd.read_csv(r"C:\Users\Administrator\Documents\UST Training\Python-Training\Day11\Titanic\titanic.csv")

avg_survived=data[data['Survived']==1]['Age'].mean()
avg_notsurvived=data[data['Survived']==0]['Age'].mean()
print(avg_survived,avg_notsurvived)

print(data.groupby(['Sex'])['Survived'].mean()*100)

data['family_size']=data['SibSp']+data['Parch']
print(data[['SibSp','Parch','family_size']].head())

data1=data.groupby(['family_size'])['Survived'].mean().reset_index()
data1.columns=['famil_size','family_survival_rate']
print(data1)


print(pd.merge(data,data1,on='family_size',how='left'))