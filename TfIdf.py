import math

#Wtd=(1+logtFtd)log(N/dFt)

def getWeight(term, docNum):
    
    #calculate the frequency of term in a document 
    tFtd=0;
    term=term.lower()
    file=open("Document.txt","r")
    lines=file.readlines()
    NumberOfDoc=len(lines)/10
    sublines=[]
    for i in range((docNum-1)*10,(docNum-1)*10+10):
        sublines.append(lines[i])
    for i in range(0,10):
        line=sublines[i].rstrip("\n")
        if i==1:
            words=line.split()
            for word in words:
                word=word.lower()
                if term==word:
                    tFtd=tFtd+1
        elif i==5:
            words=line.split()
            for j in range(len(words)-1):
                word=words[j].lower()
                if word==term:
                    tFtd=tFtd+1
            words=words[len(words)-1].split(",")
            for word in words:
                word=word.lower()
                if word==term:
                    tFtd=tFtd+1
        elif i==6:
            words=line.split(", ")
            for word in words:
                word=word.split()
                for subword in word:
                    subword=subword.lower()
                    if subword==term:
                        tFtd=tFtd+1
        elif i==7:
            words=line.split(", ")
            for word in words:
                word=word.split()
                for subword in word:
                    subword=subword.lower()
                    if subword==term:
                        tFtd=tFtd+1
        elif i==9:
            words=line.split()
            for word in words:
                word=word.lower()
                if word==term:
                    tFtd=tFtd+1
      
    #calculate the number of documents of term
    dFt=0
    file=open("documentFrequency.txt","r")
    lines=file.readlines()
    for line in lines:
        words=line.split()
        if cmp(words[0],term)==0:
            dFt=int(words[1])
    if(tFtd==0):
        Wtd=0;
    else:
        Wtd=round((1+math.log10(tFtd))*math.log10(NumberOfDoc/dFt),2)  
    return Wtd
    
def main():
    print getWeight('robson', 1)

if __name__=="__main__":
    main()
