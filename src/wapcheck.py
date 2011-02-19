# -*- coding: utf-8 -*-
'''
try:
	catch(bubble_bear)
except:
	throw(xiaxia)	
finally:
	eat(ib)
raise fb	
'''
'''
	要注意的是：
	1. 现在的记录方式是追加方式，如果要用覆盖方式，请自行用logo记录，然后一次写入（似乎它只能一次）
	2. 复制网页文件到指定路径下的功能已注释，如有需要，请自行修改
	3. 现写了的网页格式有'html', 'mht', 'jsp', 'htm', 'php', 'shtml', 'asp'，如有需要，请自行添加
	4. http://chardet.feedparser.org/download/ for chardet
	5. ....
'''
import os, sys, re, shutil, binascii, chardet
startpath = "J:\\Python25\\"					#被操作的文件夹
targetpath = "J:\\test\\"						#复制文件的目的路径
logopath = "J:\\test\\logo.txt"					#提取title存入的文件
notitle = '无标题'
codetype = 'utf8'#GB18030如果不行改成uft8
#gb2312 双字节，区别再于GB18030是最新标准字比gb2312多，不过gb2312跟uft8可兼容的系统（包括手机）更多
g_wap_pattern = ['html', 'mht', 'jsp', 'htm', 'php', 'shtml', 'asp', 'xhtml', 'aspx']
												#各种网页格式
g_code_type = ['utf8','utf-8','gb18030', 'gb2312', 'gbk', 'utf-7', 'utf-32','utf-16', 'windows-1250','ISO-8859-2','utf-32BE','IBM037','IBM437','IBM500','ibm737','IBM860','ibm861','ks_c_5601-1987','IBM01140','IBM01141','IBM01146','IBM01147','IBM01148','UnicodeFFFE', 'Johab','x-mac-japanese','x-mac-chinesetrad','x-mac-korean','x-mac-chinesesimp','x-mac-greek','x-mac-ce','x-Chinese-CNS','x-cp20001','x-Chinese-Eten','x-cp20003','x-cp20004','x-IA5-German','EUC-JP','x-cp20936','x-cp20949','x-cp50227','hz-gb-2312']		
												#第一个是用来覆盖的，其它可以修改
#logo = ["logo:\r\n"]
#以上写在这里只是为了便于修改，如果有需要，也可以写成管道方式或其它方式

'''
def ansymhttitle(string):						#不能得到非汉字，并且做复杂了
	strinfo = re.compile(r'=..')
	strlist = strinfo.findall(string)
	string = ''
	
	for i in range(0, len(strlist)):
		strlist[i] = hex(int(strlist[i].replace('=', '') , 16)).replace('0x', '') # 多此一举
		string = string + binascii.a2b_hex(strlist[i])
	return string
'''

def makefolder(inFolderName, FolderName):
	if os.path.isdir( inFolderName ):
		newFolderName = inFolderName + '' + FolderName
		if os.path.isdir( newFolderName ):
			print(newFolderName," Exists already ")
		else:
			os.mkdir(newFolderName)
			print(newFolderName," Create OK ")
	else:
		print(inFolderName," not exists, script stop ")
		
def ansymhttitle(string):
	string = string.replace('=\n', '')			#去除'=\n' 也可以换成\n
	strinfo = re.compile(r'=\w\w|=\s')#r'=..'	# 匹配字母与数字
	strlist = strinfo.findall(string)
	#print strlist								#测试时用

	for i in range(0, len(strlist)):
		string = string.replace(strlist[i], binascii.a2b_hex(strlist[i].replace('=', '')))
	return string								#替换为相应ascii码后返回
	
def gettitle(url, waptype):
	file_object = open(url)						#开打文件

	try:
		content = file_object.read( )			#读取文件内容
		#chartypeall = chardet.detect(content).values()[1]
		#print chartypeall
		#chartype = chardet.detect(content).values()[1]
		title = re.findall(r"<title>([\s\S]*?)</title>", content, re.M)
		#意思是取<title></title>间的任意多的所有字符\s是空白字符\S是非空白字符
		#r"<title>\s*(.*?)\s*</title>", 这个不对换行进行判断，现在的可以
		#titlepattern = re.compile(r"<TITLE>[...]</TITLE>")
		#title = titlepattern.search(content);	
		if(title):
			if '' == title[0]:
				title[0] = notitle				#找到为空时，无标题
		else: 
			title = re.findall(r"<TITLE>([\s\S]*?)</TITLE>", content, re.M)
			if title:							#上面对大写的<TITLE>标签进行判断
				if '' == title[0]:
					title[0] = notitle			#找到为空时，无标题
			else: 
				title.append(notitle)			#未找到时，无标题
				
		if not cmp(waptype, "mht"):				#如果是mht文件，则对其title解码
			title[0] = ansymhttitle(title[0])
		
		chartype = chardet.detect(title[0]).values()[1]
		print chartype
		g_code_type[0] = chartype
		title[0] = title[0].replace('\n', '')	#去掉换行符（主要针对<title>后面的）
		#title[0] = title[0].decode(chartype).encode(codetype)
		temp = title[0]
		for i in range(0, len(g_code_type) - 1):
			try:
				temp = title[0].decode(g_code_type[i])
				temp = temp.encode(codetype)
				break
			except:
				continue
		title[0] = temp
		print title[0].decode(codetype).encode('GB18030')
												#这里只是为了屏幕上显示的不是乱码，如果想提高效率，可以删除
	finally:
		file_object.close()					#关闭文件
		
	return title[0]
		
def searchfile(n, dirname):  
	 
	for basename in os.listdir(dirname):   
		path = os.path.join(dirname, basename)	#得到路径下所有的文件的完整路径

		if os.path.isdir(path):  	
			searchfile(n + 1, path) 			#递归搜索文件
		else:
			#pattern = re.compile(r'(.*?).html') #r'(.*?).txt'
			#if pattern.match(basenames):
				#print basenames
			if not os.path.getsize(path):		#判断文件的大小，如果为空则不执行下面的代码
				continue
				
			for i in range(0, len(g_wap_pattern)):
				if path.lower().endswith(g_wap_pattern[i]):
					print '文件路径：' + path	#当是网页文件后缀时打印路径
					#拷贝文件到目标地
					title = gettitle(path, g_wap_pattern[i])	#得到该网页的title
					#logo.append("http://" + lastpath[n] + "/" + "\t" + title + "\n")
					folder = dirname.split("\\")[-1]
					logostr = dirname.replace(startpath, 'http://').replace('\\', '/') + "/" + "\t" + title + "\n"
					makefolder(targetpath,  folder)
					shutil.copyfile(path, targetpath +  folder + '\\' + basename)
					file_logo = file(logopath, 'a')				#以追加方式打开
					try:
						file_logo.write(logostr)				#写入信息
					except IOError:  
						print('IOError')
					#finally:
					#file_logo.colse()
					break
				
if __name__ == "__main__" :
	notitle = notitle.decode(chardet.detect(notitle).values()[1]).encode(codetype)
	try :
		searchfile(1, startpath)				#递归搜索指定路径下的文件
		'''
		print logo
		print len(logo)
		file_logo = open("G:\\test\\logo.txt", 'w')
		try:
			for i int range( 0, len(logo)):
				file_logo.write(logo[i])
		except IOError:  
			print('IOError') 
		finally:	
			file_logo.colse()
		'''
	except:
		print "execute search file fun error"
	raw_input('Enter to continue...')			#暂停
	