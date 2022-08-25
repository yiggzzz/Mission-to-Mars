#!/usr/bin/env python
# coding: utf-8

# In[106]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[107]:


# Remember, set your executable path in the next cell, 
# then set up the URL (NASA Mars News) for scraping.
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[108]:


# assign the url and instruct the browser to visit it.
# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[109]:


# In the next empty cell, we'll set up the HTML parser:
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[110]:


# assign the title and summary text to variables we'll reference later
slide_elem.find('div', class_='content_title')


# In[111]:


# The title is in that mix of HTML in our output
# But we need to get just the text, and the extra HTML stuff isn't necessary.
# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[112]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[113]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[114]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[115]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[116]:


# Now we need to find the relative image URL
# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[117]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[118]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[119]:


df.to_html()


# ### Mars Weather

# In[120]:


# Visit the weather website
url = 'https://mars.nasa.gov/insight/weather/'
browser.visit(url)


# In[121]:


# Parse the data
html = browser.html
weather_soup = soup(html, 'html.parser')


# In[122]:


# Scrape the Daily Weather Report table
weather_table = weather_soup.find('table', class_='mb_table')
print(weather_table.prettify())


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# In[101]:


# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

browser.visit(url)


# In[102]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
for i in range(4):
    #create empty dictionary
    hemispheres = {}
    browser.find_by_css('a.product-item h3')[i].click()
    element = browser.links.find_by_text('Sample').first
    img_url = element['href']
    title = browser.find_by_css("h2.title").text
    hemispheres["img_url"] = img_url
    hemispheres["title"] = title
    hemisphere_image_urls.append(hemispheres)
    browser.back()


# In[103]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[104]:


# 5. Quit the browser
browser.quit()


# In[ ]:




