# from typing import List --> u can use this and import list from typing 

#most optimal appraoch moore's voting algorithm. o(n), o(1)

class Solution():
    def majority_element(self, nums):
        candidate = None
        count = 0 #its not the frequency count. max count of candidate wins here n 
        #other candidate counts votes reduces. 
        for num in nums:
            if count == 0:
                candidate = num
            
            #we want to chck both conditions so "if" or else we could have used elif.
            if candidate == num:
                count +=1
            
            else:
                count -=1 
        
            return candidate

if __name__ == "__main__":
    obj = Solution()
    nums = list(map(int,input("Enter the numbers:").split()))
    print(obj.majority_element(nums))



#better appraoch using hashing o(n), o(n)

# class Solution():
#     def majority_element(self,nums):
#         n = len(nums)
#         freq = {}
#         for num in nums:
#             if num in freq:
#                 freq[num] +=1
#             else:
#                 freq[num] =1
        
#         for key, val in freq.items():
#             if val > n//2:
#                 return key
            
# if __name__ == "__main__":
#     obj = Solution()
#     nums = list(map(int,input("Enter the numbers:").split()))
#     print(obj.majority_element(nums))




# # majority element brute force approach
# class Solution:
#     def majorityElement(self, nums: List[int]):

#         n = len(nums)

#         for i in range(n):
#             count = 0

#             for j in range(n):
#                 if nums[i] == nums[j]:
#                     count +=1

#             if count > n//2:
#                 return nums[i]

# if __name__ == "__main__":
#     obj = Solution()
#     nums = list(map(int,input("Enter the numbers:").split()))
#     print(obj.majorityElement(nums))
#     print(obj.majorityElement(nums=[3,2,3]))