#highest character frequency 
#O(n), o(n)

class Solution:
    def max_freq(self, s):
        freq = {}
        for char in s:
            if char in freq:
                freq[char] +=1
            else:
                freq[char] = 1 
        
        maximum_freq = 0
        max_char = ""

        for key, value in freq.items():
            if value > maximum_freq:
                maximum_freq = value
                max_char = key
        
        return max_char, maximum_freq
    
if __name__ == "__main__":
    obj = Solution()
    print(obj.max_freq(s="radheshammm"))
    print(obj.max_freq(s="lifeisunfair"))