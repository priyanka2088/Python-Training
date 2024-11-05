#find words starting with specific letter
import re

def find_word_in_string(input_str):
    pattern=r'\bs\w*' # takes two or more digit
    words=re.findall(pattern,input_str,re.IGNORECASE)
    return words

#input
input_string="She sells sea shells on the sea shore in Goa"
words=find_word_in_string(input_string)
print(words)