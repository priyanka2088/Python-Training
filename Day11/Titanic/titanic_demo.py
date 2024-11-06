import pandas as pd

data=pd.read_csv(r"C:\Users\Administrator\Documents\UST Training\Python-Training\Titanic\titanic.csv")
# print(data.head())
# print(data['Age'].head())

# df=data[['Age','Sex']]
# print(df.head())

# df=data[data['Age']<25]
# print(df)

#print(len(data.index))

#print(data['Age'].mean())

# df=data[(data["Sex"]=='male') & (data['Age']<25)]
# print(df.mean())

# df.to_csv("filtered_titaniv.csv",index=False)

print(len(data[data['Survived']==1].index)/len(data.index) * 100)