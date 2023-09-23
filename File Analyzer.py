#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re

def file_analysis(file_to_read):
    
    # input
    
    try:
        with open(file_to_read,'r') as f:
             read_file = f.read()
    
    except:
        print('This file is not found')
        return

    # text parsing
    
    read_file = re.sub(r'[^\w\s]',' ',read_file)
    read_file = re.sub(r'\n',' ',read_file)
        
    # word count calculation
    
    file_list = read_file.split()
    word_count = len(file_list)
    
    # character counts
    
    character_counts = len(read_file)
    
    # Word Frequency Calculation
    
    file_dictionary = {}
    for i in file_list:
        i = i.lower()
        
        if i in file_dictionary:
            file_dictionary[i]+=1
            
        else :
            file_dictionary[i]=1
            
    # output
    
    print("---------- File Analyzer Report ----------")
    print('word count: ',word_count)
    print('character count: ',character_counts)
    print('word frequency: ')
    
    for word,count in file_dictionary.items():
        print(f'{word}:{count}')
        
file_to_read= input('enter the path:')
file_analysis(file_to_read)

