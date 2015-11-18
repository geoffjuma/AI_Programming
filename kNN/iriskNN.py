#!/usr/bin/en python
import csv
import pandas as pd 
from numpy import *
import numpy as np 
from matplotlib import pyplot as plt 
from pylab import *
import operator


# Read the data from the file

def generateDatasetUsingPandas():
	data = pd.read_csv('irisdata.csv',sep = ',',header = None)
	features = data.values[0:,[0,1,2,3]]
	labels = data.values[:,4]
	return features,labels

def createDataset():
	data = np.genfromtxt("irisdata.csv", delimiter =',')
	features = data[0:,[0,1,2,3]]
	labels = data[:,4];
	return data

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

def thePlotter(data):
	sepal_length = data[:,0];
	sepal_width = data[:,1];
	petal_length = data[:,2];
	petal_width = data[:,3];
	plt.scatter (sepal_length,sepal_width,petal_length,petal_width)
	plt.title("Iris Dataset Using K-NN")
	plt.xlabel("length of leaves")
	plt.ylabel("width of leaves")
	legend()
	plt.show()

if __name__ == '__main__':
	features, labels = generateDatasetUsingPandas()
	data= createDataset()
	print classify([3.4,2.2,3.4,4.5],features,labels,3)
	thePlotter(data)
