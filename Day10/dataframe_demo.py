import pandas as pd

# name=pd.Series(["Dhoni","Virat"])
# team=pd.Series(["CSK","RCB"])

# dict_1={"Name":name,"Team":team}

# df=pd.DataFrame(dict_1)
# print(df)

l=[{"Name":"Rahul","SirName":"Krishnan"},
   {"Name":"Manu","SirName":"Vijay"},
   {"Name":"Varsha","SirName":"Raj"}]
df=pd.DataFrame(l)
print(df)

#iterrows
for(row_index,row_value) in df.iterrows():
    print("\nRow Index is :: ",row_index)
    print("Row Value ::")
    print(row_value)

#iteritems
for(col_name,col_value) in df.items():
    print("\nColumn Name is :: ",col_name)
    print("Column Value ::")
    print(col_value)

    