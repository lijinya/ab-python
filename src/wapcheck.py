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
	Ҫע����ǣ�
	1. ���ڵļ�¼��ʽ��׷�ӷ�ʽ�����Ҫ�ø��Ƿ�ʽ����������logo��¼��Ȼ��һ��д�루�ƺ���ֻ��һ�Σ�
	2. ������ҳ�ļ���ָ��·���µĹ�����ע�ͣ�������Ҫ���������޸�
	3. ��д�˵���ҳ��ʽ��'html', 'mht', 'jsp', 'htm', 'php', 'shtml', 'asp'��������Ҫ�����������
	4. http://chardet.feedparser.org/download/ for chardet
	5. ....
'''
import os, sys, re, shutil, binascii, chardet
startpath = "J:\\Python25\\"					#���������ļ���
targetpath = "J:\\test\\"						#�����ļ���Ŀ��·��
logopath = "J:\\test\\logo.txt"					#��ȡtitle������ļ�
notitle = '�ޱ���'
codetype = 'utf8'#GB18030������иĳ�uft8
#gb2312 ˫�ֽڣ���������GB18030�����±�׼�ֱ�gb2312�࣬����gb2312��uft8�ɼ��ݵ�ϵͳ�������ֻ�������
g_wap_pattern = ['html', 'mht', 'jsp', 'htm', 'php', 'shtml', 'asp', 'xhtml', 'aspx']
												#������ҳ��ʽ
g_code_type = ['utf8','utf-8','gb18030', 'gb2312', 'gbk', 'utf-7', 'utf-32','utf-16', 'windows-1250','ISO-8859-2','utf-32BE','IBM037','IBM437','IBM500','ibm737','IBM860','ibm861','ks_c_5601-1987','IBM01140','IBM01141','IBM01146','IBM01147','IBM01148','UnicodeFFFE', 'Johab','x-mac-japanese','x-mac-chinesetrad','x-mac-korean','x-mac-chinesesimp','x-mac-greek','x-mac-ce','x-Chinese-CNS','x-cp20001','x-Chinese-Eten','x-cp20003','x-cp20004','x-IA5-German','EUC-JP','x-cp20936','x-cp20949','x-cp50227','hz-gb-2312']		
												#��һ�����������ǵģ����������޸�
#logo = ["logo:\r\n"]
#����д������ֻ��Ϊ�˱����޸ģ��������Ҫ��Ҳ����д�ɹܵ���ʽ��������ʽ

'''
def ansymhttitle(string):						#���ܵõ��Ǻ��֣�������������
	strinfo = re.compile(r'=..')
	strlist = strinfo.findall(string)
	string = ''
	
	for i in range(0, len(strlist)):
		strlist[i] = hex(int(strlist[i].replace('=', '') , 16)).replace('0x', '') # ���һ��
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
	string = string.replace('=\n', '')			#ȥ��'=\n' Ҳ���Ի���\n
	strinfo = re.compile(r'=\w\w|=\s')#r'=..'	# ƥ����ĸ������
	strlist = strinfo.findall(string)
	#print strlist								#����ʱ��

	for i in range(0, len(strlist)):
		string = string.replace(strlist[i], binascii.a2b_hex(strlist[i].replace('=', '')))
	return string								#�滻Ϊ��Ӧascii��󷵻�
	
def gettitle(url, waptype):
	file_object = open(url)						#�����ļ�

	try:
		content = file_object.read( )			#��ȡ�ļ�����
		#chartypeall = chardet.detect(content).values()[1]
		#print chartypeall
		#chartype = chardet.detect(content).values()[1]
		title = re.findall(r"<title>([\s\S]*?)</title>", content, re.M)
		#��˼��ȡ<title></title>��������������ַ�\s�ǿհ��ַ�\S�Ƿǿհ��ַ�
		#r"<title>\s*(.*?)\s*</title>", ������Ի��н����жϣ����ڵĿ���
		#titlepattern = re.compile(r"<TITLE>[...]</TITLE>")
		#title = titlepattern.search(content);	
		if(title):
			if '' == title[0]:
				title[0] = notitle				#�ҵ�Ϊ��ʱ���ޱ���
		else: 
			title = re.findall(r"<TITLE>([\s\S]*?)</TITLE>", content, re.M)
			if title:							#����Դ�д��<TITLE>��ǩ�����ж�
				if '' == title[0]:
					title[0] = notitle			#�ҵ�Ϊ��ʱ���ޱ���
			else: 
				title.append(notitle)			#δ�ҵ�ʱ���ޱ���
				
		if not cmp(waptype, "mht"):				#�����mht�ļ��������title����
			title[0] = ansymhttitle(title[0])
		
		chartype = chardet.detect(title[0]).values()[1]
		print chartype
		g_code_type[0] = chartype
		title[0] = title[0].replace('\n', '')	#ȥ�����з�����Ҫ���<title>����ģ�
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
												#����ֻ��Ϊ����Ļ����ʾ�Ĳ������룬��������Ч�ʣ�����ɾ��
	finally:
		file_object.close()					#�ر��ļ�
		
	return title[0]
		
def searchfile(n, dirname):  
	 
	for basename in os.listdir(dirname):   
		path = os.path.join(dirname, basename)	#�õ�·�������е��ļ�������·��

		if os.path.isdir(path):  	
			searchfile(n + 1, path) 			#�ݹ������ļ�
		else:
			#pattern = re.compile(r'(.*?).html') #r'(.*?).txt'
			#if pattern.match(basenames):
				#print basenames
			if not os.path.getsize(path):		#�ж��ļ��Ĵ�С�����Ϊ����ִ������Ĵ���
				continue
				
			for i in range(0, len(g_wap_pattern)):
				if path.lower().endswith(g_wap_pattern[i]):
					print '�ļ�·����' + path	#������ҳ�ļ���׺ʱ��ӡ·��
					#�����ļ���Ŀ���
					title = gettitle(path, g_wap_pattern[i])	#�õ�����ҳ��title
					#logo.append("http://" + lastpath[n] + "/" + "\t" + title + "\n")
					folder = dirname.split("\\")[-1]
					logostr = dirname.replace(startpath, 'http://').replace('\\', '/') + "/" + "\t" + title + "\n"
					makefolder(targetpath,  folder)
					shutil.copyfile(path, targetpath +  folder + '\\' + basename)
					file_logo = file(logopath, 'a')				#��׷�ӷ�ʽ��
					try:
						file_logo.write(logostr)				#д����Ϣ
					except IOError:  
						print('IOError')
					#finally:
					#file_logo.colse()
					break
				
if __name__ == "__main__" :
	notitle = notitle.decode(chardet.detect(notitle).values()[1]).encode(codetype)
	try :
		searchfile(1, startpath)				#�ݹ�����ָ��·���µ��ļ�
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
	raw_input('Enter to continue...')			#��ͣ
	