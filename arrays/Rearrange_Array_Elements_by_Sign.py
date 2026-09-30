# Optimal: Use two indices and place each number directly into its final position — O(n) time, O(n) space.
# Why optimal? Same Big-O, but avoids the unnecessary intermediate 
# positive/negative lists and directly constructs the required arrangement.

# Appraoch 2 --> use 2 indices and place them directly in final position
def rearrange_by_sign(arr):
    positives = 0
    negatives = 1

    final_list = [0] * len(arr)
    for num in arr:
        if num > 0:
            final_list[positives] = num
            #positives are at 0-->2-->4-->6....
            positives +=2 
        else:
            final_list[negatives] = num
            negatives +=2 

    return final_list

arr = list(map(int, input("Enter the arr: ").split())) 
obj = rearrange_by_sign(arr)
print(obj)


# Approach 1 : Brute/naive: Separate positives and negatives, then alternate them — O(n) time, O(n) space.

# def rearrange_by_sign(arr):
#     positives = []
#     negatives = []

#     for num in arr:
#         if num>0:
#             positives.append(num)
#         else:
#             negatives.append(num)

#     final_list = []

#     for i in range(len(positives)):
#         final_list.append(positives[i])
#         final_list.append(negatives[i])

#     return final_list

# arr = list(map(int, input("Enter the arr: ").split())) 
# obj = rearrange_by_sign(arr)
# print(obj)