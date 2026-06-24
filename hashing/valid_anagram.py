#optimal approach 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = {}
        freq2 = {}

        for char in s:
            if char in freq1:
                freq1[char] +=1
            else:
                freq1[char] =1
        
        for char in t:
            if char in freq2:
                freq2[char] +=1
            else:
                freq2[char] =1 
        
        return freq1 == freq2 
    

if __name__ == "__main__":
    obj = Solution()
print(obj.isAnagram(s="anagram",t="agaramn"))
print(obj.isAnagram(s="rat", t="car"))




#brute force appraoch sorting o(nlogn), o(n)
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t)

# if __name__ == "__main__":
#     obj = Solution()
#     print(obj.isAnagram(s="anagram",t="agaramn"))
#     print(obj.isAnagram(s="rat", t="car"))

