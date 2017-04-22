#!/usr/bin/env python

'''implementation of binary search by @geoffjuma'''

data = [0,1,2,3,4,5,6,7,9,8]
n = len(data)

def binarySearch(data):
    for i in range (n):
        for j in range(n/2):
            if data[(n/2)+1]>data[n/2]:
                binarySearch(data[n/2:])
            else:
                print data[n/2]           
if __name__ == '__main__':
    binarySearch(data)

                
            
            
