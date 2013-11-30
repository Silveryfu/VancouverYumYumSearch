result=[]
def isExist(word):
	global result
	for i in range(len(result)):
		if word==result[i][0]:
			return i
	return -1
f=open('Dictionary.txt','r')
lines=f.readlines()
f.close()
for i in range(len(lines)):
	length=len(lines[i].strip('\n'))
	if length>=2:
		for j in range(length-1):
			row=isExist(lines[i][j:j+2])
			if row==-1:
				result.append([lines[i][j:j+2],i])
			else:
				result[row].append(i)
for i in range(len(result)):
	for j in range(len(result[i])):
		print result[i][j],
	print ""
