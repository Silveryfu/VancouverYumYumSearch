import threading
MATRIX=[]
WORD1=''
WORD2=''
LEN1=0
LEN2=0
LAYER=0

class RowCalculator(threading.Thread):
  def run(self):
    global WORD1
    global WORD2
    global LEN1
    global LEN2
    global MATRIX
    global LAYER
    for i in range(LAYER+1, LEN1+1):
      if(WORD1[i-1]==WORD2[LAYER-1]):
        MATRIX[LAYER].append(min(MATRIX[LAYER-1][i]+1,MATRIX[LAYER][i-1]+1,MATRIX[LAYER-1][i-1]))
      else:
        MATRIX[LAYER].append(min(MATRIX[LAYER-1][i]+1,MATRIX[LAYER][i-1]+1,MATRIX[LAYER-1][i-1]+1))
        
class ColumnCalculator(threading.Thread):
  def run(self):
    global WORD1
    global WORD2
    global LEN1
    global LEN2
    global MATRIX
    global LAYER
    for i in range(LAYER+1, LEN2+1):
      if(WORD2[i-1]==WORD1[LAYER-1]):
        MATRIX[i].append(min(MATRIX[i][LAYER-1]+1,MATRIX[i-1][LAYER]+1,MATRIX[i-1][LAYER-1]))
      else:
        MATRIX[i].append(min(MATRIX[i][LAYER-1]+1,MATRIX[i-1][LAYER]+1,MATRIX[i-1][LAYER-1]+1))



def distance(word1,word2):
  #Calculate the Distance of Two Words
  global MATRIX
  global WORD1
  global WORD2
  global LEN1
  global LEN2
  global LAYER
  len1=len(word1)
  len2=len(word2)
  if len1>len2:
    len1, len2 = len2, len1
    word1, word2 = word2, word1
  WORD1=word1
  WORD2=word2
  LEN1=len1
  LEN2=len2
  
  for i in range(len2+1):
    MATRIX.append([])
  for i in range(len1+1):
    MATRIX[0].append(i)
  for i in range(1,len2+1):
    MATRIX[i].append(i)
  #parallel processing starts here
    
  for k in range(1,len1+1):
    LAYER=k
    if(word1[k-1]==word2[k-1]):
      MATRIX[k].append(min(MATRIX[k-1][k]+1,MATRIX[k][k-1]+1,MATRIX[k-1][k-1]))
    else:
      MATRIX[k].append(min(MATRIX[k-1][k]+1,MATRIX[k][k-1]+1,MATRIX[k-1][k-1]+1))
    cc=ColumnCalculator()
    cc.start()
    rc=RowCalculator()
    rc.start()
    cc.join()   #wait till the two child-threads finish
    rc.join()
    
  return MATRIX[len2][len1]

def main():
  print distance('bats','cats')

if __name__=="__main__":
  main()
