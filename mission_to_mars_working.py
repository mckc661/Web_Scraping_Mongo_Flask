#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#import dependents
from splinter import Browser
from bs4 import BeautifulSoup


# In[ ]:


#start the splinter engine to look at the web page

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[ ]:


# assign the url to url variable
url = 'https://mars.nasa.gov/news/'
browser.visit(url)


# In[ ]:


# use beautiful soup and splinter to look at page

html = browser.html
soup = BeautifulSoup(html, 'html.parser')

# article title is found in the class of content_title
title = soup.find('div', class_='content_title')

# summary is in the class article_teaser_body

p = soup.find('div',class_='article_teaser_body')

# extract the text

new_title=title.text
new_p=p.text
print(new_title)
print(new_p)


import pandas as pd




url= 'https://space-facts.com/mars/'


# In[ ]:


tables= pd.read_html(url)
tables


# In[ ]:


df=tables[0]
df.columns = ['Stats','Mars','Earth']

df.head()


# In[ ]:


html_table = df.to_html()
html_table


# In[ ]:


df.to_html('mar_facts_table.html')


# In[ ]:




