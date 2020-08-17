from splinter import Browser
from bs4 import BeautifulSoup
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/Users/Bhavin/Downloads/chromedriver"}
    #C:\Users\Bhavin\Downloads\chromedriver_win32
    return Browser("chrome", **executable_path, headless=False)


def scrape_mars1():
    browser = init_browser()
    
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)
    time.sleep(2)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    time.sleep(2)

    mars = {}

    mars["news_title"] = soup.find_all('div', class_='content_title')[1].a.text
    mars["news_p"] = soup.find_all('div', class_='article_teaser_body')[0].text

    return mars


def scrape_mars2():
    browser = init_browser()
    
    url2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url2)
    time.sleep(2)
    html2 = browser.html
    soup = BeautifulSoup(html2, "html.parser")
    time.sleep(2)

    baseurl = 'https://www.jpl.nasa.gov'
    resultimage = soup.find('img', class_='thumb')

    featured_image_url = 'https://www.jpl.nasa.gov' + resultimage.get('src')

    return featured_image_url


def scrape_mars3():
    browser = init_browser()
    
    url3 = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url3)
    time.sleep(2)
    html3= browser.html
    soup = BeautifulSoup(html3, "html.parser")
    time.sleep(2)

    resultmars = soup.find_all('span', class_='css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0')
    mars_weather = resultmars[31].text

    return mars_weather


def scrape_mars4():
    browser = init_browser()
    
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    resultsmarstable = pd.read_html(url)
    table = resultsmarstable[0]
    table.columns = ['Description', 'Value']
    table.set_index('Description', inplace=True)
    html_table = table.to_html(index = True, header = True)
        
    return html_table


def scrape_mars5():
    browser = init_browser()

    url5='https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(url5)
    time.sleep(2)
    html5=browser.html
    soup=bs(html5, 'html.parser')
    time.sleep(2)
    resultcerberus = soup.find('img', class_='wide-image')
    cerberus_image_url = 'https://astrogeology.usgs.gov' + resultcerberus.get('src')


    url6='https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    browser.visit(url6)
    time.sleep(2)
    html6=browser.html
    soup=bs(html6, 'html.parser')
    time.sleep(2)
    resultschiaparelli = soup.find('img', class_='wide-image')
    schiaparelli_image_url = 'https://astrogeology.usgs.gov' + resultschiaparelli.get('src')
        
    
    url7='https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(url7)
    time.sleep(2)
    html7=browser.html
    soup=bs(html7, 'html.parser')
    time.sleep(2)
    resultsyrtis = soup.find('img', class_='wide-image')
    syrtis_image_url = 'https://astrogeology.usgs.gov' + resultsyrtis.get('src')
          
    
    url8='https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser.visit(url8)
    time.sleep(2)
    html8=browser.html
    soup=bs(html8, 'html.parser')
    time.sleep(2)
    resultvalles = soup.find('img', class_='wide-image')
    valles_image_url = 'https://astrogeology.usgs.gov' + resultvalles.get('src')
    

    hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": valles_image_url},
    {"title": "Cerberus Hemisphere", "img_url": cerberus_image_url},
    {"title": "Schiaparelli Hemisphere", "img_url": schiaparelli_image_url },
    {"title": "Syrtis Major Hemisphere", "img_url": syrtis_image_url },
    ]
    
    return hemisphere_image_urls

    




