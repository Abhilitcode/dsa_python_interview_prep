#optimal appraoch bt here we have to find counts of subarray = k . O(n), O(n)

def subarray_sum_equaks_k(arr,k):
    #we need to assign 0 as 1 index in hashmap bcuz if first value is itself 
    #the target(i.e 6-6=0 thn 0 wont be in hashmap n it wont get counted so 
    # we initialize and hard coded it before)

    prefix_sum = 0
    count = 0 
    hashmap = {0:1}

    for num in arr:
        prefix_sum += num 

        if prefix_sum-k in hashmap:
            count += hashmap[prefix_sum-k]

        hashmap[prefix_sum] = hashmap.get(prefix_sum,0)+1 

    return count  

arr = list(map(int, input("Enter the array: ").split())) 
k = int(input("Enter k: "))
obj  = subarray_sum_equaks_k(arr,k)
print(obj)
