'''
Pick a pivot element.
Partition the array: put elements smaller than pivot to the left, greater to the right.
Recursively sort the left and right parts.

Best -	O(n log n) 
Average -	O(n log n) 
Worst -	O(n²)

Stable - No
Sort in Place - Yes
'''

#Implementation
def partition(L,lower,upper):
  # Select first element as a pivot 
  pivot = L[lower]
  i = lower
  for j in range(lower+1,upper+1):
    if L[j] <= pivot:
      i += 1
      L[i],L[j] = L[j],L[i]
  L[lower],L[i]= L[i],L[lower]
  # Return the position of pivot
  return i

def quicksort(L,lower,upper):
  if(lower < upper):
    pivot_pos = partition(L,lower,upper);
    # Call the quick sort on leftside part of pivot
    quicksort(L,lower,pivot_pos-1)
    # Call the quick sort on rightside part of pivot
    quicksort(L,pivot_pos+1,upper)
  return L


#Lecture Implementation
def quicksort(L,l,r): # Sort L[l:r]
    if (r - l <= 1):
        return L
    (pivot,lower,upper) = (L[l],l+1,l+1)
    for i in range(l+1,r):
        if L[i] > pivot:
            # Extend upper segment
            upper = upper+1
        else:
            # Exchange L[i] with start of upper segment
            (L[i], L[lower]) = (L[lower], L[i])
            # Shift both segments
            (lower,upper) = (lower+1,upper+1)
    # Move pivot between lower and upper
    (L[l],L[lower-1]) = (L[lower-1],L[l])
    lower = lower-1
    
    # Recursive calls
    quicksort(L,l,lower)
    quicksort(L,lower+1,upper)
    return(L)
