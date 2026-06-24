#RETURN TRUE IF FOUND DUPLICATES 
#optimal appraoch O(n), o(n)--> for set

class Solution():
    def cntdup(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True 
            
            seen.add(num)
        
        return False 

if __name__ == "__main__":
    obj = Solution()
    print(obj.cntdup(nums=[1,2,2,3,1]))
    print(obj.cntdup(nums=[1,2,3,4]))


#brute force o(n^2), o(n)
# class Solution():
#     def cntdup(self, nums):
#         n = len(nums)
#         for i in range(n):
#             for j in range(i+1, n):
#                 if nums[i] == nums[j]:
#                     return True
        
#         return False 

# if __name__ == "__main__":
#     obj = Solution()
#     print(obj.cntdup(nums=[1,2,2,1]))
        