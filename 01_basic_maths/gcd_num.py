#Appraoch 2 . implement euclidean algorithm space-: o(1) time-: o(logn)

from ast import List
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        small_num = min(nums)
        large_num = max(nums)

        while small_num!=0:
            small_num, large_num = large_num%small_num, small_num 
        
        return large_num 


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