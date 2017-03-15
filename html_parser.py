import pdb
import re
import urlparse
import urllib2
from bs4 import BeautifulSoup

class HtmlParser(object):

    def __init__(self,root_url):
        self.root_url = root_url

    def parse_search(self, page_url,html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont,'html.parser', from_encoding='utf-8')
        nextpage_url = self._get_page_url(page_url, soup)
        page_item_urls = self._get_item_url(page_url, soup)
        return nextpage_url,page_item_urls

    def parse(self,item_url,html_cont):
        if html_cont is None:
            return

        soup = BeautifulSoup(html_cont,'html.parser', from_encoding='utf-8')
        new_data = self._get_item_data(item_url,soup)
        new_data['心得文'] = self._get_item_comments(soup)

    def _get_item_comments(soup):
        cmts = []
        allCards = soup.find('div',class_='cards')
        

    def _get_item_data(self,item_url,soup):
        data = {}
        data['url'] = item_url
        info = soup.find('div',class_='board-content')
        data['like_heart'] = info.find('div',class_='deg').findAll('div',class_='text')[1].text
        
        info_rows = info.find('div',class_='info-tbl').findAll('div',class_='row')
        for row in info_rows:
            val = row.find('div',class_='val')
            if val:
                data[row.find('div',class_='name').text] = val.text
        return data
        

    def _get_page_url(self,page_url,soup):
        tail = soup.find('div',class_='pagination')\
            .find('a',class_='next_page')
        if tail:
            return self.root_url+tail['href']
        else:
            return

    def _get_item_url(self,page_url,soup):
        res_data = {}
        res_data['url'] = page_url

        item_list = soup.find('div',class_='product-list').findAll('div',class_='item')
       
        item_urls = [] 
        for item in item_list:
            tail = item.find('a')
            if tail:
                item_urls.append(self.root_url+tail['href'])
        return item_urls
        '''res_data['title'] = title_node.get_text()

        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div',class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()

        #pdb.set_trace()
        return res_data'''
        
           
    def download(self, url):
        if url is None:
            return None

        response = urllib2.urlopen(url,timeout=30)

        if response.getcode() != 200:
            return None

        return response.read()
