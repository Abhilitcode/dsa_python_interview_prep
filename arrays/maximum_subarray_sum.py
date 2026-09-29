#Appraoch 2 --> kadane's algorithm o(n), o(1)
# [−2, 1, −3, 4, −1, 2, 1, −5, 4]
# idea is either select the previous sum if greater or else start fresh with new value

def maximum_subarray_sum(arr):
    current_sum = arr[0]
    max_sum = arr[0]

    for i in range(1,len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(current_sum, max_sum)

    return max_sum

arr = list(map(int, input("Enter the array: ").split()))
obj  = maximum_subarray_sum(arr)
print(obj)

# Approach 1 --> o(n^2)
# [−2, 1, −3, 4, −1, 2, 1, −5, 4]

# def maximum_subarray_sum(arr):
#     max_sum = float("-inf")

#     for i in range(len(arr)):
#         current_sum = 0
#         for j in range(i,len(arr)):
#             current_sum += arr[j]
#             max_sum = max(max_sum, current_sum)
#     return max_sum

# arr = list(map(int, input("Enter the array: ").split()))
# obj  = maximum_subarray_sum(arr)
# print(obj)

