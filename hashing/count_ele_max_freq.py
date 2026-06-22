#Count elements with max frequency
#o(n), o(n), lc --> 3005
class Solution:
    def count_elements(self, nums):
        freq = {}
        for val in nums:
            if val in freq:
                freq[val] +=1
            else:
                freq[val] =1
        
        max_value = max(freq.values())

        result = 0
        for count in freq.values():
            if max_value == count:
                #how many elements have same maximum frequency(1,1,2,2,3,3) --> 6 elements
                result += count 
        
        return result

if __name__ == "__main__":
    obj = Solution()
    print(obj.count_elements(nums=[1,2,2,1,3,3,4]))