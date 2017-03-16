# coding: utf-8
import pdb

class HtmlOutputer(object):
	def writeTXT(self,file_name,data):
		fout = open(file_name+".txt",'w')
		fout.write(data['品名'].replace('\n',' ').encode('utf-8')+'\n')
		fout.write('UrCosme指數:'+data['like_heart']+'\n')
		fout.write(data['系列'].replace('\n',' ').encode('utf-8')+'\n')
		fout.write(data['品牌'].replace('\n',' ').encode('utf-8')+'\n')
		fout.write(data['容量'].replace('\n',' ').encode('utf-8')+'\n')
		fout.write(data['價格'].replace('\n',' ').encode('utf-8')+'\n')
		fout.write(data['上市日期'].replace('\n',' ').encode('utf-8')+'\n')
		fout.write(data['屬性'].replace('\n',' ').encode('utf-8')+'\n\n')
		for cmt in data['心得文']:
			fout.write('\n'+cmt[0].replace('\n',' ').encode('utf-8').split('-')[0]+'\n')
			fout.write(cmt[1].replace(' ','').replace('\n',' ').encode('utf-8')+'\n')

		fout.close()
