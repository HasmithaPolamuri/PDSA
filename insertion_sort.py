'''
Start from the second element (index 1).
Compare it with the elements before it.
Insert it into the correct position in the sorted part.
Repeat for all elements

Best -	O(n) 
Average	- O(n²)
Worst	- O(n²)

Stable - Yes
Sort in Place - Yes
'''

def insertionsort(L):
    n = len(L)
    if n < 1:
        return(L)
    for i in range(n):
        j = i
        while(j > 0 and L[j] < L[j-1]):
            (L[j],L[j-1]) = (L[j-1],L[j])
            j = j-1
    return(L)
