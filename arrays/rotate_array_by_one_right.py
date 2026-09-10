# O(n), O(1)
#How Slicing Works (arr = [1, 2, 3, 4, 5], k = 1)arr[-1:] gets the last k elements 
# [5]arr[:-1] gets everything except the last k elements 
#  [1, 2, 3, 4]arr[-1:] + arr[:-1] 
# combines them  [5, 1, 2, 3, 4]

def rotate_by_right(arr):
    n = len(arr)
    if n <=1:
        return arr
    last = arr[-1]

    for i in range(n-1,0,-1):
        arr[i] = arr[i-1]

    arr[0] = last
    return arr 

arr = list(map(int,input("Enter the array: ").split()))
obj = rotate_by_right(arr)
print(obj)

# A deque (double-ended queue) is neither strictly FIFO nor LIFO, 
# but it can act as both depending on how you use it.

# How a Deque Works-: deque allows you to insert and remove items from both ends (the front and the rear). 
# Because of this flexibility, it is a hybrid data structure

# FIFO (First-In, First-Out) / Queue: If you add items to one end and remove them from the opposite end, 
# it works like a standard queue.

# LIFO (Last-In, First-Out) / Stack: If you add and remove items from 
# the exact same end, it works like a standard stack.

#first approach O(1), O(n) --> deque create a new space 
# from collections import deque

# def rotate_by_right(arr):
#     if not arr:
#         return arr
#     d = deque(arr)  #--> create a new block first
#     last = d.pop()
#     d.appendleft(last)

#     return list(d)

# arr = list(map(int,input("Enter the array: ").split()))
# obj = rotate_by_right(arr)
# print(obj)

#If you convert arr to deque, modify it, 
# and convert back to list, you temporarily use O(N) extra memory.
