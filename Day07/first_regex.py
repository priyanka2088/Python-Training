import re

def find_numbers_in_string(input_str):
    #pattern=r'\d'#takes a single
    pattern=r'\d+' # takes two or more digit
    number=re.findall(pattern,input_str)
    return number

#input
input_string="Thera are 4 boxes, 5 pencils and 101 windows"
number=find_numbers_in_string(input_string)
print(number)