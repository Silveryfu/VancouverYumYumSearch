import threading
MATRIX=[]


def distance(word1,word2):
  #Calculate the Distance of Two Words
  global MATRIX
  len1=len(word1)
  len2=len(word2)
  if len1<len2:  #can improve the performance
    len1, len2 = len2, len1
    word1, word2 = word2, word1
    
  for i in range(len2+1):
    MATRIX.append([])
  for i in range(len1+1):
    MATRIX[0].append(i)
  for i in range(1,len2+1):
    MATRIX[i].append(i)

  for i in range(1,len2+1):
    for j in range(1,len1+1):
      if(word2[i-1]==word1[j-1]):
        r=min(MATRIX[i-1][j]+1,MATRIX[i][j-1]+1,MATRIX[i-1][j-1])
      else:
        r=min(MATRIX[i-1][j]+1,MATRIX[i][j-1]+1,MATRIX[i-1][j-1]+1)
      MATRIX[i].append(r)
      
  return MATRIX[len2][len1]

def main():
    from timeit import Timer
    t1=Timer("distance('batsssssss','catss')","from __main__ import distance")
    print t1.timeit(10000)

if __name__=="__main__":
  main()
