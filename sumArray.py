#!/usr/bin/env python
def sumEight(data,summed):
    for i in range(len(data)-1):
        for j in range(i):
            if (data[i]+data[j]==summed):
                print 'we found it'
                print 'the values are',data[i],'and', data[j]
                break;
            break;
    return data[i],data[j]
        
        
if __name__ =='__main__':
    summed = 8
    data = [1,2,3,4,5,6,7,8]
    a,b = sumEight(data,summed)
   
