# -*- coding: utf-8 -*-
import pdb

class HtmlOutputer(object):
    
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self, count,file_name):
        fout = open(file_name+".txt",'w')

        for data in self.datas:
            fout.write(data['品名'].encode('utf-8')+'\n')
            fout.write(data['系列'].encode('utf-8')+'\n')
            fout.write(data['品牌'].encode('utf-8')+'\n')
            fout.write(data['容量'].encode('utf-8')+'\n')
            fout.write(data['價格'].encode('utf-8')+'\n')
            fout.write(data['上市日期'].encode('utf-8')+'\n')
            fout.write(data['屬性'].encode('utf-8')+'\n\n')
            for cmt in data['心得文']:
                fout.write('\n'+cmt[0].split('-')[0]+'\n')
                fout.write(cmt[1].replace(' ','').replace('\n',' ')+'\n')

        fout.close()
