# third approach O(n), O(1)
#left arr rotate thn do forward iterate
def rotate_left_by_one(arr):
    n = len(arr)
    first = arr[0]
    for i in range(1,n):
        arr[i-1] = arr[i]

    arr[-1] = first

    return arr

arr = list(map(int,input("enter the array:").split()))
obj = rotate_left_by_one(arr)
print(obj)



#second appraoch (pop elements) #o(n)

# def rotate_left_by_one(arr):
#     first = arr[0]
#     arr.pop(0)
#     arr.append(first)
#     return arr
# arr = list(map(int,input("enter the array:").split()))
# obj = rotate_left_by_one(arr)
# print(obj)



# first appraoch O(n), O(n)

# def rotate_left_by_one(arr):
#     arr = arr[1:] + arr[:1] #----> extra space is created for new arr
#     return arr  

# arr = list(map(int,input("enter the array:").split()))
# obj = rotate_left_by_one(arr)
# print(obj)