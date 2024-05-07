#!/usr/bin/env python
# coding: utf-8

# In[37]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[38]:


def scrape_reviews(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  review_containers = soup.find_all('div', class_='EGFGHd')
  for review in review_containers:
    review_text = review.find('div', class_='h3YV2d').text.strip()
    customer_name = review.find('div', class_='X5PpBb').text.strip()
    rating = review.find('div', class_='iXRFPc')['aria-label'].strip()
    print("Customer Name:", customer_name)
    print("\nRatings:",rating)
    print("\nReview:", review_text)
    print("-------------------------------------\n")


# In[39]:


url="https://play.google.com/store/apps/details?id=com.whatsapp&hl=en&gl=US"
scrape_reviews(url)


# In[ ]:




