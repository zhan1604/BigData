import csv 
import os
import math

def main():
	sportTrainingSet={}
	businessTrainingSet={}
	sportTestSet={}
	businessTestSet={} 
	sportTestSetCount=int(0)
	businessTestSetUnique=int(0)
	probabilitySport=int(0)
	probabilityBusiness=int(0)
	sportTrainingSetCount=int(0)
	businessTrainingSetCount=int(0)

	
	file=""
	sportdir= 'for sport training'
	for file in os.listdir(sportdir):
		if file.endswith(".txt"):
			file="for files" + file
			with open(file, 'r') as txtfile:
				lines=csv.reader(txtfile, delimiter=" ")
				dataset=list(lines)
				dataset=dataset.pop()
				del dataset[-1]
				print(dataset)
				for i in range(len(dataset)):

					sportTrainingSetCount+=1
					if dataset[i] in sportTrainingSet:
						sportTrainingSet[dataset[i]]+=1
					else:
						sportTrainingSet[dataset[i]]=1
	print(":",sportrainingSetCount)
	

	businessdir= 'dir for business'
	for file in os.listdir(businessdir):
		if file.endswith(".txt"):
			file="for files" + file
			with open(file, 'r') as txtfile:
				lines=csv.reader(txtfile, delimiter=" ")
				dataset=list(lines)
				dataset=dataset.pop()
				del dataset[-1]
				print(dataset)
				for i in range(len(dataset)):
					businessTrainingSetCount+=1
					if dataset[i] in businessTrainingSet:
						businessTrainingSet[dataset[i]]+=1
					else:
						businessTrainingSet[dataset[i]]=1
	print("",businessTrainingSetCount)

	for file in os.listdir('link to test data'):
		if file.endswith(".txt"):
			file=" to business test"+file
			with open(file, 'r') as csvfile:
				lines=csv.reader(csvfile, delimiter=' ')
				dataset=list(lines)
				dataset=dataset.pop()
				del dataset[-1]
				for i in range(len(dataset)):
					if dataset[i] in sportTestSet:
						sportTestSet[dataset[i]]+=1
					else:
						sportTestSetUnique+=1
						sportTestSet[dataset[i]]=1
	print(sportTestSet)
	
	for key in sportTrainingSet.keys():
		sportTrainingSet[key]=(sportTrainingSet[key]+1)/(sportTrainingSetCount+sportTestSetUnique)

	for key in businessTrainingSet.keys():
		businessTrainingSet[key]=(businessTrainingSet[key]+1)/(businessTrainingSetCount+businessTestSetUnique)

	probabilitySport=math.log(0.5)
	probabilityBusiness=math.log(0.5)

	for key in sportTestSet.keys():
		#print(key)
		if key in BusinessTrainingSet.keys():

			probabilityBusiness+=sportTestSet[key]*math.log(BusinessTrainingSet[key])
		elif key not in businessTrainingSet.keys():
			probabilityBusiness+=math.log(1/(BusinessTrainingSetCount+sportTestSetUnique))

		if key in sportTrainingSet.keys():

			probabilityBusiness+=sportTestSet[key]*math.log(sportTrainingSet[key])
		elif key not in sportTrainingSet.keys():
			probabilitySport+=math.log(1/(sportTrainingSetCount+sportTestSetUnique))

	print("",probabilitySport)
	print("",probabilityBusiness)

	if probabilityBusiness>probabilitySport:
		print("Business")
	else:
		print("Sport")

main()


