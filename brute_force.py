#!usr/bin/env python
'''tryin gto implement algorithms from second year CS classes
@geoffjuma 2/04/2017'''

import time
import numpy as np
import random

data = [0,3,2,4,5,6,3,4,2,8,6,7,9,4,6,7,5]

def dataGenerator():
    data = np.random.randint(0,1000,100)
    return data;
    

def printData(data):
    for i in range(0,len(data)):
        print data[i]
    
def findPeak(data):
    startTime = time.time();
    for i in range(0,len(data)):
        if data[i]>= data[i+1] and data[i]>=data[i-1]:
            peak = data[i]
            break;
        else:
            print 'we are still looking for it';
    endTime = time.time();
    duration = endTime-startTime;
    print 'you have taken %d to execute',duration
    return peak;

def findMax(data):
    max = data[0];
    startTime = time.time();
    for i in range(0,len(data)):
        if data[i]>max:
            max = data[i]
        else:
            pass
    endTime = time.time();
    duration = endTime-startTime;
    print 'you have taken %d to execute',duration
    return max;

def swap(a,b):
    temp = b;
    b = a;
    a = temp
    

def linearSort(data):
    startTime = time.time()
    for j in range(len(data)-1,0,-1):
        for i in range(j):
            if data[i]>data[i+1]:
                swap(data[i],data[i+1]);           
    endTime = time.time();
    duration = endTime-startTime;
    print 'you have taken %d to execute',duration
    
                
if __name__ == "__main__":
    
    #data = dataGenerator()
    #peak = findPeak(data)
    #print 'your peak is ', peak;
    #max = findMax(data)
    #print 'the maximum value is ', max
    linearSort(data)
    print data
