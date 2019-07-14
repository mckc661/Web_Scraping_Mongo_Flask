
#import dependents
from splinter import Browser
from bs4 import BeautifulSoup


def scrape():

    mars_info_table = {}


#start the splinter engine to look at the web page

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)


# assign the url to url variable
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

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

    mars_info_table['new_title']= new_title
    mars_info_table['new_p']=new_p

##########twitter mars weather#############

    url3='https://twitter.com/marswxreport?lang=en'
    browser.visit(url3)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

# find the container for the weather tweet

    weather = soup.find('div', class_='js-tweet-text-container')

# extract the text

    new_weather=weather.text

# print(new_weather)
    mars_info_table['new_weater']=new_weather

################# Mars Fact##################

    import pandas as pd




    url= 'https://space-facts.com/mars/'


    tables= pd.read_html(url)
    tables

    df=tables[0]
    df.columns = ['Stats','Mars','Earth']

    df.head()


    html_table = df.to_html()
    html_table


    df.to_html('mar_facts_table.html')

    return mars_info_table