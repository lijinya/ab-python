# -*- coding: utf-8 -*-
import os, sys, re, shutil

def searchfile(n, dirname):  
	 
	for basename in os.listdir(dirname):   
		path = os.path.join(dirname, basename)

		if os.path.isdir(path):  	
			searchfile(n + 1, path) 
		else:
			#pattern = re.compile(r'(.*?).html') #r'(.*?).txt'
			#if pattern.match(basename):
				#print basename
			if not os.path.getsize(path):
				continue
			if path.lower().endswith(".html"):
				print path
				shutil.copyfile(path, 'G:\\test\\' + basename)
			elif path.lower().endswith(".asp"): 
				print path
				shutil.copyfile(path, 'G:\\test\\' + basename)
			elif path.lower().endswith(".jsp"): 
				print path
				shutil.copyfile(path, 'G:\\test\\' + basename)
			elif path.lower().endswith(".php"): 
				print path
				shutil.copyfile(path, 'G:\\test\\' + basename)
			elif path.lower().endswith(".shtml"): 
				print path
				shutil.copyfile(path, 'G:\\test\\' + basename)
			elif path.lower().endswith(".htm"): 
				print path
				shutil.copyfile(path, 'G:\\test\\' + basename)
			elif path.lower().endswith(".aspx"): 
				print path
				shutil.copyfile(path, 'G:\\test\\' + basename)
				
				
if __name__ == "__main__" :

 try :
  searchfile(1,"G:\Python25")
  raw_input('Enter to continue...')
 except :
  print "execute search file fun error"
