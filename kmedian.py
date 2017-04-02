'''
Given an array, find the median of the subarray which contain elements less than or equal to k
'''

def solution(arr, k):
    i = 0
    j = len(arr) -1

    while(i<len(arr) and arr[i]>k):
        i+=1
    while(j>0 and arr[j]>k):
        j-=1

    previ = i
    prevj = j

    if(i>j):
        return 0
    elif(i==j):
        return arr[i]
    while(True):
        print 'i=',i,'  j=',j
        previ = i
        prevj = j
        i+=1
        j-=1
        while(arr[i]>k):
            i+=1
        while(arr[j]>k):
            j-=1
        if(i>j):
            if(previ <= prevj):
                return (arr[previ] + arr[prevj])/2.0
            else:
                raise Exception("Error")
        elif(i<j):
            continue







if __name__ == '__main__':
    print solution([16]*10+range(-1,30,1), 15)