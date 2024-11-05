import re
#pattern=r'\b\d{4}-\d{2}-\d{2}'
pattern=r'\b\d{4}-\d{2}-\d{2}|\b\d{2}/\d{2}/\d{4}'
input_str="i have work on 2024-10-14 and also on 23/12/2024"
dates=re.findall(pattern,input_str,re.IGNORECASE)
print(dates)