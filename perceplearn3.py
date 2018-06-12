import sys
import json
from collections import defaultdict

if  len(sys.argv) > 0:	
	try:
		bagOfWords = defaultdict(dict)
		weights1 = defaultdict(dict)
		weights2 = defaultdict(dict)
		avgweights1 = defaultdict(dict)
		avgweights2= defaultdict(dict)
		bias1=0
		bias2=0
		beta1=0
		beta2=0
		count=1
		total_frequency=0
		
		with open(sys.argv[1], 'r',encoding='utf8') as file:	
			for line in file:
				if line.strip():
					words = line.split();
					
					for i in range(3,len(words)):
						word = words[i].lower()
						word = ''.join(ch for ch in word if ch.isalpha())
						
						if word=='':
							continue
						
						if word not in bagOfWords:
							bagOfWords[word]=1
							weights1[word]=0
							weights2[word]=0
							avgweights1[word]=0
							avgweights2[word]=0
						else:
							bagOfWords[word]+=1
						
						total_frequency+=1
			
					
			
			for j in range(80):
				file.seek(0)
				for line in file:
					words = line.split()
					y1= 1 if words[1]=="True" else -1
					y2= 1 if words[2]=="Pos" else -1

					x1=defaultdict(dict)
					x2=defaultdict(dict)
					
					for i in range(3,len(words)):
						word = ''.join(ch for ch in words[i] if ch.isalpha())
						word = word.lower()
						
						if word=='':
							continue
							
						if word in x1:
							x1[word]+=1
						else:
							x1[word]=1
							
						if word in x2:
							x2[word]+=1
						else:
							x2[word]=1
						
							
					activation1=0
					activation2=0
					
					for key in x1:
						activation1+=weights1[key] * x1[key]
					activation1+=bias1
					
					if y1 * activation1 <=0:
						for key in x1:
							weights1[key] = weights1[key] + y1 * x1[key]
							avgweights1[key]+=y1*x1[key]*count		
						bias1+=y1
						beta1+=y1*count
					
					for key in x2:
						activation2+=weights2[key] * x2[key]
					activation2+=bias2
					
					if y2 * activation2<=0:
						for key in x2:
							weights2[key] = weights2[key] + y2 * x2[key]
							avgweights2[key]+=y2*x2[key]*count
						bias2+=y2
						beta2+=y2*count
					
					count+=1
					
			for key in weights1:
				avgweights1[key] = weights1[key] - (avgweights1[key]/float(count))
			
			for key in weights2:
				avgweights2[key] = weights2[key] - (avgweights2[key]/float(count))
							
			#calculating stop words
			sortedfrequencies = sorted((value,key) for (key,value) in bagOfWords.items())
			stopwordslen = int(round(0.00113636363*len(bagOfWords)))*-1
			sortedfrequencies = sortedfrequencies[stopwordslen:]
			stopwords=[]
			for item in sortedfrequencies:
				stopwords.append(item[1])
			print(len(bagOfWords))

		#populating json model
		model = defaultdict(dict)
		model ["bagOfWords"] = {}
		model ["bagOfWords"] = bagOfWords
		model["weights1"]={}
		model ["weights1"] = weights1
		model["weights2"]={}
		model ["weights2"] = weights2
		model ["bias1"] = bias1
		model ["bias2"] = bias2
		model["stopwords"]= stopwords
	
		vanillajson = json.dumps(model)
		fileToWrite = open("vanillamodel.txt", "w")
		fileToWrite.write(vanillajson)
		fileToWrite.close()
		
		#populating json model
		avgmodel = defaultdict(dict)
		avgmodel ["bagOfWords"] = {}
		avgmodel ["bagOfWords"] = bagOfWords
		avgmodel["weights1"]={}
		avgmodel ["weights1"] = avgweights1
		avgmodel["weights2"]={}
		avgmodel ["weights2"] = avgweights2
		avgmodel ["bias1"] = (bias1- beta1/float(count))
		avgmodel ["bias2"] = (bias2 - beta2/float(count))
		avgmodel["stopwords"]= stopwords
		
		avgjson = json.dumps(avgmodel)
		fileToWrite = open("averagedmodel.txt", "w")
		fileToWrite.write(avgjson)
		fileToWrite.close()
	except OSError as e:
		print("File not found")
else:
	print("Enter file name and path")
