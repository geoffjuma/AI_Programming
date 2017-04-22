#!/usr/bin/env python

def dataGen():
    pass


data = [4,5,3,2,6,1,8,7,9]

swap(a,b):
    temp = b
    a=b
    b=temp
    return a,b

def mergeSort(data):
    for i in range(len(data)):
        for k in range(i/2):
            if data[i+1]<data[i]:
                swap(data[i],data[i+1])
            else:
                pass
            merge()
                print data
            

def insertionSort(data):
    key = 1
    for i in range(len(data)):
        if data[key]<data[i]:
            temp = data[key]
            data[key] = data[i]
            data[i]= temp
        

def burbleSort(data):
    for k in range(len(data)+1):
        for i in range(k+1):
            if data[i+1]<data[i]:
                temp = data[i]
                data[i]=data[i+1]
                data[i+1]=temp
                print data
           
        

if __name__ =="__main__":
    mergeSort(data)
    print data
        
