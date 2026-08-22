#Appraoch 2 . implement euclidean algorithm space-: o(1) time-: o(logn)
#gcd of smallest and largest number -> finding. not the entire array list
# understand why this condition in while loop scroll down. 
from typing import List
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)

        while min_num != 0:
            min_num, max_num = max_num % min_num, min_num

        return max_num

#appraoch 1 math appraoch space-: o(1) time-: o(n+n+logn) => 
# o(n) since o(n) is the dominant term.
# import math
# from typing import List
# class Solution:
#     def findGCD(self, nums: List[int]) -> int:
#         min_num = min(nums)
#         max_num = max(nums)

#         return math.gcd(min_num, max_num)

if __name__ == "__main__":
    obj = Solution()
    print(obj.findGCD([2,5,6,9,10]))
    print(obj.findGCD([7,5,6,8,3]))

# This is the Euclidean Algorithm for finding the
# Greatest Common Divisor (GCD) of two numbers.
# The while min_num != 0: loop is used because we don't know in 
# advance how many division steps it will take to reduce the remainder to zero.
# this is same as division method we did in schools