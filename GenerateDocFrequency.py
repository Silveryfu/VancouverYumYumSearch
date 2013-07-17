import os

def generateDocFrequency():
    result=[]
    fileNameList=os.listdir("C:/Users/admin/Desktop/stemmed")
    fterm=open("Dictionary.txt","r")
    TermLines=fterm.readlines()
    for term in TermLines:
        term=term.rstrip("\n")
        counter=0
        for i in range(0,len(fileNameList)):
            f=open("C:/Users/admin/Desktop/stemmed/"+fileNameList[i],"r")
            lines=f.readlines()
            flag=1
            for line in lines:
                if flag==0:
                    break
                line=line.rstrip("\n")  
                words=line.split()
                for word in words:
                    if cmp(term,word)==0:
                        counter=counter+1
                        flag=0   #mark the term has been found, and stop searching this file
                        break
        result.append([term,counter])
        print [term,counter]
    fileResult=open("C:/Users/admin/SilveryGit/SearchEngine/documentFrequency.txt","w")
    for row in result:
        fileResult.write(str(row[0])+" "+str(row[1])+"\n")
    print "Process completed."
def main():
	generateDocFrequency()
	
if __name__ == "__main__":
	main()
