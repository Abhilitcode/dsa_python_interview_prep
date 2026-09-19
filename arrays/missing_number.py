# 3rd approach xor appraoch . same o(n), o(1)
"""the XOR rules we need:

a ^ a = 0
a ^ 0 = a

So if we XOR all numbers from 0 to n and XOR all numbers in the array, 
every number that exists in both will cancel out.
Only the missing number remains.

First loop  → XOR all numbers that SHOULD be there
Second loop → XOR all numbers that ARE there
              ↓
        matching numbers cancel
              ↓
        missing number remains

Go through every number from 0 to n, including n.
"""

# N+1 bcuz next element can also be missing such as 0,1,2. length = 3 bt the number 
# 3 can be misssing too.

def missing_number(arr):
    n = len(arr) 
    xor = 0

    #xor of numbers that should have been present.
    for i in range(n+1):
      xor = xor ^ i

    #xor of numbers that are actually present. 
    for num in arr:
      xor = xor ^ num  

    return xor

arr = list(map(int, input("Enter the array: ").split()))
obj  = missing_number(arr)
print(obj)
  

# another appraoch. o(n), o(1) optimal
# """We know the numbers should be:

# 0 + 1 + 2 + ... + n

# The sum formula is:

# n * (n + 1) / 2

# So:
# Expected sum : actual sum = missing number"""
# def missing_number(arr):
#     n = len(arr)
#     expected_sum = n*n+1//2 
#     actual_sum = sum(arr)

#     return expected_sum - actual_sum 


#1st appraopch o(nlogn)

# def missing_number(arr):
#     arr.sort()
#     for i in range(len(arr)):
#         if arr[i] !=i:
#             return i 

#     return len(arr) #--> if all values r present thn print next number which is length itself as missing

# arr = list(map(int, input("Enter the array: ").split()))
# obj  = missing_number(arr)
# print(obj)

