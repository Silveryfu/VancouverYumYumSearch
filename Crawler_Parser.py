import urllib2
import re
from HTMLParser import HTMLParser
class MyHTMLParser(HTMLParser):#inherit from HTMLParser
    def __init__(self):#Construction Function
        HTMLParser.__init__(self)
        self.dataset=[]#Initial the public variable
    def handle_data(self, data):#override the method of handling data
        data=data.strip(" \t\n.!?,")#ignore the character: ' ','\n','\t',etc
        if(data!=""):#if still remains some character, store them to the dataset
            self.dataset.append(data)
def crawler(url):
    response = urllib2.urlopen(url)
    html = response.read()
    html=html.strip(" \n\t")
    return html
def parser(url):
    html=crawler(url)
    parse = MyHTMLParser()
    parse.feed(html)
    result=parse.dataset
    parse.close()
    return result
def main():
    print parser("http://python.org")
if __name__=="__main__":
    main()
