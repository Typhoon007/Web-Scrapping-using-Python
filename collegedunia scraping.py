#!/usr/bin/env python
# coding: utf-8

# In[14]:



import requests
clg_india_url='https://collegedunia.com/btech/kottayam-colleges'
request= requests.get(clg_india_url)
request.status_code

len(request.text)

page_contents=request.text #taking the text of website in a variable 
page_contents[:400]


from bs4 import BeautifulSoup
doc = BeautifulSoup(page_contents, 'html.parser')

selection_class = "jsx-765939686 text-white font-weight-bold text-md m-0"

clg_name = doc.find_all('h3', {'class': selection_class})
len(clg_name)

clg_name[:6]

for x in clg_name:
    final_clg_name.append(x.text.strip())
len(final_clg_name)


fees_class_selection="jsx-765939686 lr-key text-lg text-primary d-block font-weight-bold"
fees=doc.find_all('span', {'class':fees_class_selection})

len(fees)

fees[: :]

fees[85]
# there are 2 outliers so making 3 sublists
fees_list1= fees[:37]
fees_list2=fees[37:86]
fees_list3=fees[87:]
fees1=[]
for x in fees_list1[0::3]:
    fees1.append(x.text)
for x in fees_list2[0::3]:
    fees1.append(x.text)
for x in fees_list3[0::3]:
    fees1.append(x.text)
len(fees1)


course_name_class= 'jsx-765939686 lr-value d-block'
course_name=doc.find_all('span' , {'class':course_name_class})
len(course_name)

course_name[: :]
course_title=[]
for x in course_name:
    course_title.append(x.get('title'))
len(course_title)

course_list1= course_title[:37]
course_list2=course_title[37:86]
course_list3=course_title[87:]
final_course_name=[]
for x in course_list1[0::3]:
    final_course_name.append(x.strip())
for x in course_list2[0::3]:
    final_course_name.append(x.strip())
for x in course_list3[0::3]:
    final_course_name.append(x.strip())
final_course_name[:5]

stripped_course_name=[]
for x in final_course_name:
    new_string=x.replace("- First Year Fees","")
    stripped_course_name.append(new_string.strip())
stripped_course_name2=[]
for x in stripped_course_name:
    new_string=x.replace("- Total Fees","")
    stripped_course_name2.append(new_string.strip())
stripped_course_name2[:6]

len(stripped_course_name2)

eligi_class='jsx-2675951502'
eligi=doc.find_all('span',{'class':eligi_class})
len(eligi)

eligi[0].text.strip()

final_eligi=[]
for x in eligi:
    final_eligi.append(x.text.strip())
final_eligi[: :]





    


# Converting to csv

import pandas as pd
clg_dict = {
    'Clg_name': final_clg_name,
    'Course': stripped_course_name2,
    'eligibility':final_eligi
}

top_colleges_df = pd.DataFrame({ key:pd.Series(value) for key, value in clg_dict.items() })
top_colleges_df[:6].style.hide_index()
top_colleges_df.to_excel('top_clgs.xlsx', index=None)

  


# In[ ]:




