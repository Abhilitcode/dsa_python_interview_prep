#3rd appraoch single pass o(n)
def second_largest(arr):
    largest = arr[0]
    second_large = float("-inf")

    for num in arr:
        if num>largest:
            second_large = largest
            largest = num 

        elif num>second_large and num != largest:
            second_large = num 

    return second_large

arr = list(map(int,input("enter the array:").split()))
obj = second_largest(arr)
print(obj)



#2nd loop apppraoch 0(n)
# -1 is used for 0 and positive nums but you can use float(-inf) to avoid such problems
#num!=largest is condition for same numbers in array.
# def second_largest(arr):
#     largest = arr[0]
#     for num in arr:
#         if num>largest:
#             largest = num 

#     second_large = float("-inf")

#     for num in arr:
#         if num>second_large and num != largest:
#             second_large = num 

#     return second_large

# arr = list(map(int,input("enter the array:").split()))
# obj = second_largest(arr)
# print(obj)


#o(nlogn) brute force appraoch
# def second_largest(arr):
#     arr.sort()
#     largest = arr[-1]
#     for i in range(len(arr)-2,-1,-1):
#         if arr[i] != largest:
#             return arr[i]

#     return -1

# arr = list(map(int,input("enter the array:").split()))
# obj = second_largest(arr)
# print(obj)