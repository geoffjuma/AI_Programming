#!/usr/bin/en python
from numpy import *
from matplotlib import pyplot as plt 
import operator

def createDataset():
	group = array([[3,104],[2,100],[1,81],[101,10],[99,5],[98,2]])
	labels = ['Romance','Romance','Romance','Action','Action,Action']
	return group,labels

def classify(intX, dataset,labels,k):
	datasetsize = dataset.shape[0]
	diffMat = tile(intX,(datasetsize,1)) - dataset
	sqDiffMat = diffMat**2
	sqDistances = sqDiffMat.sum(axis=1)
	distances = sqDistances**0.5
	sortedDistIndices = distances.argsort()
	classCount = {}
	for i in range(k):
		voteLabel = labels[sortedDistIndices[i]]
		classCount[voteLabel] = classCount.get(voteLabel,0)+1
	sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse = True)
	return sortedClassCount[0][0]

def thePlotter():
	group,labels = createDataset()
	x = group[:,0]
	y = group[:,1]
	plt.scatter (x,y)
	plt.title("K nearest neighbour")
	plt.xlabel("number of kicks")
	plt.ylabel("number of kisses")
	plt.show()

if __name__ == '__main__':
	group, labels = createDataset()
	print classify([18,90],group,labels,3)
	thePlotter()
