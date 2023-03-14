

website_url = "http:books.toscrape.com/"

class WebsiteScrapper: 
    def __init__(self) -> None:
        self.content = self.get_webiste_content(website_url)
    
    def get_website_content(self,url):
        response = requests.get(url)
        return response.content