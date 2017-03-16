# coding: utf-8
import pdb
import cPickle

class HtmlOutputer(object):
	def writeTXT(self,file_name,data,count):
		fout = open(file_name+"/txt/"+str(count)+".txt",'w')
		fout.write(data['品名']+'\n')
		fout.write('UrCosme指數:'+data['like_heart']+'\n')
		fout.write(data['系列'].replace('\n',' ')+'\n')
		fout.write(data['品牌'].replace('\n',' ')+'\n')
		fout.write(data['容量'].replace('\n',' ')+'\n')
		fout.write(data['價格'].replace('\n',' ')+'\n')
		fout.write(data['上市日期'].replace('\n',' ')+'\n')
		fout.write(data['屬性'].replace('\n',' ')+'\n\n')
		fout.write('\n'+'心得文'+'\n')
		for cmt in data['心得文']:
			fout.write('\n'+cmt[0].replace('\n',' ').split('-')[0]+'\n')
			fout.write(cmt[1].replace('\n',' ').replace('\r','')+'\n')

		fout.close()

	def writePKL(self,file_name,data,count):
		fout = open(file_name+"/pkl/"+str(count)+".pkl", 'wb')
		cPickle.dump(data,fout)
		fout.close()
