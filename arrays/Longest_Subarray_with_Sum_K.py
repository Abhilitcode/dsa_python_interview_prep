# optimal appraoch O(n), O(n)

def Longest_Subarray_with_Sum_K(arr,k):
    prefix_sum =0
    max_length =0 
    hashmap = {} 

    for i in range(len(arr)):
        prefix_sum += arr[i]

        #if running sum = k 
        if prefix_sum == k:
            max_length = i +1 

        #if runnin sum - k = old sum is in hashmap
        #keep track of current length through their index 
        if prefix_sum - k in hashmap:
            length = i - hashmap[prefix_sum-k]
            max_length = max(max_length, length) 

        #act as old sum or runnin sum index storage
        if prefix_sum not in hashmap:
            hashmap[prefix_sum] = i 

    return max_length

arr = list(map(int, input("Enter the array: ").split())) 
k = int(input("Enter k: "))
obj  = Longest_Subarray_with_Sum_K(arr,k)
print(obj)













# first appraoch . O(n^2)

# def Longest_Subarray_with_Sum_K(arr,k):
#     max_length = 0

#     for i in range(0, len(arr)):
#         total_sum = 0

#         for j in range(i, len(arr)):
#             total_sum += arr[j] 

#             if total_sum == k:
#                 max_length = max(max_length, j - i + 1)

#     return max_length 

# arr = list(map(int, input("Enter the array: ").split())) 
# k = int(input("Enter k: "))
# obj  = Longest_Subarray_with_Sum_K(arr,k)
# print(obj)