'''
Find the smallest element in the unsorted part of the list.
Swap it with the first element of the unsorted part.
Move the boundary of sorted/unsorted part one step forward.
Repeat until the list is sorted.

Best Case - O(n²)
Average Case - O(n²)
Worst Case - O(n²)

Stable - Yes
Sort in Place - Yes
'''

def selectionsort(L):
    n = len(L)
    if n < 1:
        return(L)
    for i in range(n):
        minpos = i
        for j in range(i+1,n):
            if L[j] < L[minpos]:
                minpos = j
        (L[i],L[minpos]) = (L[minpos],L[i])
    return(L)
