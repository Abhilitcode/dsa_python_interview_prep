""" Complexity

Best case: O(1) — target is the first element.

Worst case: O(n) — target is at the end or doesn't exist.

Space: O(1)

Interview question

Q: Why can't we use Binary Search here?

Because Binary Search requires the array to be sorted. 
Linear Search works even when the array is completely unsorted."""

#appraoch 

def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i 

    return -1 #--> target does not exist. 

arr = list(map(int,input("Enter the arr: ").split())) 
target = int(input("Enter the number: "))

obj = linear_search(arr, target)
print(obj)
