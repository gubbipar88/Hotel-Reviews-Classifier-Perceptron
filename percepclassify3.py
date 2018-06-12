import sys
import json
import math
from collections import defaultdict
from collections import OrderedDict

args = []
for arg in sys.argv:
	args.append(arg)
	
#load model features
with open(sys.argv[1],'r',encoding='utf8') as file:
	data = json.loads(file.read())
	bagOfWords = data["bagOfWords"]
	stopwords = data["stopwords"]
	weights1 = data ["weights1"]
	weights2 = data ["weights2"]
	bias1 = data["bias1"]
	bias2 = data["bias2"]

	
with open(sys.argv[2],'r',encoding='utf8') as file:
	
	fileToWrite = open("percepoutput.txt", "w",encoding='utf-8')
	
	for line in file:
		words = line.split()
		x1=defaultdict(dict)
		x2=defaultdict(dict)
		class1=""
		class2=""
		
		for i in range(1,len(words)):
			word = ''.join(ch for ch in words[i] if ch.isalpha())
			word = word.lower()
			
			if word=='':
				continue
					
			if word in bagOfWords and word not in stopwords:
				if word in x1:
					x1[word]+=1
				else:
					x1[word]=1
					
				if word in x2:
					x2[word]+=1
				else:
					x2[word]=1
						
		activation1=0
		for key in x1:
			activation1+=weights1[key] * x1[key]
		activation1+=bias1
		
		activation2=0
		for key in x2:
			activation2+=weights2[key] * x2[key]
		activation2+=bias2
		
			
		if activation1>0:
			class1="True"
		else:
			class1="Fake"
			
		if activation2>0:
			class2="Pos"
		else:
			class2="Neg"
		
		fileToWrite.write(words[0]+" "+class1+" "+class2+"\n")
			
	
	fileToWrite.close()
