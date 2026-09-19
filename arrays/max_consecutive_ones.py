#only better appraoch O(n), O(1)
#we r finding max consecutive ones --> note that
def max_consecutive_ones(arr):
    count = 0
    max_count = 0 

    for num in arr:
        if num ==1:
            count +=1 
            max_count = max(max_count,count)
        else:
            #reset count since we want consecutive max ones
            count =0

    return max_count

arr = list(map(int, input("Enter the array: ").split()))
obj  = max_consecutive_ones(arr)
print(obj)