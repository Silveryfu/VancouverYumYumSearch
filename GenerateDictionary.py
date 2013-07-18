#I need a dictionary in spelling correction.
#So I generate a dictionary from document stemmed.
import re
dictionary={'a':[],'b':[],'c':[],'d':[],'e':[],'f':[],'g':[],'h':[],'i':[],'j':[],'k':[],'l':[],'m':[],'n':[],'o':[],'p':[],'q':[],'r':[],'s':[],'t':[],'u':[],'v':[],'w':[],'x':[],'y':[],'z':[],'other':[]}
def add(word):
	global dictionary
	if len(word)<2:
		return True
	if not re.match("[\W\d_]",word[0]) is None:
		for item in dictionary['other']:
			if item==word:
				return
		dictionary['other'].append(word)
		return
	for item in dictionary[word[0]]:
		if(item==word):
			return
	dictionary[word[0]].append(word)
def main():
	num="abcdefghijklmnopqrstuvwxyz"
	file=open("Docs/Document.txt","r")
	dic=open("Docs/Dictionary.txt","w")
	lines=file.readlines()
	file.close()
	cnt=len(lines)/10
	for i in range(cnt):
		words=lines[10*i+1].rstrip("\n").split()
		for word in words:
			word=word.strip(" ").lower()
			add(word)
		addresses=lines[10*i+5].rstrip("\n").split()
		for j in range(len(addresses)-1):
			address=addresses[j]
			address=address.lower()
			addre=re.match("[^\d]+",address)
			if addre is None:
				add(address)
			else:
				add(addre.group(0))
		addresses=addresses[len(addresses)-1].split(",")
		for address in addresses:
			address=address.lower()
			add(address)
		descriptions=lines[10*i+6].rstrip("\n").split(", ")
		for description in descriptions:
			description = description.split()
			for descript in description:
				descript=descript.strip()
				descript=descript.lower()
				add(descript)
		types=lines[10*i+7].rstrip("\n").split(", ")
		for type in types:
			type = type.split()
			for ty in type:
				ty=ty.strip().lower()
				add(ty)
		prices=lines[10*i+9].rstrip("\n").split()
		for price in prices:
			price=price.lower()
			add(price)
	for i in range(26):
		for word in dictionary[num[i]]:
			dic.write(word+"\n")
	for word in dictionary["other"]:
		dic.write(word+"\n")
	dic.close()
if __name__ == "__main__":
	main()
