# -*- coding: utf-8 -*-
import argparse
import sys

import url_manager,html_parser,html_outputer

class AmoebaMain(object):

    def __init__(self,load_file=""):
        self.root_url = "https://www.urcosme.com"
        self.init_url = "https://www.urcosme.com/search/product?keyword=%E8%B3%87%E7%94%9F%E5%A0%82"
        self.load_file = load_file
        self.new = True if len(load_file)==0 else False
        self.urls = url_manager.UrlManager(load_file)
        self.parser = html_parser.HtmlParser(self.root_url)
        self.outputer = html_outputer.HtmlOutputer()

    def crawl_search(self):
        if self.new:
            nextpage_url = self.init_url
            print "Searching..."
            while nextpage_url:
                self.urls.add_page_url(nextpage_url)
                html_cont = self.parser.download(nextpage_url)
                nextpage_url,item_urls = self.parser.parse_search(nextpage_url,html_cont)
                if item_urls:
                    self.urls.add_item_urls(item_urls)
            print "Searched",len(self.urls.page_urls),"pages"
            print "Found",len(self.urls.item_urls),"items"

    def crawl_cont(self):
        count = 1
        while self.urls.has_new_url():
            print "\nCrawling...item No.",count,
            new_url = self.urls.get_new_url()
            html_cont = self.parser.download(new_url)
            new_data = self.parser.parse(new_url,html_cont)
            count += 1
            self.outputer.collect_data(new_data)
        
            

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-new', help='Start a whole new crawling session', action="store_true")
    #parser.add_argument('-load', help='Load former urls in pickle form and continue crawling', dest="load_file", action="store")
    
    if len(sys.argv[1:])==0:
        parser.print_help()
        parser.exit()
    args = parser.parse_args()

    if args.new:
        obj_amoeba = AmoebaMain()
        obj_amoeba.crawl_search()
        obj_amoeba.crawl_cont()
        
