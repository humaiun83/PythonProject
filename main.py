import requests
from bs4 import BeautifulSoup

website_url = "http://books.toscrape.com/"

class WebsiteScrapper: 
    def __init__(self) -> None:
        self.content = self.get_website_content(website_url)
    
    def get_website_content(self,url):
        response = requests.get(url)
        return response.content


    def get_books_topics(self):
        soup = BeautifulSoup(self.content, 'html.parser')
        topic_ul = soup.find_all('ul', class_="nav-list")[0]

        topic_li = topic_ul.find_all('li')[0]
        
        topics_ul = topic_li.find('ul')
        topics_li = topics_ul.find_all('li')

        for topic in topics_li:
            topic_name = topic.find('a').text
            print(topic_name.strip())


WebsiteScrapper().get_books_topics()
