#Appraoch 3 DUTCH NATIONAL FLAG (SINGLE PASS WELL SOLVE) o(N), O(1)
#notes ono algo in .md file

# low → position where next 0 goes
# mid → current element being examined
# high → position where next 2 goes

# Interview Questions
# Q1. Why don't we increment mid after finding 2?

# Answer:

# Because after swapping arr[mid] with arr[high], a new unprocessed element comes to mid. We need to examine it before moving forward.

# Q2. Why do we increment both low and mid when we find 0?

# Because after placing the 0 at low, the current element has been correctly processed, so both boundaries can move forward.

# Q3. Why can we use else for 2?

# Because the problem guarantees that every element is either:

# 0, 1, or 2

# So if it isn't 0 and isn't 1, it must be 2.

# Q4. Why is this better than normal sorting?

# Normal sorting takes approximately:

# O(n log n)

# The Dutch National Flag algorithm takes:

# O(n)

# while using:

# O(1)

# extra space.

def sort_for_012(arr):
    low = 0 #lowest part of region (0)
    mid = 0 #current processing. no change
    high = len(arr)-1 #highest part of region. 

    while mid <= high:
        if arr[mid] ==0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low +=1
            mid +=1 
        elif arr[mid] ==1:
            mid +=1 
        else:
            arr[high], arr[mid] = arr[mid], arr[high]
            # mid +=1 --> no need of increement since current swapped element wid high is not checked yet.
            high -=1
    return arr

arr = list(map(int,input("Enter the array: ").split()))
obj = sort_for_012(arr)
print(obj)


#Appraoch 2: o(n) counting method
# def sort_for_012(arr):
#     count_0 = 0
#     count_1 = 0
#     count_2 = 0 

#     for num in arr:
#         if num == 0:
#             count_0 +=1
#         elif num ==1:
#             count_1 +=1 
#         else:
#             count_2 +=1

#     #index dosent get reset for each for loop it iterates for each from where it ended.
#     index = 0
#     for i in range(count_0):
#         arr[index] = 0
#         index +=1

#     for i in range(count_1):
#         arr[index] = 1
#         index +=1

#     for i in range(count_2):
#         arr[index] = 2
#         index +=1

#     return arr

# arr = list(map(int,input("Enter the array: ").split()))
# obj = sort_for_012(arr)
# print(obj)


# approach 1 -: o(n log n )

# def sort_for_012(arr):
#     arr.sort()
#     return arr

# arr = list(map(int,input("Enter the array: ").split()))
# obj = sort_for_012(arr)
# print(obj)