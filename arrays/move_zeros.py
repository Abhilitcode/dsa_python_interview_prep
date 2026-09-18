#optimal two pointers appraoch O(1) --> space,  naturally shift 0's
def move_zeros(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] !=0:
            arr[i], arr[j] = arr[j], arr[i]
            j +=1 

    return arr

# Brute force approach  o(n) both
# def move_zeros(arr):
#     temp = []
#     for num in arr:
#         if num !=0:
#             temp.append(num)

#     #until arr and temp length becomes same keep add 0's
#     while len(temp) < len(arr):
#         temp.append(0)

#     return temp

arr = list(map(int,input("Enter the array: ").split()))
obj = move_zeros(arr)
print(obj)

