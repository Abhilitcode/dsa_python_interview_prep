#Complement = The number you still need to reach the target.
# refer at last for explanation

#optimal appraoch --> o(n), O(n)
from typing import List
class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [hashmap[complement],i]  #--> hashmap ke complement ka index, current index
            hashmap[nums[i]] = i #complement ka missing piece

if __name__ == "__main__":
    obj = Solution()
    print(obj.twoSum(nums=[2,7,11,15], target=9))
    print(obj.twoSum(nums=[3,2,4], target=6))

#Brute force appraoch 

# from typing import List
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         n = len(nums)
#         for i in range(n):
#             for j in range(1,n):
#                 if nums[i] + nums[j] == target:
#                     return [i,j]
        
# if __name__ == "__main__":
#     obj = Solution()
#     print(obj.twoSum(nums=[2,7,11,15], target=9))
#     print(obj.twoSum(nums=[3,2,4], target=6))

# ---------------------------------------------------------- 
#Key Lines Explained
# complement = target - nums[i]

# Calculates the exact matching number required to complete the sum.

# if complement in hashmap:

# Checks if the missing piece was already seen earlier in the array.

# return [hashmap[complement], i]

# Returns the index of the complement (which was saved earlier) and the current index i.

# hashmap[nums[i]] = i

# If the complement wasn't seen yet, remember the current number and its position for future iterations.