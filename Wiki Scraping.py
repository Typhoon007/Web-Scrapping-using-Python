#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sys
import pandas as pd
import requests
import bs4
req=requests.get('https://en.wikipedia.org/wiki/R')
# res.raise_for_status()
str1=[]
str2=[]
soup=bs4.BeautifulSoup(req.content,"lxml")
course=soup.find('div', class_='mw-body-content mw-content-ltr')
str1=course.get_text()
str2=str1[2130:10920]
print(str2)
# from fpdf import FPDF
# pdf=FPDF()
# pdf.add_page()
# pdf.set_font("Arial","B",16)
# pdf.write(4,str2)
# pdf.output("file.pdf")


# In[ ]:




