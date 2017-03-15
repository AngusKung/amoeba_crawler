# coding=utf-8
import cPickle

class UrlManager(object):

    def __init__(self,path):
        if len(path) == 0:
            self.page_urls = set()
            self.item_urls = set()
    
    def add_page_url(self, url):
        if url is None:
            return
        if url not in self.page_urls:
            self.page_urls.add(url)
            print url

    def add_item_urls(self,urls):
        if len(urls)==0:
            return
        for url in urls:
            if url not in self.item_urls:
                self.item_urls.add(url)
                print url
    
    def has_new_url(self):
        return len(self.item_urls) != 0
        
    def get_new_url(self):
        new_url = self.item_urls.pop()
        return new_url
