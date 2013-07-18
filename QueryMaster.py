import math
import sys
def argsort(seq):
    return sorted(range(len(seq)), key = seq.__getitem__, reverse=True)

def returnResult(query):
    query=query.split()
    docNum=1604
    scores=[]
    for i in range(0, docNum):
        scores.append(0.0)
    fIdf=open("Docs/documentFrequency.txt","r")
    idfs=fIdf.readlines()
    fPostings=open("Docs/FinalMatrix.txt","r")
    postings=fPostings.readlines()
    for term in query:
        tFtd=0
        for word in query:
            if word==term:
                tFtd=tFtd+1
        stair=0 #the start entry/line
        if(term[0]=='a'):
            stair=0
        elif(term[0]=='b'):
            stair=101
        elif(term[0]=='c'):
            stair=889
        elif(term[0]=='d'):
            stair=1100
        elif(term[0]=='e'):
            stair=1225
        elif(term[0]=='f'):
            stair=1281
        elif(term[0]=='g'):
            stair=1379
        elif(term[0]=='h'):
            stair=1475
        elif(term[0]=='i'):
            stair=1573
        elif(term[0]=='j'):
            stair=1609
        elif(term[0]=='k'):
            stair=1657
        elif(term[0]=='l'):
            stair=1736
        elif(term[0]=='m'):
            stair=1824
        elif(term[0]=='n'):
            stair=1961
        elif(term[0]=='o'):
            stair=2020
        elif(term[0]=='p'):
            stair=2060
        elif(term[0]=='q'):
            stair=2199
        elif(term[0]=='r'):
            stair=2211
        elif(term[0]=='s'):
            stair=2307
        elif(term[0]=='t'):
            stair=2528
        elif(term[0]=='u'):
            stair=2645
        elif(term[0]=='v'):
            stair=2660
        elif(term[0]=='w'):
            stair=2702
        elif(term[0]=='x'):
            stair=2769
        elif(term[0]=='y'):
            stair=2774
        elif(term[0]=='z'):
            stair=2803
        else:
            stair=2819
        dFt=0
        for i in range(stair, len(idfs)):
            words=idfs[i].split()
            if words[0]==term:
                dFt=int(words[1])
                break
        if(tFtd==0 or dFt==0):
            Wtq=0;
        else:
            Wtq=round((1+math.log10(tFtd))*math.log10(docNum/dFt),2)

        for i in range(stair, len(postings)):  #the docfrequency has a different order with dic, so cannot use the obtained position directly
            words=postings[i].split(",")
            if words[0]==term:
                postingArray=words
                
        for i in range(1,len(postingArray)-1):
            posting=postingArray[i].split()
            docId=posting[0]
            Wtd=float(posting[1])
            scores[int(docId)-1]=scores[int(docId)-1]+Wtd*Wtq
            
    result=argsort(scores)   #remember to plus one to obtain the right doc id
    for i in range(100):
        result[i]=str(result[i])
    result=" ".join(result[0:100])
    return result
def main(arg):
    print returnResult(arg)
if __name__=="__main__":
    main(sys.argv[1])
