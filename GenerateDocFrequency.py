import os

def generateDocFrequency():
    result=[]
    fDoc=open("Document.txt","r")
    fTerm=open("Dictionary.txt","r")
    docLines=fDoc.readlines()
    termLines=fTerm.readlines()
    docTotalLength=len(docLines)
    for term in termLines:
        term=term.rstrip("\n")
        counter=0
        docNum=0              
        for docNum in range(0,docTotalLength/10):
            flag=1
            for i in range(0,10):
                if flag==0:
                    break
                else:
                    line=docLines[docNum*10+i].rstrip("\n")
                    if i==1:
                        words=line.split()
                        for word in words:
                            word = word.lower()
                            if word==term:
                                counter=counter+1
                                flag=0
                                break
                    elif i==5:
                        words=line.split()
                        for j in range(len(words)-1):
                            word=words[j].lower()
                            if word==term:
                                counter=counter+1
                                flag=0
                                break
                        if flag==0:
                            break
                        words=words[len(words)-1].split(",")
                        for word in words:
                            word=word.lower()
                            if word==term:
                                counter=counter+1
                                flag=0
                                break
                    elif i==6:
                        words=line.split(", ")
                        for word in words:
                            word=word.split()
                            for subword in word:
                                subword=subword.lower()
                                if subword==term:
                                    counter=counter+1
                                    flag=0
                                    break
                    elif i==7:
                        words=line.split(", ")
                        for word in words:
                            word=word.split()
                            for subword in word:
                                subword=subword.lower()
                                if subword==term:
                                    counter=counter+1
                                    flag=0
                                    break
                    elif i==9:
                        words=line.split()
                        for word in words:
                            if word==term:
                                counter=counter+1
                                flag=0
                                break
                    else:
                        continue
                        
        result.append([term, counter])
        print [term,counter]

    fileResult=open("documentFrequency.txt","a+")
    for row in result:
        fileResult.write(str(row[0])+" "+str(row[1])+"\n")
        
    print "Process completed."
def main():
	generateDocFrequency()
	
if __name__ == "__main__":
	main()
