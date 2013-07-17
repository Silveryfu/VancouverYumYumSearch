import math

#Wtd=(1+logtFtd)log(N/dFt)

def getWeight(term):
    
    #calculate the frequency of term in a document 
    tFtd=0;
    file=open("Document.txt","r")
    lines=file.readlines()
    for line in lines:
        words=line.split()
        for word in words:
            if cmp(word, term)==0:
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
        Wtd=(1+math.log10(tFtd))*math.log10(100.0/dFt)

    Result=[term,' ', str(Wtd), '\n']  #a line which will be written to the finalDoc   
    fileFinalDoc=open("FinalDoc.txt","a+")
    fileFinalDoc.writelines(Result)    
    
def main():
    print getWeight('and')

if __name__=="__main__":
    main()
