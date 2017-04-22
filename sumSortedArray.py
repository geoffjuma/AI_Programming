#!/usr/bin/env python

def sortData(data):
    for i in range(len(data)-1):
        for j in range(i):
            if data[i]>data[i+1]:
                temp = data[i]
                data[i]=data[i+1]
                data[i+1]=temp
    #print data[len(data)-1]
    return data[len(data)-1]
def sumEightSorted(data,big,summed):
    for i in range(len(data)):
        if data[i]+big == summed:
            print 'we found them at ',data[i],'and',big
            break
        else:
            print 'not yet found ..'
    return data[i],big

if __name__ =='__main__':
    summed = 8
    data = [1,3,5,2,4,6,7]
    big = sortData(data)
    a,b = sumEightSorted(data,big,summed)
    
