from TfIdf import getWeight

def generateMatrix():
    fDic=open("Dictionary.txt","r")
    fDoc=open("Document.txt","r")
    docLines=fDoc.readlines()
    dicLines=fDic.readlines()
    NumberOfDoc=len(docLines)/10
    Matrix=[]
    for term in dicLines:
        term=line.rstrip("\n")
        termVector=[term,","]
        for i in range(0, NumberOfDoc):
            Wtd=getWeight(term, i+1)
            termVector.append(str(i+1)+" "+str(Wtd)+",")
            print termVector
        
