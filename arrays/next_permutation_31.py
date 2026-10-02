#refer notes for brute force. 
#brute force --> 1) generaTE ALL POSSIBLE PERMUTATION --> SORT THEM-->
# --> FIND CURRENT PERMUTATION --> RETURN THE NEXT ONE --? o(N!*N)
# [1, 2, 3, 6, 5, 4]
# [1, 3, 5, 4, 2]
#Optimal approach 
def next_permuation(arr):
    n = len(arr)
    # we have to compare from right.
    i = n-2

    #find a breaking point(pivot)
    while i>=0 and arr[i] >= arr[i+1]:
        i -=1

    #find a element which shows a smallest change(increase) as compared to current element
    #and then swap it 
    if i>=0:
        j = n-1 
        while arr[j] <= arr[i]:
            j -=1 

        arr[i], arr[j] = arr[j], arr[i]

    arr[i+1:] = reversed(arr[i+1:])
    return arr

arr = list(map(int, input("Enter the array: ").split()))
obj  = next_permuation(arr)
print(obj)


    
