""" Create a Program to read a csv file which contains large text of some novel. 
Get the frequencies of all words in the file and 
finally show the frequencies for each word in a pandas data frame."""

import pandas as pd
import string

def clean_text(textline):
    textline=textline.lower()
    textline=textline.translate(str.maketrans('','',string.punctuation))
    return textline

def find_word_frequency(file_handle):
    frequencies={}
    for line in file_handle:
        #print('***'+line+'***')
        line=line[:-1:]
        line=clean_text(line)
        line_list=line.split()
        for words in line_list:
            if words not in frequencies:
                frequencies[words]=1
            else:
                frequencies[words]+=1        
    df=pd.DataFrame(frequencies.items(),columns=['Words','Frequency'])
    return df           

       
file_handle=open(r'C:\Users\Administrator\Documents\UST Training\Python-Training\Assessments\Milestone1\data.csv','r')
frequency_df=find_word_frequency(file_handle)
frequency_df.to_csv('word_frequency.csv',index=False)
print(frequency_df)
