#Iterative Implementation
def binarysearch(L, v):  #v = target element
    low = 0
    high = len(L) - 1
    while low <= high: 
        mid = (low + high) // 2
        if L[mid ] < v:
            low = mid  + 1
        elif L[mid ] > v:
            high = mid  - 1
        else:
            return mid
    return False


#Recursive Implementation without slicing
def binarysearch(L,v,low,high): #v = target element, low = first index, high = last index
    if high - low < 0:
        return False
    mid = (high + low)//2
    if v == L[mid]:
        return mid
    if v < L[mid]:
        return(binarysearch(L,v,low,mid-1))
    else:
        return(binarysearch(L,v,mid+1,high))


#Lecture Implementation (Not recommended to achieve  time
#Due to use of slicing, this implementation takes O(n) time
def binarysearch(L,v):
    if L == []:
        return(False)
    mid = len(L)//2
    if v == L[mid]:
        return mid
    if v < L[mid]:
        return(binarysearch(L[:mid],v))
    else:
        return(binarysearch(L[mid+1:],v))
