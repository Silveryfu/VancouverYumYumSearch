from TfIdf import getWeight

def generateMatrix():
    fDic=open("Dictionary.txt","r")
    fDoc=open("Document.txt","r")
    docLines=fDoc.readlines()
    dicLines=fDic.readlines()
    dicLength=len(dicLines)
    NumberOfDoc=len(docLines)/10
    Matrix=[]
    fMatrix=open("FinalMatrix.txt","a+")
    for j in range(118,dicLength): #torres change 118 
        term=dicLines[j].rstrip("\n")
        fMatrix.write(term+",")
        for i in range(0, NumberOfDoc):
            Wtd=getWeight(term, i+1)
            if Wtd==0:
                continue
            else:
                fMatrix.write(str(i+1)+" "+str(Wtd)+",")
        fMatrix.write("\n")
        print "Proceed."

def main():
    generateMatrix()

if __name__=="__main__":
    main()
