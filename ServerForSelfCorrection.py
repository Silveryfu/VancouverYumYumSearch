import BaseHTTPServer
from LavenDistanceNoParallel import distance
import re
HOST_NAME = 'localhost' # !!!REMEMBER TO CHANGE THIS!!!
PORT_NUMBER = 8888 # Maybe set this to 9000.
index=[]
words=[]
def isExist(word):
	global index
	for i in range(len(index)):
		if(index[i][0]==word):
			return i
	return -1
def distance(word1,word2):
	#Calculate the Distance of Two Words
	result=[]
	len1=len(word1)
	len2=len(word2)
	for i in range(len2+1):
		result.append([])
	for i in range(len1+1):
		result[0].append(i)
	for i in range(1,len2+1):
		result[i].append(i)
	for i in range(1,len1+1):
		for j in range(1,len2+1):
			if(word1[(i-1):i]==word2[(j-1):j]):
				r=min(result[j-1][i]+1,result[j][i-1]+1,result[j-1][i-1])
			else:
				r=min(result[j-1][i]+1,result[j][i-1]+1,result[j-1][i-1]+1)
			result[j].append(r)
	return result[len2][len1]
def corre(arg):
	global words
	global index
	for i in range(len(words)):
		if cmp(words[i][0],arg)==0:
			return ""
		words[i][1]=0
	length=len(arg)
	if length>1:
		for i in range(length-1):
			row=isExist(arg[i:(i+2)])
			if(row!=-1):
				for j in index[row][1:]:
					words[int(j)][1]=words[int(j)][1]+1
	else:
		return ""
	correct=[]
	for i in range(len(words)):
		if(words[i][1]>(length-1)/2):
			correct.append([i])
	if len(correct)>0:
		for i in range(len(correct)):
			correct[i].append(distance(arg,words[correct[i][0]][0]))
		inde=0
		for i in range(1,len(correct)):
			if(correct[inde][1]>correct[i][1]):
				inde=i
		return words[correct[inde][0]][0]
	else:
		return ""
class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	def do_HEAD(s):
		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()
	def do_GET(s):
		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()
		arg=s.path.lower().lstrip("/")
		args=arg.split("+")
		ar=[]
		flag=True
		for arg in args:
			word=corre(arg)
			if(word!=""):
				ar.append(word)
				flag=False
			else:
				ar.append(arg)
		if(flag==False):
			s.wfile.write(" ".join(ar))
		else:
			s.wfile.write("")
def InitDic():
	global index
	global words
	file=open("SelfCorrection.txt","r")
	index=[]
	for line in file:
		index.append(line.split())
	file.close()
	file=open("Dictionary.txt","r")
	words=[]
	for line in file:
		line=line.rstrip("\n")
		words.append([line,0])
	file.close()
def main():
	server_class = BaseHTTPServer.HTTPServer
	httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
	InitDic()
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	httpd.server_close()
if __name__ == '__main__':
	main()
