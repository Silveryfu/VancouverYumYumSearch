import urllib2
import re
from HTMLParser import HTMLParser
def crawler(url):
    response = urllib2.urlopen(url)
    html = response.read()
    html=html.lstrip()
    html=html.rstrip()
    return html
def getAllLink(express,html):
    group=re.findall(express,html)
    return group
def parser(url):
    html=crawler(url)
    #link=getAllLink('http://(?:\w*\.)*python.org/[\w./]*|href=/"/[\w/]*\"',html)
    fil=open("./Origin.txt","w")
    fil.write(html)
    fil.close()
    fil=open("./Modified.txt","w")
    html.strip()
    html.strip("\n")
    result=[]
    parse = HTMLParser()
    parse.handle_data = result.append
    parse.feed(html)
    parse.close()
    fil.writelines(result)
    fil.close()
def main():
    parser("http://python.org")
if __name__=="__main__":
    main()
