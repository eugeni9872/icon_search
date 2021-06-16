from threading import Thread
import threading

import os
import requests
from bs4 import BeautifulSoup

from .consts import URL
from .exceptions import NoCategory



class IconSearch(Thread):
    category = None  # The category to search
    max_page = 1  # By default get only the page 1
    result = None
    def __init__(self, category=None, max_page=1, *args, **kwargs):
        super(IconSearch, self).__init__(*args, **kwargs)
        
        if not category:
            raise NoCategory("Category can't be None")

        self.category = category
        self.max_page = max_page

       
    
    def get_html(self):
        """Make an request to the category and get the webpage html"""
        try:
            result = requests.get(f"{URL}?{self.category}")
            if result.status_code == 200:
                self.result = result
        except Exception as e:
            print(e)

    def get_icon_tags(self):
        if self.result:
            soup = BeautifulSoup(self.result.content, "html.parser")
            icons_items = soup.findAll('img', {'class': 'lzy'})
            self.urls = [{
                'url': icon['data-src'],
                'name':  icon['data-src'].split('/')[-1]
            } for icon in icons_items]
           
    def start_download(self):
        if self.urls:
            for url in self.urls:
                pth = "{}/output/{}".format(os.environ.get('APP_PATH'), self.category)
                file_name = url.get('name')
                if not os.path.exists(pth):
                    os.makedirs(pth)

                response = requests.get(url.get('url'))
                with open(f'{pth}/{file_name}', 'wb') as file:
                    file.write(response.content)


    def run(self):
        self.get_html()
        self.get_icon_tags()
        
        self.start_download()
        
        
    
    def log(self):
        pass
