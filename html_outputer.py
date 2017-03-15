# -*- coding: utf-8 -*-
import pdb

class HtmlOutputer(object):
    
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self, count):
        fout = open()

        for data in self.datas:
            fout.write(data['title'].encode('utf-8')+' ')
            fout.write(data['summary'].replace('\n','').encode('utf-8')+'\n')

        fout.close()
