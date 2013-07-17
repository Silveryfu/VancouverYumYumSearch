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
    
    for i in range(stair, len(lines)):
        words=lines[i].split()
        if words[0]==term:
            dFt=int(words[1])
            break
    if(tFtd==0):
        Wtd=0;
    else:
        Wtd=round((1+math.log10(tFtd))*math.log10(NumberOfDoc/dFt),2)  
    return Wtd
    
def main():
    print getWeight('street/west', 1)

if __name__=="__main__":
    main()
