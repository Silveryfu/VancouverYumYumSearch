#coding: UTF-8
import urllib2
import re
from bs4 import BeautifulSoup
#from HTMLParser import HTMLParser
#class MyHTMLParser(HTMLParser):#inherit from HTMLParser
#        HTMLParser.__init__(self)
#		self.dataset=[]#Initial the public variable
#    def handle_data(self, data):#override the method of handling data
#        data=data.strip(" \t\n.!?,")#ignore the character: ' ','\n','\t',etc
#        if(data!=""):#if still remains some character, store them to the dataset
#            self.dataset.append(data)
#	此版本能搜索所有与饭店有关的内容，包括Name,Type,Description,ImageUrl,Url,Address,Score,Price,Tel
#	此版本会将搜索到的结果一行一个属性的保存在Result.txt
#	并在下次运行时打开Result.txt看看哪些restaurant已经被搜索过,不再重新搜索
#	防止想扩大饭店搜索数量或者运行到一半crash后又要从头开始搜索的情况
#	怎么样,很科学吧 ^_^
MAX = 4000
result = []
file = open("./Result.txt","a+")
lines = file.readlines()
cnt=len(lines)/10
for i in range(cnt):
	result.append(lines[10*i+2].rstrip("\n"))
flag=False;
def exist(item,list):#可以用B-Tree来实现，会快很多
	for l in list:
		if l==item:
			return True
	return False
def crawler(url):
    response = urllib2.urlopen(url)
    html = response.read()
    html=html.strip(" \n\t")
    return html
def getAllLink(url,expression):
	html = crawler(url)
	areas = re.findall(expression,html)
	for i in range(len(areas)):
		area=areas[i]
		area=area.lstrip("href=\"")
		area=area.rstrip("\"")
		areas[i]="http://66.135.44.85"+area
	areas={}.fromkeys(areas).keys()
	return areas
#def parser(url):
#    html=crawler(url)
#    parse = MyHTMLParser()
#    parse.feed(html)
#    result=parse.dataset
#    parse.close()
#    return result
def writeToFile(restaurantUrl):
	global cnt
	global result
	global flag
	global file
	#    Result Name Url Tel Score Address Description Type ImageUrl Price
	#	 0
	#	 1
	#	 2
	#	 ...
	if cnt > MAX:
		flag = True
		return
	links = getAllLink(restaurantUrl,"href=\"/\w+?/\d+?/\d+?/restaurant/[\w-]+?/[\w-]+?\"")
	if exist(restaurantUrl,result)==False:
		print cnt
		print restaurantUrl
		result.append(restaurantUrl)
		html = crawler(restaurantUrl)
		soup = BeautifulSoup(html)
		#Telephone
		#<h3 class="phone tel">(778) 706-0694</h3>
		tel = soup.find("h3", class_="phone tel")
		if not tel is None:
			tel = tel.get_text().encode("ascii",'ignore').strip(" \n\t")
		else:
			tel = ""
		#Restaurant Name
		#<h1 class="page_title" itemprop="name">Nero Belgian Waffle Bar</h1>
		title = soup.find("h1", class_="page_title").get_text().encode('ascii','ignore').strip(" \n\t")
		#Score
		#<div class="number"><div class="average digits percent-text rating">92<div class="percent">%</div></div></div>
		score = soup.find("div", class_="average")
		if score is None:
			score=""
		else:
			score=score.get_text().encode('ascii','ignore').strip("\n \t").split("\n")
			score = "".join(score)
		#Address
		#<div class="neighborhood">
		#<a href="http://66.135.44.85/n/14/1319/Vancouver/Robson-Street-West-End-restaurants" 	class="ga_event" data-ga_action="explore-resto-neighborhood" data-ga_catg="Explore" data-ga_label="test=gsl-v2-a,page=restaurants-show,link-neighborhood-name">Robson Street/West End</a>
		#</div>
		#<span class="street-address">
		#1703 Robson St
		#</span>
		#<br><span class="locality">Vancouver</span>,
		#<span class="region">BC</span>
		#<a href="http://66.135.44.85/zip/14/V6G1C8/Vancouver-restaurants.html">V6G1C8</a>
		#</div>
		address = soup.find("div", class_="address").get_text().encode('ascii','ignore').strip(" \n\t").split("\n")
		address = "".join(address)
		#Price:$ means cheap eats, $$ means moderately priced, $$$ means Higher priced, $$$$ means Fine dining
		#imageUrl
		imageUrl = soup.find("div", class_="resto_photos").find("ul")
		if not imageUrl is None:
			imageUrl = "http://66.135.44.85"+imageUrl.find("li").find("a")["href"].encode("ascii",'ignore')
		else:
			imageUrl = ""
		#Type example: Pub Food, Burgers, Diner        a string not a list
		type = []
		types = soup.find("div", class_="resto_details").find_all("a")
		for item in types:
			item = item.get_text().encode("ascii",'ignore').strip("\n\t ")
			if item[0]!="$":
				type.append(item)
			else:
				break
		type = ", ".join(type)
		#description   description[0] is the description of price
		description = soup.find("div", class_="tags").find_all("a")
		for i in range(len(description)):
			description[i] = description[i].get_text().encode("ascii",'ignore').strip("\n\t ")
		if len(description)>0:
			price = description[0]
			del description[0]
			description=", ".join(description)
		else:
			description=""
			price = ""
		cnt = cnt + 1
		file.write(str(cnt)+"\n"+title+"\n"+restaurantUrl+"\n"+tel+"\n"+score+"\n"+address+"\n"+description+"\n"+type+"\n"+imageUrl+"\n"+price+"\n")
		if links != []:
			for link in links:
				writeToFile(link)
	else:
		print "Ops"
def main():
	areas = getAllLink("http://66.135.44.85/c/14/Vancouver-restaurants.html","href=\"/\w+?/\d+?/\d+?/Vancouver/[\w-]+?\"")
	for area in areas:
		if(flag):
			break
		restaurants = getAllLink(area,"href=\"/\w+?/\d+?/\d+?/restaurant/[\w-]+?/[\w-]+?\"")
		for restaurant in restaurants:
			if(flag):
				break
			writeToFile(restaurant)				
	file.close()
if __name__=="__main__":
    main()
