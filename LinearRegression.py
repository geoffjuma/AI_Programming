#! /usr/bin/env python

import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from statistics import mean
import quandl

style.use('ggplot')

def readData():
    dataset = quandl.get("WIKI/AAP")
    return dataset

def features(dataset):
    X = np.array(dataset['Open'])
    Y = np.array(dataset['Volume'])
    return X,Y

#X = np.array([1,2,3,4,5,6,7,8,9,10])
#Y = np.array([3,6,7,9,10,12,13,20,16,22])

def linearRegression(X,Y):
    m = ((mean(X)*mean(Y))-mean(X*Y))/((mean(X)**2)- (mean(X**2)))
    b = mean(Y)-(m*mean(X))
    return m,b


def ErrorSquared(Y,new_y):
    return sum(new_y - Y)**2

if __name__ =='__main__':

    dataset = readData()
    X,Y = features(dataset)

    m,b = linearRegression(X,Y)
    new_y = [(m*x)+b for x in X]
    
    plt.title('Linear Regression')
    plt.scatter(X,Y, color ='b')
    plt.plot(X,new_y, color = 'r')
    plt.legend(loc='upper right')
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.show()
