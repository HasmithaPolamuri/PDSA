'''
Divide: Split the list into halves until each sublist has 1 element.
Conquer: Recursively sort the sublists.
Merge: Merge the sorted sublists back together.

Best Case - O(n log n)
Average Case - O(n log n)
Worst Case - O(n log n)

Stable - Yes
Sort in Place - No
'''

def merge(A,B): # Merge two sorted list A and B
    (m,n) = (len(A),len(B))
    (C,i,j) = ([],0,0)
    
    #Case 1 :- When both lists A and B have elements for comparing
    while i < m and j < n:
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    
    #Case 2 :- If list B is over, shift all elements of A to C 
    while i < m:
        C.append(A[i])
        i += 1
    
    #Case 3 :- If list A is over, shift all elements of B to C 
    while j < n:
        C.append(B[j])
        j += 1
    
    # Return sorted merged list   
    return C

# Recursively divide the problem into sub-problems to sort the input list L    
def mergesort(L): 
    n = len(L)
    if n <= 1: #If the list contains only one element or is empty return the list.
        return(L)
    Left_Half = mergesort(L[:n//2]) #Recursively sort the left half of the list
    Right_Half = mergesort(L[n//2:]) #Recursively sort the rightt half of the list
    Sorted_Merged_List = merge(Left_Half, Right_Half) # Merge two sorted list Left_Half and Right_Half
    return(Sorted_Merged_List)
