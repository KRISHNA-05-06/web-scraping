# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 22:46:44 2023

@author: KOTA SRIKRISHNA SAI
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup
#import os
#import nltk
#from nltk.tokenize import word_tokenize
#from nltk.corpus import stopwords
#nltk.download('punkt')
#nltk.download('stopwords')
#import re

# Creating a dataframe of url's given in excel sheet

input_df = pd.read_excel(r'D:\blackcoffer\Input.xlsx')

# No:of links in given excel sheet

n=len(input_df)
        
# Extract each link heading and content into text files named URL_ID.txt

for i in range(n):
    url = input_df['URL'][i]
    try:
        page = requests.get(url)
        page.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(e)
        continue
    else:
        soup = BeautifulSoup(page.content,'html.parser')
        title = soup.h1.text
        #title = soup.findAll(attrs = {'class':'td-post-title'})
        content = soup.findAll(attrs = {'class':'td-post-content'})
        content1 = content[0].text.replace('\n',' ')
        title_string = str(title)
        content_string = str(content1)
    
        with open(r"D:\blackcoffer\urlid\\"+str(input_df['URL_ID'][i])+'.txt',"w",encoding='utf-8') as file:
            file.write(title_string)
            file.write('\n')
            encoded_content = content_string.encode('utf-8')
            file.write(encoded_content.decode('utf-8')) 
            
