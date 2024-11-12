import pandas as pd
df=pd.read_csv(r"C:\Users\Administrator\Documents\UST Training\Python-Training\Day12\test_output.csv")
print(df)

def is_even_or_Not(value):
    if(value%2==0):
        return True
    else:
        return False

df["Is Even"]=df['Work Experience'].apply(is_even_or_Not)
print(df)



