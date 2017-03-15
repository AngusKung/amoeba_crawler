# -*- coding: utf-8 -*-
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
        new_data['心得文'] = self._get_item_comments(soup)#type:[[reviewer,comment],[...],...]
        return new_data


    def _get_item_comments(self,soup):
        cmts = []
        cmt_page = 1
        print "reading cmt page No.",cmt_page
        all_cards = soup.find('div',class_='cards').findAll('div',class_='card')
        cmts += self._get_cards_comments(all_cards)
        next_cmt_page = soup.find('div',class_='pagination')
        while next_cmt_page:
            next_find = next_cmt_page.find('a',class_='next_page')
            if next_find:
                cmt_page += 1
                print "reading cmt page No.",cmt_page
                next_url = self.root_url + next_find['href']
                next_cont = self.download(next_url)
                next_soup = BeautifulSoup(next_cont,'html.parser', from_encoding='utf-8')
                next_all_cards = next_soup.find('div',class_='cards').findAll('div',class_='card')
                cmts += self._get_cards_comments(next_all_cards)
                next_cmt_page = next_soup.find('div',class_='pagination')
            else:
                next_cmt_page = None
        #while soup.fin
        print len(cmts)
        pdb.set_trace()
        return cmts


    def _get_cards_comments(self,all_cards):
        cards_cmts = []
        for card in all_cards:
            tail = card.find('a')
            if card.find('div',class_='info-anchors') and tail:
                cmt_url = self.root_url + tail['href']
                reviewer,cmt = self._get_cmt(cmt_url)
                cards_cmts.append([reviewer,cmt])
        return cards_cmts

    
    def _get_cmt(self,cmt_url):
        cmt_cont = self.download(cmt_url)
        soup = BeautifulSoup(cmt_cont,'html.parser', from_encoding='utf-8')
        return soup.find('div',class_='title-word').text,soup.find('div',class_='review-content').text
        

    def _get_item_data(self,item_url,soup):
        data = {}
        data['url'] = item_url
        info = soup.find('div',class_='board-content')
        data['like_heart'] = info.find('div',class_='deg').findAll('div',class_='text')[1].text
        
        print "Crawling",info.find('div',class_='info-tbl').find('div',class_='row').find('div',class_='val').text
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
        item_urls = [] 
        ad_or_item = soup.findAll('div',class_='product-list')
        for aoi in ad_or_item:
            item_list = aoi.findAll('div',class_='item')
            for item in item_list:
                tail = item.find('a')
                if tail:
                    item_urls.append(self.root_url+tail['href'])
        return item_urls

           
    def download(self, url):
        if url is None:
            return None

        response = urllib2.urlopen(url,timeout=60)
        if response.getcode() != 200:
            return None

        return response.read()
